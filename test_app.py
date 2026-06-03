import pytest
from app import app
def test_web_ok():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
