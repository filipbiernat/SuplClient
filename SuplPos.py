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

    def get_gnss_assistance_data(self):
        lpp_pdu = self.get_lpp_provide_assistance_data_pdu()
        return lpp_pdu['lpp-MessageBody'][1][1]['criticalExtensions'][1][1]['a-gnss-ProvideAssistanceData']

    def get_gnss_common_assistance_data(self):
        return self.get_gnss_assistance_data()['gnss-CommonAssistData']

    def get_gnss_generic_assistance_data(self):
        return self.get_gnss_assistance_data()['gnss-GenericAssistData']

    def get_gnss_constellations(self):
        return list(map(lambda elem: elem['gnss-ID']['gnss-id'], self.get_gnss_generic_assistance_data()))

    def get_gnss_generic_assistance_data_element(self, gnss_id):
        return next((elem for elem in self.get_gnss_generic_assistance_data() if elem['gnss-ID']['gnss-id'] == gnss_id),
                    None)
