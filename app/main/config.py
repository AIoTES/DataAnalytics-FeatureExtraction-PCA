import os
import logging
#basedir = os.path.abspath(os.path.dirname(__file__))
log_level={'debug':10,'info':20,'warning':30,'error':40,'critical':50}
class Config:
    #return the value of the environment variable key if it exists, or default if it doesn't.
    DEBUG=False
    
class DevelopmentConfig(Config):
    DEBUG=True
    LOG_LEVEL=log_level[os.getenv('LOG_LEVEL','debug').lower()]

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    LOG_LEVEL=log_level[os.getenv('LOG_LEVEL','debug').lower()]

class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL=log_level[os.getenv('LOG_LEVEL','warning').lower()]

config_by_name = {'dev':DevelopmentConfig,'test':TestingConfig,'prod':ProductionConfig}

