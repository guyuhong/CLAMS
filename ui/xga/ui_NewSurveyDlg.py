# Form implementation generated from reading ui file 'NewSurveyDlg.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_newSurveyDlg(object):
    def setupUi(self, newSurveyDlg):
        newSurveyDlg.setObjectName("newSurveyDlg")
        newSurveyDlg.resize(530, 603)
        self.verticalLayout = QtWidgets.QVBoxLayout(newSurveyDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(parent=newSurveyDlg)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.frame_2 = QtWidgets.QFrame(parent=newSurveyDlg)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.cbShip = QtWidgets.QComboBox(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cbShip.setFont(font)
        self.cbShip.setObjectName("cbShip")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbShip)
        self.label_10 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.surveyNumEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.surveyNumEdit.setFont(font)
        self.surveyNumEdit.setObjectName("surveyNumEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.surveyNumEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.surveyNameEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.surveyNameEdit.setFont(font)
        self.surveyNameEdit.setObjectName("surveyNameEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.surveyNameEdit)
        self.label_9 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.startDateEdit = QtWidgets.QDateEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.startDateEdit.setFont(font)
        self.startDateEdit.setObjectName("startDateEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.startDateEdit)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.endDateEdit = QtWidgets.QDateEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.endDateEdit.setFont(font)
        self.endDateEdit.setObjectName("endDateEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.endDateEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.cbSeaArea = QtWidgets.QComboBox(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cbSeaArea.setFont(font)
        self.cbSeaArea.setObjectName("cbSeaArea")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbSeaArea)
        self.label_7 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.cbRegion = QtWidgets.QComboBox(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cbRegion.setFont(font)
        self.cbRegion.setObjectName("cbRegion")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbRegion)
        self.label_11 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.abstractEdit = QtWidgets.QPlainTextEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.abstractEdit.setFont(font)
        self.abstractEdit.setObjectName("abstractEdit")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.ItemRole.FieldRole, self.abstractEdit)
        self.cbChiefSci = QtWidgets.QComboBox(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cbChiefSci.setFont(font)
        self.cbChiefSci.setObjectName("cbChiefSci")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbChiefSci)
        self.cbEndPort = QtWidgets.QComboBox(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cbEndPort.setFont(font)
        self.cbEndPort.setObjectName("cbEndPort")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbEndPort)
        self.cbStartPort = QtWidgets.QComboBox(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cbStartPort.setFont(font)
        self.cbStartPort.setObjectName("cbStartPort")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbStartPort)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(parent=newSurveyDlg)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.createBtn = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.createBtn.setFont(font)
        self.createBtn.setObjectName("createBtn")
        self.horizontalLayout.addWidget(self.createBtn)
        self.cancelBtn = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(newSurveyDlg)
        QtCore.QMetaObject.connectSlotsByName(newSurveyDlg)

    def retranslateUi(self, newSurveyDlg):
        _translate = QtCore.QCoreApplication.translate
        newSurveyDlg.setWindowTitle(_translate("newSurveyDlg", "Create New Survey"))
        self.label_12.setText(_translate("newSurveyDlg", "Create New Survey"))
        self.label.setText(_translate("newSurveyDlg", "Ship"))
        self.label_10.setText(_translate("newSurveyDlg", "Survey Number (YYYYNN)"))
        self.surveyNumEdit.setToolTip(_translate("newSurveyDlg", "<html><head/><body><p>Year and cruise number typically in the form YYYYNN where YYYY is the year and NN is the cruise number. Example: 201608</p></body></html>"))
        self.label_2.setText(_translate("newSurveyDlg", "Survey Name"))
        self.label_9.setText(_translate("newSurveyDlg", "Chief Scientist"))
        self.label_3.setText(_translate("newSurveyDlg", "Start Date"))
        self.label_4.setText(_translate("newSurveyDlg", "End Date"))
        self.label_5.setText(_translate("newSurveyDlg", "Start Port"))
        self.label_6.setText(_translate("newSurveyDlg", "End Port"))
        self.label_8.setText(_translate("newSurveyDlg", "Abstract"))
        self.cbSeaArea.setToolTip(_translate("newSurveyDlg", "<html><head/><body><p>The IHO sea area where the majority of the survey took place.</p></body></html>"))
        self.label_7.setText(_translate("newSurveyDlg", "Sea Area"))
        self.cbRegion.setToolTip(_translate("newSurveyDlg", "<html><head/><body><p>The region the survey took place. This is used primarily in the creation of the survey title in the metadata exports from the database. </p></body></html>"))
        self.label_11.setText(_translate("newSurveyDlg", "Region"))
        self.abstractEdit.setToolTip(_translate("newSurveyDlg", "<html><head/><body><p>The description of the survey. This is used as the survey description in the metadata export. Often it is completed post survey.</p></body></html>"))
        self.createBtn.setText(_translate("newSurveyDlg", "Create Survey"))
        self.cancelBtn.setText(_translate("newSurveyDlg", "Cancel"))
