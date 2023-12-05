import os
from urllib3.util.ssl_ import create_urllib3_context
import yaml

ctx = create_urllib3_context()
ctx.load_default_certs()
ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

INFORES_YAML = os.path.join('../../../infores_catalog.yaml')


def extract_github_sources():
    with open(INFORES_YAML, 'r') as yaml_file, open('github_sources.txt', 'w') as github_file, open('no_url_sources.txt', 'w') as no_url_file, open('wiki_links.txt', 'w') as wiki_links:
        data = yaml.safe_load(yaml_file)
        for infores in data.get('information_resources'):
            if "xref" in infores.keys():
                if not infores.get("deprecated"):
                    for xref in infores.get("xref"):
                        if xref.startswith("https://github.com") and not xref.startswith("https://github.com/NCATSTranslator/Translator-All/wiki"):
                            github_file.write(f"{infores.get('id')},{infores.get('name')},{xref}\n")
                        elif xref.startswith("https://github.com/NCATSTranslator/Translator-All/wiki"):
                            wiki_links.write(f"{infores.get('id')},{infores.get('name')},{xref}\n")
            else:
                if not infores.get("deprecated"):
                    no_url_file.write(f"{infores.get('id')}, {infores.get('name')}\n")


if __name__ == "__main__":
    extract_github_sources()
