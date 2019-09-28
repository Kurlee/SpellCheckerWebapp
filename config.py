import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'averysecretkey'
    APP_DIR=os.path.abspath(os.path.realpath(__file__))
    TEMPLATES_DIR=os.path.join(APP_DIR, 'templates')
    STATIC_DIR=os.path.join(APP_DIR, 'static')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
      'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
      'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
      'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    DEBUG = False



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
