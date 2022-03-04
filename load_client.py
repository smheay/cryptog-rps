import e3db
from os import environ as env
from dotenv import load_dotenv

load_dotenv()
'''

Loads client information from env

'''
def load_client_test():
    print("Test")

def load_client(name):
    name = name.upper()

    config = e3db.Config(
        env[f'{name}_CLIENT_ID'],
        env[f'{name}_API_KEY_ID'],
        env[f'{name}_API_SECRET'],
        env[f'{name}_PUBLIC_KEY'],
        env[f'{name}_PRIVATE_KEY']
    )

    client = e3db.Client(config())

    return client


def return_client_id(name):
    name = name.upper()
    return env[f'{name}_CLIENT_ID']