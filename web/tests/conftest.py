'''Configure testing environment
'''

import pytest

from app import create_app

@pytest.fixture(name = 'app_test')
def fixture_app_test():
    '''Create and configure an app_test instance
    '''
    app_test = create_app()

    app_test.config.update({
        'TESTING' : True,
    })

    yield app_test

@pytest.fixture
def client(app_test):
    '''Client fixture for testing app_testlication
    '''
    return app_test.test_client()

@pytest.fixture
def runner(app_test):
    '''Runner fixture for testing app_testlication
    '''
    return app_test.test_cli_runner()
