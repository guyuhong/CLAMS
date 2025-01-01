# coding=utf-8

#     National Oceanic and Atmospheric Administration (NOAA)
#     Alaskan Fisheries Science Center (AFSC)
#     Resource Assessment and Conservation Engineering (RACE)
#     Midwater Assessment and Conservation Engineering (MACE)

#  THIS SOFTWARE AND ITS DOCUMENTATION ARE CONSIDERED TO BE IN THE PUBLIC DOMAIN
#  AND THUS ARE AVAILABLE FOR UNRESTRICTED PUBLIC USE. THEY ARE FURNISHED "AS
#  IS."  THE AUTHORS, THE UNITED STATES GOVERNMENT, ITS INSTRUMENTALITIES,
#  OFFICERS, EMPLOYEES, AND AGENTS MAKE NO WARRANTY, EXPRESS OR IMPLIED,
#  AS TO THE USEFULNESS OF THE SOFTWARE AND DOCUMENTATION FOR ANY PURPOSE.
#  THEY ASSUME NO RESPONSIBILITY (1) FOR THE USE OF THE SOFTWARE AND
#  DOCUMENTATION; OR (2) TO PROVIDE TECHNICAL SUPPORT TO USERS.

"""
.. module:: CLAMSProcess

    :synopsis: CLAMSProcess is the fcatch processing form and is
               displayed after a user selects a catch event to
               process.

| Developed by:  Rick Towler   <rick.towler@noaa.gov>
|                Kresimir Williams   <kresimir.williams@noaa.gov>
| National Oceanic and Atmospheric Administration (NOAA)
| National Marine Fisheries Service (NMFS)
| Alaska Fisheries Science Center (AFSC)
| Midwater Assesment and Conservation Engineering Group (MACE)
|
| Author:
|       Rick Towler   <rick.towler@noaa.gov>
|       Kresimir Williams   <kresimir.williams@noaa.gov>
| Maintained by:
|       Rick Towler   <rick.towler@noaa.gov>
|       Kresimir Williams   <kresimir.williams@noaa.gov>
|       Mike Levine   <mike.levine@noaa.gov>
|       Nathan Lauffenburger   <nathan.lauffenburger@noaa.gov>
"""

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import Clamsbase2Functions
from ui import ui_CLAMSProcess
#import CLAMShaul
#import CLAMScatch
#import CLAMSspecimen
#import CLAMSlength
#import CLAMSSpeciesFix
from acquisition.SensorMonitor import SensorMonitor
import messagedlg
import listseldialog
import codendstatusdlg


class CLAMSProcess(QDialog, ui_CLAMSProcess.Ui_clamsProcess):

    def __init__(self, parent=None):
        #  set up the GUI
        super(CLAMSProcess, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        # initialize variables
        self.reloadFlag=False
        self.db=parent.db
        self.survey=parent.survey
        self.ship=parent.ship
        self.activeHaul=parent.activeEvent
        self.settings=parent.settings
        self.workStation=parent.workStation
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.backLogger=parent.backLogger
        self.testing=parent.testing
        self.partitions=[]
        self.activePartition=None
        self.methotFlag=False

        #  set up some colors
        self.blue = QPalette()
        self.blue.setColor(QPalette.ColorRole.ButtonText,QColor(0, 0, 255))
        self.black = QPalette()
        self.black.setColor(QPalette.ColorRole.ButtonText,QColor(0, 0, 0))



        # set up button colors
        self.haulBtn.setPalette(self.black)
        self.catchBtn.setPalette(self.black)
        self.lengthBtn.setPalette(self.black)
        self.specBtn.setPalette(self.black)

        #  Set up the signals and slots
        self.partitionBox.activated[int].connect(self.getPartition)
        self.haulBtn.clicked.connect(self.getHaul)
        self.catchBtn.clicked.connect(self.getCatch)
        self.specBtn.clicked.connect(self.getSpecimen)
        self.lengthBtn.clicked.connect(self.getLength)
        self.fixSpeciesBtn.clicked.connect(self.goFixSpecies)
        self.editCodendStateBtn.clicked.connect(self.editCodendState)
        self.doneBtn.clicked.connect(self.goExit)

        #  set up the window position
#        screen = QDesktopWidget().screenGeometry()
#        window = self.geometry()
#        self.setGeometry((screen.width() - window.width()) / 2,
#                         (screen.height() - window.height()) / 2,
#                         window.width(), window.height())
#        self.setMinimumSize(window.width(), window.height())
#        self.setMaximumSize(window.width(), window.height())
#        self.windowAnchor = ((screen.height() - window.height()) / 2, window.height())
#        self.settings.update({"WindowAnchor":window.y() + window.height()})

        #  set the event number
        self.haulLabel.setText(self.activeHaul)

        # get the scientist - first get the list of active scientists
        self.sciList=[]
        sql = ("SELECT scientist FROM personnel WHERE active=1"
                " ORDER BY scientist")
        query = self.db.dbQuery(sql)
        for scientist, in query:
            self.sciList.append(scientist)
        #  instantiate the list dialog with the sci names
        self.listDialog = listseldialog.ListSelDialog(self.sciList, parent=self)
        self.listDialog.label.setText('Identify yourself, please.')
        #  and finally present the dialog - force the selection
        needScientist = True
        while needScientist:
            if self.listDialog.exec():
                if (self.listDialog.itemList.currentRow() < 0):
                    #  no name selected
                    self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                            "Please select your name, or a suitable substitute if yours" +
                            " cannot be found.", 'info')
                    self.message.exec()
                else:
                    #  name selected
                    needScientist = False
                    self.scientist = self.listDialog.itemList.currentItem().text()
        #  parse the first name
        p = self.scientist.split(' ')
        self.firstName = p[0]

        #  setup reoccurring dialogs
        self.message = messagedlg.MessageDlg(self)
        self.codendstate = codendstatusdlg.CodendStatusDlg(self.firstName, self)

        #  update this workstation's status to "Open". We also update the
        #  current_event value
        sql = ("UPDATE workstations SET status='open', current_event=" +
                self.activeHaul + " WHERE workstation_ID=" +
                self.workStation)
        self.db.dbExec(sql)

        #  Set the visibility of the action buttons based on the actions specified for this station
        self.haulBtn.hide()
        self.catchBtn.hide()
        self.lengthBtn.hide()
        self.specBtn.hide()
        if 'haul' in parent.modules:
            self.haulBtn.show()
        if 'catch' in parent.modules:
            self.catchBtn.show()
        if 'length' in parent.modules:
            self.lengthBtn.show()
        if 'specimen' in parent.modules:
            self.specBtn.show()
        self.haulBtn.setEnabled(True)

        #  check if we're reloading data and enable buttons if so
        sql = ("SELECT parameter_value FROM event_data WHERE event_id=" + self.activeHaul +
                " AND ship=" + self.ship + " AND survey=" + self.survey +
                " AND event_parameter='PartitionWeightType'")
        query = self.db.dbQuery(sql)
        if query.first():
            #  at least one partition has a weight type assigned so we've been
            #  here before. Enable the catch button
            self.reloadFlag = True
            self.catchBtn.setEnabled(True)

            #  now check to see if there are any existing samples
            sql = ('SELECT sample_id FROM samples WHERE event_id=' + self.activeHaul +
                    ' AND ship=' + self.ship + ' AND survey=' + self.survey)
            query = self.db.dbQuery(sql)
            if query.first():
                #  yes, there is at least one sample so we will enable the length
                #  and specimen buttons too.
                self.lengthBtn.setEnabled(True)
                self.specBtn.setEnabled(True)

        #  set up the serial devices attached to this workstation
        self.setupSerialDevices()

        # enable entry of non-codend partition data before trawl codend is on deck
        self.catchBtn.setEnabled(True)

        #  set up the partitions business
        self.setupAllPartitions()


    def setupAllPartitions(self):
        '''
        setupPartitions populates the partition drop down menu with the
        appropriate partition options
        '''

        self.partitions=[]
        self.partitionBox.clear()
        #  get the possible partitions for this gear
        sql = ("SELECT GEAR_PARTITIONS.PARTITION, EVENTS.GEAR FROM GEAR_OPTIONS, GEAR_PARTITIONS, EVENTS WHERE" +
                " (GEAR_PARTITIONS.PARTITION = GEAR_OPTIONS.PARTITION) and (GEAR_OPTIONS.GEAR = EVENTS.GEAR)" +
                " and ((EVENTS.SHIP = " + self.ship + " ) AND (EVENTS.SURVEY = " + self.survey + ") AND" +
                " (EVENTS.EVENT_ID = " + self.activeHaul + ") AND (GEAR_PARTITIONS.PARTITION_TYPE = 'Catch'))" +
                "  ORDER BY GEAR_PARTITIONS.PARTITION ASC")
        query = self.db.dbQuery(sql)

        #  loop thru partitions and populate partition dropdown
        for partition, gear in query:
            self.partitionBox.addItem(partition)
            self.partitions.append(partition)

        #  check to make sure we found something to process for this event
        if (len(self.partitions) == 0):
            #  no partitions? - must have the wrong event
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                    self.firstName + ", I am unable to find any catch partitions " +\
                    "to process. Did you select the correct event?", 'info')
            self.message.exec()
            return

        #  set (or unset) the default value in the partition drop down
        if len(self.partitions) > 1:
            #  if there is more than one option - clear the current selection to force the
            #  user to select a partition
            self.partitionBox.setCurrentIndex(-1)
        else:
            #  if there is only one option, select it
            self.partitionBox.setCurrentIndex(0)
            self.partitionBox.setEnabled(False)
            self.activePartition = self.partitions[0]


    def getPartition(self):

        #  set the active partition so the selected partition
        self.activePartition = self.partitionBox.currentText()

        #  check if the codend status has been set
        sql = ("SELECT * FROM event_data WHERE ship = " + self.ship +
                " AND survey = " + self.survey + " and event_id = " +
                self.activeHaul+ " AND partition = '"+ self.activePartition +
                "' AND event_parameter = 'CodendStatus'")
        query = self.db.dbQuery(sql)
        if not query.first():
            # value has not been recorded for this partition - display the status dialog
            self.codendstate.exec()
            codendstatus = self.codendstate.state_value
            #  and insert the status into event_data
            sql = ("INSERT INTO event_data (ship, survey, event_id, partition, " +
                    "event_parameter, parameter_value) VALUES(" + self.ship +
                    "," + self.survey + "," + self.activeHaul + ",'" +
                    self.activePartition + "' ,'CodendStatus','" +
                    codendstatus + "')")
            self.db.dbExec(sql)


    def setupSerialDevices(self):
        '''
        setupSerialDevices creates an instance of SensorMonitor and configures it accordingly.
        SensorMonitor is the CLAMS sensor data acquisition class which oversees all sensor
        acquisition. It creates threads for each configured device and handles the polling
        and parsing of data received from the devices.


        '''

        #TODO: SensorMonitor is an evolution of SerialMonitor which also supports TCP and UDP
        #      based data sources. This code should be updated to move away from only setting
        #      up serial based devices to support network devices too.

        #  create an instance of the sensor monitor
        self.serMonitor = SensorMonitor.SensorMonitor()

        #  query the devices attached to this station
        sql = ("SELECT MEASUREMENT_SETUP.DEVICE_ID, DEVICES.DEVICE_NAME " +
                "FROM MEASUREMENT_SETUP INNER JOIN DEVICES ON " +
                "MEASUREMENT_SETUP.DEVICE_ID = DEVICES.DEVICE_ID WHERE " +
                "MEASUREMENT_SETUP.WORKSTATION_ID = " +  self.workStation +
                " AND MEASUREMENT_SETUP.DEVICE_INTERFACE = 'Serial'" +
                " GROUP BY MEASUREMENT_SETUP.DEVICE_ID, DEVICES.DEVICE_NAME")
        devQuery = self.db.dbQuery(sql)

        #  loop thru the devices querying their parameters and adding them to serial monitor
        for deviceID, deviceName in devQuery:
            #  query the connection parameters for this device
            sql = ("SELECT DEVICE_PARAMETER, PARAMETER_VALUE FROM device_configuration" +
                    " WHERE DEVICE_ID = " + deviceID)
            paramQuery = self.db.dbQuery(sql)

            #  loop thru the parameters and stick in a dictionary
            connPar = {}
            for devParam, paramVal in paramQuery:
                connPar.update({devParam:paramVal})

            #  extract the parameters
            try:
                #  extract the required parameters
                port = connPar['SerialPort']
                baud = int(connPar['BaudRate'])
            except:
                QMessageBox.critical(self, "ERROR", "<font size = 14> Incomplete " +
                        "serial configuration data in 'DEVICE_CONFIGURATION' for device " +
                        deviceName + ". The device will not be enabled.")
                continue

            #  extract the optional parameters and if missing provide sane defaults
            parseType = str(connPar.get('ParseType', 'None'))
            parseExp = str(connPar.get('ParseExpression', ''))
            parseIndex = int(connPar.get('ParseIndex', 0))
            cmdPrompt = str(connPar.get('CommandPrompt', ''))
            if (parseType.lower() == 'regex'):
                try:
                    #  the regex parser requires both the expression and the index
                    parseExp = connPar['ParseExpression']
                    parseIndex = int(connPar['ParseIndex'])
                except:
                    QMessageBox.critical(self, "ERROR", "<font size = 14> Incomplete " +
                            "regex configuration data in 'DEVICE_CONFIGURATION' for device " +
                            deviceName + ". The device will not be enabled.")
                    continue

            #  add the device to the serial monitor
            try:
                self.serMonitor.addDevice(deviceID, port, baud, parseType, parseExp,
                        parseIndex, cmdPrompt)
            except Exception as e:
                #  there was an issue adding the device - report it to the user and move on
                QMessageBox.critical(self, "ERROR", "<font size = 14> Error " +
                        "adding " + deviceName + " to the SensorMonitor. " +
                        str(e) + ":" + str(e.parent) + ". The device will not be enabled.")

        #  now that all devices are added - start monitoring them. This will cause
        #  SensorMonitor to open serial or network ports and in the case of serial
        #  ports start polling. SensorMonitor will buffer data until full messages
        #  are received. Those messages are optionally parsed and then SensorMonitor
        #  emits a signal with the parsed data.
        try:
            #  start the sensor monitor
            self.serMonitor.startMonitoring()
        except Exception as e:
            #  There was an issue with a device or devices

            #  first get the human readable device names
            devNames = []
            for badDevice in e.devNames:
                sql = ("SELECT device_name FROM devices" +
                        " WHERE device_id=" + badDevice)
                query = self.db.dbQuery(sql)
                dev, = query.first()
                devNames.append(dev)

            #  construct the error text
            if (len(devNames) == 1):
                errText = 'Error opening device ' + devNames[0]
            else:
                errText = 'Error opening devices ' + ', '.join(devNames)

            #  display a warning dialog
            QMessageBox.warning(self, "Serial Port Error", "<font size = 14>" +
                    errText + ". These devices will be not be enabled.")


    def editCodendState(self):

        #  get the existing codend status
        sql = ("SELECT parameter_value FROM event_data WHERE ship = " + self.ship +
                " and survey = " + self.survey + " and event_id = " +
                self.activeHaul + " and partition = '" + self.activePartition +
                "' AND event_parameter = 'CodendStatus'")
        query = self.db.dbQuery(sql)
        currentCodendState, = query.first()

        #  if there is a current state, set that button on the dialog and display.
        #  if there is no current status, we ignore this button press (don't do anything)
        if currentCodendState:
            for btn in self.codendstate.btns:
                if btn.text() == currentCodendState:
                    btn.setChecked(True)
            #  now display the codendstate dialog
            self.codendstate.exec()
            #  update the state based on the dialog selection
            codendstatus = self.codendstate.state_value

            #  and update the database entry
            sql = ("UPDATE event_data SET parameter_value='" + codendstatus +
                    "' WHERE ship = " + self.ship + " and survey = " +
                    self.survey + " and event_id = " + self.activeHaul +
                    " and partition = '" +  self.activePartition +
                    "' AND event_parameter = 'CodendStatus'")
            self.db.dbExec(sql)


    def getHaul(self):
        '''getHaul opens up the Haul form.
        '''

        #  set the button blue to indicate the active form
        self.haulBtn.setPalette(self.blue)

        #  display the haul selection dialog
        #haulWindow = CLAMShaul.CLAMSHaul(self)
        #haulWindow.exec()

        #  set the button back to black
        self.haulBtn.setPalette(self.black)


    def getCatch(self):
        '''getCatch opens up the Catch form.
        '''

        #  make sure there is an active partition
        if (self.activePartition == None):
            #  no partition selected - issue error
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                    self.firstName + ", you need to select a partition for" +
                    " this haul first!", 'info')
            self.message.exec()
            return

        #  set the catch button blue to indicate the current form
        self.catchBtn.setPalette(self.blue)

        #  show the catch form
        #catchWindow = CLAMScatch.CLAMSCatch(self)
        #catchWindow.exec()

        #  set the button color back now that the form is closed
        self.catchBtn.setPalette(self.black)

        #  now check to see if we should enable the length and specimen buttons
        sql = ('SELECT sample_id FROM samples WHERE event_id=' + self.activeHaul +
                ' AND ship=' + self.ship + ' AND survey=' + self.survey)
        query = self.db.dbQuery(sql)
        if query.first():
            #  yes, there is at least one sample so we will enable the length
            #  and specimen buttons.
            self.lengthBtn.setEnabled(True)
            self.specBtn.setEnabled(True)


    def getLength(self):
        '''getLength opens up the Length form.
        '''

        #  make sure there is an active partition
        if (self.activePartition == None):
            #  no partition selected - issue error
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                    self.firstName + ", you need to select a partition for" +
                    " this haul first!", 'info')
            self.message.exec()
            return

        #  set the length button blue to indicate the current form
        self.lengthBtn.setPalette(self.blue)

        #  show the length form
        #lengthWindow = CLAMSlength.CLAMSLength(self)
        #lengthWindow.exec()

        #  set the button color back now that the form is closed
        self.lengthBtn.setPalette(self.black)


    def getSpecimen(self):
        '''getLength opens up the Length form.
        '''

        #  make sure there is an active partition
        if (self.activePartition == None):
            #  no partition selected - issue error
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                    self.firstName + ", you need to select a partition for" +
                    " this haul first!", 'info')
            self.message.exec()
            return

        #  set the specimen button blue to indicate the current form
        self.specBtn.setPalette(self.blue)

        #  show the specimen form
        #specimenWindow = CLAMSspecimen.CLAMSSpecimen(self)
        #specimenWindow.exec()

        #  set the button color back now that the form is closed
        self.specBtn.setPalette(self.black)


    def goFixSpecies(self):
        '''goFixSpecies opens up the SpeciesFix form. this form can be
        used for bulk correction of species and/or sex assignments when users
        forget to change one of these parameters and then measures a bunch
        of fish. Correcting this directly in the database is difficult
        due to various parent child relationships. This form handles all of
        that making corrections quick and easy.
        '''

        #  make sure there is an active partition
        if (self.activePartition == None):
            #  no partition selected - issue error
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                    self.firstName + ", you need to select a partition for" +
                    " this haul first!", 'info')
            self.message.exec()
            return

        #  display the SpeciesFix dialog
        #spcFixWindow = CLAMSSpeciesFix.CLAMSSpeciesFix(self)
        #spcFixWindow.exec()


    def goExit(self):
        '''goExit is called when the "Finshed" button is pressed

        '''
        #  close the form
        self.close()


    def closeEvent(self, event=None):
        '''closeEvent is called when the form is closed.

        When the last workstation is closed for an event we runs some checks
        on the data to make sure there aren't any major issues.

        We also update the CATCH_SUMMARY table. Currently we update it when
        any station closes. This approach was used when there was a hole in
        the "last workstation" logic where in certain cases a last workstation
        wouldn't know it is the last workstation and would fail to update the
        table. That logic has been fixed by adding the "current_event" column
        to the workstations table so in theory we can now only update
        CATCH_SUMMARY when the last workstation closes but I'm leaving it as-is
        for now.
        '''

        #  set the status for this workstation to closed
        sql = ("UPDATE workstations SET status='closed', " +
                "current_event=0 WHERE workstation_ID=" + self.workStation)
        self.db.dbExec(sql)

        #  check if we're the last station working on this event to close
        sql = ("SELECT workstation_id FROM workstations WHERE status='open' AND " +
                "current_event=" + self.activeHaul)
        query = self.db.dbQuery(sql)
        if not query.first():
            #  we ARE the last station working on this event. We'll do some checks on the
            #  data compute some summary data that is inserted into the database

            #  check "normal" trawls, don't check methots and skip when testing flag is set
            if not self.methotFlag and not self.testing:
                #  do some basic checks on the data we just collected to make sure
                #  we didn't miss anything big.
                self.sampleValidation1()

                if self.returnFlag:
                    #  user chose to fix the problem so we don't exit
                    event.ignore()
                    return

            # populate the total partition weights into the event_data table
            self.totalHaulWeight()

            # this is the last station to close - reset the active haul
            sql = ("UPDATE application_configuration SET parameter_value = 0" +
                    " WHERE parameter = 'ActiveHaul'")
            self.db.dbExec(sql)

        #  update the CATCH_SUMMARY table for this event - we'll update it every time
        #  a station exits to ensure that it is fully up-to-date
        ok, error_txt = self.updateCatchSummary()
        if not ok:
            #  let the user know there was a problem
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                    error_txt, 'info')
            self.message.exec()

        # shut down serial monitor
        try:
            self.serMonitor.stopMonitoring()
        except:
            #  we don't care if we can't close the serial ports because
            #  we probably couldn't open them in the first place.
            pass

        event.accept()


    def totalHaulWeight(self):
        '''totalHaulWeight updates the HAUL_DATA PartitionWeight parameter for each partition
        that has a PartitionWeightType of "not_subsampled". This is done by summing up the
        weights of all baskets, which is how you compute the total catch weight when you
        don't subsample.
        '''
        #  loop thru the partitions and add up baskets for any partition that is not subsampled.
        for partition in self.partitions:

            #  check if this partition is not_subsampled
            sql = ("SELECT parameter_value FROM event_data WHERE ship=" + self.ship +
                    " AND survey=" + self.survey + " AND event_id=" + self.activeHaul +
                    " AND partition='" + partition +"' AND event_parameter='PartitionWeightType'")
            query = self.db.dbQuery(sql)
            weightType, = query.first()

            if weightType.lower() in ["not_subsampled", "not subsampled"]:
                #  this partition is not subsampled, add up all of the basket weights
                total_weight = 0

                #  get the sample parent ID
                sql = ("SELECT sample_id FROM samples WHERE ship=" + self.ship +
                        " AND survey=" + self.survey + " AND event_id=" + self.activeHaul +
                        " AND partition='" + partition + "' AND sample_type='WholeHaul'")
                query = self.db.dbQuery(sql)
                parent_id, = query.first()
                parent_id = int(parent_id)

                #  get the sample IDs associated with this parent
                sql = ("SELECT sample_id FROM samples WHERE ship=" + self.ship +
                        " AND survey=" + self.survey + " AND event_id=" + self.activeHaul +
                        " AND parent_sample=" + str(parent_id))
                sampleQuery, = self.db.dbQuery(sql)

                #  loop thru those samples and add up the baskets
                for sample_id in sampleQuery:
                    #  get the weight of all baskets of this sample id
                    sql = ("SELECT weight FROM baskets WHERE ship=" + self.ship +
                            " AND survey=" + self.survey + " AND event_id=" + self.activeHaul +
                            " AND sample_id=" + sample_id)
                    query = self.db.dbQuery(sql)
                    for weight, in query:
                        try:
                            #  convert the string weight to float and append to
                            total_weight += float(weight)
                        except:
                            #  error converting basket weight to float - ignore this basket
                            pass

                #  update the partition weight in EVENT_DATA
                sql = ("UPDATE event_data set parameter_value=" + str(round(total_weight,3)) +
                        " WHERE ship=" + self.ship + " AND survey=" + self.survey +
                        " AND event_id=" + self.activeHaul + " AND partition='" +
                        partition + "' AND event_parameter='PartitionWeight'")


    def updateCatchSummary(self):
        '''
        updateCatchSummary updates the catch_summary table with data from this event. Data in catch_summary
        are generated outside the database and loaded into the table. These data need to be updated
        whenever the underlying data change. This method does this.

        '''

        event_id = self.activeHaul

        #  set the initial return state
        ok = True
        error_msg = ''

        try:

            #  create an instance of clamsbase functions
            clamsFunctions = Clamsbase2Functions.Clamsbase2Functions(self.db, self.ship,
                    self.survey)

            #  start a transaction to ensure that any other clients closed while this
            #  code is running are blocked until this transaction completes.
            self.db.startTransaction()

            #  delete existing data for this event
            sql = ("DELETE FROM catch_summary WHERE ship=" + self.ship + " AND survey=" + self.survey +
                    " AND event_id=" + event_id)
            self.db.dbExec(sql)

            #  find all the unique species samples
            sql = ("SELECT sample_id, parent_sample, partition, species_code, subcategory FROM samples " +
                    "WHERE ship=" + self.ship + " AND survey=" + self.survey + " AND event_id=" + event_id +
                    " AND sample_type='Species'")
            sampleQuery = self.db.dbQuery(sql)

            for sample_id, parent_sample, partition, species_code, subcategory in sampleQuery:
                #  call the computeCatchSummary method of clamsFunctions to, er compute the
                #  catch summary data.
                [status, vals]=clamsFunctions.computeCatchSummary(event_id, partition, species_code, subcategory)

                #  check if we successfully computed the summary data
                if status:
                    #  since status is OK, discard the empty error strings that can be returned in
                    #  vals. vals[0] is a list containing the following data:
                    #    vals = [sample id, species code, subcategory, sample id, WeightInHaul,SampledWeight,
                    #            NumberInHaul,SampledNumer,FrequencyExpansion,InMix,WholeHauled]
                    vals = vals[0]

                    #  get species name
                    sql = ("SELECT scientific_name, common_name FROM species WHERE species_code=" + species_code)
                    sppQuery = self.db.dbQuery(sql)
                    sci_name, common_name = sppQuery.first()

                    #  then insert results into catch summary table
                    sql = ("INSERT INTO catch_summary (ship,survey,event_id,partition,sample_id,parent_sample," +
                            "scientific_name,species_code,common_name,subcategory,weight_in_haul,sampled_weight," +
                            "number_in_haul,sampled_number,frequency_expansion,in_mix,whole_hauled) VALUES(" +
                            self.ship + "," + self.survey + "," + event_id + ",'" + partition + "'," + sample_id + "," +
                            parent_sample + ",'" + sci_name + "'," + species_code + ",'" + common_name +
                            "','" + subcategory + "'," + str(vals[4]) + "," + str(vals[5]) + "," +
                            str(vals[6]) + ","+str(vals[7]) + "," + str(vals[8]) + "," + str(vals[9]) +
                            "," + str(vals[10]) + ")")
                    self.db.dbExec(sql)
                else:
                    #  check to make sure there is an actionable error - computeCatchSummary can return false if there
                    #  is a sample with no measurements which we silently ignore here as it isn't necessarily an error
                    if (len(vals) > 0):
                        error_msg = ("Error computing catch summary data for event " +
                                event_id + ". Error text:" + vals[2]  + vals[1])
                        ok = False

                        #  rollback on error
                        self.db.rollback()

                        break

            #  update is complete - commit
            self.db.commit()

        except Exception as e:
            #  there was some issue updating the catch summary
            error_msg = ("Unknown error computing catch summary data for event " +
                    event_id + ". Error:" + str(e))
            ok = False

            #  rollback on error
            self.db.rollback()

        return (ok, error_msg)


    def sampleValidation1(self):
        '''
        sampleValidation1 performs some basic checks to make sure there aren't any obvious
        errors made during sampling.
        '''

        self.returnFlag = False

        #  loop thru the partitions doing common validations on the catch
        for partition in self.partitions:
            # loop though samples in this partition
            sql = ("SELECT species.common_name, samples.sample_id, samples.species_code, samples.subcategory" +
                    " FROM species, samples WHERE species.species_code = samples.species_code" +
                    " AND samples.event_id=" + self.activeHaul + " AND samples.ship=" + self.ship +
                    " AND samples.survey=" + self.survey + " AND samples.partition='" +
                    partition + "' and samples.sample_type = 'Species'")
            sampleQuery = self.db.dbQuery(sql)

            #  loop thru the sampes
            for species, key, code, subcat in sampleQuery:

                # validation #1 - check for species samples without weights
                sql = ("SELECT * FROM baskets WHERE sample_id=" + key+" AND event_id=" +
                        self.activeHaul + " AND ship=" + self.ship +
                        " AND survey=" + self.survey)
                query = self.db.dbQuery(sql)

                if not query.first():
                    # this sample has no basket weights
                    self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                            "You haven't weighed any baskets for " + species + " in the " +
                            partition + ". Do you want to return to sampling?", 'choice')
                    if self.message.exec():
                        #  return to sampling to fix problem
                        self.returnFlag = True
                        return
                    else:
                        #  user decided to delete the sample that doesn't have a weight
                        sql = ("DELETE FROM samples WHERE samples.sample_id = " + key+
                                " AND samples.event_id=" + self.activeHaul +
                                " AND samples.ship=" + self.ship +
                                " AND samples.survey=" + self.survey)
                        self.db.dbExec(sql)


                # validation #2 - are there samples of type measure lacking specimen (or length) data

                #  get the total basket weight for this sample
                sql = ("SELECT sum(weight) FROM baskets WHERE basket_type = 'Measure'" +
                        " AND sample_id=" + key+" AND event_id=" +
                        self.activeHaul + " AND ship=" + self.ship +
                        " AND survey=" + self.survey)
                query = self.db.dbQuery(sql)
                basketWeight, = query.first()
                basketWeight = float(basketWeight)

                #  make sure we have at least one basket with a weight for this sample
                if basketWeight != 0:
                    # there are "measure" baskets - check if there are specimen
                    sql = ("SELECT specimen_id FROM specimen WHERE sample_id = " + key+
                            " AND event_id=" + self.activeHaul + " AND ship=" +
                            self.ship + " AND survey=" + self.survey)
                    query = self.db.dbQuery(sql)

                    if query.first():
                        #  There are also specimen.

                        #  validation #3 - verify that there is an appropriate sample weight for
                        #  the number of specimen. First the get length/weight regression params
                        #  if available for this species
                        sql = ("SELECT parameter_value FROM species_data WHERE species_code="+
                                code + " AND subcategory='" + subcategory + "' AND lower(" +
                                "species_parameter)='a_param'")
                        query = self.db.dbQuery(sql)
                        aParm, = query.first()
                        if aParm:
                            try:
                                self.aParm=float(aParm)
                            except:
                                self.aParm=None
                        else:
                            self.aParm=None
                        sql = ("SELECT parameter_value FROM species_data WHERE species_code="+
                                code + " AND subcategory='" + subcategory +
                                "' AND lower(species_parameter)='b_param'")
                        query = self.db.dbQuery(sql)
                        bParm, = query.first()
                        if bParm:
                            try:
                                self.bParm=float(bParm)
                            except:
                                self.bParm=None
                        else:
                            self.bParm=None

                        #  if we have length/weight parameters for this species we'll compute
                        #  a theoretical weight
                        if self.aParm and self.bParm:
                            #  get the lengths
                            sql = ("SELECT measurement_value FROM  measurements WHERE " +
                                    "sample_id=" + key + "  AND event_id=" + self.activeHaul +
                                    " AND ship=" + self.ship +" AND survey=" + self.survey+
                                    " AND LOWER(measurement_type) LIKE '%length%'")
                            query = self.db.dbQuery(sql)

                            #  sum up the theoretical weights for the sampled lengths
                            calcWeight = 0
                            for length, in query:
                                try:
                                    length = float(length)
                                    calcWeight += (length ** self.aParm) * self.bParm
                                except:
                                    #  skip over bad data
                                    pass

                            #  if there are no measured fish we have to move on
                            if calcWeight==0:
                                continue

                            #  Compare the sample weight and the theoretical weight
                            deviation = (calcWeight - basketWeight) / calcWeight

                            #  check that the two weights are within the allowed threshold
                            if abs(deviation) > float(self.settings['SubSampleCheckThreshold']):
                                # The sample deviates too much from the theoretical weight
                                self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                                        "The weight of the measured sample is " +
                                        str(round(1+deviation, 0)) + "% different from the estimated " +
                                        "weight for " + species + " in the " + partition +
                                        " using length weight regression of measured fish. You might " +
                                        "have misclassified a Basket." + " Do you want to return to "
                                        "the sampling?", 'choice')
                                if self.message.exec():
                                    #  return to fix the problem
                                    self.returnFlag = True
                                    return
                                else:
                                    #  Ignore the problem - insert into override table
                                    self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                                            "OK. This exception has been logged in the overrides table.", 'info')
                                    self.message.exec()

                                    #  insert into overrides table
                                    overrideDesc = ("'Bad subsample weight. Total sampled weight=" +
                                            str(round(basketWeight,2)) + " Theoretical weight=" +
                                            str(round(calcWeight,2)) + "'")
                                    sql = ("INSERT INTO overrides (ship,survey,event_id,record_id,table_name," +
                                            "scientist,description) VALUES (" + self.ship + ", " + self.survey +
                                            "," + self.activeHaul + "," + key + ",'baskets','" +
                                            self.scientist + "'," + overrideDesc + ")")
                                    self.db.dbExec(sql)

                                    self.returnFlag = False

                    else:
                        # Huh, there are baskets with no specimen
                        self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                                "You have some basket weights of type 'Measure' for " + species +
                                " in the " + partition + " but no measurements!  Are you able " +
                                "to live with yourself?", 'choice')
                        if not self.message.exec():
                            self.returnFlag=True
                            return

