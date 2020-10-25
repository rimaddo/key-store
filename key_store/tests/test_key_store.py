from datetime import date
from typing import Any, Dict, List, Optional, Tuple

import pytest

from key_store.key_store import KeyStore
from key_store.tests.conftest import (
    EXAMPLE_DICT_1,
    EXAMPLE_DICT_2,
    EXAMPLE_DICT_3,
    EXAMPLE_OBJ_1,
    EXAMPLE_OBJ_2,
    EXAMPLE_OBJ_3,
    ExampleObj,
)


@pytest.mark.parametrize(
    "kwargs, expected_output, expected_cache",
    [
        # Expected output is None
        ({"name": "Other"}, None, {}),
        # Expected output is not None - search for string
        ({"name": "One"}, EXAMPLE_OBJ_1, {("One", None, None, None,): [EXAMPLE_OBJ_1]}),
        # Expected output is not None - search for value
        ({"value": 1}, EXAMPLE_OBJ_1, {(None, 1, None, None,): [EXAMPLE_OBJ_1]}),
        # Expected output is not None - search for date
        (
                {"date": date(2000, 1, 1)},
                EXAMPLE_OBJ_1,
                {(None, None, None, date(2000, 1, 1),): [EXAMPLE_OBJ_1]},
        ),
        # Expected output is not None - search for mix of params
        (
                {"name": "One", "value": 1, "date": date(2000, 1, 1)},
                EXAMPLE_OBJ_1,
                {("One", 1, None, date(2000, 1, 1),): [EXAMPLE_OBJ_1]},
        ),
    ]
)
def test_key_store__get_one_or_none__success__with_objs(
        kwargs: Dict[str, Any],
        expected_output: Optional[ExampleObj],
        expected_cache: Dict[Tuple, List],
        obj_key_store: KeyStore,
) -> None:
    output = obj_key_store.get_one_or_none(**kwargs)
    assert output == expected_output
    assert obj_key_store._cache == expected_cache


@pytest.mark.parametrize(
    "kwargs, expected_output, expected_cache",
    [
        # Expected output is None
        ({"name": "Other"}, None, {}),
        # Expected output is not None - search for string
        ({"name": "One"}, EXAMPLE_DICT_1, {("One", None, None, None,): [EXAMPLE_DICT_1]}),
        # Expected output is not None - search for value
        ({"value": 1}, EXAMPLE_DICT_1, {(None, 1, None, None,): [EXAMPLE_DICT_1]}),
        # Expected output is not None - search for date
        (
                {"date": date(2000, 1, 1)},
                EXAMPLE_DICT_1,
                {(None, None, None, date(2000, 1, 1),): [EXAMPLE_DICT_1]},
        ),
        # Expected output is not None - search for mix of params
        (
                {"name": "One", "value": 1, "date": date(2000, 1, 1)},
                EXAMPLE_DICT_1,
                {("One", 1, None, date(2000, 1, 1),): [EXAMPLE_DICT_1]},
        ),
    ]
)
def test_key_store__get_one_or_none__success__with_dicts(
        kwargs: Dict[str, Any],
        expected_output: Optional[ExampleObj],
        expected_cache: Dict[Tuple, List],
        dict_key_store: KeyStore,
) -> None:
    output = dict_key_store.get_one_or_none(**kwargs)
    assert output == expected_output
    assert dict_key_store._cache == expected_cache


@pytest.mark.parametrize(
    "kwargs, expected_output, expected_cache",
    [
        # Expected output is multiple -> goes to none
        ({"repeat_value": 100}, None, {}),
        # Search for missing key
        ({"missing_key_value": 10}, None, {}),
    ]
)
def test_key_store__get_one_or_none__failure__with_objs(
        kwargs: Dict[str, Any],
        expected_output: Optional[ExampleObj],
        expected_cache: Dict[Tuple, List],
        obj_key_store: KeyStore,
) -> None:
    with pytest.raises(Exception):
        output = obj_key_store.get_one_or_none(**kwargs)
        assert output == expected_output
        assert obj_key_store._cache == expected_cache


@pytest.mark.parametrize(
    "kwargs, expected_output, expected_cache",
    [
        # Expected output is multiple -> goes to none
        ({"repeat_value": 100}, None, {}),
        # Search for missing key
        ({"missing_key_value": 10}, None, {}),
    ]
)
def test_key_store__get_one_or_none__failure__with_dicts(
        kwargs: Dict[str, Any],
        expected_output: Optional[ExampleObj],
        expected_cache: Dict[Tuple, List],
        dict_key_store: KeyStore,
) -> None:
    with pytest.raises(Exception):
        output = dict_key_store.get_one_or_none(**kwargs)
        assert output == expected_output
        assert dict_key_store._cache == expected_cache


@pytest.mark.parametrize(
    "kwargs, expected_output, expected_cache",
    [
        # Get no matches
        ({"name": "No Match"}, [], {}),
        # Get one item from one key
        ({"name": "One"}, [EXAMPLE_OBJ_1], {("One", None, None, None,): [EXAMPLE_OBJ_1]}),
        # Get multiple items from one key
        (
                {"repeat_value": 100},
                [EXAMPLE_OBJ_1, EXAMPLE_OBJ_2, EXAMPLE_OBJ_3],
                {(None, None, 100, None,): [EXAMPLE_OBJ_1, EXAMPLE_OBJ_2, EXAMPLE_OBJ_3]},
        ),
        # Get one item from multiple keys
        ({"name": "One", "repeat_value": 100}, [EXAMPLE_OBJ_1], {("One", None, 100, None,): [EXAMPLE_OBJ_1]}),
    ]
)
def test_key_store__get__success__with_objs(
        kwargs: Dict[str, Any],
        expected_output: Optional[ExampleObj],
        expected_cache: Dict[Tuple, List],
        obj_key_store: KeyStore,
) -> None:
    output = obj_key_store.get(**kwargs)
    assert output == expected_output
    assert obj_key_store._cache == expected_cache


@pytest.mark.parametrize(
    "kwargs, expected_output, expected_cache",
    [
        # Get no matches
        ({"name": "No Match"}, [], {}),
        # Get one item from one key
        ({"name": "One"}, [EXAMPLE_DICT_1], {("One", None, None, None,): [EXAMPLE_DICT_1]}),
        # Get multiple items from one key
        (
                {"repeat_value": 100},
                [EXAMPLE_DICT_1, EXAMPLE_DICT_2, EXAMPLE_DICT_3],
                {(None, None, 100, None,): [EXAMPLE_DICT_1, EXAMPLE_DICT_2, EXAMPLE_DICT_3]},
        ),
        # Get one item from multiple keys
        ({"name": "One", "repeat_value": 100}, [EXAMPLE_DICT_1], {("One", None, 100, None,): [EXAMPLE_DICT_1]}),
    ]
)
def test_key_store__get__success__with_dicts(
        kwargs: Dict[str, Any],
        expected_output: Optional[ExampleObj],
        expected_cache: Dict[Tuple, List],
        dict_key_store: KeyStore,
) -> None:
    output = dict_key_store.get(**kwargs)
    assert output == expected_output
    assert dict_key_store._cache == expected_cache


@pytest.mark.parametrize(
    "kwargs, expected_output, expected_cache",
    [
        # Get no matches
        ({"wrong_key": "No Match"}, [], {}),
    ]
)
def test_key_store__get__failure__with_objs(
        kwargs: Dict[str, Any],
        expected_output: Optional[ExampleObj],
        expected_cache: Dict[Tuple, List],
        obj_key_store: KeyStore,
) -> None:
    with pytest.raises(Exception):
        output = obj_key_store.get_one_or_none(**kwargs)
        assert output == expected_output
        assert obj_key_store._cache == expected_cache


@pytest.mark.parametrize(
    "kwargs, expected_output, expected_cache",
    [
        # Get no matches
        ({"wrong_key": "No Match"}, [], {}),
    ]
)
def test_key_store__get__failure__with_dicts(
        kwargs: Dict[str, Any],
        expected_output: Optional[ExampleObj],
        expected_cache: Dict[Tuple, List],
        dict_key_store: KeyStore,
) -> None:
    with pytest.raises(Exception):
        output = dict_key_store.get_one_or_none(**kwargs)
        assert output == expected_output
        assert dict_key_store._cache == expected_cache


def test_key_store_can_be_iterated_over(obj_key_store: KeyStore, dict_key_store: KeyStore) -> None:
    obj_values = [EXAMPLE_OBJ_1, EXAMPLE_OBJ_2, EXAMPLE_OBJ_3]
    for n, item in enumerate(obj_key_store):
        assert item == obj_values[n]

    dict_values = [EXAMPLE_DICT_1, EXAMPLE_DICT_2, EXAMPLE_DICT_3]
    for n, item in enumerate(dict_key_store):
        assert item == dict_values[n]
