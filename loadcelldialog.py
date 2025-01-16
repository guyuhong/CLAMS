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
.. module:: CLAMSmain

    :synopsis: CLAMSmain presents the main CLAMS application window.
    It is the entry point for the CLAMS catch processing application.

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
from ui import ui_LoadCellDialog
import numpad


class LoadCellDialog(QDialog, ui_LoadCellDialog.Ui_loadcellDialog):
    def __init__(self, parent=None):
        super(LoadCellDialog, self).__init__(parent)

        #  copy some params for convienience
        self.settings=parent.settings
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.message=parent.message

        #  call the dialog GUI setui
        self.setupUi(self)

        #  initially disable the tare button because you need to
        #  get a gross weight before the tare
        self.tareBtn.setEnabled(False)

        #  connect button signals
        self.grossBtn.clicked.connect(self.getGross)
        self.tareBtn.clicked.connect(self.getTare)
        self.okBtn.clicked.connect(self.goOK)
        self.cancelBtn.clicked.connect(self.goExit)

        #  initialize a numpad for entering values
        self.numpad = numpad.NumPad(self)


    def getGross(self):
        self.numpad.msgLabel.setText('Enter total bag weight')
        if self.numpad.exec():
            grossWT=self.numpad.value
            self.grossLabel.setText(grossWT)
            self.tareBtn.setEnabled(True)


    def getTare(self):

        self.numpad.msgLabel.setText('Enter empty bag weight')
        if self.numpad.exec():
            if float(self.numpad.value) > float(self.settings['MaxTareWt']):
                self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                        "The load cell tare weight exceeds the maximum allowed tare weight of" +
                        self.settings['MaxTareWt'] + " kg.  Does this concern you?",
                        'choice')
                if self.message.exec():
                    return

            self.tareLabel.setText(self.numpad.value)
            tareWTnum = float(self.numpad.value)
            grossWTnum = float(self.grossLabel.text())
            haulWT = grossWTnum - tareWTnum
            self.haulWtLabel.setNum(haulWT)
            self.okBtn.setEnabled(True)


    def goOK(self):

        num = float(self.haulWtLabel.text())
        if self.radioLb.isChecked():
            #  convert lb to kg
            num = num / 2.2046
        num = round(num, 1)
        self.haulWt = str(num)
        self.done(1)


    def goExit(self):
        self.done(0)



