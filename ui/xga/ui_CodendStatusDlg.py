# Form implementation generated from reading ui file 'CodendStatusDlg.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_codendStatusDlg(object):
    def setupUi(self, codendStatusDlg):
        codendStatusDlg.setObjectName("codendStatusDlg")
        codendStatusDlg.resize(376, 551)
        self.verticalLayout = QtWidgets.QVBoxLayout(codendStatusDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=codendStatusDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_5 = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_5.setMinimumSize(QtCore.QSize(0, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_5.setFont(font)
        self.btn_5.setCheckable(True)
        self.btn_5.setAutoExclusive(True)
        self.btn_5.setObjectName("btn_5")
        self.verticalLayout_2.addWidget(self.btn_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_1 = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_1.setFont(font)
        self.btn_1.setCheckable(True)
        self.btn_1.setAutoExclusive(True)
        self.btn_1.setObjectName("btn_1")
        self.verticalLayout_2.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_2.setFont(font)
        self.btn_2.setCheckable(True)
        self.btn_2.setAutoExclusive(True)
        self.btn_2.setObjectName("btn_2")
        self.verticalLayout_2.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_3.setFont(font)
        self.btn_3.setCheckable(True)
        self.btn_3.setAutoExclusive(True)
        self.btn_3.setObjectName("btn_3")
        self.verticalLayout_2.addWidget(self.btn_3)
        self.btn_4 = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_4.setMinimumSize(QtCore.QSize(0, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_4.setFont(font)
        self.btn_4.setCheckable(True)
        self.btn_4.setAutoExclusive(True)
        self.btn_4.setObjectName("btn_4")
        self.verticalLayout_2.addWidget(self.btn_4)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(codendStatusDlg)
        QtCore.QMetaObject.connectSlotsByName(codendStatusDlg)

    def retranslateUi(self, codendStatusDlg):
        _translate = QtCore.QCoreApplication.translate
        codendStatusDlg.setWindowTitle(_translate("codendStatusDlg", "Codend Status"))
        self.groupBox.setTitle(_translate("codendStatusDlg", "Select Codend Status..."))
        self.btn_5.setText(_translate("codendStatusDlg", "Codend Status OK"))
        self.btn_1.setText(_translate("codendStatusDlg", "Codend Open INTENTIONALLY"))
        self.btn_2.setText(_translate("codendStatusDlg", "Codend Open MALFUNCTION"))
        self.btn_3.setText(_translate("codendStatusDlg", "Codend Closed NO CATCH"))
        self.btn_4.setText(_translate("codendStatusDlg", "Codend Closed UNPROCESSED"))
