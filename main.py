# -*- coding: utf-8 -*-

import gc

from extractors.riotgames.riot_extractor import RiotExtractor
from config.command_line_args import CommandLineArgs
from writers.writer import Writer
from analysis.riot_champion_points_x_champion_id import RiotChampionPointsXChampionID
from helpers.utils import Utils


# enable garbage collector
gc.enable()

# get configs
confs = CommandLineArgs().get_args()


def master_leagues():
    endpoint = confs['master_leagues_endpoint'][0]
    headers = Utils.format_header(confs['access_key'][0])

    master_leagues_json = RiotExtractor()\
        .get_data_from_api(endpoint=endpoint, headers=headers, api_name='master leagues')

    return master_leagues_json


def champion_mastery():
    endpoint_without_slash_in_the_end = Utils.remove_slash_in_end_of_string(confs['champion_mastery_endpoint'][0])
    endpoint = endpoint_without_slash_in_the_end + '/' + confs['champion_mastery_summoner_id'][0]
    headers = Utils.format_header(confs['access_key'][0])

    champion_mastery_json = RiotExtractor()\
        .get_data_from_api(endpoint=endpoint, headers=headers, api_name='champion mastery')

    return champion_mastery_json


def main():
    # executing master leagues json writer
    master = master_leagues()
    champion = champion_mastery()

    # writer both in file system
    Writer().write_json(data=master, file_name="master_leagues", output_path=confs['dest'][0])
    Writer().write_json(data=champion, file_name="champion_mastery", output_path=confs['dest'][0])

    # plotting and save championPointchart
    RiotChampionPointsXChampionID(champion).save_chart_as_image(path=confs['dest'][0])


if __name__ == '__main__':
    main()
