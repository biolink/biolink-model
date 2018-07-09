from typing import Dict, Set, List, Iterable

from dataclasses import dataclass, field

from metamodel.utils.builtins import builtin_names
from metamodel.metamodel import SchemaDefinition, Element, Definition, ClassDefinition, SlotDefinitionName, \
    ClassDefinitionName, TypeDefinitionName, DefinitionName
from metamodel.utils.metamodelcore import empty_dict, empty_set
from metamodel.utils.typereferences import RefType, ClassType, TypeType, SlotType, References


def empty_references() -> field:
    return field(default_factory=References)


@dataclass
class SchemaSynopsis:
    schema: SchemaDefinition = field(repr=False, compare=False)

    classes: Set[ClassDefinitionName] = empty_set()    # List of classes defined in schema
    slots: Set[SlotDefinitionName] = empty_set()       # List of slots defined in schema
    types: Set[TypeDefinitionName] = empty_set()       # List of types defined in schema

    slotrefs: Dict[SlotDefinitionName, References] = empty_dict()     # Slot to referencing entity
    typerefs: Dict[TypeDefinitionName, References] = empty_dict()     # Type to referencing entity
    classrefs: Dict[ClassDefinitionName, References] = empty_dict()    # Class to referencing entity

    unions: Dict[DefinitionName, References] = empty_dict()        # Entity to union references
    isarefs: Dict[DefinitionName, References] = empty_dict()       # Entity to is_a references
    mixinrefs: Dict[DefinitionName, References] = empty_dict()     # Entity to mixins references

    roots: References = empty_references()            # Entities with no isa's
    mixins: References = empty_references()           # Entities declared as mixin
    abstracts: References = empty_references()        # Entities declared as abstract

    # Slots only
    domainrefs: Dict[str, Set[str]] = empty_dict()  # Entity to slots declaring it as domain
    rangerefs: Dict[str, Set[str]] = empty_dict()   # Entity to slots declaring it as range
    inverses: Dict[str, Set[str]] = empty_dict()    # Slots declared as inverses of other slots
    slotdomains: Dict[str, str] = empty_dict()      # Slot domains
    mtdomains: Set[str] = empty_set()               # Slots with no domains declared

    # Types only
    typeofs: Dict[str, Set[str]] = empty_dict()    # target to referencing Types

    # Classes only
    classslots: Dict[str, Set[str]] = empty_dict()     # Class to class slots
    slotclasses: Dict[str, Set[str]] = empty_dict()    # Slot to referencing classes
    definingslots: Dict[str, Set[str]] = empty_dict()  # Defining slot entries
    slotusages: Dict[str, Set[str]] = empty_dict()     # Slot usage entries
    applytos: Dict[str, References] = empty_dict()      # Entity to applyto references

    def __post_init__(self):
        # Domains and ranges
        for k, v in self.schema.slots.items():
            if k != v.name:
                raise ValueError("Slot name mismatch: {k} != {v.name}")
            self.slots.add(k)
            self.summarize_element(SlotType, k, v)
            self.summarize_definition(SlotType, k, v)
            if v.domain:
                self.domainrefs.setdefault(v.domain, set()).add(k)
                self.add_ref(SlotType, k, ClassType, v.domain)
                self.slotdomains[k] = v.domain
            else:
                self.mtdomains.add(k)
            self.rangerefs.setdefault(v.range, set()).add(k)
            self.add_ref(SlotType, k, ClassType if v.range in self.schema.classes else TypeType, v.range)
            if v.inverse:
                self.inverses.setdefault(v.inverse, set()).add(k)
                self.add_ref(SlotType, k, SlotType, v.inverse)

        for k, v in self.schema.types.items():
            if k != v.name:
                raise ValueError("Type name mismatch: {k} != {v.name}")
            self.types.add(k)
            self.summarize_element(TypeType, k, v)
            self.typeofs.setdefault(v.typeof if v.typeof else 'string', set()).add(k)

        for k, v in self.schema.classes.items():
            if k != v.name:
                raise ValueError("Class name mismatch: {k} != {v.name}")
            self.classes.add(k)
            self.summarize_element(ClassType, k, v)
            self.summarize_definition(ClassType, k, v)
            if v.apply_to:
                self.applytos.setdefault(v.apply_to, References()).addref(ClassType, k)
            self.classslots[k] = set(v.slots)
            self.add_inherited_classlots(k, v)
            for slotname in v.slots:
                self.slotclasses.setdefault(slotname, set()).add(k)
                self.slotrefs.setdefault(slotname, References()).addref(ClassType, k)
            for ds in v.defining_slots:
                self.slotrefs.setdefault(ds, References()).addref(ClassType, k)
                self.definingslots.setdefault(ds, set()).add(k)
            for slotname, usage in v.slot_usage.items():
                self.slotusages.setdefault(slotname, set()).add(k)
                self.slotrefs.setdefault(slotname, References()).addref(ClassType, k)

    def add_inherited_classlots(self, classname: str, cls: ClassDefinition) -> None:
        if cls.is_a and cls.is_a in self.schema.classes:
            parent_cls = self.schema.classes[cls.is_a]
            self.classslots[classname].update(parent_cls.slots)
            self.add_inherited_classlots(classname, parent_cls)
        for mixin in cls.mixins:
            if mixin in self.schema.classes:
                self.classslots[classname].update(self.schema.classes[mixin].slots)
        for slot in cls.slots:
            self.add_inherited_classslot_slots(classname, slot)

    def add_inherited_classslot_slots(self, classname: str, slotname: SlotDefinitionName) -> None:
        if slotname in self.isarefs:
            for child in self.isarefs[slotname].slotrefs:
                self.classslots[classname].add(child)
                self.add_inherited_classslot_slots(classname, child)

    def summarize_element(self, typ: RefType, k: str, v: Element) -> None:
        pass

    def summarize_definition(self, typ: RefType, k: str, v: Definition) -> None:
        if v.is_a:
            self.isarefs.setdefault(v.is_a, References()).addref(typ, k)
            self.add_ref(typ, k, typ, v.is_a)
        else:
            self.roots.addref(typ, k)
        if v.mixin:
            self.mixins.addref(typ, k)
        if v.abstract:
            self.abstracts.addref(typ, k)
        for mixin in v.mixins:
            self.mixinrefs.setdefault(mixin, References()).addref(typ, k)
            self.add_ref(typ, k, typ, mixin)
        for union in v.union_of:
            self.unions.setdefault(union, References()).addref(typ, k)
            self.add_ref(typ, k, typ, union)

    def add_ref(self, fromtype: RefType, fromname: str, totype: RefType, toname: str, ) -> None:
        if totype is ClassType:
            self.classrefs.setdefault(toname, References()).addref(fromtype, fromname)
        elif totype is SlotType:
            self.slotrefs.setdefault(toname, References()).addref(fromtype, fromname)
        elif totype is TypeType:
            self.typerefs.setdefault(toname, References()).addref(fromtype, fromname)
        else:
            raise TypeError("Unknown typ: {typ}")

    def check_classes(self, classes: Iterable[str]) -> List[str]:
        return [c for c in classes if c not in self.classes]

    def check_slots(self, slots: Iterable[str]) -> List[str]:
        return [s for s in slots if s not in self.slots]

    def check_types(self, types: Iterable[str]) -> List[str]:
        return [t for t in types if t not in self.types and t not in builtin_names]

    def check_exist(self, elements: Iterable[str]) -> List[str]:
        return [e for e in elements if e not in self.types and e not in self.slots and
                e not in self.classes and e not in builtin_names]

    def errors(self, repair: bool = False) -> List[str]:
        rval = []
        undefined_classes = self.check_classes(self.classrefs.keys())
        if undefined_classes:
            rval += [f"\tUndefined class references: {', '.join(undefined_classes)}"]
        undefined_slots = self.check_slots(self.slotrefs.keys())
        if undefined_slots:
            rval += [f"\tUndefined slot references: {', '.join(undefined_slots)}"]
        undefined_types = self.check_types(self.typerefs.keys())
        if undefined_types:
            rval += [f"\tUndefined type references: {', '.join(undefined_types)}"]

        # Look for slot domain / class slot mismatches
        for cls in self.schema.classes.values():
            for slotname in cls.slots:
                if slotname in self.schema.slots:       # Error checked above
                    if self.schema.slots[slotname].domain != cls.name:
                        rval += [f'\tDomain mismatch: slot "{slotname}" domain is: '
                                 f'"{self.schema.slots[slotname].domain}" class "{cls.name}" claims ownership']

        # Inlined slots must be multivalued (not a inviolable rule, but we make assumptions about this elsewhere in
        # the python generator
        for slot in self.schema.slots.values():
            if slot.inlined and not slot.multivalued:
                rval += [f'\tSlot {slot.name} is declared inline but single valued']

        # Look for slot usages that don't have ancestors
        # TODO: Get this test working
        # for slot_name in self.slotusages:
        #     if len(self.slotusages[slot_name]) == 1 and not self.schema.slots[slot_name].alias:
        #         rval += [f'"{slot_name}": new slot defined in slot_usage for class "{cls.name}"']
        return rval

    def summary(self) -> str:
        rval = ['']
        rval += [f"Classes: {len(self.classes)}"]

        nc, ns, nt = 0, 0, 0
        for cr in self.classrefs.values():
            nc += len(cr.classrefs)
            ns += len(cr.slotrefs)
            nt += len(cr.typerefs)
        rval += [f"\tReferenced by: {nc} classes, {ns} slots, {nt} types "]

        rval += [f"\tRoot: {len(self.roots.classrefs)}"]
        leaves = [c for c in self.classes if c not in self.isarefs]
        rval += [f"\tLeaf: {len(leaves)}"]
        rval += [f"\tStandalone: {len([c for c in self.roots.classrefs if c in leaves])}"]
        rval += [f"\tDeclared mixin: {len(self.mixins.classrefs)}"]
        rval += [f"\tUndeclared mixin: {len([c for c in self.mixinrefs if c not in self.mixins.classrefs])}"]
        rval += [f"\tAbstract: {len(self.abstracts.classrefs)}"]
        undefined_classes = [f'"{c}"' for c in self.classrefs if c not in self.classes]
        if undefined_classes:
            rval += [f"\tUndefined references: {', '.join(undefined_classes)}"]

        rval += ['']
        rval += [f"Slots: {len(self.slots)}"]
        nc, ns, nt = 0, 0, 0
        for cr in self.slotrefs.values():
            nc += len(cr.classrefs)
            ns += len(cr.slotrefs)
            nt += len(cr.typerefs)
        rval += [f"\tReferenced by: {nc} classes, {ns} slots, {nt} types "]
        rval += [f"\tRoot: {len(self.roots.slotrefs)}"]
        leaves = [c for c in self.slots if c not in self.isarefs]
        rval += [f"\tLeaf: {len(leaves)}"]
        rval += [f"\tStandalone: {len([c for c in self.roots.slotrefs if c in leaves])}"]
        rval += [f"\tDeclared mixin: {len(self.mixins.slotrefs)}"]
        rval += [f"\tUndeclared mixin: {len([c for c in self.mixinrefs if c not in self.mixins.slotrefs])}"]
        rval += [f"\tAbstract: {len(self.abstracts.slotrefs)}"]

        unused_slots = [s for s in self.slots if s not in self.slotrefs]
        rval += [f"\tUnused: {len(unused_slots)}"]
        for slot in sorted(unused_slots):
            rval.append(f'\t\t\t"{slot}"')
        undefined_slots = [s for s in self.slotrefs if s not in self.slots]
        if undefined_slots:
            rval += [f"\tUndefined: {len(undefined_slots)}"]
        rval += ["\tDomains:"]
        rval += [f"\t\tUndeclared: {len(self.mtdomains)}"]

        domain_matches = set()
        not_in_domain = set()
        domain_mismatches = set()
        unkdomains = set()
        for slot, dom in self.slotdomains.items():
            if dom in self.classes:
                if slot in self.classslots[dom]:
                    domain_matches.add(slot)
                elif slot not in self.slotclasses:
                    not_in_domain.add(slot)
                else:
                    domain_mismatches.add(slot)
            else:
                unkdomains.add(f"{slot}:{dom}")
        rval += [f"\t\tMatching: {len(domain_matches)}"]
        rval += [f"\t\tNot in domain: {len(not_in_domain)}"]
        if len(not_in_domain):
            rval += ["\t\t\tslot.name: slot.name"]
        for slot in sorted(not_in_domain):
            rval.append(f'\t\t\t"{slot}": "{self.slotdomains[slot]}"')
        rval += [f"\t\tMismatches: {len(domain_mismatches)}"]
        for slot in sorted(domain_mismatches):
            rval.append(f'\t\t\tSlot: "{slot}" declared domain: "{self.slotdomains[slot]}" '
                        f'actual domain(s): {", ".join(self.slotclasses[slot])}')
        if unkdomains:
            rval += [f"\t\tUnknown domain: {', '.join(sorted(unkdomains))}"]

        rval += ["\tRanges:"]
        rval += ["\t\tBuiltin:"]
        for rng, slots in sorted(self.rangerefs.items()):
            if rng in builtin_names:
                rval += [f"\t\t\t{rng}: {len(slots)}"]
        rval += ["\t\tType:"]
        for rng, slots in sorted(self.rangerefs.items()):
            if rng in self.types:
                rval += [f"\t\t\t{rng}: {len(slots)}"]
        rval += ["\t\tClass:"]
        for rng, slots in sorted(self.rangerefs.items()):
            if rng in self.classes:
                rval += [f"\t\t\t{rng}: {len(slots)}"]
        rval += ["\t\tUnknown:"]
        for rng, slots in sorted(self.rangerefs.items()):
            if rng not in builtin_names and rng not in self.types and rng not in self.classes:
                rval += [f"\t\t\t{rng}: {len(slots)}"]

        rval += ['']
        rval += [f"Types: {len(self.types)}"]
        if len(self.types):
            nc, ns, nt = 0, 0, 0
            for typ in self.typerefs:
                if typ not in builtin_names:
                    nc += len(self.typerefs[typ].classrefs)
                    ns += len(self.typerefs[typ].slotrefs)
                    nt += len(self.typerefs[typ].typerefs)
            rval += [f"\tReferenced by: {nc} classes, {ns} slots, {nt} types "]
            for builtin in builtin_names:
                rval += [f"\t{builtin}: {len(self.typeofs.get(builtin, []))}"]
        return '\n'.join(rval)
