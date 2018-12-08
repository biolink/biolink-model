import biolinkmodel.datamodel as bl
import json

def run():
    g = bl.Gene('HGNC:1')
    a = bl.AnatomicalEntity('CL:0000182')
    stage = bl.LifeStage('UBERON:0007222')
    r = bl.RelationshipType('RO:0002206')
    iid = 'IX:1'
    assoc = bl.GeneToExpressionSiteAssociation(id=iid,
                                               subject=g.id,
                                               relation=r.id,
                                               object=a.id,
                                               stage_qualifier=stage.id)
    print(assoc)
    #print(json.dumps(assoc))
    

if __name__ == "__main__":
    run()

