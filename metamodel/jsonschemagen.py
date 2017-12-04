from .schemautils import *

def tr_class(c, schema):
    props = {}
    obj = {
        "title": c.name,
        "type": "object",
        "properties": props,
        "description": c.description
        "required": []
    }

    # Slots:
    # JSON-Schema does not have inheritance,
    # so we duplicate slots from inherited parents and mixins
    slots = c.slots
    if slots is None:
        slots = []
    for x in get_parents_refl(c, schema):
        if x.slots:
            slots += x.slots
    for s in slots:
        stype = "string";
        props[s] = {
            "type": {
                "$ref": "#/definitions/{}".format(s)
            }
        }

    return obj

def tr_slot(s, schema):
    obj = None
    range = s.range
    # TODO: allow inlining
    if s.multivalued:
        obj = {
            "type" : "array",
            "items" : {
                "$ref": jref(range)
            }
        }
    else:
        obj = {
            "$ref" : jref(range)
        }
    return obj

def jref(n):
    return "#/definitions/{}".format(n)

def write_json_schema(schema):

    obj = {
    }
    for c in schema.classes:
        obj[c.name] = tr_class(c, schema)
    for s in schema.slots:
        obj[s.name] = tr_slot(s, schema)
    return obj
