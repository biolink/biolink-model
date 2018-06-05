from typing import Set

from dataclasses import dataclass

from metamodel.utils.metamodelcore import empty_set


@dataclass(repr=False, frozen=True)
class RefType:
    name: str

    def __repr__(self):
        return self.name


ClassType = RefType('Class')
TypeType = RefType('Type')
SlotType = RefType('Slot')


@dataclass
class References:
    """
    Summary of references to a given class. The reference class is the key to the dictionary carrying classrefs
    """
    classrefs: Set[str] = empty_set()     # Class-class references (e.g. is_a)
    slotrefs: Set[str] = empty_set()      # Slot-class references (e.g. domain, range, contains)
    typerefs: Set[str] = empty_set()      # Type-class references (Is this possible?)

    def addref(self, fromtype: RefType, fromname: str) -> None:
        if fromtype is ClassType:
            self.classrefs.add(fromname)
        elif fromtype is TypeType:
            self.typerefs.add(fromname)
        elif fromtype is SlotType:
            self.slotrefs.add(fromname)
        else:
            raise TypeError(f"Unknown typ: {fromtype}")

    def update(self, other: "References") -> None:
        self.classrefs.update(other.classrefs)
        self.slotrefs.update(other.slotrefs)
        self.typerefs.update(other.typerefs)
