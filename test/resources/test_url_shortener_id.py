# Import the resource/controllers we're testing
from resources.url_shortener_id import *

# client is a fixture, injected by the `pytest-flask` plugin
def test_get_url_shortener(client):
    # Hace una llamada test a /url_shortener/1
    response = client.get("/url_shortener/1")

    # Validate the response
    assert response.status_code == 200
    assert response.json == {
        "id": 1, 
        "url_corta": "http://gali.st/A81MDs1",
        "url_original": "https://github.com/goblinbr/python-flask-rest-api-example/tree/master/app"
    }