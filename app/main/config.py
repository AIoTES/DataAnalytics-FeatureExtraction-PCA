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

