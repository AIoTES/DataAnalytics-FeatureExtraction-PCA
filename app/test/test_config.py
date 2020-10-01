#
# Copyright (c) 2019 Universidad Politecnica de Madrid.
#
# This file is part of ACTIVAGE.
# See http://www.activageproject.eu/ for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
