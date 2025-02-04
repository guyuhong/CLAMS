# Form implementation generated from reading ui file 'NoiseAnalysis.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 601)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Spectrogram_Widget = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Spectrogram_Widget.sizePolicy().hasHeightForWidth())
        self.Spectrogram_Widget.setSizePolicy(sizePolicy)
        self.Spectrogram_Widget.setObjectName("Spectrogram_Widget")
        self.gridLayout.addWidget(self.Spectrogram_Widget, 1, 0, 1, 1)
        self.Time_Series_Widget = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_Series_Widget.sizePolicy().hasHeightForWidth())
        self.Time_Series_Widget.setSizePolicy(sizePolicy)
        self.Time_Series_Widget.setMinimumSize(QtCore.QSize(400, 0))
        self.Time_Series_Widget.setObjectName("Time_Series_Widget")
        self.gridLayout.addWidget(self.Time_Series_Widget, 0, 0, 1, 1)
        self.Spectrum_and_SPL_Widget = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Spectrum_and_SPL_Widget.sizePolicy().hasHeightForWidth())
        self.Spectrum_and_SPL_Widget.setSizePolicy(sizePolicy)
        self.Spectrum_and_SPL_Widget.setObjectName("Spectrum_and_SPL_Widget")
        self.Time_Series_Widget.raise_()
        self.gridLayout.addWidget(self.Spectrum_and_SPL_Widget, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 2, 2, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 4)
        self.Run_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Run_button.setObjectName("Run_button")
        self.gridLayout_2.addWidget(self.Run_button, 0, 9, 1, 4)
        self.Lat_deg_box = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Lat_deg_box.setObjectName("Lat_deg_box")
        self.gridLayout_2.addWidget(self.Lat_deg_box, 6, 3, 1, 4)
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 3, 12, 1, 1)
        self.Nfft_spin_box = QtWidgets.QSpinBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Nfft_spin_box.setFont(font)
        self.Nfft_spin_box.setObjectName("Nfft_spin_box")
        self.gridLayout_2.addWidget(self.Nfft_spin_box, 2, 10, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 10, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.Browse_button = QtWidgets.QToolButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Browse_button.sizePolicy().hasHeightForWidth())
        self.Browse_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Browse_button.setFont(font)
        self.Browse_button.setObjectName("Browse_button")
        self.gridLayout_2.addWidget(self.Browse_button, 0, 0, 1, 9)
        self.Time_spin_box = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Time_spin_box.setFont(font)
        self.Time_spin_box.setObjectName("Time_spin_box")
        self.gridLayout_2.addWidget(self.Time_spin_box, 2, 5, 1, 3)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 8, 1, 2)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 3)
        self.Date_box = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Date_box.setObjectName("Date_box")
        self.gridLayout_2.addWidget(self.Date_box, 3, 3, 1, 5)
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 8, 1, 2)
        self.Time_box = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Time_box.setFont(font)
        self.Time_box.setObjectName("Time_box")
        self.gridLayout_2.addWidget(self.Time_box, 3, 10, 1, 2)
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 5, 0, 1, 5)
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 3)
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 6, 7, 1, 6)
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 3)
        self.Lon_deg_box = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Lon_deg_box.setObjectName("Lon_deg_box")
        self.gridLayout_2.addWidget(self.Lon_deg_box, 7, 3, 1, 4)
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 7, 7, 1, 6)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 8, 0, 1, 3)
        self.Shaft_box = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Shaft_box.setObjectName("Shaft_box")
        self.gridLayout_2.addWidget(self.Shaft_box, 8, 3, 1, 4)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 9, 0, 1, 3)
        self.Speed_box = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Speed_box.setObjectName("Speed_box")
        self.gridLayout_2.addWidget(self.Speed_box, 9, 3, 1, 4)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 11, 0, 1, 2)
        self.Comment_box = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Comment_box.sizePolicy().hasHeightForWidth())
        self.Comment_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Comment_box.setFont(font)
        self.Comment_box.setObjectName("Comment_box")
        self.gridLayout_2.addWidget(self.Comment_box, 11, 2, 1, 11)
        self.Write_button = QtWidgets.QToolButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Write_button.sizePolicy().hasHeightForWidth())
        self.Write_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Write_button.setFont(font)
        self.Write_button.setObjectName("Write_button")
        self.gridLayout_2.addWidget(self.Write_button, 12, 0, 1, 13)
        self.Filename_button = QtWidgets.QTextBrowser(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Filename_button.sizePolicy().hasHeightForWidth())
        self.Filename_button.setSizePolicy(sizePolicy)
        self.Filename_button.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Filename_button.setObjectName("Filename_button")
        self.gridLayout_2.addWidget(self.Filename_button, 1, 0, 1, 13)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Time to Analyze (s)"))
        self.Run_button.setText(_translate("MainWindow", "Process Data"))
        self.label_15.setText(_translate("MainWindow", "UTC"))
        self.Browse_button.setText(_translate("MainWindow", "Browse File"))
        self.label_2.setText(_translate("MainWindow", "Nfft"))
        self.label_6.setText(_translate("MainWindow", "Date (YYYYMMDD)"))
        self.label_8.setText(_translate("MainWindow", "Time (HHMM)"))
        self.label_16.setText(_translate("MainWindow", "Vessel Parameters"))
        self.label_7.setText(_translate("MainWindow", "Latitude"))
        self.label_11.setText(_translate("MainWindow", "in Decimal Minutes (e.g., 56 45.189)"))
        self.label_9.setText(_translate("MainWindow", "Longitude"))
        self.label_13.setText(_translate("MainWindow", "in Decimal Minutes (e.g., 156 54.859)"))
        self.label_3.setText(_translate("MainWindow", "Shaft speed (RPM)"))
        self.label_4.setText(_translate("MainWindow", "SOG (knots)"))
        self.label_5.setText(_translate("MainWindow", "Noise Comments"))
        self.Write_button.setText(_translate("MainWindow", "Write to log file"))
        self.Filename_button.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">File chosen</span></p></body></html>"))
