# Form implementation generated from reading ui file 'ABLSpecialStudiesDlg.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ablspeciesstudiesDlg(object):
    def setupUi(self, ablspeciesstudiesDlg):
        ablspeciesstudiesDlg.setObjectName("ablspeciesstudiesDlg")
        ablspeciesstudiesDlg.resize(760, 230)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ablspeciesstudiesDlg.sizePolicy().hasHeightForWidth())
        ablspeciesstudiesDlg.setSizePolicy(sizePolicy)
        ablspeciesstudiesDlg.setMinimumSize(QtCore.QSize(760, 230))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(ablspeciesstudiesDlg)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(ablspeciesstudiesDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.otolithBtn = QtWidgets.QPushButton(ablspeciesstudiesDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otolithBtn.sizePolicy().hasHeightForWidth())
        self.otolithBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.otolithBtn.setFont(font)
        self.otolithBtn.setCheckable(True)
        self.otolithBtn.setObjectName("otolithBtn")
        self.verticalLayout.addWidget(self.otolithBtn)
        self.stomachBtn = QtWidgets.QPushButton(ablspeciesstudiesDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stomachBtn.sizePolicy().hasHeightForWidth())
        self.stomachBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stomachBtn.setFont(font)
        self.stomachBtn.setCheckable(True)
        self.stomachBtn.setObjectName("stomachBtn")
        self.verticalLayout.addWidget(self.stomachBtn)
        self.energeticBtn = QtWidgets.QPushButton(ablspeciesstudiesDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.energeticBtn.sizePolicy().hasHeightForWidth())
        self.energeticBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.energeticBtn.setFont(font)
        self.energeticBtn.setCheckable(True)
        self.energeticBtn.setObjectName("energeticBtn")
        self.verticalLayout.addWidget(self.energeticBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.isotopeMarshBtn = QtWidgets.QPushButton(ablspeciesstudiesDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isotopeMarshBtn.sizePolicy().hasHeightForWidth())
        self.isotopeMarshBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.isotopeMarshBtn.setFont(font)
        self.isotopeMarshBtn.setCheckable(True)
        self.isotopeMarshBtn.setObjectName("isotopeMarshBtn")
        self.verticalLayout_2.addWidget(self.isotopeMarshBtn)
        self.geneticsBtn = QtWidgets.QPushButton(ablspeciesstudiesDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geneticsBtn.sizePolicy().hasHeightForWidth())
        self.geneticsBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.geneticsBtn.setFont(font)
        self.geneticsBtn.setCheckable(True)
        self.geneticsBtn.setObjectName("geneticsBtn")
        self.verticalLayout_2.addWidget(self.geneticsBtn)
        self.clearBtn = QtWidgets.QPushButton(ablspeciesstudiesDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")
        self.verticalLayout_2.addWidget(self.clearBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.isotopeAndrewsBtn = QtWidgets.QPushButton(ablspeciesstudiesDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isotopeAndrewsBtn.sizePolicy().hasHeightForWidth())
        self.isotopeAndrewsBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.isotopeAndrewsBtn.setFont(font)
        self.isotopeAndrewsBtn.setCheckable(True)
        self.isotopeAndrewsBtn.setObjectName("isotopeAndrewsBtn")
        self.verticalLayout_3.addWidget(self.isotopeAndrewsBtn)
        self.tsmriBtn = QtWidgets.QPushButton(ablspeciesstudiesDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tsmriBtn.sizePolicy().hasHeightForWidth())
        self.tsmriBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tsmriBtn.setFont(font)
        self.tsmriBtn.setCheckable(True)
        self.tsmriBtn.setObjectName("tsmriBtn")
        self.verticalLayout_3.addWidget(self.tsmriBtn)
        self.doneBtn = QtWidgets.QPushButton(ablspeciesstudiesDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doneBtn.sizePolicy().hasHeightForWidth())
        self.doneBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName("doneBtn")
        self.verticalLayout_3.addWidget(self.doneBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ablspeciesstudiesDlg)
        QtCore.QMetaObject.connectSlotsByName(ablspeciesstudiesDlg)

    def retranslateUi(self, ablspeciesstudiesDlg):
        _translate = QtCore.QCoreApplication.translate
        ablspeciesstudiesDlg.setWindowTitle(_translate("ablspeciesstudiesDlg", "Special Studies"))
        self.label_3.setText(_translate("ablspeciesstudiesDlg", "Optional Special Studies"))
        self.otolithBtn.setText(_translate("ablspeciesstudiesDlg", "Otolith"))
        self.stomachBtn.setText(_translate("ablspeciesstudiesDlg", "Stomach"))
        self.energeticBtn.setText(_translate("ablspeciesstudiesDlg", "Energetics"))
        self.isotopeMarshBtn.setText(_translate("ablspeciesstudiesDlg", "Isotope_Marsh"))
        self.geneticsBtn.setText(_translate("ablspeciesstudiesDlg", "Genetics"))
        self.clearBtn.setText(_translate("ablspeciesstudiesDlg", "Clear"))
        self.isotopeAndrewsBtn.setText(_translate("ablspeciesstudiesDlg", "Isotope_Andrews"))
        self.tsmriBtn.setText(_translate("ablspeciesstudiesDlg", "TSMRI"))
        self.doneBtn.setText(_translate("ablspeciesstudiesDlg", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ablspeciesstudiesDlg = QtWidgets.QDialog()
    ui = Ui_ablspeciesstudiesDlg()
    ui.setupUi(ablspeciesstudiesDlg)
    ablspeciesstudiesDlg.show()
    sys.exit(app.exec())
