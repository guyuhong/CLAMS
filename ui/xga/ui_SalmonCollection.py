# Form implementation generated from reading ui file 'SalmonCollection.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_salmoncollectionDlg(object):
    def setupUi(self, salmoncollectionDlg):
        salmoncollectionDlg.setObjectName("salmoncollectionDlg")
        salmoncollectionDlg.resize(880, 597)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(salmoncollectionDlg.sizePolicy().hasHeightForWidth())
        salmoncollectionDlg.setSizePolicy(sizePolicy)
        salmoncollectionDlg.setMinimumSize(QtCore.QSize(200, 0))
        self.gridLayout_2 = QtWidgets.QGridLayout(salmoncollectionDlg)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=salmoncollectionDlg)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=salmoncollectionDlg)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.Btn4 = QtWidgets.QPushButton(parent=self.groupBox)
        self.Btn4.setMinimumSize(QtCore.QSize(200, 100))
        self.Btn4.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Btn4.setFont(font)
        self.Btn4.setText("")
        self.Btn4.setCheckable(True)
        self.Btn4.setObjectName("Btn4")
        self.gridLayout.addWidget(self.Btn4, 0, 4, 1, 1)
        self.clearBtn = QtWidgets.QPushButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy)
        self.clearBtn.setMinimumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")
        self.gridLayout.addWidget(self.clearBtn, 4, 0, 1, 1)
        self.Btn7 = QtWidgets.QPushButton(parent=self.groupBox)
        self.Btn7.setMinimumSize(QtCore.QSize(200, 100))
        self.Btn7.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Btn7.setFont(font)
        self.Btn7.setText("")
        self.Btn7.setCheckable(True)
        self.Btn7.setObjectName("Btn7")
        self.gridLayout.addWidget(self.Btn7, 2, 2, 1, 1)
        self.Btn6 = QtWidgets.QPushButton(parent=self.groupBox)
        self.Btn6.setMinimumSize(QtCore.QSize(200, 100))
        self.Btn6.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Btn6.setFont(font)
        self.Btn6.setText("")
        self.Btn6.setCheckable(True)
        self.Btn6.setObjectName("Btn6")
        self.gridLayout.addWidget(self.Btn6, 2, 1, 1, 1)
        self.Btn5 = QtWidgets.QPushButton(parent=self.groupBox)
        self.Btn5.setMinimumSize(QtCore.QSize(200, 100))
        self.Btn5.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Btn5.setFont(font)
        self.Btn5.setText("")
        self.Btn5.setCheckable(True)
        self.Btn5.setObjectName("Btn5")
        self.gridLayout.addWidget(self.Btn5, 2, 0, 1, 1)
        self.doneBtn = QtWidgets.QPushButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doneBtn.sizePolicy().hasHeightForWidth())
        self.doneBtn.setSizePolicy(sizePolicy)
        self.doneBtn.setMinimumSize(QtCore.QSize(200, 200))
        self.doneBtn.setMaximumSize(QtCore.QSize(1667775, 1667775))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName("doneBtn")
        self.gridLayout.addWidget(self.doneBtn, 4, 4, 1, 1)
        self.Btn3 = QtWidgets.QPushButton(parent=self.groupBox)
        self.Btn3.setMinimumSize(QtCore.QSize(200, 100))
        self.Btn3.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Btn3.setFont(font)
        self.Btn3.setText("")
        self.Btn3.setCheckable(True)
        self.Btn3.setObjectName("Btn3")
        self.gridLayout.addWidget(self.Btn3, 0, 2, 1, 1)
        self.Btn2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.Btn2.setMinimumSize(QtCore.QSize(200, 100))
        self.Btn2.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Btn2.setFont(font)
        self.Btn2.setText("")
        self.Btn2.setCheckable(True)
        self.Btn2.setObjectName("Btn2")
        self.gridLayout.addWidget(self.Btn2, 0, 1, 1, 1)
        self.Btn1 = QtWidgets.QPushButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn1.sizePolicy().hasHeightForWidth())
        self.Btn1.setSizePolicy(sizePolicy)
        self.Btn1.setMinimumSize(QtCore.QSize(200, 100))
        self.Btn1.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Btn1.setFont(font)
        self.Btn1.setText("")
        self.Btn1.setCheckable(True)
        self.Btn1.setObjectName("Btn1")
        self.gridLayout.addWidget(self.Btn1, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)

        self.retranslateUi(salmoncollectionDlg)
        QtCore.QMetaObject.connectSlotsByName(salmoncollectionDlg)

    def retranslateUi(self, salmoncollectionDlg):
        _translate = QtCore.QCoreApplication.translate
        salmoncollectionDlg.setWindowTitle(_translate("salmoncollectionDlg", "Special Studies"))
        self.label_3.setText(_translate("salmoncollectionDlg", "Missing fins?"))
        self.clearBtn.setText(_translate("salmoncollectionDlg", "Clear"))
        self.doneBtn.setText(_translate("salmoncollectionDlg", "Done"))
