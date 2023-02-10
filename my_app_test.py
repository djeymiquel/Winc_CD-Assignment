import pytest 
from my_app import app
# from my  # Flask instance of the API

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    # assert response.data.decode('utf-8') == 'Hello, world!'
    
def test_assignment_route():
    response = app.test_client().get('/assignment')
    assert response.status_code == 200
    # assert response.data.decode('utf-8') == 'This is my final assignment!'
    