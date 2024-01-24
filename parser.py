import requests
import json


def parse_json(name):
    r = requests.get(f'https://www.codewars.com/api/v1/users/{name}')
    dict_j = r.json()
    return (dict_j['honor'],
            dict_j['leaderboardPosition'],
            dict_j['ranks']['overall']['name'],
            dict_j['codeChallenges']['totalCompleted'])


if __name__ == '__main__':
    print(parse_json('Pogudo'))
