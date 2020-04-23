import unittest

from pathlib import Path


from analysis.riot_champion_points_x_champion_id import RiotChampionPointsXChampionID


class RiotExtractorTest(unittest.TestCase):
    def setup_method(self, method):
        self.test = "Testing"
        mock_data = [
            {
                'championId': 64,
                'championLevel': 7,
                'championPoints': 989585,
                'lastPlayTime': 1587584240000,
                'championPointsSinceLastLevel': 967985,
                'championPointsUntilNextLevel': 0,
                'chestGranted': True,
                'tokensEarned': 0,
                'summonerId': '38qXY5lYF21b3TYLcF8j8lw0DlVrfdc8e8rCF55vdH1YlA'
            },
            {
                'championId': 67,
                'championLevel': 7,
                'championPoints': 245872,
                'lastPlayTime': 1586666672000,
                'championPointsSinceLastLevel': 224272,
                'championPointsUntilNextLevel': 0,
                'chestGranted': False,
                'tokensEarned': 0,
                'summonerId': '38qXY5lYF21b3TYLcF8j8lw0DlVrfdc8e8rCF55vdH1YlA'
            }
        ]

        self.chart = RiotChampionPointsXChampionID(mock_data)

    def test_plot_chart(self):
        chart = self.chart.plot_chart()

        self.assertEqual(str(type(chart)), "<class 'pygal.graph.bar.Bar'>", 'Testing type value')

    def test_save_chart_as_image(self):
        path = 'tests/'

        self.chart.save_chart_as_image(path)

        exists_png = Path(path + 'champion_points_champion_id.png').exists()
        exists_svg = Path(path + 'champion_points_champion_id.svg').exists()

        self.assertEqual(exists_png, True, 'Checking if image (png) is save in file System')
        self.assertEqual(exists_svg, True, 'Checking if image (svg) is save in file System')
