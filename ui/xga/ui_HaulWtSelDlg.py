# Form implementation generated from reading ui file 'HaulWtSelDlg.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_haulwtselDlg(object):
    def setupUi(self, haulwtselDlg):
        haulwtselDlg.setObjectName("haulwtselDlg")
        haulwtselDlg.resize(322, 350)
        haulwtselDlg.setMinimumSize(QtCore.QSize(320, 350))
        self.verticalLayout = QtWidgets.QVBoxLayout(haulwtselDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=haulwtselDlg)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btn_0 = QtWidgets.QPushButton(parent=haulwtselDlg)
        self.btn_0.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.verticalLayout.addWidget(self.btn_0)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_1 = QtWidgets.QPushButton(parent=haulwtselDlg)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.verticalLayout.addWidget(self.btn_1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_2 = QtWidgets.QPushButton(parent=haulwtselDlg)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.verticalLayout.addWidget(self.btn_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.btn_3 = QtWidgets.QPushButton(parent=haulwtselDlg)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.verticalLayout.addWidget(self.btn_3)

        self.retranslateUi(haulwtselDlg)
        QtCore.QMetaObject.connectSlotsByName(haulwtselDlg)

    def retranslateUi(self, haulwtselDlg):
        _translate = QtCore.QCoreApplication.translate
        haulwtselDlg.setWindowTitle(_translate("haulwtselDlg", "Haul Weight Method"))
        self.label.setText(_translate("haulwtselDlg", "Haul Weight Estimation"))
        self.btn_0.setText(_translate("haulwtselDlg", "PushButton"))
        self.btn_1.setText(_translate("haulwtselDlg", "PushButton"))
        self.btn_2.setText(_translate("haulwtselDlg", "PushButton"))
        self.btn_3.setText(_translate("haulwtselDlg", "PushButton"))
