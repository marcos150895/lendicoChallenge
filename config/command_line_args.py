# -*- coding: utf-8 -*-

#
#   This class contains the arguments to running the application,
#   if these arguments are input in the running the overwrite the default variables
#

import argparse
from collections import defaultdict

from helpers.logger import Logger
from helpers.singleton import Singleton


class CommandLineArgs(Singleton):
    def __init__(self):
        self.get_args()
        self.logger = Logger().getLogger()

    def get_args(self):
        try:
            ap = argparse.ArgumentParser()

            ap.add_argument("--dest", required=True, default="", help="path that script will put the api files")
            ap.add_argument("--dest_format", default="json", required=False, help="file format to output")
            ap.add_argument("--master_leagues_endpoint", default="", required=False, help="endpoint to access master leagues api")
            ap.add_argument("--champion_mastery_endpoint", default="", required=False, help="endpoint to access champion mastery api")
            ap.add_argument("--champion_mastery_summoner_id", default="", required=False, help="summoner id to filter api by summoner")
            ap.add_argument("--access_key", required=True, default="", help="access key to access API")

            args = ap.parse_args()

            return args

        except Exception as ex:
            self.logger.error("can't get command line arguments")
            self.logger.error('Error: {}'.format(ex))
