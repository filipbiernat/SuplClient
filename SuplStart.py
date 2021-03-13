# !/usr/bin/python
import socket
from random import randrange
from SuplPdu import SuplPdu


class SuplStart(SuplPdu):

    def __init__(self, supl_codec, lpp_codec):
        super().__init__(supl_codec, lpp_codec, 'SUPLSTART')
        self._fill_pdu_length()

    def _fill_pdu(self):
        self.pdu = {'version': {'maj': 2, 'min': 1, 'servind': 0},
                    'sessionID': {'setSessionID': {'sessionId': randrange(0xFFFF),
                                                   'setId': ('iPAddress',
                                                             ('ipv4Address', SuplStart.__get_client_ip_address()))}},
                    'message': ('msSUPLSTART',
                                {'locationId': {'cellInfo': ('ver2-CellInfo-extension',
                                                             ('wlanAP',
                                                              {'apMACAddress': (b'\xff\xff\xff\xff\xff\xff', 48)})),
                                                'status': 'current'},
                                 'sETCapabilities': {'posProtocol': {'rrc': False,
                                                                     'rrlp': True,
                                                                     'tia801': False,
                                                                     'ver2-PosProtocol-extension': {'lpp': True}},
                                                     'posTechnology': {'aFLT': False,
                                                                       'agpsSETBased': True,
                                                                       'agpsSETassisted': False,
                                                                       'autonomousGPS': True,
                                                                       'eCID': False,
                                                                       'eOTD': False,
                                                                       'oTDOA': False},
                                                     'prefMethod': 'agpsSETBasedPreferred'}})}

    @staticmethod
    def __get_client_ip_address():
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return socket.inet_aton(ip_address)
