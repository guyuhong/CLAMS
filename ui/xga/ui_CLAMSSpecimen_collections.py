# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q:\CLAMS\ui\xga\CLAMSSpecimen_collections.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_clamsSpecimen(object):
    def setupUi(self, clamsSpecimen):
        clamsSpecimen.setObjectName(_fromUtf8("clamsSpecimen"))
        clamsSpecimen.resize(1047, 647)
        self.label_10 = QtGui.QLabel(clamsSpecimen)
        self.label_10.setGeometry(QtCore.QRect(440, 29, 162, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.speciesLabel = QtGui.QLabel(clamsSpecimen)
        self.speciesLabel.setGeometry(QtCore.QRect(92, 20, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.speciesLabel.setFont(font)
        self.speciesLabel.setAutoFillBackground(True)
        self.speciesLabel.setFrameShape(QtGui.QFrame.Panel)
        self.speciesLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.speciesLabel.setLineWidth(1)
        self.speciesLabel.setText(_fromUtf8(""))
        self.speciesLabel.setObjectName(_fromUtf8("speciesLabel"))
        self.label_9 = QtGui.QLabel(clamsSpecimen)
        self.label_9.setGeometry(QtCore.QRect(19, 17, 150, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_2 = QtGui.QLabel(clamsSpecimen)
        self.label_2.setGeometry(QtCore.QRect(19, 39, 79, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.sciLabel = QtGui.QLabel(clamsSpecimen)
        self.sciLabel.setGeometry(QtCore.QRect(590, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sciLabel.setFont(font)
        self.sciLabel.setAutoFillBackground(True)
        self.sciLabel.setFrameShape(QtGui.QFrame.Panel)
        self.sciLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.sciLabel.setLineWidth(1)
        self.sciLabel.setText(_fromUtf8(""))
        self.sciLabel.setObjectName(_fromUtf8("sciLabel"))
        self.bottomBox = QtGui.QGroupBox(clamsSpecimen)
        self.bottomBox.setGeometry(QtCore.QRect(20, 560, 981, 61))
        self.bottomBox.setTitle(_fromUtf8(""))
        self.bottomBox.setObjectName(_fromUtf8("bottomBox"))
        self.addspcBtn = QtGui.QPushButton(self.bottomBox)
        self.addspcBtn.setGeometry(QtCore.QRect(10, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addspcBtn.setFont(font)
        self.addspcBtn.setObjectName(_fromUtf8("addspcBtn"))
        self.commentBtn = QtGui.QPushButton(self.bottomBox)
        self.commentBtn.setGeometry(QtCore.QRect(440, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commentBtn.setFont(font)
        self.commentBtn.setObjectName(_fromUtf8("commentBtn"))
        self.deleteBtn = QtGui.QPushButton(self.bottomBox)
        self.deleteBtn.setGeometry(QtCore.QRect(310, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName(_fromUtf8("deleteBtn"))
        self.doneBtn = QtGui.QPushButton(self.bottomBox)
        self.doneBtn.setGeometry(QtCore.QRect(839, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName(_fromUtf8("doneBtn"))
        self.collectBtn = QtGui.QPushButton(self.bottomBox)
        self.collectBtn.setGeometry(QtCore.QRect(580, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.collectBtn.setFont(font)
        self.collectBtn.setObjectName(_fromUtf8("collectBtn"))
        self.protoBtn = QtGui.QPushButton(self.bottomBox)
        self.protoBtn.setEnabled(True)
        self.protoBtn.setGeometry(QtCore.QRect(150, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.protoBtn.setFont(font)
        self.protoBtn.setObjectName(_fromUtf8("protoBtn"))
        self.printBtn = QtGui.QPushButton(self.bottomBox)
        self.printBtn.setGeometry(QtCore.QRect(710, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.printBtn.setFont(font)
        self.printBtn.setObjectName(_fromUtf8("printBtn"))
        self.groupBox = QtGui.QGroupBox(clamsSpecimen)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 151, 481))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btn_0 = QtGui.QPushButton(self.groupBox)
        self.btn_0.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName(_fromUtf8("btn_0"))
        self.verticalLayout.addWidget(self.btn_0)
        self.btn_1 = QtGui.QPushButton(self.groupBox)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.verticalLayout.addWidget(self.btn_1)
        self.btn_2 = QtGui.QPushButton(self.groupBox)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.verticalLayout.addWidget(self.btn_2)
        self.btn_3 = QtGui.QPushButton(self.groupBox)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.verticalLayout.addWidget(self.btn_3)
        self.btn_4 = QtGui.QPushButton(self.groupBox)
        self.btn_4.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName(_fromUtf8("btn_4"))
        self.verticalLayout.addWidget(self.btn_4)
        self.btn_5 = QtGui.QPushButton(self.groupBox)
        self.btn_5.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName(_fromUtf8("btn_5"))
        self.verticalLayout.addWidget(self.btn_5)
        self.btn_6 = QtGui.QPushButton(self.groupBox)
        self.btn_6.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName(_fromUtf8("btn_6"))
        self.verticalLayout.addWidget(self.btn_6)
        self.btn_7 = QtGui.QPushButton(self.groupBox)
        self.btn_7.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName(_fromUtf8("btn_7"))
        self.verticalLayout.addWidget(self.btn_7)
        self.btn_8 = QtGui.QPushButton(self.groupBox)
        self.btn_8.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName(_fromUtf8("btn_8"))
        self.verticalLayout.addWidget(self.btn_8)
        self.btn_9 = QtGui.QPushButton(self.groupBox)
        self.btn_9.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName(_fromUtf8("btn_9"))
        self.verticalLayout.addWidget(self.btn_9)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.measureView = QtGui.QTableView(clamsSpecimen)
        self.measureView.setGeometry(QtCore.QRect(170, 300, 841, 251))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.measureView.setFont(font)
        self.measureView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.measureView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.measureView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.measureView.setObjectName(_fromUtf8("measureView"))
        self.measureView.verticalHeader().setVisible(True)
        self.picLabel = QtGui.QLabel(clamsSpecimen)
        self.picLabel.setGeometry(QtCore.QRect(370, 80, 361, 201))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.picLabel.setFont(font)
        self.picLabel.setAutoFillBackground(True)
        self.picLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.picLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.picLabel.setText(_fromUtf8(""))
        self.picLabel.setObjectName(_fromUtf8("picLabel"))
        self.samplingMethodBox = QtGui.QComboBox(clamsSpecimen)
        self.samplingMethodBox.setGeometry(QtCore.QRect(760, 250, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.samplingMethodBox.setFont(font)
        self.samplingMethodBox.setObjectName(_fromUtf8("samplingMethodBox"))
        self.label_3 = QtGui.QLabel(clamsSpecimen)
        self.label_3.setGeometry(QtCore.QRect(760, 220, 191, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(clamsSpecimen)
        self.label_5.setGeometry(QtCore.QRect(761, 70, 151, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.protoLabel = QtGui.QLabel(clamsSpecimen)
        self.protoLabel.setGeometry(QtCore.QRect(761, 100, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.protoLabel.setFont(font)
        self.protoLabel.setFrameShape(QtGui.QFrame.Box)
        self.protoLabel.setText(_fromUtf8(""))
        self.protoLabel.setObjectName(_fromUtf8("protoLabel"))
        self.cycleBtn = QtGui.QPushButton(clamsSpecimen)
        self.cycleBtn.setEnabled(True)
        self.cycleBtn.setGeometry(QtCore.QRect(180, 120, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cycleBtn.setFont(font)
        self.cycleBtn.setCheckable(False)
        self.cycleBtn.setChecked(False)
        self.cycleBtn.setObjectName(_fromUtf8("cycleBtn"))
        self.autoCheck = QtGui.QCheckBox(clamsSpecimen)
        self.autoCheck.setGeometry(QtCore.QRect(199, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.autoCheck.setFont(font)
        self.autoCheck.setObjectName(_fromUtf8("autoCheck"))
        self.label_6 = QtGui.QLabel(clamsSpecimen)
        self.label_6.setGeometry(QtCore.QRect(180, 220, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.specimenLabel = QtGui.QLabel(clamsSpecimen)
        self.specimenLabel.setGeometry(QtCore.QRect(180, 250, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.specimenLabel.setFont(font)
        self.specimenLabel.setFrameShape(QtGui.QFrame.Box)
        self.specimenLabel.setText(_fromUtf8(""))
        self.specimenLabel.setObjectName(_fromUtf8("specimenLabel"))
        self.label = QtGui.QLabel(clamsSpecimen)
        self.label.setGeometry(QtCore.QRect(760, 140, 111, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lengthTypeBox = QtGui.QComboBox(clamsSpecimen)
        self.lengthTypeBox.setGeometry(QtCore.QRect(760, 170, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lengthTypeBox.setFont(font)
        self.lengthTypeBox.setObjectName(_fromUtf8("lengthTypeBox"))

        self.retranslateUi(clamsSpecimen)
        QtCore.QMetaObject.connectSlotsByName(clamsSpecimen)

    def retranslateUi(self, clamsSpecimen):
        clamsSpecimen.setWindowTitle(_translate("clamsSpecimen", "CLAMS Specimen", None))
        self.label_10.setText(_translate("clamsSpecimen", "Today\'s Scientist", None))
        self.label_9.setText(_translate("clamsSpecimen", "Current", None))
        self.label_2.setText(_translate("clamsSpecimen", "Species", None))
        self.addspcBtn.setText(_translate("clamsSpecimen", "Species", None))
        self.commentBtn.setText(_translate("clamsSpecimen", "Comment", None))
        self.deleteBtn.setText(_translate("clamsSpecimen", "Delete", None))
        self.doneBtn.setText(_translate("clamsSpecimen", "Done", None))
        self.collectBtn.setText(_translate("clamsSpecimen", "Collect", None))
        self.protoBtn.setText(_translate("clamsSpecimen", "Protocol", None))
        self.printBtn.setText(_translate("clamsSpecimen", "Print", None))
        self.btn_0.setText(_translate("clamsSpecimen", "0", None))
        self.btn_1.setText(_translate("clamsSpecimen", "1", None))
        self.btn_2.setText(_translate("clamsSpecimen", "2", None))
        self.btn_3.setText(_translate("clamsSpecimen", "3", None))
        self.btn_4.setText(_translate("clamsSpecimen", "4", None))
        self.btn_5.setText(_translate("clamsSpecimen", "5", None))
        self.btn_6.setText(_translate("clamsSpecimen", "6", None))
        self.btn_7.setText(_translate("clamsSpecimen", "7", None))
        self.btn_8.setText(_translate("clamsSpecimen", "8", None))
        self.btn_9.setText(_translate("clamsSpecimen", "9", None))
        self.label_3.setText(_translate("clamsSpecimen", "Sampling Method", None))
        self.label_5.setText(_translate("clamsSpecimen", "Current Protocol", None))
        self.cycleBtn.setText(_translate("clamsSpecimen", "Next", None))
        self.autoCheck.setText(_translate("clamsSpecimen", "Auto Next", None))
        self.label_6.setText(_translate("clamsSpecimen", "Specimen ID", None))
        self.label.setText(_translate("clamsSpecimen", "Length type", None))

