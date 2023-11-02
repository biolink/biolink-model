from collections import defaultdict
import json
from typing import Any, List
from linkml_runtime.utils.schemaview import SchemaView



file_path = 'src/biolink_model/schema/biolink_model.yaml'

# Read the file content
with open(file_path, 'r') as file:
    file_content_str = file.read()

# Parse the YAML content
sv = SchemaView(file_content_str)


def get_tree_node_recursive(root_node: dict, parent_to_child_map: dict) -> dict:
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
            child_node = get_tree_node_recursive(child_node, parent_to_child_map)
            children.append(child_node)
        root_node["children"] = sorted(children, key=lambda x: x["name"])
    return root_node


def load_predicate_tree_data(return_parent_to_child_dict: bool = False) -> list[list[Any] | dict]:
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
            predicate_tree = get_tree_node_recursive(root_node, parent_to_child_dict)
        if slot.mixins:
            for mixin in slot.mixins:
                parent_name_english = mixin
                parent_name = convert_predicate_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(slot_name)
                root_node = {"name": "related_to_at_instance_level"}
                predicate_tree = get_tree_node_recursive(root_node, parent_to_child_dict)
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
                category_tree = get_tree_node_recursive(root_node, parent_to_child_dict)
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
    aspect_tree = get_tree_node_recursive(root_node, parent_to_child_dict)

    return [aspect_tree]


def load_category_er_tree_data(return_parent_to_child_dict: bool = False) -> tuple:
    """
    Load the category tree data from the model.

    :param linkml_version: The version of the linkml model.
    :type linkml_version: str
    :param return_parent_to_child_dict: Whether to return the parent to child dictionary.
    :type return_parent_to_child_dict: bool
    :return: The category tree data.
    :rtype: tuple

    """

    # First build the standard category tree
    category_tree, parent_to_child_map = load_category_tree_data(return_parent_to_child_dict=True)
    child_to_parent_map = {child_name: parent_name for parent_name, children_names in parent_to_child_map.items()
                          for child_name in children_names}

    # Then move gene/protein-related subbranches under one new sub-branch within BiologicalEntity
    biological_entity_sub_branches = parent_to_child_map["BiologicalEntity"]
    sub_branches_to_keep = {"BiologicalProcessOrActivity", "DiseaseOrPhenotypicFeature", "OrganismalEntity"}
    sub_branches_to_move = biological_entity_sub_branches.difference(sub_branches_to_keep)
    new_sub_branch = "GeneticOrMolecularBiologicalEntity"
    for sub_branch_to_move in sub_branches_to_move:
        child_to_parent_map[sub_branch_to_move] = new_sub_branch
    parent_to_child_map_revised = defaultdict(set)
    for child, parent in child_to_parent_map.items():
        parent_to_child_map_revised[parent].add(child)
    parent_to_child_map_revised["BiologicalEntity"].add(new_sub_branch)

    root_node = {"name": "NamedThing", "parent": None}
    category_tree_for_er = get_tree_node_recursive(root_node, parent_to_child_map_revised)

    return ([category_tree_for_er], parent_to_child_map_revised) if return_parent_to_child_dict else ([category_tree_for_er])


def convert_predicate_to_trapi_format(english_predicate: str) -> str:
    # Converts a string like "treated by" to "treated_by"
    return english_predicate.replace(' ', '_')


def convert_category_to_trapi_format(english_category: str) -> str:
    # Converts a string like "named thing" to "NamedThing"
    return "".join([f"{word[0].upper()}{word[1:]}" for word in english_category.split(" ")])


def generate_viz_json():
    pred_data = load_predicate_tree_data()

    with open('src/docs/predicates.json', 'w') as json_file:
        json.dump(pred_data, json_file, indent=4)

    cat_data = load_category_tree_data()

    with open('src/docs/categories.json', 'w') as json_file:
        json.dump(cat_data, json_file, indent=4)

    aspect_data = load_aspect_tree_data()

    with open('src/docs/aspects.json', 'w') as json_file:
        json.dump(aspect_data, json_file, indent=4)


if __name__ == "__main__":
    generate_viz_json()

