'''

    VialNumberDuplicate

    VialNumberDuplicate is a CLAMS validation class that checks if finclip_vial_number is a duplicate finclip_vial_number within a Survey

    Validations are classes that are used by the CLAMS specimen module
    to check


'''
from PyQt4.QtCore import *
from PyQt4 import QtSql

class FinclipVialNumberDuplicate(QObject):

    def __init__(self, db, speciesCode,  subcategory='None'):
        '''
            The init methods of CLAMS validations are run whenever a new protocol
            or species is selected in the specimen module. Any setup that the
            validation requires should be done here. The two input arguments are:

                db - a reference to the CLAMS QtSQLDatabase object
                speciesCode - the

        '''

        #  call the superclass init
        QObject.__init__(self, None)


    def validate(self,  currentValue,  measurements,  values):
        '''
            The validate method is called when
        '''

        vial_num = currentValue
        query=QtSql.QSqlQuery("SELECT parameter_value FROM application_configuration WHERE parameter = 'ActiveSurvey'")
        query.first()
        survey=query.value(0).toString()
        query=QtSql.QSqlQuery("SELECT parameter_value FROM application_configuration WHERE parameter = 'ActiveEvent'")
        query.first()
        event_id=query.value(0).toString()        
        query=QtSql.QSqlQuery("SELECT device_id FROM measurements WHERE measurement_type ='finclip_vial_num' AND measurement_value ='"+vial_num+"' AND survey ="+survey+ 'AND event_id = ' +event_id)
        if query.first():
            #  number check failed - number is a repeat within this haul and survey
            result = (False, 'This vial number already exists in the database for this haul.  Do you want to re-enter?')

        else:
            #  number check succeeded - vial number is o.k.
            result = (True, '')

        return result

