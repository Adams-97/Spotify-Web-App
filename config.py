from os import environ, path
from dotenv import load_dotenv

# Loading in from secret and shared env files
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env.shared"))
load_dotenv(path.join(basedir, ".env.secret"))


class Config:
    """Basic config that gets overwritten by the subclasses below."""
    HOST = environ.get('HOST', '127.0.0.1')
    PORT = environ.get('PORT', 5000)
    CLIENT_ID = environ.get('CLIENT_ID')
    REDIRECT_URI = environ.get('REDIRECT_URI')


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass


# APP_MODE env var can then be used to decide flask configuration
config_dic = {
    'DEV': DevConfig,
    'TEST': TestConfig,
    'PROD': ProdConfig
}
app_config = config_dic[environ['APP_MODE']]