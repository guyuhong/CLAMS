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
    :module:: TimeDlg

    :synopsis: This dialog gets date/time input from the user.
               I think this is mainly used when a user is
               editing past measurements/actions in an event and
               they have to provide a time for that action.

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

from PyQt6.QtCore import QDateTime, QDate, QTime, Qt
from PyQt6.QtWidgets import QDialog

from ui import ui_TimeDlg


class TimeDlg(QDialog, ui_TimeDlg.Ui_timeDlg):

    def __init__(self, parent=None):
        super(TimeDlg, self).__init__(parent)
        self.setupUi(self)

        self.okBtn.clicked.connect(self.exit)
        self.pbGetCurrentTime.clicked.connect(self.getCurrentTime)
        self.cancelBtn.clicked.connect(self.cancel)
        self.timeEdit.setDisplayFormat('hh:mm:ss.zzz')

    def setTime(self, time):
        initTime = QDateTime().fromString(time, 'MMddyyyy hh:mm:ss.zzz')
        self.dateEdit.setDate(initTime.date())
        self.timeEdit.setTime(initTime.time())

    def getCurrentTime(self):
        self.dateEdit.setDate(QDate.currentDate())
        self.timeEdit.setTime(QTime.currentTime())

    def enableGetTimeButton(self, enable):
        if enable:
            self.pbGetCurrentTime.setEnabled(True)
        else:
            self.pbGetCurrentTime.setEnabled(False)

    def cancel(self):
        self.time=None
        self.reject()

    def exit(self):
        # get times
        self.qTime=QDateTime(self.dateEdit.date(), self.timeEdit.time(),  Qt.LocalTime)
        self.time=self.qTime.toString('MMddyyyy hh:mm:ss.zzz')
        self.accept()


