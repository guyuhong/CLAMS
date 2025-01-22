# Form implementation generated from reading ui file 'CLAMSEdit.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_clamsEdit(object):
    def setupUi(self, clamsEdit):
        clamsEdit.setObjectName("clamsEdit")
        clamsEdit.resize(1020, 760)
        self.deleteBtn = QtWidgets.QPushButton(parent=clamsEdit)
        self.deleteBtn.setGeometry(QtCore.QRect(20, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        self.tableBox = QtWidgets.QComboBox(parent=clamsEdit)
        self.tableBox.setGeometry(QtCore.QRect(210, 30, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableBox.setFont(font)
        self.tableBox.setObjectName("tableBox")
        self.label_4 = QtWidgets.QLabel(parent=clamsEdit)
        self.label_4.setGeometry(QtCore.QRect(210, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.commitBtn = QtWidgets.QPushButton(parent=clamsEdit)
        self.commitBtn.setGeometry(QtCore.QRect(20, 339, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commitBtn.setFont(font)
        self.commitBtn.setObjectName("commitBtn")
        self.insertBtn = QtWidgets.QPushButton(parent=clamsEdit)
        self.insertBtn.setGeometry(QtCore.QRect(20, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.insertBtn.setFont(font)
        self.insertBtn.setObjectName("insertBtn")
        self.clearHaulBtn = QtWidgets.QPushButton(parent=clamsEdit)
        self.clearHaulBtn.setGeometry(QtCore.QRect(20, 690, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearHaulBtn.setFont(font)
        self.clearHaulBtn.setObjectName("clearHaulBtn")
        self.tableTypeBox = QtWidgets.QComboBox(parent=clamsEdit)
        self.tableTypeBox.setGeometry(QtCore.QRect(20, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableTypeBox.setFont(font)
        self.tableTypeBox.setObjectName("tableTypeBox")
        self.label_5 = QtWidgets.QLabel(parent=clamsEdit)
        self.label_5.setGeometry(QtCore.QRect(20, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cancelBtn = QtWidgets.QPushButton(parent=clamsEdit)
        self.cancelBtn.setGeometry(QtCore.QRect(20, 460, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.dataView = QtWidgets.QTableView(parent=clamsEdit)
        self.dataView.setGeometry(QtCore.QRect(210, 160, 781, 571))
        self.dataView.setObjectName("dataView")
        self.fieldBox = QtWidgets.QComboBox(parent=clamsEdit)
        self.fieldBox.setGeometry(QtCore.QRect(210, 100, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fieldBox.setFont(font)
        self.fieldBox.setObjectName("fieldBox")
        self.label = QtWidgets.QLabel(parent=clamsEdit)
        self.label.setGeometry(QtCore.QRect(460, 110, 46, 14))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.valueEdit = QtWidgets.QLineEdit(parent=clamsEdit)
        self.valueEdit.setGeometry(QtCore.QRect(490, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valueEdit.setFont(font)
        self.valueEdit.setObjectName("valueEdit")
        self.filterBtn = QtWidgets.QPushButton(parent=clamsEdit)
        self.filterBtn.setGeometry(QtCore.QRect(730, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.filterBtn.setFont(font)
        self.filterBtn.setObjectName("filterBtn")
        self.label_6 = QtWidgets.QLabel(parent=clamsEdit)
        self.label_6.setGeometry(QtCore.QRect(210, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=clamsEdit)
        self.label_7.setGeometry(QtCore.QRect(490, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(clamsEdit)
        QtCore.QMetaObject.connectSlotsByName(clamsEdit)

    def retranslateUi(self, clamsEdit):
        _translate = QtCore.QCoreApplication.translate
        clamsEdit.setWindowTitle(_translate("clamsEdit", "CLAMS Data Editor"))
        self.deleteBtn.setText(_translate("clamsEdit", "Delete Record"))
        self.label_4.setText(_translate("clamsEdit", "Tables"))
        self.commitBtn.setText(_translate("clamsEdit", "Commit changes"))
        self.insertBtn.setText(_translate("clamsEdit", "Insert Record"))
        self.clearHaulBtn.setText(_translate("clamsEdit", "Clear haul data"))
        self.label_5.setText(_translate("clamsEdit", "Table Type"))
        self.cancelBtn.setText(_translate("clamsEdit", "Cancel changes"))
        self.label.setText(_translate("clamsEdit", "="))
        self.filterBtn.setText(_translate("clamsEdit", "Filter"))
        self.label_6.setText(_translate("clamsEdit", "Field"))
        self.label_7.setText(_translate("clamsEdit", "Value"))
