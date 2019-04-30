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
