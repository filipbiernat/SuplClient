# !/usr/bin/python

import socket
import sys
import pprint


class Connection:

    def __init__(self, host, port, supl_codec, debug):
        self.supl_codec = supl_codec
        self.debug = debug
        self.__establish_connection(host, port)

    def send(self, message_name, supl_pdu):
        encoded_supl_pdu = self.supl_codec.encode("ULP-PDU", supl_pdu)
        try:
            self.connection.sendall(encoded_supl_pdu)
        except socket.error:
            print('Sending failed')
            sys.exit()
        if self.debug:
            print('Sent ' + message_name + ':')
            pprint.pprint(supl_pdu)

    def receive(self, message_name):
        buffer_size = 0x4000;
        reply = self.connection.recv(buffer_size)
        supl_pdu = self.supl_codec.decode("ULP-PDU", reply)
        if self.debug:
            print('Received ' + message_name + ':')
            pprint.pprint(supl_pdu)
        return supl_pdu

    def __establish_connection(self, host, port):
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print('Failed to create socket')
            sys.exit()
        print('Socket Created')
        try:
            remote_ip = socket.gethostbyname(host)
        except socket.gaierror:
            print('Hostname could not be resolved. Exiting')
            sys.exit()
        self.connection.connect((remote_ip, port))
        print('Socket Connected to ' + host + ' on ip ' + remote_ip)
