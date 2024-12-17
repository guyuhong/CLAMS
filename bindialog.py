

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from ui import ui_BinDialog
import numpad


class BinDialog(QDialog, ui_BinDialog.Ui_binDialog):
    def __init__(self, parent=None):

        #  execute superclass inits and setup UI
        super(BinDialog, self).__init__()
        self.setupUi(self)

        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.message=parent.message

        #  set some initial state vars to track input
        self.widthFlag=False
        self.lengthFlag=False
        self.depthFlag=False
        self.densityFlag=False

        #  connect the signals
        self.widthBtn.clicked.connect(self.getWidth)
        self.lengthBtn.clicked.connect(self.getLength)
        self.depthBtn.clicked.connect(self.getDepth)
        self.densityBtn.clicked.connect(self.getDensity)
        self.compBtn.clicked.connect(self.getCompute)
        self.okBtn.clicked.connect(self.OK)
        self.cancelBtn.clicked.connect(self.goExit)

        #  create an instance of numpad for numerical input
        self.numpad = numpad.NumPad(self)


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




'''
Simple dialogs can be tested by executing directly in main, but dialogs that
require additional setup and/or the full application event loop running must
be executed by a testing class that executes the dialog within the event loop.
'''
class dialogTest(QObject):
        def __init__(self):
            super(dialogTest, self).__init__(None)

            #  we use a timer here to add runTest to the event processing queue and
            #  then exit the init. Execution will return to main, where the
            #  application event loop will be started by the call to app.exec() which
            #  will then start processing events on the queue which will then execute
            #  runTest with the event loop running.
            startTimer = QTimer(self)
            startTimer.timeout.connect(self.runTest)
            startTimer.setSingleShot(True)
            startTimer.start(0)


        def runTest(self):

            #  BinDialog requires a list of sounds, icons, and an instance of
            #  messagedlg so we set all of that up here

            #  set up the error sound and icon for the test - in this case we put
            #  them in a list to mimic how CLAMS passes around icons and sounds
            errorSoundFile = 'sounds/Error.wav'
            errorSound = QSoundEffect()
            errorSound.setSource(QUrl.fromLocalFile(errorSoundFile))
            self.errorSounds = [errorSound]

            errorIconFile = 'icons/squidworth.jpg'
            errorIcon = QPixmap.fromImage(QImage(errorIconFile))
            self.errorIcons = [errorIcon]

            #  create an instance of the message dialog since the BinDialog
            #  requires it.
            self.message = messagedlg.MessageDlg()

            #  create an instance of the dialog and show
            testDialog = BinDialog(parent=self)
            testDialog.exec()
            result = testDialog.haulWT

            #  print the output to the console
            print(result)

            #  exit the application
            QApplication.instance().quit()



if __name__ == "__main__":
    #  import test specific libraries
    import sys
    import messagedlg
    from PyQt6.QtMultimedia import QSoundEffect

    #  create an instance of QApplication
    app = QApplication(sys.argv)

    #  instantiate the test
    form = dialogTest()

    #  and start the application event loop
    app.exec()

