# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\acquisition\serial\ui\SerialFaker.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SerialFaker(object):
    def setupUi(self, SerialFaker):
        SerialFaker.setObjectName("SerialFaker")
        SerialFaker.resize(681, 242)
        self.centralwidget = QtWidgets.QWidget(SerialFaker)
        self.centralwidget.setObjectName("centralwidget")
        self.lengthText = QtWidgets.QLineEdit(self.centralwidget)
        self.lengthText.setGeometry(QtCore.QRect(180, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lengthText.setFont(font)
        self.lengthText.setObjectName("lengthText")
        self.smallScaleText = QtWidgets.QLineEdit(self.centralwidget)
        self.smallScaleText.setGeometry(QtCore.QRect(180, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.smallScaleText.setFont(font)
        self.smallScaleText.setObjectName("smallScaleText")
        self.largeScaleText = QtWidgets.QLineEdit(self.centralwidget)
        self.largeScaleText.setGeometry(QtCore.QRect(180, 150, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.largeScaleText.setFont(font)
        self.largeScaleText.setObjectName("largeScaleText")
        self.barCodeText = QtWidgets.QLineEdit(self.centralwidget)
        self.barCodeText.setGeometry(QtCore.QRect(180, 200, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.barCodeText.setFont(font)
        self.barCodeText.setObjectName("barCodeText")
        self.sendBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn1.setGeometry(QtCore.QRect(380, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sendBtn1.setFont(font)
        self.sendBtn1.setObjectName("sendBtn1")
        self.sendBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn2.setGeometry(QtCore.QRect(380, 100, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sendBtn2.setFont(font)
        self.sendBtn2.setObjectName("sendBtn2")
        self.sendBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn3.setGeometry(QtCore.QRect(380, 150, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sendBtn3.setFont(font)
        self.sendBtn3.setObjectName("sendBtn3")
        self.sendBtn4 = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn4.setGeometry(QtCore.QRect(380, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sendBtn4.setFont(font)
        self.sendBtn4.setObjectName("sendBtn4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 141, 24))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 141, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 141, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 141, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 141, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.fileBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.fileBtn1.setGeometry(QtCore.QRect(540, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fileBtn1.setFont(font)
        self.fileBtn1.setObjectName("fileBtn1")
        SerialFaker.setCentralWidget(self.centralwidget)
        self.actionConfigure_Ports = QtGui.QAction(SerialFaker)
        self.actionConfigure_Ports.setObjectName("actionConfigure_Ports")

        self.retranslateUi(SerialFaker)
        QtCore.QMetaObject.connectSlotsByName(SerialFaker)

    def retranslateUi(self, SerialFaker):
        _translate = QtCore.QCoreApplication.translate
        SerialFaker.setWindowTitle(_translate("SerialFaker", "Don\'t make it, fake it"))
        self.sendBtn1.setText(_translate("SerialFaker", "Send"))
        self.sendBtn2.setText(_translate("SerialFaker", "Send"))
        self.sendBtn3.setText(_translate("SerialFaker", "Send"))
        self.sendBtn4.setText(_translate("SerialFaker", "Send"))
        self.label.setText(_translate("SerialFaker", "Serial Faker"))
        self.label_2.setText(_translate("SerialFaker", "Length Board"))
        self.label_3.setText(_translate("SerialFaker", "Small Scale"))
        self.label_4.setText(_translate("SerialFaker", "Large scale"))
        self.label_5.setText(_translate("SerialFaker", "Barcode"))
        self.fileBtn1.setText(_translate("SerialFaker", "file"))
        self.actionConfigure_Ports.setText(_translate("SerialFaker", "Configure Ports..."))
