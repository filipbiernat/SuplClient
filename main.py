# !/usr/bin/python

import asn1tools
from Connection import Connection
from SuplStart import SuplStart


def query_assistance_data():
    supl_codec = asn1tools.compile_files(['ASN1Definitions/SUPL.asn',
                                          'ASN1Definitions/ULP.asn',
                                          'ASN1Definitions/ULP-Components.asn'], 'uper')
    lpp_codec = asn1tools.compile_files('ASN1Definitions/LPP.asn', 'uper')

    connection = Connection('108.177.126.192', 7276, supl_codec, debug=True)

    supl_start = SuplStart()
    connection.send(supl_start.name, supl_start.pdu)
    connection.receive('SUPLRESPONSE')


if __name__ == '__main__':
    query_assistance_data()
