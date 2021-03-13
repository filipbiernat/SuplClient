# !/usr/bin/python
from SuplPdu import SuplPdu


class SuplResponse(SuplPdu):

    def __init__(self, supl_codec, lpp_codec, pdu):
        super().__init__(supl_codec, lpp_codec, 'SUPLRESPONSE')
        self.pdu = pdu

    def get_session_id(self):
        return self.pdu['sessionID']
