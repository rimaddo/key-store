from dataclasses import dataclass
from datetime import date

import pytest

from key_store.key_store import KeyStore


# --------------------------- TEST CLASSES ----------------------------------- #

@dataclass(frozen=True)
class ExampleObj:
    name: str
    date: date
    value: int
    repeat_value: int
    missing_key_value: int


# --------------------------- TEST CONSTANTS ---------------------------------- #


EXAMPLE_OBJ_1 = ExampleObj(
    name="One",
    value=1,
    repeat_value=100,
    missing_key_value=10,
    date=date(2000, 1, 1),
)
EXAMPLE_OBJ_2 = ExampleObj(
    name="Two",
    value=2,
    repeat_value=100,
    missing_key_value=20,
    date=date(2000, 1, 2),
)
EXAMPLE_OBJ_3 = ExampleObj(
    name="Three",
    value=3,
    repeat_value=100,
    missing_key_value=30,
    date=date(2000, 1, 3),
)

EXAMPLE_DICT_1 = {
    "name": "One",
    "date": date(2000, 1, 1),
    "value": 1,
    "repeat_value": 100,

}
EXAMPLE_DICT_2 = {
    "name": "Two",
    "date": date(2000, 1, 2),
    "value": 2,
    "repeat_value": 100,
}
EXAMPLE_DICT_3 = {
    "name": "Three",
    "date": date(2000, 1, 3),
    "value": 3,
    "repeat_value": 100,
}


# --------------------------- TEST FIXTURES ---------------------------------- #


@pytest.fixture
def obj_key_store() -> KeyStore:
    return KeyStore(
        keys=["name", "value", "repeat_value", "date"],
        objects=[
            EXAMPLE_OBJ_1,
            EXAMPLE_OBJ_2,
            EXAMPLE_OBJ_3,
        ]
    )


@pytest.fixture
def dict_key_store() -> KeyStore:
    return KeyStore(
        keys=["name", "value", "repeat_value", "date"],
        objects=[
            EXAMPLE_DICT_1,
            EXAMPLE_DICT_2,
            EXAMPLE_DICT_3,
        ]
    )