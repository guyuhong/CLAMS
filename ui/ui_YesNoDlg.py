# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\ui\YesNoDlg.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_YesNoDlg(object):
    def setupUi(self, YesNoDlg):
        YesNoDlg.setObjectName("YesNoDlg")
        YesNoDlg.resize(354, 180)
        YesNoDlg.setMinimumSize(QtCore.QSize(354, 180))
        YesNoDlg.setMaximumSize(QtCore.QSize(354, 180))
        self.groupBox = QtWidgets.QGroupBox(YesNoDlg)
        self.groupBox.setGeometry(QtCore.QRect(10, 33, 331, 141))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.yesBtn = QtWidgets.QPushButton(self.groupBox)
        self.yesBtn.setGeometry(QtCore.QRect(10, 15, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yesBtn.setFont(font)
        self.yesBtn.setObjectName("yesBtn")
        self.noBtn = QtWidgets.QPushButton(self.groupBox)
        self.noBtn.setGeometry(QtCore.QRect(10, 75, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.noBtn.setFont(font)
        self.noBtn.setObjectName("noBtn")
        self.msgLabel = QtWidgets.QLabel(YesNoDlg)
        self.msgLabel.setGeometry(QtCore.QRect(10, 2, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.msgLabel.setFont(font)
        self.msgLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.msgLabel.setObjectName("msgLabel")

        self.retranslateUi(YesNoDlg)
        QtCore.QMetaObject.connectSlotsByName(YesNoDlg)

    def retranslateUi(self, YesNoDlg):
        _translate = QtCore.QCoreApplication.translate
        YesNoDlg.setWindowTitle(_translate("YesNoDlg", "Yes or No?"))
        self.yesBtn.setText(_translate("YesNoDlg", "Yes"))
        self.noBtn.setText(_translate("YesNoDlg", "No"))
        self.msgLabel.setText(_translate("YesNoDlg", "Are you..."))
