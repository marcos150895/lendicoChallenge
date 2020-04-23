import unittest
from unittest.mock import patch

from extractors.riotgames.riot_extractor import RiotExtractor


class RiotExtractorTest(unittest.TestCase):
    def setup_method(self, method):
        self.extractor = RiotExtractor()

    @patch("requests.request")
    def test_get_data_from_api(self, mock_get):
        mock_data = {
            'tier': 'MASTER',
            'leagueId': '7d301bfc-9867-3390-b1f7-da7f42d12cf9',
            'queue': 'RANKED_SOLO_5x5',
            'name': 'Zyras Demolishers',
            'entries': [
                {
                    'summonerId': '38qXY5lYF21b3TYLcF8j8lw0DlVrfdc8e8rCF55vdH1YlA',
                    'summonerName': 'Shn1',
                    'leaguePoints': 0,
                    'rank': 'I',
                    'wins': 33,
                    'losses': 15,
                    'veteran': False,
                    'inactive': False,
                    'freshBlood': True,
                    'hotStreak': False
                }
            ]
        }

        class MockedResponse:
            def __init__(self):
                self.status_code = 200

            def json(self):
                return mock_data

        mock_get.return_value = MockedResponse()

        data = self.extractor.get_data_from_api(endpoint="lendicotest.com/endpoint", headers="{}")

        self.assertEqual(data['tier'], 'MASTER', 'Testing tier value')
        self.assertEqual(data['leagueId'], '7d301bfc-9867-3390-b1f7-da7f42d12cf9', 'Testing league value')
        self.assertEqual(data['queue'], 'RANKED_SOLO_5x5', 'Testing queue value')
        self.assertEqual(data['name'], 'Zyras Demolishers', 'Testing name value')
        self.assertEqual(data['entries'][0]['summonerId'], '38qXY5lYF21b3TYLcF8j8lw0DlVrfdc8e8rCF55vdH1YlA')

    @patch("requests.request")
    def test_get_data_from_api_error(self, mock_get):
        mocked_data = {
            'status': {
                'message': 'Forbidden',
                'status_code': 403
            }
        }

        class MockedResponse:
            def __init__(self):
                self.status_code = 400

            def json(self):
                return mocked_data

        mock_get.return_value = MockedResponse()

        data = self.extractor.get_data_from_api(endpoint="lendicotest.com/endpoint", headers="{}")

        self.assertEqual(data, None, 'Testing error status message value')
