# Versatuple
`Versatuple` ("versatile tuple") is a extension of [`collections.namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple) with default values, field updaters, field shortcuts, factories and validators.
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

### Basic Syntax
- `Versatuple` is based on [`collections.namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple) and can be used in generally the same way in the base case.
  - One important difference is that `Versatuple` requires field names to be lowercase.
  - There are also a few reserved keywords that can't be used as field names: `new`, `validators`, and `is_valid`.
```python
Person = versatuple("Person",("name", "age"))
p = Person("Chip", 33)
print(p)
```
```
Person(name='Chip', age=33)
```

### Default Values
- Supply a tuple of the same length as the field names with the keyword `defaults` to specify default values for fields.
- Use the `.new()` method to create with defaults.
- If `defaults` is not supplied, calling `.new()` will give `None` for each field.
```python
Person = versatuple("Person",
                    ("name", "age"),
                    defaults=("Anonymous", 0))
Dog = versatuple("Dog", ("name", "breed")) # no defaults specified
print(Person.new())
print(Dog.new())
```
```
Person(name='Anonymous', age=0)
Dog(name=None, breed=None)
```

### Immutable Field Setters
- Being immutable, a `Versatuple`'s fields cannot be updated. 
- However, it is very easy to create copies of the `Versatuple` with updated fields.
- Use the capitalized field name as a method, and pass the desired value.
  - This returns a new `Versatuple` with all the same fields except for the updated field.
  - This effect can be chained for easy tuple creation.
```python
Address = versatuple("Address",
                     ("recipient", "number", "street", "city", "state", "zip"))
address = Address.new() \
                 .Recipient("Chip McCallahan") \
                 .Number(1234) \
                 .Street("Blobby Ave") \
                 .City("Chip City") \
                 .State("Denial") \
                 .Zip(56789)
print(address)
```
```
Address(recipient='Chip McCallahan', number=1234, street='Blobby Ave', city='Chip City', state='Denial', zip=56789)
```
- NOTE: This code snippet creates 7 different tuple objects, one for each method call. **From a runtime perspective, this is not efficient**; however it makes for easy coding. In the future, this may be updated to include a Builder pattern for better performance.

### Field Validation
- Validate fields by supplying `validators` and then calling `.is_valid()` on a tuple instance.
```python
Person = versatuple("Person",
                    ("name", "age"),
                    validators = {
                        "name": lambda name: name == name.capitalize(),
                        "age": lambda age: 0 <= age
                    })
for p in (Person("Chip", 33), Person("melinda", 33), Person("Morton", -1)):
    print(f"{p} is_valid: {p.is_valid()}")
```
```
Person(name='Chip', age=33) is_valid: True
Person(name='melinda', age=33) is_valid: False
Person(name='Morton', age=-1) is_valid: False
```

### Field Shortcuts

### Factories
