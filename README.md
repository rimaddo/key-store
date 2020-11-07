# Key Store

Helper library for filtering and getting object matched to one or more search
attribute. Includes a cache so that on repeat calls of the same search criteria
the objects do not need re-filtering.

## Install

Install with pip via `pip install key-store`.

### Create a new KeyStore

To create a new key-store from a list of object (or dictionaries) and keys

```python
from dataclasses import dataclass

from key_store import KeyStore


@dataclass
class ExampleClass:
    name: str
    value: int
    group: str


# With objects
store = KeyStore(
    keys=["name", "value", "group"],
    objects=[
        ExampleClass(name="Example 1", value=1, group="A"),
        ExampleClass(name="Example 2", value=2, group="B"),
        ExampleClass(name="Example 3", value=3, group="A"),
        ExampleClass(name="Example 4", value=4, group="B"),
    ],
)


# With dictionaries
dict_store = KeyStore(
    keys=["name", "value", "group"],
    objects=[
        {"name": "Example 1", "value": 1, "group": "A"},
        {"name": "Example 2", "value": 2, "group": "B"},
        {"name": "Example 3", "value": 3, "group": "A"},
        {"name": "Example 4", "value": 4, "group": "B"},
    ],
)
```

From this point onwards the examples will use objects, however all of the same
actions can be performed with dictionaries.

If you are using a data class or dictionary then you can use the
`get_keys` function to automatically create you keys input like;

```python
from key_store import get_keys

# Instead of writing out the keys manually you can use
get_keys(ExampleClass) 
# returns: ["name", "value", "group"]
```

### Get One
If you want to search for a single item in your store and get that item the you
should use the get one method. For example; 

```python
store.get_one(name="Example 1")
# returns: ExampleClass(name="Example 1", value=1, group="A")
```

Searches can be done using one search criteria as in the example above or multiple
like;

```python
store.get_one(group="A", value=3)
# returns: ExampleClass(name="Example 3", value=3, group="A")
```

If an object matching the search criteria doesn't exist in the store then the
`get_one` function will raise an error;

```python
store.get_one(name="Example 1", group="C")
# returns: a raised error
```


### Get One Or None

If you're not sure if an object matching the search criteria exists in the store
and you don't want to raise an error then you can use the `get_one_or_none`
method. For example;

```python
store.get_one_or_none(name="Example 1", group="C")
# returns: None
```

### Get

The get function returns a list of objects that match with the search criteria,
or an empty list if none match.

Multiple matches exist;
```python
obj_store.get(group="A")
# returns: [
#    ExampleClass(name="Example 1", value=1, group="A"),
#    ExampleClass(name="Example 3", value=3, group="A"),
#]
```

A single match exits;
```python
obj_store.get(group="A", value=3)
# returns: [
#    ExampleClass(name="Example 3", value=3, group="A"),
#]
```

No matches exist;
```python
obj_store.get(name="Not in store")
# returns: []
```

