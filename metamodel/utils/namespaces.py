from typing import Dict, Optional

from rdflib import Namespace

SIO = Namespace('http://semanticscience.org/resource/SIO_')
HGNC = Namespace('https://monarchinitiative.org/gene/')
OBOID = Namespace('http://purl.obolibrary.org/obo/_')
BIOENTITY = Namespace("http://bioentity.io/vocab/")
YUML = Namespace('http://yuml.me/diagram/nofunky/class/')

known_namespaces: Dict[str, Namespace] = {
    'SIO': SIO,
    'HGNC': HGNC,
    'OBO': OBOID,
    'BIOENTITY': BIOENTITY,
    'YUML': YUML
}

def nsname_to_url(nsname: str) -> Optional[str]:
    if ':' in nsname and '://' not in nsname:
        raise ValueError("Not a nsname: {nsname}")
    prefix = nsname.split(':')[0].upper()
