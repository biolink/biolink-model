from .schemautils import *
import yaml
import logging

def tr_class(c, schema):
    props = {}
    obj = {
        "title": c.name,
        "type": "object",
        "properties": props,
        "description": c.description,
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


def tr_class(c, schema):
    obj = {
        'id': c.name,
        'schema_generating': True,
        'description' : c.description,
        'display_name': c.name,
        'document_category': c.name,
        #boost_weights: annotation_class^2.0 annotation_class_label^1.0 bioentity^2.0 bioentity_label^1.0 bioentity_name^1.0 annotation_extension_class^2.0 annotation_extension_class_label^1.0 reference^1.0 panther_family^1.0 panther_family_label^1.0 bioentity_isoform^1.0 regulates_closure^1.0 regulates_closure_label^1.0
        #result_weights: bioentity^7.0 bioentity_name^6.0 qualifier^5.0 annotation_class^4.7 annotation_extension_json^4.5 assigned_by^4.0 taxon^3.0 evidence_type^2.5 evidence_with^2.0 panther_family^1.5 type^1.0 bioentity_isoform^0.5 reference^0.25 date^0.10
        #filter_weights: aspect^10.0 taxon_subset_closure_label^9.0 type^8.5 evidence_subset_closure_label^8.0 regulates_closure_label^7.0 annotation_class_label^6.0 qualifier^5.0 annotation_extension_class_closure_label^4.0 assigned_by^3.0 panther_family_label^2.0
        'weight': 20
        }
    fields = []
    slots = get_slots_inf(c, schema)
    for sn in slots:
        s = get_slot(sn, schema)
        field = {}
        if not s:
            logging.error("No slot info for: {}".format(sn))
            field = {
                'id': sn,
                'display_name': sn
            }
        else:
            field = {
                'id': get_slot_name(s.name),
                'description': s.description,
                'display_name': s.name,
            }
            if s.multivalued:
                field['cardinality'] = 'multi'
        field['property'] = []
        fields.append(field)
    obj['fields'] = fields
    return obj

def write_golr_yaml_to_dir(schema, dir):
    for c in schema.classes:
        if c.abstract:
            continue
        cn = underscore_style(c.name)
        obj = tr_class(c, schema)
        fn = "{}/{}-config.yaml".format(dir, cn)
        f = open(fn,'w')
        f.write(yaml.dump(obj))
        f.close()
        
