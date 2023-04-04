"""Versatuple class"""
# pylint: disable=invalid-name,too-many-locals

from collections import namedtuple
from typing import Iterable


def versatuple(class_name: str, field_names: Iterable[str],
               field_validators_dict=None, field_shortcuts=None, defaults=None):
    """Create a versatuple class (extension of collections.namedtuple).

       Every field name will also turn into something like a setter, except that
       since the resulting object is immutable, the setter will return a copy
       of the object with that field updated. For example, if a versatuple
       vt = (color: yellow, count: 10) was called with vt2 = vt.with_count(20), it would
       result in vt being unchanged and vt2 = (color: yellow, count: 20).
       
       Field validator dict is an optional dict mapping field names to validators.
       For example for a dict entry like {"count": lambda c: 0 <= c < 100}, when
       vt.is_valid() is called it would return True if vt.count was in that range and
       False otherwise.
       
       Field shortcuts is an optional sequence of triples in the
       format (field f, method m, value v). The 'method m' is assigned to the tuple. When 
       called it will assign the value v to the field f and return an updated tuple. For
       example, suppose the tuple has a field "color", and there exists a Color enum. 
       The triple ("color", "yellow", Color.YELLOW) would assign a .yellow() method to
       the resulting tuples, which would return a new versatuple with Color.YELLOW assigned
       to the "color" field.
       """
    RESERVED_NAMES = {"field_validators", "is_valid", "new"}
    if len(RESERVED_NAMES.intersection(field_names)) > 0:
        raise ValueError(f"Field names {RESERVED_NAMES.intersection(field_names)} are reserved.")
    nt_class = namedtuple(class_name, field_names)

    def safe_setattr(cls, attr, val):
        if attr in cls.__dict__:
            raise ValueError(f"Cannot set attr {attr} because it already exists.")
        setattr(cls, attr, val)

    # Factory method to create new instance.
    defaults = defaults or [None] * len(field_names)
    if len(defaults) != len(field_names):
        raise ValueError(f"Length of defaults ({len(defaults)} must match length of "
                         f"field names ({len(field_names)}).")
    @classmethod
    def new_factory(cls):
        return cls(*defaults)
    safe_setattr(nt_class, "new", new_factory)

    # Immutable Setters
    def immutable_setter(field_name):
        def setter(self, value):
            self_dict = self._asdict()
            self_dict[field_name] = value
            return nt_class(**self_dict)
        return setter
    for field_name in field_names:
        safe_setattr(nt_class, f"with_{field_name}", immutable_setter(field_name))

    # Field Validators
    safe_setattr(nt_class, "field_validators", field_validators_dict or {})
    def is_valid(self):
        for field_name in set(self._fields).intersection(set(self.field_validators.keys())):
            validator = self.field_validators[field_name]
            value = getattr(self, field_name)
            if not validator(value):
                return False
        return True
    safe_setattr(nt_class, "is_valid", is_valid)

    # Field Shortcuts
    def build_shortcut(field_name, value):
        def shortcut(self):
            self_dict = self._asdict()
            self_dict[field_name] = value
            return nt_class(**self_dict)
        return shortcut
    for shortcut in field_shortcuts or ():
        field_name, shortcut_name, value = shortcut
        safe_setattr(nt_class, shortcut_name, build_shortcut(field_name, value))

    return nt_class
