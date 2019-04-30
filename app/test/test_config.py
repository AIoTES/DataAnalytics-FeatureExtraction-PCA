import os
import unittest
import logging

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import config_by_name
#from app.main.config import basedir

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        logging.basicConfig(level=config_by_name['dev'].LOG_LEVEL)
        return app

    def test_app_is_development(self):
        logging.info("...running in development mode...")
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(current_app is None)

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        logging.basicConfig(level=config_by_name['test'].LOG_LEVEL)
        return app

    def test_app_is_testing(self):
        logging.debug("...running in testing mode...")
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'])


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        logging.basicConfig(level=config_by_name['prod'].LOG_LEVEL)
        return app

    def test_app_is_production(self):
        logging.info("this message should not be displayed")
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'] is False)

if __name__ == '__main__':
    unittest.main()
