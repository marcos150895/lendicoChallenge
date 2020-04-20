import json

from helpers.logger import Logger


class Writer:

    def __init__(self):
        self.logger = Logger().getLogger()

    def write_json(self, data="", file_name="data.json", output_path="/"):
        try:

            if data is not None:
                self.logger.info("Writing {} in json format".format(file_name))

                with open('{}/{}.json'.format(output_path, file_name), 'w') as f:
                    json.dump(data, f)
            else:
                raise ValueError('file data is none, cannot write in file system')

        except Exception as ex:
            self.logger.error("can't write json in file system")
            self.logger.error('Error: {}'.format(ex))
