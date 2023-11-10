# test_prod.py

import pytest
from dev.app.prod import prod

def test_prod():
    print("testing prod")
    res = prod(3, 4)
    assert res == 12


@pytest.mark.parametrize(
    "args, expected_result",
    [
        ((0, 0), 0),
        ((3, 0), 0),
        ((-11, -12), 132),
    ])
def test_basic_param_prod(args, expected_result):
    res = prod(*args)
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
    res = prod(*args)
    assert res == expected_result


def test_arguments():
    try:
        # 1. Use invalid argument on purpose and see that exception is triggered
        # "" is a string and should not be accepted
        # use some invalid value e.g. res = prod("x", 2) to trigger exception
        res = prod(3, "test")

        # 2. Try also valid value e.g. res = prod(5, 7) to see that test fails
        # res = prod(5, 7)
    except TypeError as err:
        # if TypeError is caught
        pass
    else:
        print("test_prod.py: Invalid argument is not caught")
        pytest.fail()
        # assert False
