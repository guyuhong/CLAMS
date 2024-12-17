#!/usr/bin/env python

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from ui import ui_BinDialog
import numpad
import messagedlg


class BinDialog(QDialog, ui_BinDialog.Ui_binDialog):
    def __init__(self, parent=None):
        super(BinDialog, self).__init__(parent)
        self.setupUi(self)
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.message=parent.message

        self.widthLabel.palette().setColor(self.widthLabel.backgroundRole(), QColor(255, 255, 255))
        self.lengthLabel.palette().setColor(self.lengthLabel.backgroundRole(), QColor(255, 255, 255))
        self.depthLabel.palette().setColor(self.depthLabel.backgroundRole(), QColor(255, 255, 255))
        self.haulWtLabel.palette().setColor(self.haulWtLabel.backgroundRole(), QColor(255, 255, 255))

        self.widthFlag=False
        self.lengthFlag=False
        self.depthFlag=False
        self.densityFlag=False

        self.widthBtn.clicked.connect(self.getWidth)
        self.lengthBtn.clicked.connect(self.getLength)
        self.depthBtn.clicked.connect(self.getDepth)
        self.densityBtn.clicked.connect(self.getDensity)
        self.compBtn.clicked.connect(self.getCompute)
        self.okBtn.clicked.connect(self.OK)
        self.cancelBtn.clicked.connect(self.goExit)

        self.numpad = numpad.NumPad(self)
        self.message = messagedlg.MessageDlg(self)


    def getWidth(self):
        self.numpad.msgLabel.setText('Enter bin width')
        if self.numpad.exec():
            width = self.numpad.value
            self.widthLabel.setText(width)
            self.widthFlag = True


    def getLength(self):
        self.numpad.msgLabel.setText('Enter bin length')
        if self.numpad.exec():
            length = self.numpad.value
            self.lengthLabel.setText(length)
            self.lengthFlag = True


    def getDepth(self):
        self.numpad.msgLabel.setText('Enter bin fish level depth')
        if self.numpad.exec():
            depth = self.numpad.value
            self.depthLabel.setText(depth)
            self.depthFlag = True


    def getDensity(self):
        self.numpad.msgLabel.setText('Enter density of fish (if other than 1)')
        if self.numpad.exec():
            density = self.numpad.value
            self.densityLabel.setText(density)
            self.densityFlag = True


    def getCompute(self):
        if not self.widthFlag:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],
                    " No width was entered! ", 'info')
            self.message.exec()
            return
        if not self.lengthFlag:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],
                    " No Length was entered! ", 'info')
            self.message.exec()
            return
        if not self.depthFlag:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],
                    " No Depth was entered! ", 'info')
            self.message.exec()
            return

        width = float(self.widthLabel.text())
        length = float(self.lengthLabel.text())
        depth = float(self.depthLabel.text())
        density = float(self.densityLabel.text())

        self.haulWT = str(round(width * length * depth * density *1000, 0))
        self.haulWtLabel.setText(self.haulWT)

    def OK(self):
        self.accept()

    def goExit(self):
        self.reject()



