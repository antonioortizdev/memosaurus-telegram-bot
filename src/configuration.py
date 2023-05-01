from os import getenv
from dotenv import load_dotenv


def get(key: str) -> str:
    value = getenv(key)
    if (value == None or value == ''):
        raise Exception(f'Environment variable {key} is not set.')

    return value


load_dotenv()
