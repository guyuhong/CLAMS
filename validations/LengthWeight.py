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
.. module:: LengthWeight

    :synopsis: LengthWeight checks that the measured weight falls within
               the expected range given the previously recorded length
               using the length weight regression for the specified
               species+subcategory

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

class LengthWeight(QObject):

    def __init__(self, db, speciesCode,  subcategory='None'):
        '''
            The init methods of CLAMS validations are run whenever a new protocol
            or species is selected in the specimen module. Any setup that the
            validation requires should be done here. The three input arguments are:

                db - a reference to the active dbConnection class object
                speciesCode - the species code of the current specimen
                subcategory - the subcategory of the current specimen

            If you need to pass additional data to a validation, you should
            add this data to the species_data table and query it out here in
            the init method (see LengthRange.py for example.)

        '''

        #  call the superclass init
        QObject.__init__(self, None)

        #  get the length to weight regression parameters for this species+subcat from
        #  the species_data table

        #  Get the valid length weight parameters for this species from the species table
        sql=("SELECT parameter_value FROM species_data WHERE species_code="+speciesCode+
             " AND subcategory='"+subcategory+"' AND lower(species_parameter)='a_param'")
        query = db.dbQuery(sql)
        aParam, = query.first()
        if aParam:
            #  don't convert to float here, we'll do that in the validate method so
            #  it is easier to report a parameter issue to the user
            self.aParm = aParam
        else:
            self.aParm = None

        sql=("SELECT parameter_value FROM species_data WHERE species_code="+speciesCode+
             " AND subcategory='"+subcategory+"' AND lower(species_parameter)='b_param'")
        query = db.dbQuery(sql)
        bParam, = query.first()
        if bParam:
            #  don't convert to float here, we'll do that in the validate method so
            #  it is easier to report a parameter issue to the user
            self.bParm = bParam
        else:
            self.bParm = None

        # get the allowable deviation tolerance
        sql = "SELECT parameter_value FROM application_configuration WHERE lower(parameter)='lw_tolerance'"
        query = db.dbQuery(sql)
        lwTolerance, = query.first()
        if lwTolerance:
            self.tolerance = lwTolerance
        else:
            self.tolerance = None


    def validate(self, currentValue,  measurements,  values):
        '''
            The validate method is called when a measurement is made for a specific
            measurement type. Each measurement can have from 0-N validations. When
            a specific measurement is made, say "barcode", all validations
            assigned to the barcode measurement will have their validate methods
            called. Each one should verify that the currentValue is valid based
            on the logic of each particular validation.

                currentValue - the just measured value
                measurements - a list of the measurement types for this
                    protocol, in order.
                values - a list of the stored values of those measurements.
                    In order of the measurements.

            This validation checks that a measured weight falls within the
            expected range given a previously measured length and the length
            weight regression for the species+subcat. For this validation
            to work, the length measurement must come before the weight
            measurement in the protocol.

            This is a fairly simple example, but the validation can be much
            more complex (but usually don't need to be.) Also, remember that
            these run each time a measurement configured for the validation
            runs so you don't want them to take too long to execute as it
            will slow data collection.

        '''
        #  check if we don't have any regression params
        if self.aParm is None and self.bParm is None and self.tolerance is None:
            #  there are no lw regression parameters for this species+subcat so bail
            result = (True, '')
            return result

        #  check if we have all params and they are numeric - obviously this would be
        #  more efficient to do this in the init but we don't have a mechanism to raise
        #  errors like this during the validation init so we're going to do it here.
        try:
            aParam = float(self.aParm)
        except:
            result = (False, "LengthWeight Validation Error. Non-numeric 'a_param' for " +
                    "this species+subcateory.")
            return result
        try:
            bParam = float(self.bParm)
        except:
            result = (False, "LengthWeight Validation Error. Non-numeric 'b_param' for " +
                    "this species+subcateory.")
            return result
        try:
            lwTolerance = float(self.tolerance)
        except:
            result = (False, "LengthWeight Validation Error. Non-numeric 'lw_tolerance' for " +
                    "this species+subcateory.")
            return result

        try:
            weight = float(currentValue)
        except:
            result = (False, "Non-numeric weight recorded!?! You should re-weigh your specimen.")
            return result

        #  TODO: make sure that internally all length measurements (e.g. fork_length, total_length,
        #        bell_diameter, etc.) are passed in the measurements dict as "length". Initially "length"
        #        measurements were not specific and were simply called "length" but that was changed
        #        and I don't know if a generic 'length' is currently used or the specific length type
        #        is passed in the measurements dict. If the specific type is passed, this code needs
        #        to be updated to match

        #  get the measured length
        length = float(values[measurements.index('length')])
        if length == None:
            result = (False, "There's no length recorded yet! LengthWeight validation cannot run.")
            return result

        #  calculate the theoretical weight based on the length and LW regression
        calcWt = (length ** aParam) * bParam

        #  compute the allowable deviation
        errorDev = (weight / calcWt - 1) * 100

        #  ensure that the weight is within tolerance
        if abs(errorDev) > lwTolerance:
           #  length weight check failed - weight is outside valid range
            result = (False, 'This weight is ' + str(round((errorDev+100), 0)) +
                    ' % of the expected weight. Do you want to re-enter the weight?')
        else:
            #  length weight check succeeded - weight is o.k.
            result = (True, '')

        return result

'''
The validationTest class enables testing of validations by creating a database
connection, creating an instance of the validation object, and then executing its
validate method.

This class will need to be customized a bit for each individual validation.
'''
class validationTest(QObject):
        def __init__(self):
            super(validationTest, self).__init__(None)

            #  we use a timer here to add runTest to the event processing queue and
            #  then exit the init. Execution will return to main, where the
            #  application event loop will be started by the call to app.exec() which
            #  will then start processing events on the queue which will then execute
            #  runTest with the event loop running.
            startTimer = QTimer(self)
            startTimer.timeout.connect(self.runTest)
            startTimer.setSingleShot(True)
            startTimer.start(0)


        def runTest(self):
            '''runTest attempts to create a database connection by presenting a dialog
            requesting credentials. If successful, it instantiates the validation and
            runs the validate method of said validation. You should set up any
            specific parameters required for this validation's test here.
            '''

            #  set up the required parameters for this test
            speciesCode = '21740'
            subcategory = 'None'
            currentValue = '.0000055'
            measureTypes = ['length']
            values = [1]

            #  create a connection dialog to get connection params - by default
            #  this will create a dbConnection object and store it in the "db"
            #  attribute.
            conenctionDialog = connectdlg.ConnectDlg(None, None, None)
            ok = conenctionDialog.exec()

            #  if we've connected to the database, create and run the validation
            if ok:
                db = conenctionDialog.db

                #  create the validation using the db connection and specified species
                #  and subcategory.
                self.validation = LengthWeight(db, speciesCode, subcategory)

                #  execute the validation
                ok = self.validation.validate(currentValue, measureTypes, values)

                #  print the results
                print(ok)

            else:
                print("Unable to connect to the database")

            #  exit the application
            QApplication.instance().quit()


if __name__ == '__main__':
    #  import test specific libraries
    import sys
    from pathlib import Path
    from PyQt6.QtCore import *
    from PyQt6.QtGui import *
    from PyQt6.QtWidgets import *

    file = Path(__file__).resolve()
    sys.path.append(str(file.parents[1]))
    import connectdlg

    #  create an instance of QApplication
    app = QApplication(sys.argv)

    #  instantiate the test
    form = validationTest()

    #  and start the application event loop
    app.exec()

