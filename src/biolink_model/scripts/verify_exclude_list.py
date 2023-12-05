import os
import requests
import csv
import time
import urllib3
from urllib3.util.ssl_ import create_urllib3_context
import yaml

ctx = create_urllib3_context()
ctx.load_default_certs()
ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

EXCLUDE_YAML = os.path.join('../../../semmed-exclude-list.yaml')


def validate():
    with open(EXCLUDE_YAML, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        for exclusion in data.get('excluded_semmedb_records'):
            if exclusion.get("subject_code") != 'n/a' and exclusion.get("semmed_subject_code").startswith("T"):
                raise ValueError("Subject and object codes should not start with T", exclusion)
            if exclusion.get("object_code") != 'n/a' and exclusion.get("semmed_subject_code").startswith("T"):
                raise ValueError("Subject and object codes should not start with T", exclusion)
            if exclusion.get("subject_t_code") is not None and not exclusion.get("semmed_subject_t_code").startswith("T"):
                raise ValueError("Subject T and object T codes should start with T", exclusion)
            if exclusion.get("object_t_code") is not None and not exclusion.get("semmed_object_t_code").startswith("T"):
                raise ValueError("Subject T and object T codes should start with T", exclusion)
            if exclusion.get("semmed_predicate") is not None:
                if exclusion.get("semmed_predicate") != exclusion.get("semmed_predicate").upper():
                    raise ValueError("Predicate should be uppercase", exclusion)


if __name__ == "__main__":
    validate()
