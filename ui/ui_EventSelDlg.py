# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\ui\EventSelDlg.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_eventselDlg(object):
    def setupUi(self, eventselDlg):
        eventselDlg.setObjectName("eventselDlg")
        eventselDlg.resize(543, 454)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(eventselDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(eventselDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.eventTable = QtWidgets.QTableWidget(eventselDlg)
        self.eventTable.setMaximumSize(QtCore.QSize(16777215, 350))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eventTable.setFont(font)
        self.eventTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.eventTable.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.eventTable.setRowCount(10)
        self.eventTable.setColumnCount(3)
        self.eventTable.setObjectName("eventTable")
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.eventTable)
        self.newEventBtn = QtWidgets.QPushButton(eventselDlg)
        self.newEventBtn.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newEventBtn.setFont(font)
        self.newEventBtn.setObjectName("newEventBtn")
        self.verticalLayout.addWidget(self.newEventBtn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelBtn = QtWidgets.QPushButton(eventselDlg)
        self.cancelBtn.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.okBtn = QtWidgets.QPushButton(eventselDlg)
        self.okBtn.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(eventselDlg)
        QtCore.QMetaObject.connectSlotsByName(eventselDlg)

    def retranslateUi(self, eventselDlg):
        _translate = QtCore.QCoreApplication.translate
        eventselDlg.setWindowTitle(_translate("eventselDlg", "Event Selection"))
        self.label.setText(_translate("eventselDlg", "Events in database"))
        item = self.eventTable.horizontalHeaderItem(0)
        item.setText(_translate("eventselDlg", "Event"))
        item = self.eventTable.horizontalHeaderItem(1)
        item.setText(_translate("eventselDlg", "Gear"))
        item = self.eventTable.horizontalHeaderItem(2)
        item.setText(_translate("eventselDlg", "Haulback Time"))
        self.newEventBtn.setText(_translate("eventselDlg", "Start New Event"))
        self.cancelBtn.setText(_translate("eventselDlg", "Cancel"))
        self.okBtn.setText(_translate("eventselDlg", "OK"))
