# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\noaa-afsc-mace\CLAMS\ui\CLAMSMain.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_clamsMain(object):
    def setupUi(self, clamsMain):
        clamsMain.setObjectName("clamsMain")
        clamsMain.resize(1000, 650)
        clamsMain.setMinimumSize(QtCore.QSize(850, 600))
        clamsMain.setMaximumSize(QtCore.QSize(3840, 2160))
        self.centralwidget = QtWidgets.QWidget(parent=clamsMain)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.schemaLabel = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(True)
        self.schemaLabel.setFont(font)
        self.schemaLabel.setText("")
        self.schemaLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.schemaLabel.setObjectName("schemaLabel")
        self.verticalLayout_3.addWidget(self.schemaLabel)
        self.titleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(56)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_3.addWidget(self.titleLabel)
        self.subtitleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        self.subtitleLabel.setFont(font)
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.verticalLayout_3.addWidget(self.subtitleLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.shipLabel = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        self.shipLabel.setFont(font)
        self.shipLabel.setObjectName("shipLabel")
        self.verticalLayout_2.addWidget(self.shipLabel)
        self.surveyLabel = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        self.surveyLabel.setFont(font)
        self.surveyLabel.setObjectName("surveyLabel")
        self.verticalLayout_2.addWidget(self.surveyLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.trawlEventBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.trawlEventBtn.setEnabled(False)
        self.trawlEventBtn.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        self.trawlEventBtn.setFont(font)
        self.trawlEventBtn.setObjectName("trawlEventBtn")
        self.verticalLayout.addWidget(self.trawlEventBtn)
        self.procBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.procBtn.setEnabled(False)
        self.procBtn.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        self.procBtn.setFont(font)
        self.procBtn.setObjectName("procBtn")
        self.verticalLayout.addWidget(self.procBtn)
        self.utilitiesBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.utilitiesBtn.setEnabled(False)
        self.utilitiesBtn.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        self.utilitiesBtn.setFont(font)
        self.utilitiesBtn.setObjectName("utilitiesBtn")
        self.verticalLayout.addWidget(self.utilitiesBtn)
        self.adminBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.adminBtn.setEnabled(False)
        self.adminBtn.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        self.adminBtn.setFont(font)
        self.adminBtn.setObjectName("adminBtn")
        self.verticalLayout.addWidget(self.adminBtn)
        self.exitBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exitBtn.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout.addWidget(self.exitBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        clamsMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(clamsMain)
        QtCore.QMetaObject.connectSlotsByName(clamsMain)

    def retranslateUi(self, clamsMain):
        _translate = QtCore.QCoreApplication.translate
        clamsMain.setWindowTitle(_translate("clamsMain", "Catch Logger for Midwater Acoustic Surveys"))
        self.titleLabel.setText(_translate("clamsMain", "CLAMS"))
        self.subtitleLabel.setText(_translate("clamsMain", "Catch Logger for Acoustic Midwater Surveys"))
        self.shipLabel.setText(_translate("clamsMain", "Ship:                          "))
        self.surveyLabel.setText(_translate("clamsMain", "Survey:                       "))
        self.trawlEventBtn.setText(_translate("clamsMain", "Log Event"))
        self.procBtn.setText(_translate("clamsMain", "Enter Catch"))
        self.utilitiesBtn.setText(_translate("clamsMain", "Utilities"))
        self.adminBtn.setText(_translate("clamsMain", "Administration"))
        self.exitBtn.setText(_translate("clamsMain", "Exit"))
