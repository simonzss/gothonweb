from nose.tools import *
from bin.app_engine import *
from tests.tools import assert_response

def test_index():
    resp=app.request("/")
    assert_response(resp,status="303 See Other")

    resp=app.request("/game",method='POST')
    assert_response(resp,status="303")

    resp=app.request("/game",method='GET')
    assert_response(resp,status="200")

    # data=map.START
    # resp=app.request("/game",method="GET",data=data)
    # assert_response(resp,contains=data.name,status="200")
