# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\acquisition\serial\ui\SerialConsole.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SerialConsole(object):
    def setupUi(self, SerialConsole):
        SerialConsole.setObjectName("SerialConsole")
        SerialConsole.resize(387, 550)
        SerialConsole.setMinimumSize(QtCore.QSize(325, 550))
        self.centralwidget = QtWidgets.QWidget(SerialConsole)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dataText = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dataText.setFont(font)
        self.dataText.setObjectName("dataText")
        self.verticalLayout.addWidget(self.dataText)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.errText = QtWidgets.QTextBrowser(self.centralwidget)
        self.errText.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errText.setFont(font)
        self.errText.setObjectName("errText")
        self.verticalLayout.addWidget(self.errText)
        SerialConsole.setCentralWidget(self.centralwidget)

        self.retranslateUi(SerialConsole)
        QtCore.QMetaObject.connectSlotsByName(SerialConsole)

    def retranslateUi(self, SerialConsole):
        _translate = QtCore.QCoreApplication.translate
        SerialConsole.setWindowTitle(_translate("SerialConsole", "Simple Serial Console"))
        self.label_2.setText(_translate("SerialConsole", "Serial Data (Device Name - Data)"))
        self.label.setText(_translate("SerialConsole", "Last Error"))
