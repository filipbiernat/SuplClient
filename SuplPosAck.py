# !/usr/bin/python
from SuplPdu import SuplPdu


class SuplPosAck(SuplPdu):

    def __init__(self, supl_codec, lpp_codec, session_id):
        super().__init__(supl_codec, lpp_codec, 'SUPLPOSACK')
        self.pdu['sessionID'] = session_id
        self._fill_pdu_length()

    def _fill_pdu(self):
        self.pdu = {'version': {'maj': 2, 'min': 0, 'servind': 0},
                    'message': ('msSUPLPOS',
                                {'posPayLoad': ('ver2-PosPayLoad-extension',
                                                {'lPPPayload': [b'\x92\x08(\x00']})})}
