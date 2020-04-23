from helpers.singleton import Singleton
from helpers.logger import Logger

from pathlib import Path


class Utils(Singleton):

    @staticmethod
    def format_header(token):
        headers = {
            'X-Riot-Token': token
        }

        return headers

    @staticmethod
    def remove_slash_in_end_of_string(text):

        last_char = text[len(text) - 1:]

        if last_char == '/':
            return text[:len(text) - 1]

        return text

    @staticmethod
    def create_path_if_not_exists(path):
        logger = Logger().getLogger()

        p = Path(path)

        if not p.exists():
            try:
                p.mkdir(parents=True, exist_ok=True)
            except Exception as ex:
                logger.error("Creation of the directory %s failed" % path)
                logger.error(ex)
            else:
                logger.info("Successfully created the directory %s" % path)
