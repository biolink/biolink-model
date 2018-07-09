from enum import Enum
from typing import Dict, Optional

from rdflib import XSD, URIRef

from metamodel.utils.namespaces import BIOENTITY

""" Built in types """


class Builtin(Enum):
    string = 0
    integer = 1
    float = 2
    double = 3
    boolean = 4
    time = 5
    date = 6
    uri = 7
    anytype = 8


builtin_names: Dict[str, Builtin] = {
    'string': Builtin.string,
    'integer': Builtin.integer,
    'float': Builtin.float,
    'double': Builtin.double,
    'boolean': Builtin.boolean,
    'time': Builtin.time,
    'date': Builtin.date,
    'uri': Builtin.uri,
    'anytype': Builtin.anytype
}


def builtin_uri(name: Optional[str], expand: bool = False) -> Optional[str]:
    if name is None:
        name = DEFAULT_BUILTIN_TYPE_NAME
    elif name not in builtin_names:
        return None
    elif builtin_names[name] is Builtin.uri:
        name = 'anyURI'
    elif builtin_names[name] is Builtin.anytype:
        name = 'anyType'
    return XSD[name] if expand else f'xsd:{name}'


DEFAULT_BUILTIN_TYPE_NAME = "string"

python_builtins: Dict[Builtin, str] = {
    Builtin.string: 'str',
    Builtin.integer: 'int',
    Builtin.float: 'float',
    Builtin.double: 'float',
    Builtin.boolean: 'bool',
    Builtin.time: 'datetime.time',
    Builtin.date: 'datetime.date',
    Builtin.uri: 'str',
    Builtin.anytype: 'Any'
}
