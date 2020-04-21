import pandas as pd
import pygal

from helpers.logger import Logger
from helpers.utils import Utils


class RiotChampionPointsXChampionID:

    def __init__(self, data):
        self.logger = Logger().getLogger()
        self.data = data
        self.chart = self.plot_chart()

    def plot_chart(self):
        try:
            self.logger.info("Plotting chart")

            # filter only championId and championPoints columns
            dataframe = pd.DataFrame(self.data)[['championId', 'championPoints']]
            dataframe['championId'] = dataframe['championId'].astype(str)

            # sort values to get the top 10 values descending
            dataframe = dataframe.sort_values(by=['championPoints'], ascending=False).head(10)

            chart = pygal.Bar(x_title='champion ID', y_title='champion Points')
            chart.title = 'Top 10 championPoints by championId'

            # adding data into chart object
            for index, row in dataframe.iterrows():
                chart.add('id ' + row['championId'], row['championPoints'])

            self.logger.info("chart plotted")

            return chart

        except Exception as ex:
            self.logger.error("can't plot chart")
            self.logger.error('Error: {}'.format(ex))

    def save_chart_as_image(self, path=""):
        try:
            path = Utils.remove_slash_in_end_of_string(path)
            path_full_png = path + '/champion_points_champion_id.png'
            path_full_svg = path + '/champion_points_champion_id.svg'

            self.chart.render_to_file(path_full_svg)
            self.chart.render_to_png(filename=path_full_png)

            self.logger.info("chart saved at {} as svg".format(path_full_svg))
            self.logger.info("chart saved at {} as png".format(path_full_png))

        except Exception as ex:
            self.logger.error("can't save chart in {}".format(path))
            self.logger.error('Error: {}'.format(ex))

