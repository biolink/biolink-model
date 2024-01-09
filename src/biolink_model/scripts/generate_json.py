from collections import defaultdict
import json
from typing import Any, List, Union
from linkml_runtime.utils.schemaview import SchemaView

file_path = 'src/biolink_model/schema/biolink_model.yaml'

# Read the file content
with open(file_path, 'r') as file:
    file_content_str = file.read()

# Parse the YAML content
sv = SchemaView(file_content_str)


def get_tree_class_recursive(root_node: dict, parent_to_child_map: dict) -> dict:
    """
    Recursively get the tree node.

    :param root_node: The root node of the tree.
    :type root_node: dict
    :param parent_to_child_map: A dictionary mapping parent nodes to child nodes.
    :type parent_to_child_map: dict
    :return: The tree node.
    :rtype: dict

    """
    root_name = root_node["name"]
    children_names = parent_to_child_map.get(root_name, [])
    if children_names:
        children = []
        for child_name in children_names:
            child_node = {"name": child_name, "parent": root_name}
            child_node = get_tree_class_recursive(child_node, parent_to_child_map)
            children.append(child_node)
        root_node["children"] = sorted(children, key=lambda x: x["name"])
        # test

    return root_node


def load_predicate_tree_data(return_parent_to_child_dict: bool = False) -> Union[List[List[Any]], dict]:
    """
    Load the predicate tree data from the model.

    :return: The predicate tree data.
    """
    parent_to_child_dict = defaultdict(set)
    predicate_tree = []
    for slot_name in sv.all_slots(imports=True):
        slot = sv.get_slot(slot_name)
        if slot.deprecated:
            continue
        slot_name = convert_predicate_to_trapi_format(slot_name)
        parent_name_english = slot.is_a
        if parent_name_english:
            parent_name = convert_predicate_to_trapi_format(parent_name_english)
            parent_to_child_dict[parent_name].add(slot_name)
            root_node = {"name": "related_to"}
            predicate_tree = get_tree_slot_recursive(root_node, parent_to_child_dict)
        if slot.mixins:
            for mixin in slot.mixins:
                parent_name_english = mixin
                parent_name = convert_predicate_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(slot_name)
                root_node = {"name": "related_to_at_instance_level"}
                predicate_tree = get_tree_slot_recursive(root_node, parent_to_child_dict)
    return ([predicate_tree], parent_to_child_dict) if return_parent_to_child_dict else ([predicate_tree])


def load_qualifier_tree_data(return_parent_to_child_dict: bool = False) -> Union[List[List[Any]], dict]:
    """
    Load the qualifier tree data from the model.

    :return: The qualifier tree data.
    """
    parent_to_child_dict = defaultdict(set)
    predicate_tree = []
    for slot_name in sv.all_slots(imports=True):
        slot = sv.get_slot(slot_name)
        if slot.deprecated:
            continue
        slot_name = convert_predicate_to_trapi_format(slot_name)
        parent_name_english = slot.is_a
        if parent_name_english:
            parent_name = convert_predicate_to_trapi_format(parent_name_english)
            parent_to_child_dict[parent_name].add(slot_name)
            root_node = {"name": "qualifier"}
            predicate_tree = get_tree_slot_recursive(root_node, parent_to_child_dict)
    return ([predicate_tree], parent_to_child_dict) if return_parent_to_child_dict else ([predicate_tree])


def load_category_tree_data(return_parent_to_child_dict: bool = False) -> tuple:
    """
    Load the category tree data from the model.

    :param return_parent_to_child_dict: Whether to return the parent to child dictionary.
    :type return_parent_to_child_dict: bool
    :return: The category tree data.
    :rtype: tuple
    """
    parent_to_child_dict = defaultdict(set)
    category_tree = {}
    for class_name in sv.all_classes(imports=True):
        cls = sv.get_class(class_name)
        if cls.deprecated:
            continue
        class_name = convert_predicate_to_trapi_format(class_name)
        if cls.is_a:
            parent_name_english = cls.is_a
            if parent_name_english:
                parent_name = convert_predicate_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(class_name)
                root_node = {"name": "NamedThing", "parent": None}
                category_tree = get_tree_class_recursive(root_node, parent_to_child_dict)
                parent_name = convert_category_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(class_name)

    return ([category_tree], parent_to_child_dict) if return_parent_to_child_dict else ([category_tree])


def load_association_tree_data(return_parent_to_child_dict: bool = False) -> tuple:
    """
    Load the category tree data from the model.

    :param return_parent_to_child_dict: Whether to return the parent to child dictionary.
    :type return_parent_to_child_dict: bool
    :return: The category tree data.
    :rtype: tuple
    """
    parent_to_child_dict = defaultdict(set)
    category_tree = {}
    for class_name in sv.all_classes(imports=True):
        cls = sv.get_class(class_name)
        if cls.deprecated:
            continue
        class_name = convert_predicate_to_trapi_format(class_name)
        if cls.is_a:
            parent_name_english = cls.is_a
            if parent_name_english:
                parent_name = convert_predicate_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(class_name)
                root_node = {"name": "Association", "parent": None}
                category_tree = get_tree_class_recursive(root_node, parent_to_child_dict)
                parent_name = convert_category_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(class_name)

    return ([category_tree], parent_to_child_dict) if return_parent_to_child_dict else ([category_tree])


def load_aspect_tree_data() -> List[dict]:
    aspect_enum_field_name = "GeneOrGeneProductOrChemicalEntityAspectEnum"
    # Build aspects tree
    parent_to_child_dict = defaultdict(set)
    root_name = "[root]"
    enum = sv.get_enum(aspect_enum_field_name)
    for aspect_name in enum.permissible_values:
        parent = sv.permissible_value_parent(aspect_name, aspect_enum_field_name) if aspect_name else root_name
        direct_parent = parent[0] if parent else root_name
        parent_to_child_dict[direct_parent].add(aspect_name)
    root_node = {"name": root_name, "parent": None}
    aspect_tree = get_tree_slot_recursive(root_node, parent_to_child_dict)

    return [aspect_tree]


def convert_predicate_to_trapi_format(english_predicate: str) -> str:
    # Converts a string like "treated by" to "treated_by"
    return english_predicate.replace(' ', '_')


def convert_category_to_trapi_format(english_category: str) -> str:
    # Converts a string like "named thing" to "NamedThing"
    return "".join([f"{word[0].upper()}{word[1:]}" for word in english_category.split(" ")])


def get_tree_slot_recursive(root_node: dict, parent_to_child_map: dict) -> dict:
    """
    Recursively get the tree node.

    :param root_node: The root node of the tree.
    :type root_node: dict
    :param parent_to_child_map: A dictionary mapping parent nodes to child nodes.
    :type parent_to_child_map: dict
    :return: The tree node.
    :rtype: dict

    """
    root_name = root_node["name"]
    children_names = parent_to_child_map.get(root_name, [])
    if children_names:
        children = []
        for child_name in children_names:
            child_node = {"name": child_name, "parent": root_name}
            child_node = get_tree_slot_recursive(child_node, parent_to_child_map)
            children.append(child_node)
        root_node["children"] = sorted(children, key=lambda x: x["name"])
        # test

    return root_node


"""
            elements: {
                nodes: [
                    {data: {id: 'a', label: 'treats', mdFile: "treats", mixin: "true"}},
                    {data: {id: 'b', label: 'contraindicated in', mdFile: "contraindicated in", mixin: "false"}},
                    {data: {id: 'c', label: 'studied_to_treat', mdFile: "studied to treat", mixin: "false"}},
                    {data: {id: 'd', label: 'taken_or_studied_or_treats', mdFile: "studied to treat", mixin: "false"}}

                ],
                edges: [
                    {data: {id: 'ab', source: 'a', target: 'b'}},
                    {data: {id: 'bc', source: 'a', target: 'c'}},
                    {data: {id: 'ca', source: 'd', target: 'a'}},
                    {data: {id: 'ca', source: 'b', target: 'a'}}
                ]
            },
"""

def get_predicate_dager(nodes: list, edges: list):
    for slot_name in sv.all_slots(imports=True):
        slot = sv.get_slot(slot_name)
        if slot.deprecated:
            print("deprecated ", slot.name)
            continue
        if ("treat" in slot.name
            or "related to" in slot.name
            or "condition" in slot.name
            or "associated with" in slot.name
            or "indicated" in slot.name
            or "models" in slot.name
                     or "contributes to" in slot.name
            or slot.name == "affects"
        or slot.name == "causes"
            or "trials" in slot.name
            or "likelihood" in slot.name) and not slot.deprecated and "canonical_predicate" in slot.annotations:
        #if ("related to" in sv.slot_ancestors(slot.name) or (slot.mixin and "canonical_predicate" in slot.annotations)) and not slot.deprecated:
            print("adding ", slot.name)
            nodes.append(
                {
                    "data": {
                        "id": slot.name,
                        "label": slot.name,
                        "mdFile": convert_predicate_to_trapi_format(slot.name),
                        "mixin": "true" if slot.mixin else "false"
                    }
                }
            )
            for parent in sv.slot_parents(slot.name, mixins=True):
                if slot.deprecated:
                    continue
                if (("treat" in slot.name
                     or "condition" in slot.name
                     or "associated with" in slot.name
                     or "indicated" in slot.name
                     or "contributes to" in slot.name
                     or slot.name == "affects"
                     or slot.name == "causes"
                     or "related to" in slot.name
                     or "models" in slot.name
                     or "trials" in slot.name
                     or "likelihood" in slot.name)
                    and not sv.get_element(parent).deprecated) and "canonical_predicate" in slot.annotations:
                    edges.append(
                        {
                            "data": {
                                "id": f"{parent}-{slot.name}",
                                "source": parent,
                                "target": slot.name
                            }
                        }
                    )

    return nodes, edges


def generate_viz_json():

    # Generate the dagre viz data
    nodes, edges = get_predicate_dager([], [])
    elements = {"nodes": nodes, "edges": edges}
    with open('src/docs/treats_dagre.json', 'w') as json_file:
        json.dump(elements, json_file, indent=4)

    # Generate the d3 viz data
    pred_data = load_predicate_tree_data()
    qualifier_data = load_qualifier_tree_data()
    cat_data = load_category_tree_data()
    aspect_data = load_aspect_tree_data()
    association_data = load_association_tree_data()

    with open('src/docs/predicates.json', 'w') as json_file:
        json.dump(pred_data, json_file, indent=4)

    with open('src/docs/qualifiers.json', 'w') as json_file:
        json.dump(qualifier_data, json_file, indent=4)

    with open('src/docs/categories.json', 'w') as json_file:
        json.dump(cat_data, json_file, indent=4)

    with open('src/docs/associations.json', 'w') as json_file:
        json.dump(association_data, json_file, indent=4)

    with open('src/docs/aspects.json', 'w') as json_file:
        json.dump(aspect_data, json_file, indent=4)


if __name__ == "__main__":
    generate_viz_json()

