'''

    checkOrganismWeight

    checkOrganismWeight is a CLAMS validation class that checks if

    Validations are classes that are used by the CLAMS specimen module
    to check


'''

from PyQt6.QtCore import *

class LengthRange(QObject):

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

        #  Get the valid weight range for this species from the species table
        sql = ("SELECT parameter_value FROM species_data WHERE species_code="+speciesCode+
               " AND subcategory='"+subcategory+"' AND lower(species_parameter)='min_length'")
        query = self.db.dbQuery(sql)
        minLength, = query.first()
        if minLength:
            self.minLength=float(minLength)
        else:
            self.minLength=0
        sql = ("SELECT parameter_value FROM species_data WHERE species_code="+speciesCode+
               " AND subcategory='"+subcategory+"' AND lower(species_parameter)='max_length'")
        query = self.db.dbQuery(sql)
        maxLength, = query.first()
        if maxLength:
            self.maxLength=float(maxLength)
        else:
            self.maxLength=999


    def validate(self,   currentValue,  measurements,  values):
        '''
            The validate method is called when
        '''

        thisLength = float(currentValue)
        if (thisLength < self.minLength) or (thisLength > self.maxLength):
            #  Length check failed - Length is outside valid range
            result = (False, 'The length is out of range for this species. Do you want to re-enter length?')

        else:
            # Length check succeeded - Length is o.k.
            result = (True, '')

        return result

