from shopsconnector.connector import utils
import pytest
from json import dumps


@utils.deserilize_json
def _test_deserilize(message):
    return message


@utils.serilize_json
def _test_serilize(message):
    return message


@pytest.mark.parametrize("data", [{'hi' : 'by'}])
def test_decorators_v1(data):
    assert _test_deserilize(dumps(data)) == data
    assert _test_serilize(data) == dumps(data)


@pytest.mark.parametrize("data", [1,2])
def test_decorators_v2(data):
    with pytest.raises(TypeError):
        _test_deserilize(data)
    assert _test_serilize(data) == dumps(data)
