import os
import requests
import csv
import time
import urllib3
from urllib3.util.ssl_ import create_urllib3_context

ctx = create_urllib3_context()
ctx.load_default_certs()
ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT


INFORES_TSV = os.path.join('infores_catalog_nodes.tsv')


def is_valid_urls(url: str) -> bool:
    retries = 3
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
            print(f"Exception: {e}. Retrying...")
            time.sleep(1)
    return False


class InformationResource:

    def __init__(self) -> None:
        infores_map = {}

    def dump(self):
        raise NotImplementedError

    def validate(self):
        infores_map = {}
        with open(INFORES_TSV, 'r') as tsv_file:
            reader = csv.reader(tsv_file, delimiter='\t')
            for line in reader:
                if len(line) < 5:
                    raise ValueError("Invalid infores TSV: too few items in a line")
                if line[2] == 'id' or line[0] == 'deprecated':
                    continue
                elif line[3] == '' and line[0] != 'deprecated':
                    print(line)
                else:
                    # exceptions for resolvable URLs that don't return 200 response for some reason (e.g. require
                    # user to accept a popup before resolving):
                    if line[2] == 'infores:athena' \
                            or line[2] == 'infores:isb-wellness' \
                            or line[2] == 'infores:isb-incov' \
                            or line[2] == 'infores:preppi' \
                            or line[2] == 'infores:ttd' \
                            or line[2] == 'infores:flybase' \
                            or line[2] == 'infores:lincs' \
                            or line[2] == 'infores:aeolus' \
                            or is_valid_urls(line[3]):
                        infores_map[line[2]] = {
                            "status": line[0],
                            "name": line[1],
                            "url": line[3],
                            "synonyms": line[4],
                            "description": line[5],
                        }
                    else:
                        print(line)
                        print("Invalid infores URL:" + line[3] + " for " + line[2])
                        raise ValueError("invalid return code for URL" + line[3] + " for " + line[2])


if __name__ == "__main__":
    InformationResource().validate()
