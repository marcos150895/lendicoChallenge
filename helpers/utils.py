from helpers.singleton import Singleton


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
