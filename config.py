from pathlib import Path
import random, string
import os


class Config(object):
    CSRF_ENABLED = True
    SECRET = "6e00a96d47c817655b8fc37087a25cda16324ca44aca44e1e5928a97a76d9700c08093ab859d9fb68ea1003b34ac7e7629"
    TEMPLATE_FOLDER = Path(__file__).absolute() / "templates"
    ROOT_DIR = Path(__file__).parent.absolute()
    APP = None
    SQLACLCHEMY_DATABASE_URI = "mysql+mysqldb://user:passwd@host:port/database"


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = "localhost"
    PORT_HOST = 8000
    URL_MAIN = f"http://{IP_HOST}:{PORT_HOST}/"


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = "localhost"  # geralmente o ip de um servidor na nuvem
    PORT_HOST = 5000
    URL_MAIN = f"http://{IP_HOST}:{PORT_HOST}/"


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    IP_HOST = "localhost"  # geralmente é ip de um servidor na nuvem
    PORT_HOST = 8080
    URL_MAIN = f"http://{IP_HOST}:{PORT_HOST}/"


app_config = {
    "development": DevelopmentConfig(),
    "testing": TestingConfig(),
    "production": ProductionConfig(),
}

app_active = os.getenv("FLASK_ENV")
