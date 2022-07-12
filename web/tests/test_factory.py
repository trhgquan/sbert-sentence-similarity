'''Testing factory file (aka __init__.py)
'''

from app import create_app

def test_config():
    '''Test if configuration is working or not
    '''
    assert not create_app().testing
    assert create_app({
        'TESTING' : True,
    }).testing

def test_hello(client):
    '''Test if server is alive
    '''
    response = client.get('/')
    assert response.status_code == 200
