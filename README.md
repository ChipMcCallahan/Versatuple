# Versatuple
```
pip install git+https://github.com/ChipMcCallahan/Versatuple.git
```
Versatuple ("versatile tuple") is a extension of namedtuple with default values, field updaters, field shortcuts, factories and validators.

- Import example
```python
from versatuple import versatuple
```

- Base case: `versatuple` can always be used like `collections.namedtuple`. Example:
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
