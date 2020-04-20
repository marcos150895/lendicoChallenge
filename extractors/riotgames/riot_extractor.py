import requests

from helpers.logger import Logger


class RiotExtractor:
    def __init__(self):
        self.logger = Logger().getLogger()

    def get_data_from_api(self, endpoint="", headers="" , api_name=""):
        try:
            self.logger.info("getting {}'s data from {} with headers {}".format(api_name, endpoint, headers))

            response = requests.request("GET", endpoint, headers=headers)

            if response.status_code >= 400:
                raise ValueError('API dont works as expected, getting status code {} and error {}'
                                 .format(response.status_code, response.json()))

            return response.json()

        except Exception as ex:
            self.logger.error("getting {}'s data from {} with headers {}".format(api_name, endpoint, headers))
            self.logger.error('Error: {}'.format(ex))
