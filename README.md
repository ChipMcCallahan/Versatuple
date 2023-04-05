# Versatuple
Versatuple ("versatile tuple") is a extension of [`collections.namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple) with default values, field updaters, field shortcuts, factories and validators.
- Like `namedtuple`, its fields can be accessed by instance properties.
- Like all tuples, instances are immutable if their property values are immutable.

### Installation
```
pip install git+https://github.com/ChipMcCallahan/Versatuple.git
```

### Importing
```python
from versatuple import versatuple
```

### Basic syntax
- Versatuple is based on [`collections.namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple) and can be used the same way in the base case.
```python
Person = versatuple("Person",("name", "age"))
p = Person("Chip", 33)
print(p)
```
```
Person(name='Chip', age=33)
```

- Default values: supply a tuple of the same length as the field names to specify defaults.
  - Use the `.new()` method to create with defaults.
```python
Person = versatuple("Person",
                    ("name", "age"),
                    defaults=("Anonymous", 0))
p = Person.new()
print(p)
```
```
Person(name='Anonymous', age=0)
```
