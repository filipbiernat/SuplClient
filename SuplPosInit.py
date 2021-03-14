# !/usr/bin/python
import pprint
from datetime import datetime

from SuplPdu import SuplPdu


class SuplPosInit(SuplPdu):

    def __init__(self, supl_codec, lpp_codec, session_id, latitude, longitude, debug=False):
        super().__init__(supl_codec, lpp_codec, 'SUPLPOSINIT', debug)
        self.pdu['sessionID'] = session_id
        self.__fill_position(latitude, longitude)
        self._fill_pdu_length()

    def __fill_position(self, latitude, longitude):
        encoded_latitude_sign = 'north' if latitude >= 0 else 'south'

        # 3GPP TS23.032, 6.1 The relation between the coded number N and the range of (absolute) latitudes X it encodes
        # is the following (X in degrees): N <= 2^23 / 90 * X < N+1
        encoded_latitude = int(abs(latitude) / 90 * (1 << 23))
        # except for N=2^23-1, for which the range is extended to include N+1.
        encoded_latitude = min(encoded_latitude, (1 << 23) - 1)

        # 3GPP TS23.032, 6.1 The relation between the coded number N and the range of longitude X it encodes is the
        # following (X in degrees): N <= 2^24 / 360 * X < N+1
        encoded_longitude = int(longitude / 360 * (1 << 24))
        # Corner case: value of 180 degrees has to be represented as -180 degrees (-2^23).
        if encoded_longitude == (1 << 23):
            encoded_longitude = -(1 << 23)

        self.pdu['message'][1]['position'] = {'positionEstimate': {'latitudeSign': encoded_latitude_sign,
                                                                   'latitude': encoded_latitude,
                                                                   'longitude': encoded_longitude},
                                              'timestamp': datetime.now()}

    def _fill_pdu(self):
        self.pdu = {'version': {'maj': 2, 'min': 1, 'servind': 0},
                    'message': ('msSUPLPOSINIT',
                                {'locationId': {'cellInfo': ('ver2-CellInfo-extension',
                                                             ('wlanAP',
                                                              {'apMACAddress': (b'\xff\xff\xff\xff\xff\xff', 48)})),
                                                'status': 'current'},
                                 'requestedAssistData': {'acquisitionAssistanceRequested': True,
                                                         'almanacRequested': False,
                                                         'dgpsCorrectionsRequested': False,
                                                         'ionosphericModelRequested': True,
                                                         'navigationModelData': {'gpsToe': 0,
                                                                                 'gpsWeek': 0,
                                                                                 'nSAT': 0,
                                                                                 'toeLimit': 0},
                                                         'navigationModelRequested': True,
                                                         'realTimeIntegrityRequested': False,
                                                         'referenceLocationRequested': True,
                                                         'referenceTimeRequested': True,
                                                         'utcModelRequested': False,
                                                         'ver2-RequestedAssistData-extension': {
                                                             'ganssRequestedGenericAssistanceDataList': [
                                                                 {'ganssAlmanac': False,
                                                                  'ganssAuxiliaryInformation': True,
                                                                  'ganssId': 4,
                                                                  'ganssNavigationModelData': {'ganssToe': 0,
                                                                                               'ganssWeek': 0,
                                                                                               't-toeLimit': 0},
                                                                  'ganssRealTimeIntegrity': False,
                                                                  'ganssReferenceMeasurementInfo': False,
                                                                  'ganssUTCModel': False},
                                                                 {'ganssAlmanac': False,
                                                                  'ganssAuxiliaryInformation': True,
                                                                  'ganssId': 0,
                                                                  'ganssNavigationModelData': {'ganssToe': 0,
                                                                                               'ganssWeek': 0,
                                                                                               't-toeLimit': 0},
                                                                  'ganssRealTimeIntegrity': False,
                                                                  'ganssReferenceMeasurementInfo': False,
                                                                  'ganssUTCModel': False}]}},
                                 'sETCapabilities': {'posProtocol': {'rrc': False,
                                                                     'rrlp': True,
                                                                     'tia801': False,
                                                                     'ver2-PosProtocol-extension': {'lpp': True,
                                                                                                    'posProtocolVersionLPP': {
                                                                                                        'editorialVersionField': 1,
                                                                                                        'majorVersionField': 14,
                                                                                                        'technicalVersionField': 0}}},
                                                     'posTechnology': {'aFLT': False,
                                                                       'agpsSETBased': True,
                                                                       'agpsSETassisted': False,
                                                                       'autonomousGPS': True,
                                                                       'eCID': False,
                                                                       'eOTD': False,
                                                                       'oTDOA': False},
                                                     'prefMethod': 'agpsSETBasedPreferred'},
                                 'sUPLPOS': {'posPayLoad': ('ver2-PosPayLoad-extension',
                                                            {'lPPPayload': [self._get_lpp_provide_capabilities_pdu(),
                                                                            self._get_lpp_request_assistance_data_pdu()]})}})}

    def _get_lpp_provide_capabilities_pdu(self):
        lpp_pdu = {'transactionID': {'initiator': 'targetDevice', 'transactionNumber': 0},
                   'endTransaction': True,
                   'lpp-MessageBody': ('c1',
                                       ('provideCapabilities',
                                        {'criticalExtensions': ('c1', self._get_lpp_provide_capabilities())}))}
        if self.debug:
            print('Encoded LPP Provide Capabilities PDU:')
            pprint.pprint(lpp_pdu)
        return self.lpp_codec.encode("LPP-Message", lpp_pdu)

    @staticmethod
    def _get_lpp_provide_capabilities():
        return ('provideCapabilities-r9',
                {'a-gnss-ProvideCapabilities': {'assistanceDataSupportList': {
                    'gnss-CommonAssistanceDataSupport': {'gnss-ReferenceLocationSupport': {},
                                                         'gnss-ReferenceTimeSupport': {
                                                             'gnss-SystemTime': {'gnss-ids': (b'\x80', 1)}}},
                    'gnss-GenericAssistanceDataSupport': [{'gnss-AcquisitionAssistanceSupport': {},
                                                           'gnss-AlmanacSupport': {'almanacModel': (b'@', 2)},
                                                           'gnss-ID': {'gnss-id': 'gps'},
                                                           'gnss-NavigationModelSupport': {'clockModel': (b'\x10', 4),
                                                                                           'orbitModel': (b'\x10', 4)},
                                                           'gnss-RealTimeIntegritySupport': {}},
                                                          {'gnss-AcquisitionAssistanceSupport': {},
                                                           'gnss-AlmanacSupport': {'almanacModel': (b'\x08', 5)},
                                                           'gnss-AuxiliaryInformationSupport': {},
                                                           'gnss-ID': {'gnss-id': 'glonass'},
                                                           'gnss-NavigationModelSupport': {},
                                                           'gnss-RealTimeIntegritySupport': {}},
                                                          {'gnss-AcquisitionAssistanceSupport': {},
                                                           'gnss-AlmanacSupport': {'almanacModel': (b'\x80', 1)},
                                                           'gnss-ID': {'gnss-id': 'galileo'},
                                                           'gnss-NavigationModelSupport': {'clockModel': (b'\x80', 1),
                                                                                           'orbitModel': (b'\x80', 1)},
                                                           'gnss-RealTimeIntegritySupport': {}}]},
                    'gnss-SupportList': [{'adr-Support': False,
                                          'agnss-Modes': {'posModes': (b'@', 2)},
                                          'gnss-ID': {'gnss-id': 'gps'},
                                          'gnss-Signals': {'gnss-SignalIDs': (b'\x01', 8)},
                                          'velocityMeasurementSupport': True},
                                         {'adr-Support': False,
                                          'agnss-Modes': {'posModes': (b'@', 2)},
                                          'gnss-ID': {'gnss-id': 'glonass'},
                                          'gnss-Signals': {'gnss-SignalIDs': (b'\x01', 8)},
                                          'velocityMeasurementSupport': True},
                                         {'adr-Support': False,
                                          'agnss-Modes': {'posModes': (b'@', 2)},
                                          'gnss-ID': {'gnss-id': 'galileo'},
                                          'gnss-Signals': {'gnss-SignalIDs': (b'\x01', 8)},
                                          'velocityMeasurementSupport': True}],
                    'locationCoordinateTypes': {'ellipsoidArc': False,
                                                'ellipsoidPoint': False,
                                                'ellipsoidPointWithAltitude': False,
                                                'ellipsoidPointWithAltitudeAndUncertaintyEllipsoid': True,
                                                'ellipsoidPointWithUncertaintyCircle': False,
                                                'ellipsoidPointWithUncertaintyEllipse': False,
                                                'polygon': False},
                    'velocityTypes': {'horizontalVelocity': False,
                                      'horizontalVelocityWithUncertainty': False,
                                      'horizontalWithVerticalVelocity': False,
                                      'horizontalWithVerticalVelocityAndUncertainty': True}}})

    def _get_lpp_request_assistance_data_pdu(self):
        lpp_pdu = {'transactionID': {'initiator': 'targetDevice', 'transactionNumber': 1},
                   'endTransaction': False,
                   'lpp-MessageBody': ('c1',
                                       ('requestAssistanceData',
                                        {'criticalExtensions': ('c1', self._get_lpp_request_assistance_data())}))}
        if self.debug:
            print('Encoded LPP Request Assistance Data PDU:')
            pprint.pprint(lpp_pdu)
        return self.lpp_codec.encode("LPP-Message", lpp_pdu)

    @staticmethod
    def _get_lpp_request_assistance_data():
        return ('requestAssistanceData-r9',
                {'a-gnss-RequestAssistanceData': {'gnss-CommonAssistDataReq': {'gnss-IonosphericModelReq': {},
                                                                               'gnss-ReferenceLocationReq': {},
                                                                               'gnss-ReferenceTimeReq': {
                                                                                   'gnss-TimeReqPrefList': [
                                                                                       {'gnss-id': 'gps'},
                                                                                       {'gnss-id': 'glonass'},
                                                                                       {'gnss-id': 'galileo'}]}},
                                                  'gnss-GenericAssistDataReq': [{'gnss-AlmanacReq': {},
                                                                                 'gnss-ID': {'gnss-id': 'gps'},
                                                                                 'gnss-NavigationModelReq': (
                                                                                     'reqNavList',
                                                                                     {'svReqList': (b'\xff\xff\xff\xff'
                                                                                                    b'\xff\xff\xff\xfe',
                                                                                                    64)}),
                                                                                 'gnss-RealTimeIntegrityReq': {},
                                                                                 'gnss-UTCModelReq': {}},
                                                                                {'gnss-AlmanacReq': {},
                                                                                 'gnss-AuxiliaryInformationReq': {},
                                                                                 'gnss-ID': {'gnss-id': 'glonass'},
                                                                                 'gnss-NavigationModelReq': (
                                                                                     'reqNavList',
                                                                                     {'svReqList': (b'\xff\xff\xff\xff'
                                                                                                    b'\xff\xff\xff\xfe',
                                                                                                    64)}),
                                                                                 'gnss-RealTimeIntegrityReq': {},
                                                                                 'gnss-TimeModelsReq': [
                                                                                     {'deltaTreq': True,
                                                                                      'gnss-TO-IDsReq': 1}],
                                                                                 'gnss-UTCModelReq': {}},
                                                                                {'gnss-AlmanacReq': {},
                                                                                 'gnss-ID': {'gnss-id': 'galileo'},
                                                                                 'gnss-NavigationModelReq': (
                                                                                     'reqNavList',
                                                                                     {'svReqList': (b'\xff\xff\xff\xff'
                                                                                                    b'\xff\xff\xff\xfe',
                                                                                                    64)}),
                                                                                 'gnss-RealTimeIntegrityReq': {},
                                                                                 'gnss-UTCModelReq': {}}]},
                 'commonIEsRequestAssistanceData': {'primaryCellID': {'cellidentity': (b'D \xe0 ', 28),
                                                                      'mcc': [3, 1, 0],
                                                                      'mnc': [2, 6, 0]}}})
