import pytest
import requests
import json

target_ip = "10.5.0.3"


def test_get_prod_id():
    res = requests.get(f"http://{target_ip}:5000/product/1")
    res = res.json()["id"]
    expected_result = 1
    assert res == expected_result


def test_get_mult_info():
    res = requests.get(f"http://{target_ip}:5000/mult")
    res = res.text
    expected_result = '''This endpoint allows to multiply numbers.\n
                    Use POST method to send two numbers   \n 
                    factor_1 and factor_2  \n
                    of type int or float.  \n
                    format request body as JSON. \n
                    Response will include info about  \n
                    their product.  \n
        '''
    assert res == expected_result
@pytest.mark.parametrize(
    "args, expected_result",
    [
        pytest.param((0, 0), 0, id="zero - zero"),
        pytest.param((0, 1), 0, id="zero - positive"),
        pytest.param((0, -2), 0, id="zero - negative"),
        pytest.param((3, 0), 0, id="positive - zero"),
        pytest.param((-4, 0), 0, id="negative - zero"),
        pytest.param((0.0, 0), 0, id="float zero - zero"),
        pytest.param((0, 0.0), 0, id="zero - float zero"),
        pytest.param((0.0, 0.0), 0, id="float zero - float zero"),
        pytest.param((5, 6), 30, id="positive - positive"),
        pytest.param((7, -8), -56, id="positive - negative"),
        pytest.param((-9, 10), -90, id="negative - positive"),
        pytest.param((-11, -12), 132, id="negative - negative"),
        pytest.param((13.0, 14), 182, id="float positive - positive"),
    ])
def test_param_prod(args, expected_result):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "factor_1": args[0],
        "factor_2": args[1]
    }
    payload = json.dumps(payload)
    url = f"http://{target_ip}:5000/mult"
    res = requests.post(url, headers=headers, data=payload)
    res = res.json()["Success"]

    assert res == expected_result
