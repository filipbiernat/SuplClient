# !/usr/bin/python
import datetime
from SuplPdu import SuplPdu


class SuplPosInit(SuplPdu):

    def __init__(self, supl_codec, lpp_codec, session_id):
        super().__init__(supl_codec, lpp_codec, 'SUPLPOSINIT')
        self.pdu['sessionID'] = session_id
        self._fill_pdu_length()

    def _fill_pdu(self):
        self.pdu = {'version': {'maj': 2, 'min': 1, 'servind': 0},
                    'message': ('msSUPLPOSINIT',
                                {'locationId': {'cellInfo': ('ver2-CellInfo-extension',
                                                             ('wlanAP',
                                                              {'apMACAddress': (b'\xff\xff\xff\xff\xff\xff', 48)})),
                                                'status': 'current'},
                                 'position': {'positionEstimate': {'latitude': 4657141,
                                                                   'latitudeSign': 'north',
                                                                   'longitude': 953207},
                                              'timestamp': datetime.datetime(2021, 3, 13, 13, 43, 24)},
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
                                                         'ver2-RequestedAssistData-extension': {'ganssRequestedGenericAssistanceDataList': [{'ganssAlmanac': False,
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
                                                                                                    'posProtocolVersionLPP': {'editorialVersionField': 1,
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
                                                                            b'\x92\x08\x10bb\x12`D'
                                                                            b' \xe0&\xe0'
                                                                            b'\x80A\x81\x06'
                                                                            b'`!\xff\xff'
                                                                            b'\xff\xff\xff\xff'
                                                                            b'\xff\xfc\x02\xce'
                                                                            b'@\x05\x0f\xff'
                                                                            b'\xff\xff\xff\xff'
                                                                            b'\xff\xff\xe0\x03'
                                                                            b'0\xd0\xff\xff'
                                                                            b'\xff\xff\xff\xff'
                                                                            b'\xff\xfe\x00']})}})}

    def _get_lpp_provide_capabilities_pdu(self):
        msg = {'transactionID': {'initiator': 'targetDevice', 'transactionNumber': 3},
               'endTransaction': True,
               'lpp-MessageBody': ('c1',
                                   ('provideCapabilities',
                                    {'criticalExtensions': ('c1', self._get_lpp_provide_capabilities())}))}
        return self.lpp_codec.encode("LPP-Message", msg)

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
