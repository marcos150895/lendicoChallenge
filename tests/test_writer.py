import unittest

from writers.writer import Writer
import json


class WriterTest(unittest.TestCase):
    def setup_method(self, method):
        self.writer = Writer()

    def test_write_json(self):
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

        # configuration to execute tests
        file_name = 'fake_data'
        output_path = ''
        self.writer.write_json(data=mock_data, file_name=file_name, output_path=output_path)

        full_output_path = file_name + '.json' if output_path == "" else '{}/{}.json'.format(output_path, file_name)

        # reading json from writer process
        with open(full_output_path) as f:
            data_from_disk = json.load(f)

        # validate if data is equals the disk
        self.assertEqual(mock_data, data_from_disk, 'Testing if file from disk has the same values')
