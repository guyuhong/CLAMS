# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\noaa-afsc-mace\CLAMS\ui\CLAMSLength.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_clamsLength(object):
    def setupUi(self, clamsLength):
        clamsLength.setObjectName("clamsLength")
        clamsLength.resize(1019, 654)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(clamsLength)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=clamsLength)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.speciesList = QtWidgets.QListWidget(parent=clamsLength)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(75)
        sizePolicy.setHeightForWidth(self.speciesList.sizePolicy().hasHeightForWidth())
        self.speciesList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.speciesList.setFont(font)
        self.speciesList.setObjectName("speciesList")
        self.verticalLayout_3.addWidget(self.speciesList)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.otherBox = QtWidgets.QGroupBox(parent=clamsLength)
        self.otherBox.setEnabled(False)
        self.otherBox.setTitle("")
        self.otherBox.setObjectName("otherBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.otherBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.otherBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.samplingMethodBox = QtWidgets.QComboBox(parent=self.otherBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.samplingMethodBox.setFont(font)
        self.samplingMethodBox.setObjectName("samplingMethodBox")
        self.verticalLayout_6.addWidget(self.samplingMethodBox)
        self.label = QtWidgets.QLabel(parent=self.otherBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.lengthTypeBox = QtWidgets.QComboBox(parent=self.otherBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lengthTypeBox.setFont(font)
        self.lengthTypeBox.setObjectName("lengthTypeBox")
        self.verticalLayout_6.addWidget(self.lengthTypeBox)
        self.gridLayout.addWidget(self.otherBox, 3, 1, 1, 1)
        self.groupSexBox = QtWidgets.QGroupBox(parent=clamsLength)
        self.groupSexBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupSexBox.sizePolicy().hasHeightForWidth())
        self.groupSexBox.setSizePolicy(sizePolicy)
        self.groupSexBox.setTitle("")
        self.groupSexBox.setObjectName("groupSexBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupSexBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.maleBtn = QtWidgets.QPushButton(parent=self.groupSexBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.maleBtn.setFont(font)
        self.maleBtn.setCheckable(True)
        self.maleBtn.setObjectName("maleBtn")
        self.verticalLayout.addWidget(self.maleBtn)
        self.femaleBtn = QtWidgets.QPushButton(parent=self.groupSexBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.femaleBtn.setFont(font)
        self.femaleBtn.setCheckable(True)
        self.femaleBtn.setObjectName("femaleBtn")
        self.verticalLayout.addWidget(self.femaleBtn)
        self.unsexBtn = QtWidgets.QPushButton(parent=self.groupSexBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.unsexBtn.setFont(font)
        self.unsexBtn.setCheckable(True)
        self.unsexBtn.setObjectName("unsexBtn")
        self.verticalLayout.addWidget(self.unsexBtn)
        self.gridLayout.addWidget(self.groupSexBox, 3, 0, 1, 1)
        self.picLabel = QtWidgets.QLabel(parent=clamsLength)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picLabel.sizePolicy().hasHeightForWidth())
        self.picLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.picLabel.setFont(font)
        self.picLabel.setAutoFillBackground(True)
        self.picLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.picLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.picLabel.setText("")
        self.picLabel.setObjectName("picLabel")
        self.gridLayout.addWidget(self.picLabel, 2, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(parent=clamsLength)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 2)
        self.sciLabel = QtWidgets.QLabel(parent=clamsLength)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sciLabel.sizePolicy().hasHeightForWidth())
        self.sciLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sciLabel.setFont(font)
        self.sciLabel.setAutoFillBackground(False)
        self.sciLabel.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
        self.sciLabel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.sciLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.sciLabel.setLineWidth(1)
        self.sciLabel.setText("")
        self.sciLabel.setObjectName("sciLabel")
        self.gridLayout.addWidget(self.sciLabel, 1, 0, 1, 2)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=clamsLength)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.measureView = QtWidgets.QTableView(parent=clamsLength)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(75)
        sizePolicy.setHeightForWidth(self.measureView.sizePolicy().hasHeightForWidth())
        self.measureView.setSizePolicy(sizePolicy)
        self.measureView.setMinimumSize(QtCore.QSize(0, 325))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.measureView.setFont(font)
        self.measureView.setObjectName("measureView")
        self.measureView.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.measureView)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lfPlot = QtWidgets.QGraphicsView(parent=clamsLength)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfPlot.sizePolicy().hasHeightForWidth())
        self.lfPlot.setSizePolicy(sizePolicy)
        self.lfPlot.setMinimumSize(QtCore.QSize(0, 0))
        self.lfPlot.setObjectName("lfPlot")
        self.horizontalLayout_3.addWidget(self.lfPlot)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=clamsLength)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.sumTable = QtWidgets.QTableWidget(parent=clamsLength)
        self.sumTable.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sumTable.sizePolicy().hasHeightForWidth())
        self.sumTable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sumTable.setFont(font)
        self.sumTable.setObjectName("sumTable")
        self.sumTable.setColumnCount(0)
        self.sumTable.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.sumTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sumTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sumTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sumTable.setVerticalHeaderItem(3, item)
        self.verticalLayout_4.addWidget(self.sumTable)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.bottomBox = QtWidgets.QGroupBox(parent=clamsLength)
        self.bottomBox.setTitle("")
        self.bottomBox.setObjectName("bottomBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottomBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.manualBtn = QtWidgets.QPushButton(parent=self.bottomBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.manualBtn.setFont(font)
        self.manualBtn.setObjectName("manualBtn")
        self.horizontalLayout.addWidget(self.manualBtn)
        self.extraBtn_2 = QtWidgets.QPushButton(parent=self.bottomBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.extraBtn_2.setFont(font)
        self.extraBtn_2.setCheckable(True)
        self.extraBtn_2.setObjectName("extraBtn_2")
        self.horizontalLayout.addWidget(self.extraBtn_2)
        self.deleteBtn = QtWidgets.QPushButton(parent=self.bottomBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout.addWidget(self.deleteBtn)
        self.commentBtn = QtWidgets.QPushButton(parent=self.bottomBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.commentBtn.setFont(font)
        self.commentBtn.setObjectName("commentBtn")
        self.horizontalLayout.addWidget(self.commentBtn)
        self.doneBtn = QtWidgets.QPushButton(parent=self.bottomBox)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName("doneBtn")
        self.horizontalLayout.addWidget(self.doneBtn)
        self.verticalLayout_5.addWidget(self.bottomBox)

        self.retranslateUi(clamsLength)
        QtCore.QMetaObject.connectSlotsByName(clamsLength)

    def retranslateUi(self, clamsLength):
        _translate = QtCore.QCoreApplication.translate
        clamsLength.setWindowTitle(_translate("clamsLength", "CLAMS Length"))
        self.label_5.setText(_translate("clamsLength", "Species List"))
        self.label_2.setText(_translate("clamsLength", "Sampling Method"))
        self.label.setText(_translate("clamsLength", "Length type"))
        self.maleBtn.setText(_translate("clamsLength", "Male"))
        self.femaleBtn.setText(_translate("clamsLength", "Female"))
        self.unsexBtn.setText(_translate("clamsLength", "Unsexed"))
        self.label_10.setText(_translate("clamsLength", "Scientist"))
        self.label_3.setText(_translate("clamsLength", "Measurements"))
        self.label_4.setText(_translate("clamsLength", "Summary"))
        item = self.sumTable.verticalHeaderItem(0)
        item.setText(_translate("clamsLength", "Male"))
        item = self.sumTable.verticalHeaderItem(1)
        item.setText(_translate("clamsLength", "Female"))
        item = self.sumTable.verticalHeaderItem(2)
        item.setText(_translate("clamsLength", "Unsexed"))
        item = self.sumTable.verticalHeaderItem(3)
        item.setText(_translate("clamsLength", "Total"))
        self.manualBtn.setText(_translate("clamsLength", "Manual Length"))
        self.extraBtn_2.setText(_translate("clamsLength", "Show Plot"))
        self.deleteBtn.setText(_translate("clamsLength", "Delete"))
        self.commentBtn.setText(_translate("clamsLength", "Comment"))
        self.doneBtn.setText(_translate("clamsLength", "Done"))
