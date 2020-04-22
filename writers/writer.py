import json

from helpers.logger import Logger
from helpers.utils import  Utils


class Writer:

    def __init__(self):
        self.logger = Logger().getLogger()

    def write_json(self, data="", file_name="data.json", output_path=""):
        try:

            output_path = Utils.remove_slash_in_end_of_string(output_path)
            full_output_path = file_name + '.json' if output_path == "" else '{}/{}.json'.format(output_path, file_name)

            if data is not None:
                self.logger.info("Writing {} in json format".format(file_name))

                with open(full_output_path, 'w') as f:
                    json.dump(data, f)
            else:
                raise ValueError('file data is none, cannot write in file system')

        except Exception as ex:
            self.logger.error("can't write json in file system")
            self.logger.error('Error: {}'.format(ex))
