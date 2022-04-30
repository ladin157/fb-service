import os


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('FLASK_SECRET', 'f495b66803a6512d')
    SECURITY_SALT = os.environ.get('FLASK_SALT', '14be1971fc014f1b84')

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    LOG_PATH = '/var/log/fb-service/fb-service.log'
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'static')
    IMAGE_FOLDER = os.path.join(STATIC_FOLDER, 'images')
    AVATAR_FOLDER = os.path.join(IMAGE_FOLDER, 'avatars')

    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    AUTH_TOKEN = '0001f9f05a59574bbf602d6117ad6d2d'
    GOOGLE_API_KEY = 'AIzaSyCDcUmm1LO0yeRVqdPsxo2ku6-weisiWHk'


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TB_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ben:Ben0102%40@159.65.13.232:3306/fb'
    # SQLALCHEMY_DATABASE_URI = 'mysql://ben:Ben0102%40@159.65.13.232:3306/fb'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ben:Ben0102%40@159.65.13.232:3306/fb'
    # SQLALCHEMY_DATABASE_URI = 'mysql://ben:Ben0102%40@159.65.13.232:3306/fb'


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
