import unittest

from helpers.utils import Utils


class UtilsTest(unittest.TestCase):
    def setup_method(self, method):
        self.utils = Utils()
        self.header = self.utils.format_header("TOKEN-XXXXXX1")

    def test_contract_format_header(self):
        keys = self.header.keys()

        # validate number of keys in dict
        self.assertEqual(len(keys), 1, 'Testing Length of keys')

        # validate the content of key

        fake_keys = {'X-Riot-Token':'TOKEN-XXXXXX1'}.keys()
        self.assertEqual(keys, fake_keys, 'Testing contract validation')

    def test_remove_slash_in_end_of_string(self):
        slash_in_the_end = self.utils.remove_slash_in_end_of_string('https://lendico.com.br/')
        without_slash_in_the_end = self.utils.remove_slash_in_end_of_string('https://lendico.com.br/')

        # validate if method remove slash in the end of string
        self.assertEqual(slash_in_the_end, 'https://lendico.com.br', 'Testing removing slash in the end of string')

        # validate if method dont remove the last char
        self.assertEqual(without_slash_in_the_end,
                         'https://lendico.com.br',
                         'Testing dont remove last char when string dont have slash in the end of string')


# if __name__ == '__main__':
#     unittest.main()
