from http import HTTPStatus

import pytest

from app.main import app

@pytest.mark.talk_run
def test_end_to_end():
    #'Arange'
    client = app.test_client()


    #Act
    body = {"url":"https:meetup.com/indypy"}
    response = client.post("/top-word", json=body)

    #assert 
    assert response.status_code == HTTPStatus.OK