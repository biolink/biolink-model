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

INFORES_YAML = os.path.join('../infores_catalog.yaml')


def extract_github_sources():
    with open(INFORES_YAML, 'r') as yaml_file, open('github_sources.txt', 'w') as github_file, open('no_url_sources.txt', 'w') as no_url_file:
        data = yaml.safe_load(yaml_file)
        for infores in data.get('information_resources'):
            if "xref" in infores.keys():
                for xref in infores.get("xref"):
                    if xref.startswith("https://github.com"):
                        github_file.write(f"{infores.get('name')} {xref}\n")
            else:
                no_url_file.write(f"NO URL {infores.get('name')}\n")

# Example usage
extract_github_sources()


if __name__ == "__main__":
    extract_github_sources()
