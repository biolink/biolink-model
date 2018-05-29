from enum import Enum
from typing import Dict

""" Built in types """


class Builtin(Enum):
    string = 0
    integer = 1
    float = 2
    double = 3
    boolean = 4
    time = 5
    date = 6


builtin_names: Dict[str, Builtin] = {
    'string': Builtin.string,
    'integer': Builtin.integer,
    'float': Builtin.float,
    'double': Builtin.double,
    'boolean': Builtin.boolean,
    'time': Builtin.time,
    'date': Builtin.date
}