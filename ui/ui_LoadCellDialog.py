<<<<<<< Updated upstream
# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\noaa-afsc-mace\CLAMS\ui\LoadCellDialog.ui'
=======
# Form implementation generated from reading ui file 'C:\Users\Melina.Shak\Documents\CLAMS\ui\LoadCellDialog.ui'
>>>>>>> Stashed changes
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_loadcellDialog(object):
    def setupUi(self, loadcellDialog):
        loadcellDialog.setObjectName("loadcellDialog")
        loadcellDialog.setEnabled(True)
        loadcellDialog.resize(439, 282)
        self.verticalLayout = QtWidgets.QVBoxLayout(loadcellDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=loadcellDialog)
        self.label_2.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=loadcellDialog)
        self.label_3.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.tareBtn = QtWidgets.QPushButton(parent=loadcellDialog)
        self.tareBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.tareBtn.setFont(font)
        self.tareBtn.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
        self.tareBtn.setText("")
        self.tareBtn.setAutoDefault(False)
        self.tareBtn.setFlat(False)
        self.tareBtn.setObjectName("tareBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tareBtn)
        self.grossBtn = QtWidgets.QPushButton(parent=loadcellDialog)
<<<<<<< Updated upstream
        self.grossBtn.setEnabled(True)
=======
        self.grossBtn.setEnabled(False)
>>>>>>> Stashed changes
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.grossBtn.setFont(font)
        self.grossBtn.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
        self.grossBtn.setText("")
        self.grossBtn.setAutoDefault(False)
        self.grossBtn.setFlat(False)
        self.grossBtn.setObjectName("grossBtn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.grossBtn)
        self.verticalLayout.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(parent=loadcellDialog)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(parent=loadcellDialog)
        self.label.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.haulWtLabel = QtWidgets.QLabel(parent=loadcellDialog)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.haulWtLabel.setFont(font)
        self.haulWtLabel.setAutoFillBackground(False)
        self.haulWtLabel.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
        self.haulWtLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.haulWtLabel.setLineWidth(2)
        self.haulWtLabel.setText("")
        self.haulWtLabel.setObjectName("haulWtLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.haulWtLabel)
        self.verticalLayout.addLayout(self.formLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=loadcellDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioKg = QtWidgets.QRadioButton(parent=self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.radioKg.setFont(font)
        self.radioKg.setChecked(True)
        self.radioKg.setObjectName("radioKg")
        self.horizontalLayout.addWidget(self.radioKg)
        self.radioLb = QtWidgets.QRadioButton(parent=self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.radioLb.setFont(font)
        self.radioLb.setObjectName("radioLb")
        self.horizontalLayout.addWidget(self.radioLb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelBtn = QtWidgets.QPushButton(parent=self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.okBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.okBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(loadcellDialog)
        QtCore.QMetaObject.connectSlotsByName(loadcellDialog)

    def retranslateUi(self, loadcellDialog):
        _translate = QtCore.QCoreApplication.translate
        loadcellDialog.setWindowTitle(_translate("loadcellDialog", "Load Cell"))
        self.label_2.setText(_translate("loadcellDialog", "Gross Weight"))
        self.label_3.setText(_translate("loadcellDialog", "Tare Weight"))
        self.label.setText(_translate("loadcellDialog", "Haul Weight"))
        self.radioKg.setText(_translate("loadcellDialog", "Kg"))
        self.radioLb.setText(_translate("loadcellDialog", "Lb"))
        self.cancelBtn.setText(_translate("loadcellDialog", "Cancel"))
        self.okBtn.setText(_translate("loadcellDialog", "OK"))
