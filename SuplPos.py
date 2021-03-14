# !/usr/bin/python
import pprint
from SuplPdu import SuplPdu


class SuplPos(SuplPdu):

    def __init__(self, supl_codec, lpp_codec, pdu, debug=False):
        super().__init__(supl_codec, lpp_codec, 'SUPLPOS', debug)
        self.pdu = pdu

    def get_lpp_provide_assistance_data_pdu(self):
        encoded_lpp_pdu = self.pdu['message'][1]['posPayLoad'][1]['lPPPayload'][0]
        lpp_pdu = self.lpp_codec.decode("LPP-Message", encoded_lpp_pdu)
        if self.debug:
            print('Decoded LPP Provide Assistance Data PDU:')
            pprint.pprint(lpp_pdu)
        return lpp_pdu
