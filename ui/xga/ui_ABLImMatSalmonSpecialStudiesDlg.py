# Form implementation generated from reading ui file 'ABLImMatSalmonSpecialStudiesDlg.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ablimmatsalmonspeciesstudiesDlg(object):
    def setupUi(self, ablimmatsalmonspeciesstudiesDlg):
        ablimmatsalmonspeciesstudiesDlg.setObjectName("ablimmatsalmonspeciesstudiesDlg")
        ablimmatsalmonspeciesstudiesDlg.resize(759, 217)
        self.groupBox = QtWidgets.QGroupBox(parent=ablimmatsalmonspeciesstudiesDlg)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 721, 171))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.stomachBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.stomachBtn.setGeometry(QtCore.QRect(10, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stomachBtn.setFont(font)
        self.stomachBtn.setCheckable(True)
        self.stomachBtn.setObjectName("stomachBtn")
        self.thiamineBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.thiamineBtn.setGeometry(QtCore.QRect(490, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thiamineBtn.setFont(font)
        self.thiamineBtn.setCheckable(True)
        self.thiamineBtn.setObjectName("thiamineBtn")
        self.doneBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.doneBtn.setGeometry(QtCore.QRect(490, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName("doneBtn")
        self.clearBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.clearBtn.setGeometry(QtCore.QRect(250, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")
        self.isotopeBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.isotopeBtn.setGeometry(QtCore.QRect(250, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.isotopeBtn.setFont(font)
        self.isotopeBtn.setCheckable(True)
        self.isotopeBtn.setObjectName("isotopeBtn")
        self.otolithBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.otolithBtn.setGeometry(QtCore.QRect(10, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.otolithBtn.setFont(font)
        self.otolithBtn.setCheckable(True)
        self.otolithBtn.setObjectName("otolithBtn")
        self.label_3 = QtWidgets.QLabel(parent=ablimmatsalmonspeciesstudiesDlg)
        self.label_3.setGeometry(QtCore.QRect(280, 10, 197, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(ablimmatsalmonspeciesstudiesDlg)
        QtCore.QMetaObject.connectSlotsByName(ablimmatsalmonspeciesstudiesDlg)

    def retranslateUi(self, ablimmatsalmonspeciesstudiesDlg):
        _translate = QtCore.QCoreApplication.translate
        ablimmatsalmonspeciesstudiesDlg.setWindowTitle(_translate("ablimmatsalmonspeciesstudiesDlg", "Special Studies"))
        self.stomachBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Stomach"))
        self.thiamineBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Thiamine"))
        self.doneBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Done"))
        self.clearBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Clear"))
        self.isotopeBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Isotope"))
        self.otolithBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Otolith"))
        self.label_3.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Optional Special Studies"))
