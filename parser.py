import urllib.request
import json

from model import User


class Parser:
    def __init__(self, user_name=None, url='https://www.codewars.com/api/v1/users/'):
        self.dictionary = None
        self.user_name = user_name
        self.url = url
        self.user = User()
        self.request_parser()
        self.deep_keys(self.get_dict())

    def get_user(self):
        return self.user

    def request_parser(self):
        try:
            with urllib.request.urlopen(f'{self.url}{self.user_name}') as response:
                json_dictionary = response.read()
            self.dictionary = json.loads(json_dictionary)
        except ValueError:
            raise ValueError('Ошибка при подключении к API')

    def deep_keys(self, obj):
        for key, val in obj.items():
            self.user.__dict__[key] = val
            if isinstance(val, dict):
                self.deep_keys(val)  # Передается на заполнение в дальнейшие вызовы...
        return

    def __str__(self):
        return str(self.dictionary)

    def get_dict(self):
        return self.dictionary


# def model_parser():
#     user = User()
#     user.__dict__ =
#     print(user.__dict__)


if __name__ == '__main__':
    test = Parser('Pogudo')
    print(test.get_dict())
    # print(test)
    # user = User()
    # for k, v in test.get_dict().items():
    #     user.__dict__[k] = v
    # print(f'{k} - {v}')
    # print(user.__dict__)
    # for k, v in user.__dict__.items():
    #     print(f'{k} - {v}')
    # user = User()
    # deep_keys(test.get_dict(), user)
    # print(user.honor)
