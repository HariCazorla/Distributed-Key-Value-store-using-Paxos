import requests


def setValue(body):
    url = "http://localhost:8081/"
    resp = requests.post(url, verify=False, data=body)
    return resp.content.decode("utf-8")


def getValue(key):
    url = "http://localhost:8081/key=" + key
    resp = requests.get(url, verify=False)
    return resp.content.decode("utf-8")


def test_setValue():
    body = "{\"fruit\":\"apple\"}"
    assert setValue(body) == "Successful!"


def test_getValue_instore():
    assert getValue("fruit") == "apple"


def test_getValue_notinstore():
    assert getValue("xyz") == "-"
