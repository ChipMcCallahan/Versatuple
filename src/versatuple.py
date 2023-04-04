"""Versatuple class"""

from collections import namedtuple
from typing import Iterable

def versatuple(class_name: str, field_names: Iterable[str]):
    nt = namedtuple(class_name, field_names)
    return nt