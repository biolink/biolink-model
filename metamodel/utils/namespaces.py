from typing import Dict, Optional

from rdflib import Namespace

SIO = Namespace('http://semanticscience.org/resource/SIO_')
HGNC = Namespace('https://monarchinitiative.org/gene/')
OBOID = Namespace('http://purl.obolibrary.org/obo/_')
BIOENTITY = Namespace("http://w3id.org/biolink/vocab/")
OBO = Namespace("http://purl.obolibrary.org/obo/")
META = Namespace("http://w3id.org/biolink/vocab/meta/")
BIOTOP = Namespace("http://purl.org/biotop/biotop.owl#")

known_namespaces: Dict[str, Namespace] = {
    'SIO': SIO,
    'HGNC': HGNC,
    'OBO_': OBOID,
    'BIOENTITY': BIOENTITY,
    'OBO': OBO,
    'META': META,
    'BIOTOP': BIOTOP
}


def nsname_to_url(nsname: str) -> Optional[str]:
    if ':' in nsname and '://' not in nsname:
        raise ValueError("Not a nsname: {nsname}")
    prefix, name = nsname.split(':')
    prefix = prefix.upper()
    return known_namespaces[prefix][name] if prefix in known_namespaces else None
