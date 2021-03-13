# !/usr/bin/python


class SuplStart:

    def __init__(self):
        self.name = 'SUPLSTART'
        self.pdu = self.__fill_pdu()

    @staticmethod
    def __fill_pdu():
        pdu = {'length': 29,
               'message': ('msSUPLSTART',
                           {'locationId': {'cellInfo': ('ver2-CellInfo-extension',
                                                        ('wlanAP',
                                                         {'apMACAddress': (b'\xff\xff\xff\xff'
                                                                           b'\xff\xff',
                                                                           48)})),
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
                                                'prefMethod': 'agpsSETBasedPreferred'}}),
               'sessionID': {'setSessionID': {'sessionId': 38228,
                                              'setId': ('iPAddress',
                                                        ('ipv4Address', b'\n\x17db'))}},
               'version': {'maj': 2, 'min': 1, 'servind': 0}}
        return pdu
