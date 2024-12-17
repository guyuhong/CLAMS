# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\noaa-afsc-mace\CLAMS\ui\CLAMSProcess.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_clamsProcess(object):
    def setupUi(self, clamsProcess):
        clamsProcess.setObjectName("clamsProcess")
        clamsProcess.resize(914, 656)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(clamsProcess)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=clamsProcess)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.haulLabel = QtWidgets.QLabel(parent=clamsProcess)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.haulLabel.setFont(font)
        self.haulLabel.setAutoFillBackground(False)
        self.haulLabel.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
        self.haulLabel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.haulLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.haulLabel.setLineWidth(1)
        self.haulLabel.setText("")
        self.haulLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.haulLabel.setObjectName("haulLabel")
        self.verticalLayout.addWidget(self.haulLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.haulBtn = QtWidgets.QPushButton(parent=clamsProcess)
        self.haulBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.haulBtn.setFont(font)
        self.haulBtn.setAutoFillBackground(True)
        self.haulBtn.setCheckable(False)
        self.haulBtn.setObjectName("haulBtn")
        self.horizontalLayout.addWidget(self.haulBtn)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=clamsProcess)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.partitionBox = QtWidgets.QComboBox(parent=clamsProcess)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.partitionBox.setFont(font)
        self.partitionBox.setObjectName("partitionBox")
        self.verticalLayout_2.addWidget(self.partitionBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.catchBtn = QtWidgets.QPushButton(parent=clamsProcess)
        self.catchBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.catchBtn.setFont(font)
        self.catchBtn.setAutoFillBackground(True)
        self.catchBtn.setCheckable(False)
        self.catchBtn.setObjectName("catchBtn")
        self.horizontalLayout.addWidget(self.catchBtn)
        self.lengthBtn = QtWidgets.QPushButton(parent=clamsProcess)
        self.lengthBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lengthBtn.setFont(font)
        self.lengthBtn.setAutoFillBackground(True)
        self.lengthBtn.setCheckable(False)
        self.lengthBtn.setObjectName("lengthBtn")
        self.horizontalLayout.addWidget(self.lengthBtn)
        self.specBtn = QtWidgets.QPushButton(parent=clamsProcess)
        self.specBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.specBtn.setFont(font)
        self.specBtn.setAutoFillBackground(True)
        self.specBtn.setCheckable(False)
        self.specBtn.setObjectName("specBtn")
        self.horizontalLayout.addWidget(self.specBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(parent=clamsProcess)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fixSpeciesBtn = QtWidgets.QPushButton(parent=clamsProcess)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fixSpeciesBtn.setFont(font)
        self.fixSpeciesBtn.setAutoFillBackground(True)
        self.fixSpeciesBtn.setObjectName("fixSpeciesBtn")
        self.verticalLayout_3.addWidget(self.fixSpeciesBtn)
        self.editCodendStateBtn = QtWidgets.QPushButton(parent=clamsProcess)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editCodendStateBtn.setFont(font)
        self.editCodendStateBtn.setObjectName("editCodendStateBtn")
        self.verticalLayout_3.addWidget(self.editCodendStateBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.doneBtn = QtWidgets.QPushButton(parent=clamsProcess)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.doneBtn.setFont(font)
        self.doneBtn.setAutoFillBackground(True)
        self.doneBtn.setObjectName("doneBtn")
        self.horizontalLayout_2.addWidget(self.doneBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(clamsProcess)
        QtCore.QMetaObject.connectSlotsByName(clamsProcess)

    def retranslateUi(self, clamsProcess):
        _translate = QtCore.QCoreApplication.translate
        clamsProcess.setWindowTitle(_translate("clamsProcess", "CLAMS Haul Processing"))
        self.label.setText(_translate("clamsProcess", "Haul Number"))
        self.haulBtn.setText(_translate("clamsProcess", "Haul Form"))
        self.label_2.setText(_translate("clamsProcess", "Partiton"))
        self.catchBtn.setText(_translate("clamsProcess", "Catch Form"))
        self.lengthBtn.setText(_translate("clamsProcess", "Length Form"))
        self.specBtn.setText(_translate("clamsProcess", "Specimen Form"))
        self.fixSpeciesBtn.setText(_translate("clamsProcess", "Fix Species/Sex Assignment"))
        self.editCodendStateBtn.setText(_translate("clamsProcess", "Edit Codend State"))
        self.doneBtn.setText(_translate("clamsProcess", "Finished processing haul"))
