# !/usr/bin/python


class SuplPosAck:

    def __init__(self, session_id):
        self.name = 'SUPLPOSACK'

        self.pdu = self.__fill_pdu()
        self.pdu['sessionID'] = session_id

    @staticmethod
    def __fill_pdu():
        pdu = {'length': 39,
               'version': {'maj': 2, 'min': 0, 'servind': 0},
               'message': ('msSUPLPOS',
                           {'posPayLoad': ('ver2-PosPayLoad-extension',
                                           {'lPPPayload': [b'\x92\x08(\x00']})})}
        return pdu
