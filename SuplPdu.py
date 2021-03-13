# !/usr/bin/python


class SuplPdu:

    def __init__(self, supl_codec, lpp_codec, name):
        self.supl_codec = supl_codec
        self.lpp_codec = lpp_codec
        self.name = name
        self._fill_pdu()

    def _fill_pdu(self):
        self.pdu = None

    def _fill_pdu_length(self):
        if self.pdu is not None:
            if 'length' not in self.pdu:
                self.pdu['length'] = 0  # Create placeholder before encoding

            encoded_pdu = self.supl_codec.encode("ULP-PDU", self.pdu).hex()
            self.pdu['length'] = len(encoded_pdu) // 2  # 2 chars -> 1 byte
