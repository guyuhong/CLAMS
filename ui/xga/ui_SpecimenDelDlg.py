# Form implementation generated from reading ui file 'SpecimenDelDlg.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_specimendelDlg(object):
    def setupUi(self, specimendelDlg):
        specimendelDlg.setObjectName("specimendelDlg")
        specimendelDlg.resize(765, 227)
        self.okBtn = QtWidgets.QPushButton(parent=specimendelDlg)
        self.okBtn.setGeometry(QtCore.QRect(520, 160, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName("okBtn")
        self.cancelBtn = QtWidgets.QPushButton(parent=specimendelDlg)
        self.cancelBtn.setGeometry(QtCore.QRect(270, 160, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.label = QtWidgets.QLabel(parent=specimendelDlg)
        self.label.setGeometry(QtCore.QRect(20, 9, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.delSpecimen = QtWidgets.QTableWidget(parent=specimendelDlg)
        self.delSpecimen.setGeometry(QtCore.QRect(20, 40, 721, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.delSpecimen.setFont(font)
        self.delSpecimen.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectColumns)
        self.delSpecimen.setObjectName("delSpecimen")
        self.delSpecimen.setColumnCount(0)
        self.delSpecimen.setRowCount(0)
        self.delBtn = QtWidgets.QPushButton(parent=specimendelDlg)
        self.delBtn.setGeometry(QtCore.QRect(20, 160, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.delBtn.setFont(font)
        self.delBtn.setObjectName("delBtn")

        self.retranslateUi(specimendelDlg)
        QtCore.QMetaObject.connectSlotsByName(specimendelDlg)

    def retranslateUi(self, specimendelDlg):
        _translate = QtCore.QCoreApplication.translate
        specimendelDlg.setWindowTitle(_translate("specimendelDlg", "Delete Specimen"))
        self.okBtn.setText(_translate("specimendelDlg", "Done"))
        self.cancelBtn.setText(_translate("specimendelDlg", "Cancel"))
        self.label.setText(_translate("specimendelDlg", "Select measurement to delete"))
        self.delBtn.setText(_translate("specimendelDlg", "Delete"))
