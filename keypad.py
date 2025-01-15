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
    :module:: KeyPad

    :synopsis: KeyPad is a big GUI keyboard which allows touch alpha input.

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
from ui import ui_KeyPad

class KeyPad(QDialog, ui_KeyPad.Ui_keypad):

    def __init__(self, message,  parent=None):
        super(KeyPad,  self).__init__(parent)
        self.setupUi(self)
        self.dispEdit.setText(message)
#        buttons=['self._1_Btn', 'self._2_Btn', 'self._3_Btn', 'self._4_Btn', 'self._5_Btn', 'self._6_Btn',
#        'self._7_Btn', 'self._8_Btn', 'self._9_Btn', 'self._0_Btn']

        self._1_Btn.clicked.connect(self.getDigit)
        self._2_Btn.clicked.connect(self.getDigit)
        self._3_Btn.clicked.connect(self.getDigit)
        self._4_Btn.clicked.connect(self.getDigit)
        self._5_Btn.clicked.connect(self.getDigit)
        self._6_Btn.clicked.connect(self.getDigit)
        self._7_Btn.clicked.connect(self.getDigit)
        self._8_Btn.clicked.connect(self.getDigit)
        self._9_Btn.clicked.connect(self.getDigit)
        self._0_Btn.clicked.connect(self.getDigit)

        self.A_Btn.clicked.connect(self.getDigit)
        self.B_Btn.clicked.connect(self.getDigit)
        self.C_Btn.clicked.connect(self.getDigit)
        self.D_Btn.clicked.connect(self.getDigit)
        self.E_Btn.clicked.connect(self.getDigit)
        self.F_Btn.clicked.connect(self.getDigit)
        self.G_Btn.clicked.connect(self.getDigit)
        self.H_Btn.clicked.connect(self.getDigit)
        self.J_Btn.clicked.connect(self.getDigit)
        self.K_Btn.clicked.connect(self.getDigit)
        self.I_Btn.clicked.connect(self.getDigit)
        self.L_Btn.clicked.connect(self.getDigit)
        self.M_Btn.clicked.connect(self.getDigit)
        self.N_Btn.clicked.connect(self.getDigit)
        self.O_Btn.clicked.connect(self.getDigit)
        self.P_Btn.clicked.connect(self.getDigit)
        self.Q_Btn.clicked.connect(self.getDigit)
        self.R_Btn.clicked.connect(self.getDigit)
        self.S_Btn.clicked.connect(self.getDigit)
        self.T_Btn.clicked.connect(self.getDigit)
        self.U_Btn.clicked.connect(self.getDigit)
        self.V_Btn.clicked.connect(self.getDigit)
        self.W_Btn.clicked.connect(self.getDigit)
        self.X_Btn.clicked.connect(self.getDigit)
        self.Y_Btn.clicked.connect(self.getDigit)
        self.Z_Btn.clicked.connect(self.getDigit)
        self.colon_Btn.clicked.connect(self.getDigit)
        self.comma_Btn.clicked.connect(self.getDigit)
        self.dot_Btn.clicked.connect(self.getDigit)
        self.quest_Btn.clicked.connect(self.getDigit)
        self.dash_Btn.clicked.connect(self.getDigit)

        self.spaceBtn.clicked.connect(self.getSpace)
        self.backBtn.clicked.connect(self.getSpace)

        self.cancelBtn.clicked.connect(self.Cancel)
        self.clearBtn.clicked.connect(self.Clear)
        self.okBtn.clicked.connect(self.Enter)
        self.okFlag=False



    def getDigit(self):
        self.dispEdit.insertPlainText(self.sender().text())

    def getSpace(self):
        button = self.sender().text()
        existing = self.dispEdit.toPlainText ()
        if button=='Space':
            self.dispEdit.insertPlainText(' ')
        else:# backspace
            self.dispEdit.setText(existing[:-1])
            p=self.dispEdit.textCursor()
            p.setPosition(len(existing)-1)
            self.dispEdit.setTextCursor(p)


    def Clear(self):
        self.dispEdit.clear()

    def Cancel(self):
        self.okFlag=False
        self.done(1)


    def Enter(self):
        self.okFlag=True
        self.done(1)





