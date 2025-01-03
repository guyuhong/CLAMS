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
.. module:: CodendStatusDlg

    :synopsis: CodendStatusDlg displays the codend status dialog
               that allows the user to enter the state of the codend
               when the net is retrieved.

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
from ui import ui_CodendStatusDlg


class CodendStatusDlg(QDialog, ui_CodendStatusDlg.Ui_codendStatusDlg):
    def __init__(self, sciName, parent=None):
        super(CodendStatusDlg, self).__init__(parent)
        self.setupUi(self)
        self.survey=parent.survey
        self.ship=parent.ship
        self.activeHaul=parent.activeHaul
        self.activePartition=parent.activePartition
        self.state_value=None
        self.firstName=sciName
        self.errorIcons=parent.errorIcons
        self.errorSounds=parent.errorSounds
        self.message=parent.message
        self.btns = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5]
        for btn in self.btns:
            btn.clicked.connect(self.getStatus)

        self.exitTimer = QTimer(self)
        self.exitTimer.setSingleShot(True)
        self.exitTimer.timeout.connect(self.close)


    def getStatus(self):
        btn = self.sender()
        if btn.isChecked():
            self.state_value = btn.text()
            self.exitTimer.start(500)


    def closeEvent(self, event):
        
        #  get the current button state, if any
        for btn in self.btns:
            if btn.isChecked():
                self.state_value = btn.text()
        
        #  don't allow
        if not self.state_value:
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                    "Sorry " + self.firstName + ", you need to select a codend state!", 'info')
            self.message.exec()
            event.reject()
        else:
            event.accept()

