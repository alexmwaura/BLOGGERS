import os

class Config:

    '''

    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    RANDOM_BASE_URL = "http://quotes.stormconsultancy.co.uk/random.json"
    POPULAR_BASE_URL = "http://quotes.stormconsultancy.co.uk/popular.json"
    
    RANDOM_API_KEY = os.environ.get("RANDOM_API_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:32915974@localhost/blog'

class ProdConfig(Config):
    '''
    Production configuration child class
    '''

    pass

class DevConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''

    Development configuration child class

    Args:

        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production':ProdConfig
}    