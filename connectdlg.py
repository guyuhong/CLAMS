# coding=utf-8

#     National Oceanic and Atmospheric Administration (NOAA)
#     Alaskan Fisheries Science Center (AFSC)
#     Resource Assessment and Conservation Engineering (RACE)
#     Midwater Assessment and Conservation Engineering (MACE)

#  THIS SOFTWARE AND ITS DOCUMENTATION ARE CONSIDERED TO BE IN THE PUBLIC DOMAIN
#  AND THUS ARE AVAILABLE FOR UNRESTRICTED PUBLIC USE. THEY ARE FURNISHED "AS
#  IS."  THE AUTHORS, THE UNITED STATES GOVERNMENT, ITS INSTRUMENTALITIES,
#  OFFICERS, EMPLOYEES, AND AGENTS MAKE NO WARRANTY, EXPRESS OR IMPLIED,
#  AS TO THE USEFULNESS OF THE SOFTWARE AND DOCUMENTATION FOR ANY PURPOSE.
#  THEY ASSUME NO RESPONSIBILITY (1) FOR THE USE OF THE SOFTWARE AND
#  DOCUMENTATION; OR (2) TO PROVIDE TECHNICAL SUPPORT TO USERS.

"""
.. module:: ConnectDlg

    :synopsis: ConnectDlg presents a simple login dialog and
               optionally returns an instance of dbConnection
               created using the provided credentials.

| Developed by:  Rick Towler   <rick.towler@noaa.gov>
|                Kresimir Williams   <kresimir.williams@noaa.gov>
| National Oceanic and Atmospheric Administration (NOAA)
| National Marine Fisheries Service (NMFS)
| Alaska Fisheries Science Center (AFSC)
| Midwater Assesment and Conservation Engineering Group (MACE)
|
| Author:
|       Rick Towler   <rick.towler@noaa.gov>
|       Kresimir Williams   <kresimir.williams@noaa.gov>
| Maintained by:
|       Rick Towler   <rick.towler@noaa.gov>
|       Kresimir Williams   <kresimir.williams@noaa.gov>
|       Mike Levine   <mike.levine@noaa.gov>
|       Nathan Lauffenburger   <nathan.lauffenburger@noaa.gov>
"""

from PyQt6 import QtCore, QtWidgets
from ui import ui_ConnectDlg
import dbConnection


class ConnectDlg(QtWidgets.QDialog, ui_ConnectDlg.Ui_connectDlg):

    def __init__(self, source, username, password, label=None,
            bioSchema=None, enableBioschema=False, createConnection=True,
            schemaList=None, parent=None):

        #  set up the GUI
        super(ConnectDlg, self).__init__(parent)
        self.setupUi(self)

        #  save some attributes
        self.dbLabel = label
        self.createConnection = createConnection

        # load in bio schema options
        if not isinstance(schemaList, list):
            schemaList = [schemaList]
        self.schemaBox.addItems(schemaList)

        #  set up signals
        self.connectBtn.clicked.connect(self.connectClicked)
        self.cancelBtn.clicked.connect(self.cancelClicked)

        #  create a QSettings object with a (potentially) unique registry key. This allows
        #  different apps to store different creds
        self.regKey = 'ConnectDlg'
        if (label):
            self.regKey = self.regKey + '_' + str(self.dbLabel)
        self.appSettings = QtCore.QSettings('CLAMS', self.regKey)

        #  set the dialog state - if args are not provided during init, we try to pull them
        #  from the registry
        if (username == None):
            username = self.appSettings.value('username', '')
        self.userName.setText(username)
        if (source == None):
            source = self.appSettings.value('dbname', '')
        self.databaseName.setText(source)
        if (password == None):
            password = ''
        self.passwordName.setText('')
        if (bioSchema == None):
            self.bioSchema = self.appSettings.value('bioschema', '')
        else:
            self.bioSchema = bioSchema
        idx = self.schemaBox.findText(self.bioSchema, QtCore.Qt.MatchFlag.MatchExactly)
        if (idx > -1):
            self.schemaBox.setCurrentIndex(idx)
        else:
            self.schemaBox.setCurrentIndex(0)

        if not enableBioschema:
            self.schemaBox.setEnabled(False)
            self.schemaBox.setVisible(False)
            self.schemaLabel.setVisible(False)
        else:
            self.schemaBox.setEnabled(True)


    #  define the getters and setters for the dialog fields
    def setUsername(self, text):
        self.userName.setText(text)


    def getUsername(self):
        return str(self.userName.text())


    def setPassword(self, text):
        self.passwordName.setText(text)


    def getPassword(self):
        return str(self.passwordName.text())


    def setSource(self, text):
        self.databaseName.setText(text)


    def getSource(self):
        return str(self.databaseName.text())


    def getBioSchema(self):
        return str(self.schemaBox.currentText())


    def setBioSchema(self, text):
        #  only set the bioSchema combobox on a match, otherwise leave it as is.
        idx = self.schemaBox.findText(text, QtCore.Qt.MatchExactly)
        if (idx > -1):
            self.schemaBox.setCurrentIndex(idx)


    def connectClicked(self):
        """
          connect to the database.
        """

        if (self.createConnection):
            #  create the database connection object
            self.db = dbConnection.dbConnection(self.databaseName.text(), self.userName.text(),
                    self.passwordName.text(), self.dbLabel)

            #  store the bioSchema in the db object
            self.db.bioSchema = self.schemaBox.currentText()

            try:
                #  attempt to connect to the database
                self.db.dbOpen()

                #  save the updated credentials
                self.appSettings.setValue('dbName',self.databaseName.text())
                self.appSettings.setValue('username',self.userName.text())
                self.appSettings.setValue('bioschema',self.schemaBox.currentText())

                #  accept the event
                self.accept()

            except dbConnection.DBError as e:
                #  ooops, there was a problem
                errorMsg = ('Unable to connect to ' + self.userName.text() + '@' +
                        self.databaseName.text() + '\n' + e.error)
                QtWidgets.QMessageBox.critical(self, "Database Login Error", errorMsg)
                self.reject()
        else:

            #  if we're not creating a connection object blindly save the updated credentials
            self.appSettings.setValue('dbName',self.databaseName.text())
            self.appSettings.setValue('username',self.userName.text())
            self.appSettings.setValue('bioschema',self.schemaBox.currentText())

            self.accept()


    def cancelClicked(self):
        """
          Cancel connection.
        """
        self.reject()



