def get_slots_inf(c, schema):
    slots = c.slots
    if not slots:
        slots = []
    fs = [get_slot_name_from_obj(f) for f in slots]
    if c.is_a:
        fs += get_slots_inf(get_cls(c.is_a, schema), schema)
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
        ps += get_parents_refl(get_cls(c.is_a, schema), schema)
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
