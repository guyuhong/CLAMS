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
.. module:: ABLJuvSalmonSpecialStudiesDlg

    :synopsis: ABLJuvSalmonSpecialStudiesDlg presents a dialog to choose optional special studies
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
from ui import ui_ABLJuvSalmonSpecialStudiesDlg
from sys import argv


class ABLJuvSalmonSpecialStudiesDlg(QDialog, ui_ABLJuvSalmonSpecialStudiesDlg.Ui_abljuvsalmonspeciesstudiesDlg):
    def __init__(self,  parent=None):
        super(ABLJuvSalmonSpecialStudiesDlg, self).__init__(parent)
        self.setupUi(self)

        # variable declarations
        self.stomach = ''
        self.isotope = ''
        self.wf = ''
        self.fh = ''
        self.bia = ''
        self.igf = ''
        self.thiamine = ''
        self.sp_st = ''
        self.sp_wf = ''
        self.sp_fh = ''
        self.sp_is = ''
        self.sp_igf = ''
        self.sp_bia = ''
        self.sp_th = ''
        self.result = ()

        # signal/slot connections
        self.wfBtn.clicked.connect(self.getWF)
        self.stomachBtn.clicked.connect(self.getStomach)
        self.isotopeBtn.clicked.connect(self.getIsotope)
        self.fhBtn.clicked.connect(self.getFH)
        self.biaBtn.clicked.connect(self.getBIA)
        self.igfBtn.clicked.connect(self.getIGF)
        self.thiamineBtn.clicked.connect(self.getNutrition)
        self.doneBtn.clicked.connect(self.Enter)
        self.clearBtn.clicked.connect(self.Clear)

    def setup(self, parent):
        """
        sets the text of all of the buttons and unchecks all of them
        :param parent: not used in this function
        :return: none
        """
        # set button text
        self.stomachBtn.setText('Stomach')
        self.wfBtn.setText('Whole Fish')
        self.fhBtn.setText('Fish Head')
        self.isotopeBtn.setText('Isotope')
        self.biaBtn.setText('BIA')
        self.igfBtn.setText('IGF')
        self.thiamineBtn.setText('Nutrition')

        # uncheck all buttons
        self.stomachBtn.setChecked(False)
        self.wfBtn.setChecked(False)
        self.fhBtn.setChecked(False)
        self.isotopeBtn.setChecked(False)
        self.igfBtn.setChecked(False)
        self.biaBtn.setChecked(False)
        self.thiamineBtn.setChecked(False)

    def getStomach(self):
        """
        sets the self.stomach and self.sp_st variables and changes the text to 'Collected' for the stomach button
        :return: none
        """
        self.stomach = 'STOM'
        self.stomachBtn.setText('Collected')
        self.sp_st = ','

    def getIsotope(self):
        """
        sets the self.isotope and self.sp_is variables and changes the text to 'Collected' for the isotope button
        :return: none
        """
        self.isotope = 'ISO'
        self.isotopeBtn.setText('Collected')
        self.sp_is = ','

    def getWF(self):
        """
        sets the self.wf and self.sp_wf variables and changes the text to 'Collected' for the whole fish button
        :return: none
        """
        self.wf = 'WF'
        self.wfBtn.setText('Collected')
        self.sp_wf = ','

    def getFH(self):
        """
        sets the self.fh and self.sp_fh variables and changes the text to 'Collected' for the fish head button
        :return: none
        """
        self.fh = 'FH'
        self.fhBtn.setText('Collected')
        self.sp_fh = ','

    def getIGF(self):
        """
        sets the self.igf and self.sp_igf variables and changes the text to 'Collected' for the igf button
        :return: none
        """
        self.igf = 'IGF'
        self.igfBtn.setText('Collected')
        self.sp_igf = ','

    def getBIA(self):
        """
        sets the self.bia and self.sp_bia variables and changes the text to 'Collected' for the bia button
        :return: none
        """
        self.bia = 'BIA'
        self.biaBtn.setText('Collected')
        self.sp_bia = ','

    def getNutrition(self):
        """
        sets the self.thiamine and self.sp_th variables and changes the text to 'Collected' for the thiamine button
        :return: none
        """
        self.thiamine = 'NUT'
        self.thiamineBtn.setText('Collected')
        self.sp_th = ','

    def Clear(self):
        """
        'clears' all of the clicks by resetting the variables and the button texts and unchecks the buttons
        :return: none
        """
        # reset the variables
        self.stomach = ''
        self.isotope = ''
        self.wf = ''
        self.fh = ''
        self.bia = ''
        self.igf = ''
        self.thiamine = ''
        self.sp_st = ''
        self.sp_wf = ''
        self.sp_fh = ''
        self.sp_is = ''
        self.sp_igf = ''
        self.sp_bia = ''
        self.sp_th = ''

        # reset the button texts
        self.isotopeBtn.setText('Isotope')
        self.wfBtn.setText('Whole Fish')
        self.stomachBtn.setText('Stomach')
        self.fhBtn.setText('Fish Head')
        self.biaBtn.setText('BIA')
        self.igfBtn.setText('IGF')
        self.thiamineBtn.setText('Nutrition')

        # uncheck all buttons
        self.stomachBtn.setChecked(False)
        self.wfBtn.setChecked(False)
        self.fhBtn.setChecked(False)
        self.biaBtn.setChecked(False)
        self.isotopeBtn.setChecked(False)
        self.igfBtn.setChecked(False)
        self.thiamineBtn.setChecked(False)

    def Enter(self):
        """
        sets the result tuple to access from the calling dialog with the variables
        :return: self.accept the dialog and return
        """
        self.result = (True, self.thiamine + self.sp_th + self.stomach + self.sp_st + self.wf + self.sp_wf +
                       self.fh + self.sp_fh + self.bia + self.sp_bia + self.igf + self.sp_igf + self.isotope)

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
    form = ABLJuvSalmonSpecialStudiesDlg()
    #  show it
    form.show()
    #  and start the application...
    app.exec()
"""
