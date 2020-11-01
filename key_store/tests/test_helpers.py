from collections import namedtuple
from typing import List, Type

import pytest

from key_store.helpers import T, get_keys
from key_store.tests.conftest import EXAMPLE_DICT_1, EXAMPLE_OBJ_1, ExampleObj


class ClassicClass(object):

    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value


NamedTuple = namedtuple('NamedTuple', 'name, value')


@pytest.mark.parametrize(
    "obj, expected_output",
    [
        (EXAMPLE_OBJ_1, ("name", "date", "value", "repeat_value", "missing_key_value")),
        (EXAMPLE_DICT_1, ("name", "date", "value", "repeat_value")),
        (ExampleObj, ("name", "date", "value", "repeat_value", "missing_key_value")),
    ]
)
def test_get_keys__success(obj: Type[T], expected_output: List[str]) -> None:
    output = get_keys(obj=obj)
    assert output == expected_output


@pytest.mark.parametrize(
    "obj",
    [
        ClassicClass(name="name", value=1),
        NamedTuple(name="name", value=1),
    ]
)
def test_get_keys__failure(obj: Type[T]) -> None:
    with pytest.raises(AttributeError):
        get_keys(obj=obj)
