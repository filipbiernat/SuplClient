# !/usr/bin/python


class SuplResponse:

    def __init__(self, pdu):
        self.name = 'SUPLSTART'
        self.pdu = pdu

    def get_session_id(self):
        return self.pdu['sessionID']
