# Form implementation generated from reading ui file 'ABLJuvSalmonSpecialStudiesDlg.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_abljuvsalmonspeciesstudiesDlg(object):
    def setupUi(self, abljuvsalmonspeciesstudiesDlg):
        abljuvsalmonspeciesstudiesDlg.setObjectName("abljuvsalmonspeciesstudiesDlg")
        abljuvsalmonspeciesstudiesDlg.resize(759, 299)
        self.groupBox = QtWidgets.QGroupBox(parent=abljuvsalmonspeciesstudiesDlg)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 721, 251))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.wfBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.wfBtn.setGeometry(QtCore.QRect(10, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wfBtn.setFont(font)
        self.wfBtn.setCheckable(True)
        self.wfBtn.setObjectName("wfBtn")
        self.stomachBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.stomachBtn.setGeometry(QtCore.QRect(10, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stomachBtn.setFont(font)
        self.stomachBtn.setCheckable(True)
        self.stomachBtn.setObjectName("stomachBtn")
        self.biaBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.biaBtn.setGeometry(QtCore.QRect(490, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.biaBtn.setFont(font)
        self.biaBtn.setCheckable(True)
        self.biaBtn.setObjectName("biaBtn")
        self.thiamineBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.thiamineBtn.setGeometry(QtCore.QRect(10, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thiamineBtn.setFont(font)
        self.thiamineBtn.setCheckable(True)
        self.thiamineBtn.setObjectName("thiamineBtn")
        self.doneBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.doneBtn.setGeometry(QtCore.QRect(490, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName("doneBtn")
        self.clearBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.clearBtn.setGeometry(QtCore.QRect(250, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")
        self.igfBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.igfBtn.setGeometry(QtCore.QRect(490, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.igfBtn.setFont(font)
        self.igfBtn.setCheckable(True)
        self.igfBtn.setObjectName("igfBtn")
        self.isotopeBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.isotopeBtn.setGeometry(QtCore.QRect(250, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.isotopeBtn.setFont(font)
        self.isotopeBtn.setCheckable(True)
        self.isotopeBtn.setObjectName("isotopeBtn")
        self.fhBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.fhBtn.setGeometry(QtCore.QRect(250, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fhBtn.setFont(font)
        self.fhBtn.setCheckable(True)
        self.fhBtn.setObjectName("fhBtn")
        self.label_3 = QtWidgets.QLabel(parent=abljuvsalmonspeciesstudiesDlg)
        self.label_3.setGeometry(QtCore.QRect(280, 10, 197, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(abljuvsalmonspeciesstudiesDlg)
        QtCore.QMetaObject.connectSlotsByName(abljuvsalmonspeciesstudiesDlg)

    def retranslateUi(self, abljuvsalmonspeciesstudiesDlg):
        _translate = QtCore.QCoreApplication.translate
        abljuvsalmonspeciesstudiesDlg.setWindowTitle(_translate("abljuvsalmonspeciesstudiesDlg", "Special Studies"))
        self.wfBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Whole Fish"))
        self.stomachBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Stomach"))
        self.biaBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "BIA"))
        self.thiamineBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Thiamine"))
        self.doneBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Done"))
        self.clearBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Clear"))
        self.igfBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "IGF"))
        self.isotopeBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Isotope"))
        self.fhBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Fish Head"))
        self.label_3.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Optional Special Studies"))
