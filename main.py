# !/usr/bin/python

import asn1tools
from Connection import Connection
from SuplStart import SuplStart
from SuplResponse import SuplResponse
from SuplPosInit import SuplPosInit
from SuplPos import SuplPos
from SuplPosAck import SuplPosAck


def query_assistance_data():
    supl_codec = asn1tools.compile_files(['ASN1Definitions/SUPL.asn',
                                          'ASN1Definitions/ULP.asn',
                                          'ASN1Definitions/ULP-Components.asn'], 'uper')
    lpp_codec = asn1tools.compile_files('ASN1Definitions/LPP.asn', 'uper')

    latitude = 49.883427
    longitude = 19.492598

    connection = Connection('108.177.126.192', 7276, supl_codec, debug=True)

    supl_start = SuplStart(supl_codec, lpp_codec)
    connection.send(supl_start.name, supl_start.pdu)

    received_pdu = connection.receive('SUPLRESPONSE')
    supl_response = SuplResponse(supl_codec, lpp_codec, received_pdu)
    session_id = supl_response.get_session_id()

    supl_pos_init = SuplPosInit(supl_codec, lpp_codec, session_id, latitude, longitude, debug=True)
    connection.send(supl_pos_init.name, supl_pos_init.pdu)

    received_pdu = connection.receive('SUPLPOS')
    supl_pos = SuplPos(supl_codec, lpp_codec, received_pdu, debug=True)

    supl_pos_ack = SuplPosAck(supl_codec, lpp_codec, session_id)
    connection.send(supl_pos_ack.name, supl_pos_ack.pdu)

    connection.receive('SUPLEND')

    supl_pos.get_lpp_provide_assistance_data_pdu()


if __name__ == '__main__':
    query_assistance_data()
