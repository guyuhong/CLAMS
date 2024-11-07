"""
UDP_Sniffer.py can listen for data on or broadcast data as UDP datagrams
on one or more network interfaces and ports.

Sometimes it is convenient to make data available to other computers on
your network by transmitting simple data streams as UDP datagrams. When
you are doing this, you often need to test if data is being received by
a particular machine or maybe you are testing or developing applications
that receive simple UDP datagrams and you need to transmit some data.
This application can do both,

You must provide the mode argument when running the application. This
tells the application which mode to run in.

    'listen' will run in listen mode where the port(s) are opened
             and any data received on them is displayed with metadata

    'tx'     will run in transmit mode where a local port is opened
             and used to transmit data to the ports specified in the
             config file. The data that is sent is also set in the
             config file.

The optional argument '--config_file' can be used to specify the
path to the config file. The default is './udp_sniffer.yml'


This is best run from a command prompt: python ./UDP_Sniffer.py listen


You can use CTRL-C to exit the application when run from the console/command prompt.

"""

import os
import sys
import yaml
import argparse
import logging
from PyQt6 import QtCore, QtNetwork


class UDP_Sniffer(QtCore.QObject):

    stopRunning = QtCore.pyqtSignal()

    def __init__(self, mode, config_file, parent=None):
        #  initialize the superclass
        super(UDP_Sniffer, self).__init__(parent)

        #  create some internal attributes
        self.udp_sockets = []
        self.tx_timer = None

        # set the params
        self.mode = str(mode).strip().lower()
        self.config_file = config_file

        #  connect the stop signal to our stop method
        self.stopRunning.connect(self.stop_app)

        #  start things up after we get the event loop running by using a timer
        QtCore.QTimer.singleShot(0, self.start_app)


    def start_app(self):

        #  bump the cursor
        print()

        #  create a logger to log to the console
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(module)s - %(message)s')
        consoleLogger = logging.StreamHandler(sys.stdout)
        consoleLogger.setFormatter(formatter)
        self.logger.addHandler(consoleLogger)

        self.logger.info("Reading config file: " + self.config_file)
        self.logger.info("Starting UDP_Sniffer")
        self.logger.info("    Mode: " + self.mode)

        #  read the configuration file
        with open(self.config_file, 'r') as cf_file:
            try:
                config = yaml.safe_load(cf_file)
            except yaml.YAMLError as exc:
                self.logger.error('Error reading configuration file ' + self.config_file)
                self.logger.error('    Error string:' + str(exc))
                self.logger.error("Application exiting...")
                QtCore.QCoreApplication.instance().quit()
                return

        #  get the general params
        if 'local_address' in config:
            local_address = config['local_address']
        else:
            local_address = '0.0.0.0'

        if 'dest_address' in config:
            dest_address = config['dest_address']
        else:
            dest_address = '127.0.0.255'
        if 'tx_interval_ms' in config:
            try:
                tx_interval_ms = int(config['tx_interval_ms'])
            except:
                tx_interval_ms = 1000
        else:
            tx_interval_ms = 1000
        if 'local_port' in config:
            try:
                self.local_port = int(config['local_port'])
            except:
                self.local_port = 44999
        else:
            self.local_port = 44999

        #  make sure there is a 'ports' section in the config file
        if 'ports' not in config:
            self.logger.error("The required 'ports' section is missing from config file. ")
            self.logger.error("Application exiting...")
            QtCore.QCoreApplication.instance().quit()
            return

        #  get the port configuration (the port_number: tx_data mapping)
        self.udp_config = config['ports']

        #  set the local address
        self.local_address = QtNetwork.QHostAddress(local_address)
        self.dest_address = QtNetwork.QHostAddress(dest_address)

        if self.mode == 'tx':
            #  in TX mode we open a single local port and periodically
            #  send data from that port to the specified ports.

            #  create the socket on the specified interface and port
            self.logger.info("    Opening port %s:%i", local_address, self.local_port)
            udp_socket = QtNetwork.QUdpSocket(self)
            udp_socket.bind(self.local_address, self.local_port)

            #  add this to our list of socket objects
            self.udp_sockets.append(udp_socket)

            #  report the config
            self.logger.info("    TX Port config: ")
            for port in self.udp_config:
                self.logger.info("        Destination port %i  transmit data: %s", port,
                        str(self.udp_config[port]))

            #  create the transmit timer and start it
            self.tx_timer = QtCore.QTimer(self)
            self.tx_timer.timeout.connect(self.tx_udp_data)
            self.tx_timer.start(tx_interval_ms)

            self.logger.info("Starting to transmit...")

        else:
            #  anything other than 'tx' is listen mode. We open a udp socket for each of the ports
            #  specified in the config file and listen on them
            for port in self.udp_config:
                try:
                    #  create the local port we will listen on
                    local_port = int(port)
                    self.logger.info("    Opening port %s:%i for listen", local_address, local_port)
                    udp_socket = QtNetwork.QUdpSocket()
                    udp_socket.bind(self.local_address, local_port)
                    udp_socket.readyRead.connect(self.udp_data_available)

                    #  add this to our list of socket objects
                    self.udp_sockets.append(udp_socket)
                except Exception as e:
                    self.logger.error('Error opening port: ' + str(e))

            self.logger.info("Starting to listen...")

        self.logger.info("Press <CTRL>-C to stop application.")


    def tx_udp_data(self):

        for port in self.udp_config:

            #  convert the data to a byte array, but first and <cr><ls>
            this_data = (str(self.udp_config[port]) + '\r\n').encode()

            #  and transmit
            tx_bytes = self.udp_sockets[0].writeDatagram(this_data, self.dest_address,
                int(port))

            # and report
            self.logger.info('Transmitted %i byte datagram on local port %i to %s port %i: %s' %
                    (tx_bytes, self.local_port, self.dest_address.toString(),int(port),
                    self.udp_config[port]))


    @QtCore.pyqtSlot()
    def udp_data_available(self):

        #  get a reference to the port object that Rx'd the data
        udp_source = self.sender()

        while udp_source.hasPendingDatagrams():

            #  get the length of the next datagram and read it
            datagram_len = udp_source.pendingDatagramSize()
            data, source_host, source_port = udp_source.readDatagram(datagram_len)

            #  try to decode ASCII data
#            try:
            data = data.decode().strip('\r\n')
#            except:
#                data = 'UNABLE TO DECODE - DATAGRAM IS NOT PURE UTF-8'

            #  report the results
            self.logger.info('Received %i byte datagram on local port %i from %s port %i: %s' %
                    (datagram_len, udp_source.localPort(), source_host.toString(),source_port, data))


    @QtCore.pyqtSlot()
    def stop_app(self):

        #  stop the TX timer if needed
        if self.tx_timer:
            self.tx_timer.stop()

        #  close the sockets
        self.logger.info("Closing socket(s)...")
        for sock in self.udp_sockets:
            sock.close()

        self.logger.info("Application exiting...")
        QtCore.QCoreApplication.instance().quit()
        return


    def external_stop(self):
        '''
        external_stop is called when one of the main thread exit handlers are called.
        It emits a stop signal that is then received by the QCoreApplication which then
        shuts everything down in the QCoreApplication thread.
        '''
        self.stopRunning.emit()


def exit_handler(a,b=None):
    '''
    exit_handler is called when CTRL-c is pressed on Windows
    '''
    global ctrlc_pressed

    if not ctrlc_pressed:
        #  make sure we only act on the first ctrl-c press
        ctrlc_pressed = True
        print("CTRL-C detected. Shutting down...")
        console_app.external_stop()

    return True


def signal_handler(*args):
    '''
    signal_handler is called when ctrl-c is pressed when the python console
    has focus. On Linux this is also called when the terminal window is closed
    or when the Python process gets the SIGTERM signal.
    '''
    global ctrlc_pressed

    if not ctrlc_pressed:
        #  make sure we only act on the first ctrl-c press
        ctrlc_pressed = True
        print("CTRL-C or SIGTERM/SIGHUP detected. Shutting down...")
        console_app.external_stop()

    return True


if __name__ == '__main__':

    #  create a state variable to track if the user typed ctrl-c to exit
    ctrlc_pressed = False

    #  Set up the handlers to trap ctrl-c
    if sys.platform == "win32":
        #  On Windows, we use win32api.SetConsoleCtrlHandler to catch ctrl-c
        import win32api
        win32api.SetConsoleCtrlHandler(exit_handler, True)
    else:
        #  On linux we can use signal to get not only ctrl-c, but
        #  termination and hangup signals also.
        import signal
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGHUP, signal_handler)

    #  set the default args
    config_file = "./UDP_Sniffer.yml"

    #  create the argument parser. Set the application description.
    parser = argparse.ArgumentParser(prog='UDP_Sniffer', description="Listens for or transmits data as UDP "+
            "and can be used to check and diagnose UDP data broadcast issues and to help test applications "+
            "that receive data over UDP.")

    #  specify the positional arguments: ODBC connection, username, password
    parser.add_argument("mode", help="Specify the mode. Modes are 'listen' to listen for incoming data " +
            "and 'tx' to transmit data (to mimic SCS for testing.) Use the '--config_file' argument to set the " +
            "path to the config file that defines the ports to listen/transmit on. The default path is " +
            "./UDP_Sniffer.yml")
    parser.add_argument("-c", "--config_file", help="Specify the YML file containing the  port number " +
            "to data mapping. Default: ./UDP_Sniffer.yml")

    #  parse our arguments
    args = parser.parse_args()
    if (args.config_file):
        config_file = os.path.normpath(str(args.config_file))

    #  create an instance of QCoreApplication and and instance of the our example application
    app = QtCore.QCoreApplication(sys.argv)
    console_app = UDP_Sniffer(args.mode, config_file, parent=app)

    #  and start the event loop
    sys.exit(app.exec())
