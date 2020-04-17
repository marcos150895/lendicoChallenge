import requests


class MasterLeaguesExtractor():
    def __init__(self):
        pass

    def getData(self, endpoint, data, headers):
        url = "https://br1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5"

        headers = {
            'X-Riot-Token': 'RGAPI-72f8e007-17e0-4006-8f21-87ab0b28bf5d'
        }

        response = requests.request("GET", url, headers=headers, data = {})

        print(response.text.encode('utf8'))
