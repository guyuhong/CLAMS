# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\ui\FEATGonadDlg.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(245, 337)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pb_take_nad = QtWidgets.QPushButton(Dialog)
        self.pb_take_nad.setGeometry(QtCore.QRect(10, 60, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_take_nad.setFont(font)
        self.pb_take_nad.setObjectName("pb_take_nad")
        self.pb_nad_wt = QtWidgets.QPushButton(Dialog)
        self.pb_nad_wt.setGeometry(QtCore.QRect(10, 130, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_nad_wt.setFont(font)
        self.pb_nad_wt.setObjectName("pb_nad_wt")
        self.pb_done = QtWidgets.QPushButton(Dialog)
        self.pb_done.setGeometry(QtCore.QRect(150, 270, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_done.setFont(font)
        self.pb_done.setObjectName("pb_done")
        self.pb_cancel = QtWidgets.QPushButton(Dialog)
        self.pb_cancel.setGeometry(QtCore.QRect(10, 270, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_cancel.setFont(font)
        self.pb_cancel.setObjectName("pb_cancel")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 191, 41))
        self.label_4.setStyleSheet("font: 14pt \"Calibri\";")
        self.label_4.setObjectName("label_4")
        self.l_cur_code = QtWidgets.QLabel(Dialog)
        self.l_cur_code.setGeometry(QtCore.QRect(40, 220, 191, 41))
        self.l_cur_code.setStyleSheet("font: 14pt \"Calibri\";")
        self.l_cur_code.setObjectName("l_cur_code")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gonads"))
        self.label.setText(_translate("Dialog", "Gonad Collection"))
        self.pb_take_nad.setText(_translate("Dialog", "Take Gonad"))
        self.pb_nad_wt.setText(_translate("Dialog", "Gonad Weight"))
        self.pb_done.setText(_translate("Dialog", "Done"))
        self.pb_cancel.setText(_translate("Dialog", "Cancel"))
        self.label_4.setText(_translate("Dialog", "Current Barcode"))
        self.l_cur_code.setText(_translate("Dialog", "None"))
