# !/usr/bin/python
import datetime


class SuplPosInit:

    def __init__(self, session_id):
        self.name = 'SUPLPOSINIT'

        self.pdu = self.__fill_pdu()
        self.pdu['sessionID'] = session_id

    @staticmethod
    def __fill_pdu():
        pdu = {'length': 179,
               'version': {'maj': 2, 'min': 1, 'servind': 0},
               'message': ('msSUPLPOSINIT',
                           {'locationId': {'cellInfo': ('ver2-CellInfo-extension',
                                                        ('wlanAP',
                                                         {'apMACAddress': (b'\xff\xff\xff\xff'
                                                                           b'\xff\xff',
                                                                           48)})),
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
                                                       {'lPPPayload': [b'\x92\x07\x08!'
                                                                       b'\xe4\x00(\x05'
                                                                       b'\x04\x14\x02\x81'
                                                                       b'\x8a\x01L\x01'
                                                                       b'\x10l\x03b\xc4J\x1bH'
                                                                       b'\x06\x04\x1b\x06'
                                                                       b'\xc4D@\x82',
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
        return pdu
