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
    :module:: TakingOvaryFemaleRockfish

    :synopsis: TakingOvaryFemaleRockfish is a conditional that checks if a body should be frozen

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
        Melina Shak <melina.shak@noaa.gov>
"""
import unittest

from PyQt6.QtCore import *

class TakingOvaryFemaleRockfish(QObject):

    def __init__(self, db):
        '''
            The init methods of CLAMS conditionals are run whenever a new protocol
            or species is selected in the specimen module. Any setup that the
            conditional requires should be done here. The three input arguments are:

                db - a reference to the active dbConnection class object

            If you need to pass additional data to a validation, you should
            add this data to the species_data table and query it out here in
            the init method (see LengthRange.py for example.)

        '''
        #  call the superclass init
        QObject.__init__(self, None)


    def evaluate(self, measurements, values, result):
        '''
            The evaluate method is called when a measurement is taken to determine
            what changes in the protocol. Each measurement can have from 0-N validations. When
            a specific measurement is made, say "barcode", all validations
            assigned to the barcode measurement will have their validate methods
            called. Each one should verify that the currentValue is valid based
            on the logic of each particular validation.

                measurements - a list of the measurement types for this
                    protocol, in order.
                values - a list of the stored values of those measurements.
                    In order of the measurements.
                result -

            For example, this conditional is for the body count measurement and when
            a count value is logged, it will check to see if that value is greater than 50.

            This is a fairly simple example, but the conditional can be
            more complex (but usually don't need to be.) Also, remember that
            these run each time a measurement configured for the conditional
            runs so you don't want them to take too long to execute as it
            will slow data collection.

        '''

        #  first make sure we have a sex measurement...
        if values[measurements.index('sex')]:
            
            if str(values[measurements.index('sex')]).lower()=='male':
                #  for males we don't take ovaries, their weights, or livers
                if 'ovary_taken' in measurements:
                    result[measurements.index('ovary_taken')]=False
            
            
            #  DISABLE THIS CODE FOR WINTER 2013 - We want the option to weigh ovaries even
            #  though we aren't taking a specimen for preservation.
#            elif values[measurements.index('ovary_taken')]=='0':
#                #  if we don't take an ovary from a female, we don't get the weight or take a liver
#                if 'liver_weight' in measurements:
#                    result[measurements.index('liver_weight')]=False
#                if 'ovary_weight' in measurements:
#                    result[measurements.index('ovary_weight')]=False

        return result

'''
The conditionalTest class enables testing of conditionals by creating an 
instance of the conditional object, and then executing its evaluate method.

This class will need to be customized a bit for each individual validation.
'''
class conditionalTest(unittest.TestCase):
    db = None
    takingOvaryFemaleRockfish = TakingOvaryFemaleRockfish(db)

    measurements = ['sex', 'ovary_taken']

    def testMale(self):
        values = ['male']
        results = [1, 2]

        ok = self.takingOvaryFemaleRockfish.evaluate(self.measurements, values, results)
        self.assertEqual([1, False], ok)

    def testFemale(self):
        values = ['female']
        results = [1, 2]

        ok = self.takingOvaryFemaleRockfish.evaluate(self.measurements, values, results)
        self.assertEqual([1, 2], ok)

if __name__ == '__main__':
    unittest.main()

