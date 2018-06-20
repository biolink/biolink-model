from typing import NewType, Any

from dataclasses import field


def empty_list():
    return field(default_factory=list)


def empty_dict():
    return field(default_factory=dict)


def empty_set():
    return field(default_factory=set)


URI = NewType('URI', str)


class Identifier:
    def __init__(self, v: str) -> None:
        self.v = v

    def __str__(self):
        return str(self.v)

    def __repr__(self):
        return repr(self.v)

    def __eq__(self, other: Any) -> bool:
        return str(self) == str(other)

    def __lt__(self, other: Any) -> bool:
        return str(self) < str(other)

    def __gt__(self, other: Any) -> bool:
        return str(self) < str(other)

    def urlform(self) -> str:
        return underline(str(self))

