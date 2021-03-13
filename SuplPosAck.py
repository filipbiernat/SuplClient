# !/usr/bin/python
import datetime


class SuplPosAck:

    def __init__(self, slp_session_id):
        self.name = 'SUPLPOSACK'
        self.pdu = self.__fill_pdu()
        self.set_slp_session_id(slp_session_id)

    def set_slp_session_id(self, slp_session_id):
        self.pdu['sessionID']['slpSessionID'] = slp_session_id

    @staticmethod
    def __fill_pdu():
        pdu = {'length': 39,
               'message': ('msSUPLPOS',
                           {'posPayLoad': ('ver2-PosPayLoad-extension',
                                           {'lPPPayload': [b'\x92\x08(\x00']})}),
               'sessionID': {'setSessionID': {'sessionId': 38228,
                                              'setId': ('iPAddress',
                                                        ('ipv4Address', b'\n\x17db'))}},
               'version': {'maj': 2, 'min': 0, 'servind': 0}}
        return pdu
