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
.. module:: LengthRange

    :synopsis: LengthRange is a validation that queries the database using
               species code and subcategory to get the min and max length values
               for that species+subcategory. Returns false if the length falls
               outside the accepted range.

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

class LengthRange(QObject):

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

        #  Get the minimum length for this species from the species_data table
        sql = ("SELECT parameter_value FROM species_data WHERE species_code=" + speciesCode +
               " AND subcategory='" + subcategory + "' AND lower(species_parameter)='min_length'")
        query = db.dbQuery(sql)
        minLength, = query.first()
        if minLength:
            try:
                self.minLength = float(minLength)
            except:
                self.minLength = 0
        else:
            self.minLength = 0

        #  Get the maximum length for this species from the species_data table
        sql = ("SELECT parameter_value FROM species_data WHERE species_code="+ speciesCode +
               " AND subcategory='"+subcategory+"' AND lower(species_parameter)='max_length'")
        query = db.dbQuery(sql)
        maxLength, = query.first()
        if maxLength:
            try:
                self.maxLength = float(maxLength)
            except:
                self.maxLength = 9999
        else:
            self.maxLength = 9999


    def validate(self, currentValue, measureTypes, values):
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

            This validation checks if the measured length is within the range
            of acceptable lengths for this species+subcategory.

            This is a fairly simple example, but the validation can be much
            more complex (but usually don't need to be.) Also, remember that
            these run each time a measurement configured for the validation
            runs so you don't want them to take too long to execute as it
            will slow data collection.
        '''

        #  make sure the length is numeric
        try:
            thisLength = float(currentValue)
        except:
            result = (False, 'Non-numeric length value collected. Do you want to re-enter length?')
            return result

        #  check if the length is within the valid range
        if (thisLength < self.minLength) or (thisLength > self.maxLength):
            #  Length check failed - Length is outside valid range
            result = (False, 'The length is out of range for this species. Do you want to re-enter length?')

        else:
            # Length check succeeded - Length is o.k.
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
            currentValue = 50
            measureTypes = []
            values = [None]

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
                self.validation = LengthRange(db, speciesCode, subcategory)

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


