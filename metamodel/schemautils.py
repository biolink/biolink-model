import logging

def get_slots_inf(c, schema):
    slots = c.slots
    if not slots:
        slots = []
    fs = [get_slot_name_from_obj(f) for f in slots]
    if c.is_a:
        fs += get_slots_inf(get_cls(c.is_a, schema), schema)
    return fs

def get_slot_names_inf(c, schema, use_mixins=False):
    slots = c.slots
    if not slots:
        slots = []
    fs = [f for f in slots]
    if c.is_a:
        fs += get_slot_names_inf(get_cls(c.is_a, schema), schema)
    if use_mixins and c.mixins:
        for m in c.mixins:
            mc = get_cls(m, schema)
            if not mc:
                logging.error("Cannot find mixin: {} mixed from: {}".format(m, c.name))
            else:
                fs += get_slots_inf(mc, schema)
    return fs

def get_slot_name_from_obj(f):
    slotname = None
    if isinstance(f,str):
        slotname = f
    elif isinstance(f,dict):
        # TODO
        slotname = f['name']
    else:
        slotname = f.name
    pyslotname = get_slot_name(slotname)
    return pyslotname

def get_parents_refl(c, schema):
    ps = [c]
    if c.is_a:
        pcls = get_cls(c.is_a, schema)
        if not pcls:
            logging.error("No parent class: {} for {}".format(c.is_a, c.name))
        ps += get_parents_refl(pcls, schema)
    return ps

def get_slot_parents_refl(s, schema):
    ps = [c]
    if s.is_a:
        pslot = get_slot(s.is_a, schema)
        if not pslot:
            logging.error("No parent class: {} for {}".format(s.is_a, s.name))
        ps += get_slot_parents_refl(pslot, schema)
    return ps

def get_cls(cn, schema):
    for c in schema.classes:
        if c.name == cn:
            return c
        
def get_schema_class_name(c):
    return get_class_name(c + " schema")
def get_class_name(c):
    return c.title().replace(" ","")

def get_slot_name(c):
    return c.replace(" ","_").lower()

def underscore_style(c):
    return c.replace(" ","_").lower()

def get_slot(sn, schema):
    for s in schema.slots:
        if s.name == sn:
            return s

def get_slot_range(sn, schema, classdef=None):
    if classdef is not None and classdef.slot_usage is not None:
        for su in classdef.slot_usage:
            logging.info("CHECKING {}".format(su.name))
            if su.name == sn and su.range:
                return su.range
    s = get_slot(sn, schema)
    if s:
        return s.range
    else:
        logging.warning("No defined slot: {}".format(sn))

