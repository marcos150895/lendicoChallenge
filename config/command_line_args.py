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

    def get_default_args(self):
        try:
            args = {
                'dest': "",
                'dest_format': "json",
                'master_leagues_endpoint': "",
                'champion_mastery_endpoint': "",
                'champion_mastery_summoner_id': "",
                'access_key': ""
            }

            return args

        except Exception as ex:
            self.logger.error("can't use default args")
            self.logger.error('Error: {}'.format(ex))

    def get_running_args(self):
        try:
            ap = argparse.ArgumentParser()

            ap.add_argument("--dest", required=True, help="path that script will put the api files")
            ap.add_argument("--dest_format", required=False, help="file format to output")
            ap.add_argument("--master_leagues_endpoint", required=False, help="endpoint to access master leagues api")
            ap.add_argument("--champion_mastery_endpoint", required=False, help="endpoint to access champion mastery api")
            ap.add_argument("--champion_mastery_summoner_id", required=False, help="summoner id to filter api by summoner")
            ap.add_argument("--access_key", required=True, help="access key to access API")

            args = vars(ap.parse_args())

            return args

        except Exception as ex:
            self.logger.error("can't get command line arguments")
            self.logger.error('Error: {}'.format(ex))

    def get_args(self):
        try:
            default_args = self.get_default_args()
            running_args = self.get_running_args()

            args = defaultdict(list)

            for k, v in default_args.items():
                for x, y in running_args.items():
                    if k == x and y is not None and args[k] is not None:
                        args[k].append(y)
                    elif k == x and v is not None:
                        args[k].append(v)

            return args

        except Exception as ex:
            self.logger.error("can't merge default and command line arguments")
            self.logger.error('Error: {}'.format(ex))

