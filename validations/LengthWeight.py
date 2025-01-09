'''

    checkOrganismWeight

    checkOrganismWeight is a CLAMS validation class that checks if

    Validations are classes that are used by the CLAMS specimen module
    to check
    
    Validation on pollock length weight relationship updated KW/TH/ML on 02/02/2020 based on all
    collected pollock length weights to date (~116k)


'''
from PyQt6.QtCore import *

class LengthWeight(QObject):

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

        #  Get the valid length weight parameters for this species from the species table
        sql=("SELECT parameter_value FROM species_data WHERE species_code="+speciesCode+
             " AND subcategory='"+subcategory+"' AND lower(species_parameter)='a_param'")
        query = self.db.dbQuery(sql)
        aParam, = query.first()
        if aParam:
            self.aParm=float(aParam)
        else:
            self.aParm=0

        sql=("SELECT parameter_value FROM species_data WHERE species_code="+speciesCode+
             " AND subcategory='"+subcategory+"' AND lower(species_parameter)='b_param'")
        query = self.db.dbQuery(sql)
        bParam, = query.first()
        if bParam:
            self.bParm=float(bParam)
        else:
            self.bParm=999

        # get the deviation tolerance
        sql = "SELECT parameter_value FROM application_configuration WHERE lower(parameter)='lw_tolerance'"
        query = self.db.dbQuery(sql)
        lwTolerance, = query.first()
        self.tolerance=float(lwTolerance)

    def validate(self, currentValue,  measurements,  values):
        '''
            The validate method is called when
        '''

        weight = float(currentValue)
        length = float(values[measurements.index('length')])
        if length==None:
            result = (False, "There's no length")
            return result
        if self.aParm<0.1:# theres no lw parameters for this species
            result = (True, '')
            return result
        calcWt=(length**self.aParm)*self.bParm
        errorDev=(weight/calcWt-1)*100
        if abs(errorDev)>self.tolerance:# bad weight
           #  length weight check failed - weight is outside valid range
            result = (False, 'This weight is '+str(round((errorDev+100), 0))+' % of the expected weight. Do you want to re-enter the weight?')

        else:
            #  length weight check succeeded - weight is o.k.
            result = (True, '')

        return result

