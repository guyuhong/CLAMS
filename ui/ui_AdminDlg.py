# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\noaa-afsc-mace\CLAMS\ui\AdminDlg.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_admindlg(object):
    def setupUi(self, admindlg):
        admindlg.setObjectName("admindlg")
        admindlg.resize(437, 330)
        self.verticalLayout = QtWidgets.QVBoxLayout(admindlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=admindlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.createSurveyBtn = QtWidgets.QPushButton(parent=admindlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.createSurveyBtn.setFont(font)
        self.createSurveyBtn.setObjectName("createSurveyBtn")
        self.verticalLayout.addWidget(self.createSurveyBtn)
        self.selectSurveyBtn = QtWidgets.QPushButton(parent=admindlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.selectSurveyBtn.setFont(font)
        self.selectSurveyBtn.setObjectName("selectSurveyBtn")
        self.verticalLayout.addWidget(self.selectSurveyBtn)
        self.setupBtn = QtWidgets.QPushButton(parent=admindlg)
        self.setupBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setupBtn.setFont(font)
        self.setupBtn.setObjectName("setupBtn")
        self.verticalLayout.addWidget(self.setupBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.doneBtn = QtWidgets.QPushButton(parent=admindlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName("doneBtn")
        self.verticalLayout.addWidget(self.doneBtn)

        self.retranslateUi(admindlg)
        QtCore.QMetaObject.connectSlotsByName(admindlg)

    def retranslateUi(self, admindlg):
        _translate = QtCore.QCoreApplication.translate
        admindlg.setWindowTitle(_translate("admindlg", "CLAMS Administration"))
        self.label.setText(_translate("admindlg", "CLAMS Administration"))
        self.createSurveyBtn.setText(_translate("admindlg", "Create Survey"))
        self.selectSurveyBtn.setText(_translate("admindlg", "Change Active Survey"))
        self.setupBtn.setText(_translate("admindlg", "Edit and Setup"))
        self.doneBtn.setText(_translate("admindlg", "Done"))
