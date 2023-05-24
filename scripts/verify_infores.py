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

INFORES_YAML = os.path.join('infores_catalog.yaml')


def is_valid_urls(url: str) -> bool:
    retries = 3
    url = url[0]
    print("Checking URL: " + url)
    for i in range(retries):
        try:
            with urllib3.PoolManager(ssl_context=ctx) as http:
                response = http.request("GET", url, headers={'User-Agent': 'Mozilla/5.0'})
                if response.status == 200:
                    return True
                else:
                    print(f"Response status code: {response.status}. Retrying...")
                    time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(url)
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return True
    except requests.exceptions.RequestException as e:
        print(f"Exception: {e}")
        print(f"Response status code: {response.status}.", url)
    return False


class InformationResource:

    def __init__(self) -> None:
        infores_map = {}

    def dump(self):
        raise NotImplementedError

    def validate(self):
        with open(INFORES_YAML, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)
            for infores in data.get('information_resources'):
                # exceptions for resolvable URLs that don't return 200 response for some reason (e.g. require
                # user to accept a popup before resolving):
                if infores.get("id") == 'infores:athena' \
                        or infores.get("id") == 'infores:isb-wellness' \
                        or infores.get("id") == 'infores:isb-incov' \
                        or infores.get("id") == 'infores:preppi' \
                        or infores.get("id") == 'infores:ttd' \
                        or infores.get("id") == 'infores:flybase' \
                        or infores.get("id") == 'infores:xenbase' \
                        or infores.get("id") == 'infores:aeolus' \
                        or infores.get("xref") is None \
                        or is_valid_urls(infores.get("xref")):
                    print(infores.get('id'), "has valid URL (xref)")
                else:
                    print(infores)
                    print("Invalid infores URL:" + infores.get("xref") + " for " + infores.get("name"))
                    raise ValueError("invalid return code for URL" + infores.get("name") + " for " + infores.get("id"))


if __name__ == "__main__":
    InformationResource().validate()
