# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\noaa-afsc-mace\CLAMS\ui\ConnectDlg.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_connectDlg(object):
    def setupUi(self, connectDlg):
        connectDlg.setObjectName("connectDlg")
        connectDlg.resize(300, 209)
        connectDlg.setMinimumSize(QtCore.QSize(300, 200))
        connectDlg.setMaximumSize(QtCore.QSize(330, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(connectDlg)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(parent=connectDlg)
        self.label_4.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=connectDlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.databaseName = QtWidgets.QLineEdit(parent=connectDlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.databaseName.setFont(font)
        self.databaseName.setObjectName("databaseName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.databaseName)
        self.userName = QtWidgets.QLineEdit(parent=connectDlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.userName.setFont(font)
        self.userName.setObjectName("userName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.userName)
        self.label_3 = QtWidgets.QLabel(parent=connectDlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.passwordName = QtWidgets.QLineEdit(parent=connectDlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.passwordName.setFont(font)
        self.passwordName.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordName.setObjectName("passwordName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passwordName)
        self.label_2 = QtWidgets.QLabel(parent=connectDlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.schemaLabel = QtWidgets.QLabel(parent=connectDlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.schemaLabel.setFont(font)
        self.schemaLabel.setObjectName("schemaLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.schemaLabel)
        self.schemaBox = QtWidgets.QComboBox(parent=connectDlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.schemaBox.setFont(font)
        self.schemaBox.setObjectName("schemaBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.schemaBox)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connectBtn = QtWidgets.QPushButton(parent=connectDlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.connectBtn.setFont(font)
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout.addWidget(self.connectBtn)
        self.cancelBtn = QtWidgets.QPushButton(parent=connectDlg)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(connectDlg)
        QtCore.QMetaObject.connectSlotsByName(connectDlg)

    def retranslateUi(self, connectDlg):
        _translate = QtCore.QCoreApplication.translate
        connectDlg.setWindowTitle(_translate("connectDlg", "Open Database"))
        self.label_4.setText(_translate("connectDlg", "Open Database Connection"))
        self.label.setText(_translate("connectDlg", "Database"))
        self.databaseName.setToolTip(_translate("connectDlg", "<html><head/><body><p>Enter the ODBC connection name for the</p><p>database you wish to connect to.</p></body></html>"))
        self.userName.setToolTip(_translate("connectDlg", "<html><head/><body><p>Enter the database username you wish use</p><p>for this connection.</p></body></html>"))
        self.label_3.setText(_translate("connectDlg", "Password"))
        self.passwordName.setToolTip(_translate("connectDlg", "<html><head/><body><p>Enter the password for the user you specified above.</p></body></html>"))
        self.label_2.setText(_translate("connectDlg", "User name"))
        self.schemaLabel.setText(_translate("connectDlg", "Biodata Schema"))
        self.schemaBox.setToolTip(_translate("connectDlg", "<html><head/><body><p>Specify the database schema that will be used to</p><p>query biological data from. This will almost always</p><p>be &quot;clamsbase2&quot;.</p></body></html>"))
        self.connectBtn.setText(_translate("connectDlg", "Connect"))
        self.cancelBtn.setText(_translate("connectDlg", "Cancel"))
