"""
messagedlg is a generic message dialog that presents an icon, text, and
a set of buttons. The buttons presented depend on the 'mode' that is
passed when setMessage is called. The dialog returns the text of the button
that was selected by the user.

For example, the choice dialog presents "yes" and "no" buttons. In the example
below, the variable yesNo will contain either 1 (Yes) or 0 (No) depending
on what the user selects:

mDialog.setMessage(errorIcon, errorSounds, "Do you want to do this?", 'choice')
yesNo = self.message.exec()

"""

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from ui import ui_MessageDlg


class MessageDlg(QDialog, ui_MessageDlg.Ui_messageDlg):

    def __init__(self,  parent=None):

        #  execute superclass inits
        super(MessageDlg, self).__init__(parent)
        #  setup the UI elements
        self.setupUi(self)

        #  connect signals
        self.btn_1.clicked.connect(self.goYes)
        self.btn_2.clicked.connect(self.goNo)
        self.btn_3.clicked.connect(self.goYes)


    def setMessage(self, icon, sound, str_val, mode=''):

        #  play the message sound
        sound.play()

        #  set up the buttons based on the mode
        if mode.lower() == 'choice':
            self.btn_1.setText('Yes')
            self.btn_2.setText('No')
            self.btn_2.show()
            self.btn_3.hide()

        elif mode.lower() == 'specdel':
            self.btn_1.setText('Specimen')
            self.btn_2.setText('Cancel')
            self.btn_3.setText('Measurement')
            self.btn_2.show()
            self.btn_3.show()

        else:
            self.btn_1.setText('OK')
            self.btn_2.hide()
            self.btn_3.hide()

        #  set the label to the passed message string
        self.msgLabel.setText(str_val)

        #  try to load the icon
        try:
            #  see if it is an animated icon (animated gif)
            self.iconLabel.setMovie(icon)
            icon.start()
        except:
            #  nope - it's a regular icon
            self.iconLabel.setPixmap(icon)


    def goYes(self):
        self.response = self.sender().text()
        self.accept()


    def goNo(self):
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

            #  set up the error sound and icon for the test
            errorSoundFile = 'sounds/Blaster.wav'
            errorSound = QSoundEffect()
            errorSound.setSource(QUrl.fromLocalFile(errorSoundFile))

            errorIconFile = 'icons/plankton.jpg'
            errorIcon = QPixmap.fromImage(QImage(errorIconFile))

            #  create an instance of the dialog and show
            testDialog = MessageDlg()
            testDialog.setMessage(errorIcon, errorSound, "Do you want to do this?",
                    'choice')
            result = testDialog.exec()

            #  print the output to the console
            print(result)

            #  exit the application
            QApplication.instance().quit()


if __name__ == "__main__":
    #  import test specific libraries
    import sys
    from PyQt6.QtMultimedia import QSoundEffect

    #  create an instance of QApplication
    app = QApplication(sys.argv)

    #  instantiate the test
    form = dialogTest()

    #  and start the application event loop
    app.exec()



