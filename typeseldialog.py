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
    :module:: TypeSelDialog

    :synopsis: TypeSelDialog is presented when a basket is
               weighed in the Catch module and it prompts the user for
               the basket's sample type. Like many of the dialogs, the
               buttons are empty and are populated based on the sample
               types configured in the database.

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
from ui import ui_TypeSelDialog

class TypeSelDialog(QDialog, ui_TypeSelDialog.Ui_typeselDialog):
    def __init__(self, parent=None):
        super(TypeSelDialog, self).__init__(parent)
        self.setupUi(self)
        self.basketType = None
        
        #hide buttons and hook up slots
        for i in range(4):
            exec(str("self.btn_"+str(i)+".hide()"))
            exec(str('self.connect(self.btn_'+str(i)+', SIGNAL("clicked()"), self.selType)'))
        # set it up
        for i in range(len(parent.basketTypes)):
            exec(str("self.btn_"+str(i)+".show()"))
            exec(str("self.btn_"+str(i)+".setText(parent.basketTypes[i])"))
        
        self.numDlg = parent.numpad
        
    def buttonSetup(self, validList):
        self.Type=None
        for i in range(len(validList)):
            if not validList[i]:
                exec(str("self.btn_"+str(i)+".setEnabled(False)"))
            else:
                exec(str("self.btn_"+str(i)+".setEnabled(True)"))
        

    def selType(self):
            self.count=None
            self.basketType=self.sender().text()
            if self.basketType=='Count':
                self.numDlg.msgLabel.setText("Enter Count")
                self.numDlg.exec_()
                if (self.numDlg.value != None):
                    #  get the value from the numpad
                    self.count=self.numDlg.value
                else:
                    # the user cancelled the numpad selection
                    return
            
                       
            self.accept()
            
    def closeEvent(self, event=None):
        if self.basketType==None:
            self.reject()
            pass

