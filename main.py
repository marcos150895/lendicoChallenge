# -*- coding: utf-8 -*-

import gc

from extractors.riotgames.riot_extractor import RiotExtractor
from config.command_line_args import CommandLineArgs
from writers.writer import Writer


# enable garbage collector
gc.enable()

# get configs
confs = CommandLineArgs().get_args()


def format_header():
    headers = {
        'X-Riot-Token': confs['access_key'][0]
    }

    return headers


def master_leagues():
    endpoint = confs['master_leagues_endpoint'][0]
    headers = format_header()

    maste_leagues_json = RiotExtractor().get_data_from_api(endpoint=endpoint, headers=headers, api_name='master leagues')

    return maste_leagues_json


def champion_mastery():
    ## tratar esse barra
    endpoint = confs['champion_mastery_endpoint'][0] + '/' + confs['champion_mastery_summoner_id'][0]
    headers = format_header()

    champion_mastery_json = RiotExtractor()\
        .get_data_from_api(endpoint=endpoint, headers=headers, api_name='champion mastery')

    return champion_mastery_json



def main():
    # executing master leagues json writer
    master = master_leagues()
    champion = champion_mastery()

    Writer().write_json(data=master, file_name="master_leagues", output_path=confs['dest'][0])
    Writer().write_json(data=champion, file_name="champion_mastery", output_path=confs['dest'][0])


if __name__ == '__main__':
    main()

