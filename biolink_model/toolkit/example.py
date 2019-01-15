if __name__ == '__main__':
    import biolink_model.toolkit as btk

    print('"related_to" is an edge label:', btk.is_edgelabel('related_to'))
    print()

    print('"related to" is an edge label:', btk.is_edgelabel('related to'))
    print()

    print('"named thing" is a category:', btk.is_category('named thing'))
    print()

    print('Best mapping for "SEMMEDDB:AFFECTS":', btk.get_by_mapping('SEMMEDDB:AFFECTS'))
    print()

    print('All mappings for "SEMMEDDB:AFFECTS":', btk.get_all_by_mapping('SEMMEDDB:AFFECTS'))
    print()

    print('Named thing object:', btk.get_element('named thing'))
    print()
