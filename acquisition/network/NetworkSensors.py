
from PyQt4 import QtCore, QtNetwork

class NetworkSensors(QtCore.QObject):
    '''
    A new class for connecting sensors and collecting data on the network
    
    **Public Methods**

    **addSensor** -- connect a sensor to a host IP & port, works for both UDP and TCP connection types

    **close** -- Disconnect all sensors.

    **removeSensor** -- remove a specific sensor to a host IP & port.

    **pollSensor** -- performs a one time query on all connected sensors

    Signals

    **datagramReceived** -- This signal is emitted when network sends sensor-specific 
                                        data on the connecting port

        @rtype: dictionary
        @returns: A dictionary keyed by sensor name. The values associated with
        the dictionary keys themselves are dictionaries containing the data associated
        with the sensor.

    **pollReceived** -- This signal is emitted when poll is requested for all sensors

        @rtype: dictionary
        @returns: A dictionary keyed by sensor name. The values associated with
        the dictionary keys themselves are dictionaries containing the data associated
        with the sensor.

    **SCSError** -- This signal is emitted when there is a problem with the SCS client.

        @rtype: int
        @returns: A integer value representing the error. Values are:
        1 - Network error. The connection to the SCS server has been lost.
        2 - Parse error. The SCS client was unable to parse the data returned
        from the server. Usually this means that some data was corrupted upon
        delivery from the server to the client.

        @rtype: QSCSError
        @returns: A exception object containing a bit more information about the
        error.
    '''

    #  define signals
    error = QtCore.pyqtSignal(int, str)
    datagramReceived = QtCore.pyqtSignal(dict)
    dataTimeout = QtCore.pyqtSignal(int)
    
    def __init__(self, parent=None, print_raw=False):
        '''
        Initialize the client class instance
        '''
        super(NetworkSensors, self).__init__(parent)

        # Establish empty dictionary to add one or more connections
        self.socket = {}
        # Set up look-up dictionary for socket to sensor name
        self.sensorName = {}
        # Set up empty dictionary to add a buffer for each connection
        self.rxBuffer = {}
        # Set up data dictionary for polling option
        self.data = {}
        # Option to display all raw data
        self.print_raw = print_raw
        # Time before a message is emitted that there hasn't been any data received in seconds
        self.dataTimeoutInt = 10
        #Initialize first sensor for timer
        self.firstSensor = True


    @QtCore.pyqtSlot()
    def receiveData(self):
        '''
        Receive data from an open UDP connection
        Find the specific sensor connection and emit
        '''
        # Determine which connection/socket was activated
        activeSocket = self.sender()
        
        # Current sensor
        sensor = self.sensorName[activeSocket]
        
        while activeSocket.hasPendingDatagrams():
            # We've received something so add time to the timer
            self.Timer.start()

            #  get the length of the next datagram and read it
            datagram_len = activeSocket.pendingDatagramSize()
            if datagram_len>0:
                data, source_host, source_port = activeSocket.readDatagram(datagram_len)
                data = data.decode()
                data = data.rstrip('\r\n')
                if data != '-Unknown-':

                    # This is the form of the output currently used for SCSClient, so match for now
                    dataToSend = {sensor:{'data_value':data}}
                    # Save data for polling option
                    self.data[sensor] = {'data_value':data}
                    # Emit datagram
                    self.datagramReceived.emit(dataToSend)
        
                            # print to screen if requested
                    if self.print_raw:
                        print(dataToSend)
    
    
    def noData(self):
        self.Timer.stop()
        self.dataTimeout.emit(self.dataTimeoutInt)
        self.Timer.start()
        
        
    def addSensor(self, sensorName, host, port, connection_type):
        '''
        Add a sensor connection to the socket dictionary
        '''
        # Use connection_type string to determine how to handle the socket setup
        if connection_type == 'UDP':
            # Initialize the connection with QUdpSocket
            print(sensorName)
            self.socket[sensorName] = QtNetwork.QUdpSocket(self)
            self.socket[sensorName].bind(int(port))
            self.socket[sensorName].readyRead.connect(self.receiveData)
        
        elif connection_type == 'TCP':
            # Initialize a QTcpSocket
            self.socket[sensorName] = QtNetwork.QTcpSocket(self)
            self.socket[sensorName].readyRead.connect(self.receiveData)
            self.socket[sensorName].connectToHost(host, port)
        
        self.sensorName[self.socket[sensorName]] = sensorName
        self.rxBuffer[sensorName] = ''
            
        # Once there is one sensor added, start the timer
        if self.firstSensor is True:
            self.startTimer()
            self.firstSensor = False

    def removeSensor(self, sensorName, host, port):
        '''
        Remove a sensor connection from the socket dictionary
        '''
        # Close the connection with the sensorName key to the socket dictionary
        self.close(self.socket[sensorName])
        # Remove the dictionary entry
        self.socket.pop(sensorName)

    def startTimer(self):
        self.Timer = QtCore.QTimer(self)
        self.Timer.timeout.connect(self.noData)
        self.Timer.setInterval(self.dataTimeoutInt*1000)
        self.Timer.start()

    def close(self):
        '''
        Close connection
        '''
        for name in self.socket:
            self.socket[name].close()



if __name__ == "__main__":
    import sys
    app = QtCore.QCoreApplication(sys.argv)

    client = NetworkSensors(print_raw = True)
    #client.addSensor('GPS', '', 4800, 'UDP')
    #client.addSensor('EK80', '', 4801, 'UDP')
    #client.addSensor('SST-SBE38', '10.48.17.223', 5001, 'TCP')
    #client.addSensor('SST-Mid-Hull', '10.48.17.223', 5002, 'TCP')
    #client.addSensor('SST-Sal', '10.48.17.223', 5003, 'TCP')
    app.exec_()
