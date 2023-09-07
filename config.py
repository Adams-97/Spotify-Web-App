from os import environ, path
from dotenv import load_dotenv

# Loading in from secret and shared env files
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env.shared'))
load_dotenv(path.join(basedir, '.env.secret'))


class Config:
    """Basic dev config that gets overwritten by the subclasses below."""
    APP_MODE = environ.get('APP_MODE', 'DEV')
    HOST = environ.get('HOST', '127.0.0.1')
    PORT = environ.get('PORT', 5000)
    CLIENT_ID = environ.get('CLIENT_ID')
    REDIRECT_URI = environ.get('REDIRECT_URI')
    DB_DIALECT = environ.get('DIALECT', 'sqlite')  # Default to db in local area
    DB_USER = environ.get('DB_USER')
    DB_PASS = environ.get('DB_PASS')
    DB_HOST = environ.get('DB_HOST')
    DB_PORT = environ.get('DB_PORT')
    DATABASE = environ.get('DATABASE', 'dev_db.db')  # Default to db in local area
    DB_QUERY = environ.get('DB_QUERY')


class ProdConfig(Config):
    DEBUG = False


class TestConfig(Config):
    DIALECT = environ.get('DB_DIALECT')
    TESTING = True


# APP_MODE env var can then be used to decide flask configuration
config_dic = {
    'DEV': Config,
    'TEST': TestConfig,
    'PROD': ProdConfig
}

try:
    app_config = config_dic[environ['APP_MODE']]
except KeyError:
    print('APP_MODE environment variable needs to be set to any of:\n DEV, PROD, TEST')