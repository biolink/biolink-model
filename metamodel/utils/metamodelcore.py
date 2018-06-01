from typing import NewType

from dataclasses import field


def empty_list():
    return field(default_factory=list)


def empty_dict():
    return field(default_factory=dict)


def empty_set():
    return field(default_factory=set)


URI = NewType('URI', str)


