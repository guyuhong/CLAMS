# Form implementation generated from reading ui file 'QSCSTestPollCompare.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_QSCSTestPollCompare(object):
    def setupUi(self, QSCSTestPollCompare):
        QSCSTestPollCompare.setObjectName("QSCSTestPollCompare")
        QSCSTestPollCompare.resize(486, 312)
        self.centralwidget = QtWidgets.QWidget(parent=QSCSTestPollCompare)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.compareButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.compareButton.setObjectName("compareButton")
        self.horizontalLayout.addWidget(self.compareButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.scsText = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.scsText.setObjectName("scsText")
        self.verticalLayout.addWidget(self.scsText)
        QSCSTestPollCompare.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=QSCSTestPollCompare)
        self.statusbar.setObjectName("statusbar")
        QSCSTestPollCompare.setStatusBar(self.statusbar)

        self.retranslateUi(QSCSTestPollCompare)
        QtCore.QMetaObject.connectSlotsByName(QSCSTestPollCompare)

    def retranslateUi(self, QSCSTestPollCompare):
        _translate = QtCore.QCoreApplication.translate
        QSCSTestPollCompare.setWindowTitle(_translate("QSCSTestPollCompare", "pyQt SCS Client Tester"))
        self.compareButton.setText(_translate("QSCSTestPollCompare", "Compare"))
        self.label_2.setText(_translate("QSCSTestPollCompare", "Sensors from database compared to SCS stream"))
