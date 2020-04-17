# -*- coding: utf-8 -*-

import os
import sys

from config.CommandLineArgs import CommandLineArgs
from extractors.riotgames.master_leagues_extractor import request
from helpers.logger import Logger

# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))  +'/config/')
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))  +'/extractors/')
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))  +'/helpers/')


if __name__ == '__main__':
    request()