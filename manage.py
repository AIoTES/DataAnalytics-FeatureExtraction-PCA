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

from flask_script import Manager
from app import blueprint
from app.main import create_app

app = create_app(os.getenv('WORKING_ENV','dev'))
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run(host=os.getenv('API_HOST','0.0.0.0'), port=os.getenv('API_PORT',5000))

@manager.command
def test():
    """Runs the unit tests."""
    logging.info("launching tests")
    prev_working_env=os.getenv('WORKING_ENV','test')
    os.environ["WORKING_ENV"]='test'
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    os.environ["WORKING_ENV"]=prev_working_env
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
