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
    :module:: HaulWtSelDlg

    :synopsis: HaulWtSelDlg is presented when the user clicks the
               "Haul Weight Type" button for any partition in the
               Haul form. This is where the user selects how they
               will determine/enter the total weight of the catch.

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

from PyQt6.QtWidgets import QDialog
import loadcelldialog
import bindialog
import numpad
from ui import ui_HaulWtSelDlg

class HaulWtSelDlg(QDialog, ui_HaulWtSelDlg.Ui_haulwtselDlg):
    def __init__(self,  parent=None):
        super(HaulWtSelDlg, self).__init__(parent)
        self.setupUi(self)
        self.ok=False
        self.settings=parent.settings
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.message=parent.message
        self.numpad=numpad.NumPad(self)

        self.btn_0.setText("Not Subsampled")
        self.btn_1.setText("Bin Volumetric")
        self.btn_2.setText("Load Cell")
        self.btn_3.setText("Guesstimate")

        # hook up slots
        self.btn_0.clicked.connect(self.noSubsample)
        self.btn_1.clicked.connect(self.binVolumetric)
        self.btn_2.clicked.connect(self.loadCell)
        self.btn_3.clicked.connect(self.getGuess)


    def noSubsample(self):

        self.weightType = "not_subsampled"
        self.weight = 'TBD'
        self.ok=True
        self.close()


    def binVolumetric(self):
        '''
            getBinVolumetric displays the modal bin dialog so the user
            can enter the value.  If the user clicks ok the weight
            label is updated.
        '''

        BinDlg = bindialog.BinDialog(self)
        if BinDlg.exec_():
            self.weight = BinDlg.haulWT
            self.weightType = "bin_volumetric"
            self.ok=True
            self.close()


    def loadCell(self):
        '''
            getLoadCell displays the modal load cell dialog so the user
            can enter the load cell value.  If the user clicks ok the weight
            label is updated.
        '''

        LCellDlg = loadcelldialog.LoadCellDialog(self)
        if LCellDlg.exec_():
            self.weight = LCellDlg.haulWt
            self.weightType = "load_cell"
            self.ok=True
            self.close()


    def getGuess(self):
        '''
            getGuess displays the number pad so the user can enter their
            visual estimate. If the user clicks ok the weight label is
            updated.
        '''
        self.numpad.msgLabel.setText("Enter your visual estimate" )
        if self.numpad.exec_():
            self.weight = self.numpad.value
            self.weightType = "visual_estimate"
            self.ok=True
            self.close()



