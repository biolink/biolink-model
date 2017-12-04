import pytest
import yaml
import logging
from biolinkmodel.datamodel import *

def test_make_assoc():
    print("HI")
    a = DiseaseToPhenotypicFeatureAssociation(subject='x', relation='r', object='o')
    print('A={}'.format(a))
    
    
