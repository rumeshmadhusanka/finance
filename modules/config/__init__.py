import os
from os import environ

from dotenv import load_dotenv

try:
    dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
    load_dotenv(dotenv_path)
except Exception as e:
    print("Could not load .env file ", e)


class Config(object):

    PORT = environ.get("PORT")
    DATABASE_URL = environ.get("DATABASE_URL")
    COMPANIES = environ.get("COMPANIES").split(",")


if __name__ == "__main__":
    p = Config()
    print(p.PORT)
    print(p.COMPANIES)
