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
.. module:: ABLSpecialStudiesDlg

    :synopsis: ABLSpecialStudiesDlg presents a dialog to choose optional special studies
                performed; specific for ABL

| Developed by:  Rick Towler   <rick.towler@noaa.gov>
|                Kresimir Williams   <kresimir.williams@noaa.gov>
| National Oceanic and Atmospheric Administration (NOAA)
| National Marine Fisheries Service (NMFS)
| Alaska Fisheries Science Center (AFSC)
| Midwater Assessment and Conservation Engineering Group (MACE)
|
| Author:
|       Rick Towler   <rick.towler@noaa.gov>
|       Kresimir Williams   <kresimir.williams@noaa.gov>
| Maintained by:
|       Rick Towler   <rick.towler@noaa.gov>
|       Kresimir Williams   <kresimir.williams@noaa.gov>
|       Mike Levine   <mike.levine@noaa.gov>
|       Nathan Lauffenburger   <nathan.lauffenburger@noaa.gov>
| Updated December 2024 by:
|       Alicia Billings <alicia.billings@noaa.gov>
|           specific updates:
|               - PyQt import statement
|               - signal/slot connections
|               - moved variable declarations into __init__
|               - added some function explanation
|               - fixed any PEP8 issues
|               - added a main to test if works (commented out)
"""

from PyQt6.QtWidgets import *
from ui import ui_ABLSpecialStudiesDlg
from sys import argv


class ABLSpecialStudiesDlg(QDialog, ui_ABLSpecialStudiesDlg.Ui_ablspeciesstudiesDlg):
    def __init__(self,  parent=None):
        super(ABLSpecialStudiesDlg, self).__init__(parent)
        self.setupUi(self)

        # variable declarations
        self.stomach = ''
        self.isotopeMarsh = ''
        self.isotopeAndrews = ''
        self.genetics = ''
        self.otolith = ''
        self.energetic = ''
        self.tsmri = ''
        self.sp_st = ''
        self.sp_ot = ''
        self.sp_ge = ''
        self.sp_isM = ''
        self.sp_isA = ''
        self.sp_en = ''
        self.sp_ts = ''
        self.result = ()

        # signal/slot connections
        self.otolithBtn.clicked.connect(self.getOtolith)
        self.stomachBtn.clicked.connect(self.getStomach)
        self.isotopeMarshBtn.clicked.connect(self.getIsotopeM)
        self.isotopeAndrewsBtn.clicked.connect(self.getIsotopeA)
        self.geneticsBtn.clicked.connect(self.getGenetics)
        self.energeticBtn.clicked.connect(self.getEnergetic)
        self.tsmriBtn.clicked.connect(self.getTSMRI)
        self.doneBtn.clicked.connect(self.Enter)
        self.clearBtn.clicked.connect(self.Clear)

    def setup(self, parent):
        """
        sets the text of all of the buttons and unchecks all of them
        :param parent: not used in this function
        :return: none
        """
        # set button texts
        self.stomachBtn.setText('Stomach')
        self.otolithBtn.setText('Otolith')
        self.geneticsBtn.setText('Genetics')
        self.isotopeMarshBtn.setText('Honeyfield')
        self.isotopeAndrewsBtn.setText('Isotope_Andrews')
        self.energeticBtn.setText('Energetics')
        self.tsmriBtn.setText('TSMRI')

        # uncheck all buttons
        self.stomachBtn.setChecked(False)
        self.otolithBtn.setChecked(False)
        self.geneticsBtn.setChecked(False)
        self.isotopeMarshBtn.setChecked(False)
        self.isotopeAndrewsBtn.setChecked(False)
        self.energeticBtn.setChecked(False)
        self.tsmriBtn.setChecked(False)

    def getStomach(self):
        """
        sets the self.stomach and self.sp_st variables and changes the text to 'Collected' for the stomach button
        :return: none
        """
        self.stomach = 'STOM'
        self.stomachBtn.setText('Collected')
        self.sp_st = ','

    def getIsotopeM(self):
        """
        sets the self.isotopeMarsh and self.sp_isM variables and changes the text to 'Collected' for the
        Isotope_Marsh button
        :return: none
        """
        self.isotopeMarsh = 'Honeyfield'
        self.isotopeMarshBtn.setText('Collected')
        self.sp_isM = ','

    def getIsotopeA(self):
        """
        sets the self.isotopeAndrews and self.sp_isA variables and changes the text to 'Collected' for the
        Isotope_Andrews button
        :return: none
        """
        self.isotopeAndrews = 'ISO_Andrews'
        self.isotopeAndrewsBtn.setText('Collected')
        self.sp_isA = ','

    def getOtolith(self):
        """
        sets the self.otolith and self.sp_ot variables and changes the text to 'Collected' for the otolith button
        :return: none
        """
        self.otolith = 'OTO'
        self.otolithBtn.setText('Collected')
        self.sp_ot = ','

    def getGenetics(self):
        """
        sets the self.genetics and self.sp_ge variables and changes the text to 'Collected' for the genetics button
        :return: none
        """
        self.genetics = 'GEN'
        self.geneticsBtn.setText('Collected')
        self.sp_ge = ','

    def getTSMRI(self):
        """
        sets the self.tsmri and self.sp_ts variables and changes the text to 'Collected' for the tsmri button
        :return: none
        """
        self.tsmri = 'TSMRI'
        self.tsmriBtn.setText('Collected')
        self.sp_ts = ','

    def getEnergetic(self):
        """
        sets the self.energetic and self.sp_en variables and changes the text to 'Collected' for the
        energetics button
        :return: none
        """
        self.energetic = 'ENRG'
        self.energeticBtn.setText('Collected')
        self.sp_en = ','

    def Clear(self):
        """
        'clears' all of the clicks by resetting the variables and the button texts and unchecks the buttons
        :return: none
        """
        # reset variables
        self.stomach = ''
        self.isotopeMarsh = ''
        self.isotopeAndrews = ''
        self.genetics = ''
        self.energetic = ''
        self.otolith = ''
        self.tsmri = ''
        self.sp_st = ''
        self.sp_ot = ''
        self.sp_ge = ''
        self.sp_isM = ''
        self.sp_isA = ''
        self.sp_en = ''
        self.sp_ts = ''

        # reset button text
        self.isotopeMarshBtn.setText('Isotope_Marsh')
        self.isotopeAndrewsBtn.setText('Isotope_Andrews')
        self.stomachBtn.setText('Stomach')
        self.otolithBtn.setText('Otolith')
        self.geneticsBtn.setText('Genetics')
        self.energeticBtn.setText('Energetics')
        self.tsmriBtn.setText('TSMRI')

        # uncheck buttons
        self.stomachBtn.setChecked(False)
        self.otolithBtn.setChecked(False)
        self.geneticsBtn.setChecked(False)
        self.energeticBtn.setChecked(False)
        self.isotopeMarshBtn.setChecked(False)
        self.isotopeAndrewsBtn.setChecked(False)
        self.tsmriBtn.setChecked(False)

    def Enter(self):
        """
        sets the result tuple to access from the calling dialog with the variables
        :return: self.accept the dialog and return
        """
        self.result = (True, self.tsmri + self.sp_ts + self.stomach + self.sp_st + self.otolith + self.sp_ot +
                       self.genetics + self.sp_ge + self.energetic + self.sp_en + self.isotopeMarsh +
                       self.sp_isM + self.isotopeAndrews)

        if self.result[-1] != '':
            if self.result[-1][-1] == ',':
                self.result = (True, self.result[-1][0:-1])
            self.accept()

    def closeEvent(self, event):
        """
        sets the result tuple to access from the calling dialog
        :return: self.reject and return
        """
        self.result = (False, '')
        self.reject()


"""
if __name__ == "__main__":
    #  create an instance of QApplication
    app = QApplication(argv)
    #  create an instance of the dialog
    form = ABLSpecialStudiesDlg()
    #  show it
    form.show()
    #  and start the application...
    app.exec()
"""
