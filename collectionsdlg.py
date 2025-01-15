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
    :module:: CollectionsDlg

    :synopsis: CollectionsDlg

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
from ui import ui_CollectionsDlg

class CollectionsDlg(QDialog, ui_CollectionsDlg.Ui_collectionsDlg):

    def __init__(self,  activeCollections=[], parent=None):
        super(CollectionsDlg, self).__init__(parent)
        self.setupUi(self)

        # Populate the GUI
	
        self.checkboxes=[self.checkBox_1,self.checkBox_2,self.checkBox_3,
		self.checkBox_4,self.checkBox_5,self.checkBox_6]
        for box in self.checkboxes:
	        box.hide()

        for i, col in enumerate(activeCollections):
            self.checkboxes[i].setText(col)
            self.checkboxes[i].show()

        self.printExitButton.clicked.connect(self.goOnward)
        self.cancelBtn.clicked.connect(self.goExit)


    def goOnward(self):
        self.accept()


    def goExit(self):
        self.reject()

