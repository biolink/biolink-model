# Auto generated from biolink_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-07-25T22:57:28
# Schema: Biolink-Model
#
# id: https://w3id.org/biolink/biolink-model
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Double, Float, Integer, String, Time, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDTime

metamodel_version = "1.7.0"
version = "4.2.6-rc5"

# Namespaces
AGRKB = CurieNamespace('AGRKB', 'https://www.alliancegenome.org/')
APO = CurieNamespace('APO', 'http://purl.obolibrary.org/obo/APO_')
ASPGD = CurieNamespace('AspGD', 'http://www.aspergillusgenome.org/cgi-bin/locus.pl?dbid=')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
BIGG_METABOLITE = CurieNamespace('BIGG_METABOLITE', 'http://identifiers.org/bigg.metabolite/')
BIGG_REACTION = CurieNamespace('BIGG_REACTION', 'http://identifiers.org/bigg.reaction/')
BIOGRID = CurieNamespace('BIOGRID', 'http://identifiers.org/biogrid/')
BIOSAMPLE = CurieNamespace('BIOSAMPLE', 'http://identifiers.org/biosample/')
BSPO = CurieNamespace('BSPO', 'http://purl.obolibrary.org/obo/BSPO_')
BTO = CurieNamespace('BTO', 'http://purl.obolibrary.org/obo/BTO_')
CAID = CurieNamespace('CAID', 'http://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=')
CARO = CurieNamespace('CARO', 'http://purl.obolibrary.org/obo/CARO_')
CAS = CurieNamespace('CAS', 'http://identifiers.org/cas/')
CATH = CurieNamespace('CATH', 'http://identifiers.org/cath/')
CATH_SUPERFAMILY = CurieNamespace('CATH_SUPERFAMILY', 'http://identifiers.org/cath.superfamily/')
CDD = CurieNamespace('CDD', 'http://identifiers.org/cdd/')
CHADO = CurieNamespace('CHADO', 'http://gmod.org/wiki/Chado/')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
CHEMBL_MECHANISM = CurieNamespace('CHEMBL_MECHANISM', 'https://www.ebi.ac.uk/chembl/mechanism/inspect/')
CHEMBL_TARGET = CurieNamespace('CHEMBL_TARGET', 'http://identifiers.org/chembl.target/')
CID = CurieNamespace('CID', 'http://pubchem.ncbi.nlm.nih.gov/compound/')
CIO = CurieNamespace('CIO', 'http://purl.obolibrary.org/obo/CIO_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CLINICALTRIALS = CurieNamespace('CLINICALTRIALS', 'http://identifiers.org/clinicaltrials/')
CLINVAR = CurieNamespace('CLINVAR', 'http://identifiers.org/clinvar')
CLO = CurieNamespace('CLO', 'http://purl.obolibrary.org/obo/CLO_')
COAR_RESOURCE = CurieNamespace('COAR_RESOURCE', 'http://purl.org/coar/resource_type/')
COG = CurieNamespace('COG', 'https://www.ncbi.nlm.nih.gov/research/cog-project/')
CPT = CurieNamespace('CPT', 'https://www.ama-assn.org/practice-management/cpt/')
CTD = CurieNamespace('CTD', 'http://ctdbase.org/')
CTD_CHEMICAL = CurieNamespace('CTD_CHEMICAL', 'http://ctdbase.org/detail.go?type=chem&acc=')
CTD_DISEASE = CurieNamespace('CTD_DISEASE', 'http://ctdbase.org/detail.go?type=disease&db=MESH&acc=')
CTD_GENE = CurieNamespace('CTD_GENE', 'http://ctdbase.org/detail.go?type=gene&acc=')
CHEMBANK = CurieNamespace('ChemBank', 'http://chembank.broadinstitute.org/chemistry/viewMolecule.htm?cbid=')
COMPLEXPORTAL = CurieNamespace('ComplexPortal', 'https://www.ebi.ac.uk/complexportal/complex/')
DBSNP = CurieNamespace('DBSNP', 'http://identifiers.org/dbsnp/')
DDANAT = CurieNamespace('DDANAT', 'http://purl.obolibrary.org/obo/DDANAT_')
DGIDB = CurieNamespace('DGIdb', 'https://www.dgidb.org/interaction_types')
DOID = CurieNamespace('DOID', 'http://purl.obolibrary.org/obo/DOID_')
DOID_PROPERTY = CurieNamespace('DOID-PROPERTY', 'http://purl.obolibrary.org/obo/doid#')
DRUGBANK = CurieNamespace('DRUGBANK', 'http://identifiers.org/drugbank/')
DRUGCENTRAL = CurieNamespace('DrugCentral', 'http://drugcentral.org/drugcard/')
EC = CurieNamespace('EC', 'http://www.enzyme-database.org/query.php?ec=')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
EDAM_DATA = CurieNamespace('EDAM-DATA', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('EDAM-FORMAT', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('EDAM-OPERATION', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('EDAM-TOPIC', 'http://edamontology.org/topic_')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/EFO_')
EGGNOG = CurieNamespace('EGGNOG', 'http://identifiers.org/eggnog/')
EMAPA = CurieNamespace('EMAPA', 'http://purl.obolibrary.org/obo/EMAPA_')
ENSEMBL = CurieNamespace('ENSEMBL', 'http://identifiers.org/ensembl/')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_')
FAO = CurieNamespace('FAO', 'http://purl.obolibrary.org/obo/FAO_')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
FBBT = CurieNamespace('FBbt', 'http://purl.obolibrary.org/obo/FBbt_')
FBCV = CurieNamespace('FBcv', 'http://purl.obolibrary.org/obo/FBcv_')
FBDV = CurieNamespace('FBdv', 'http://purl.obolibrary.org/obo/FBdv_')
FMA = CurieNamespace('FMA', 'http://purl.obolibrary.org/obo/FMA_')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
FYECO = CurieNamespace('FYECO', 'https://www.pombase.org/term/')
FYPO = CurieNamespace('FYPO', 'http://purl.obolibrary.org/obo/FYPO_')
GENEPIO = CurieNamespace('GENEPIO', 'http://purl.obolibrary.org/obo/GENEPIO_')
GENO = CurieNamespace('GENO', 'http://purl.obolibrary.org/obo/GENO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
GOLD_META = CurieNamespace('GOLD_META', 'http://identifiers.org/gold.meta/')
GOP = CurieNamespace('GOP', 'http://purl.obolibrary.org/obo/go#')
GOREL = CurieNamespace('GOREL', 'http://purl.obolibrary.org/obo/GOREL_')
GSID = CurieNamespace('GSID', 'https://scholar.google.com/citations?user=')
GTEX = CurieNamespace('GTEx', 'https://www.gtexportal.org/home/gene/')
GTOPDB = CurieNamespace('GTOPDB', 'https://www.guidetopharmacology.org/GRAC/LigandDisplayForward?ligandId=')
HAMAP = CurieNamespace('HAMAP', 'http://identifiers.org/hamap/')
HANCESTRO = CurieNamespace('HANCESTRO', 'http://www.ebi.ac.uk/ancestro/ancestro_')
HCPCS = CurieNamespace('HCPCS', 'http://purl.bioontology.org/ontology/HCPCS/')
HGNC = CurieNamespace('HGNC', 'http://identifiers.org/hgnc/')
HGNC_FAMILY = CurieNamespace('HGNC_FAMILY', 'http://identifiers.org/hgnc.family/')
HMDB = CurieNamespace('HMDB', 'http://identifiers.org/hmdb/')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
HSAPDV = CurieNamespace('HsapDv', 'http://purl.obolibrary.org/obo/HsapDv_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
ICD10 = CurieNamespace('ICD10', 'https://icd.who.int/browse10/2016/en#/')
ICD9 = CurieNamespace('ICD9', 'http://translator.ncats.nih.gov/ICD9_')
IDO = CurieNamespace('IDO', 'http://purl.obolibrary.org/obo/IDO_')
INCHI = CurieNamespace('INCHI', 'http://identifiers.org/inchi/')
INCHIKEY = CurieNamespace('INCHIKEY', 'http://identifiers.org/inchikey/')
INO = CurieNamespace('INO', 'http://purl.obolibrary.org/obo/INO_')
INTACT = CurieNamespace('INTACT', 'http://identifiers.org/intact/')
IUPHAR_FAMILY = CurieNamespace('IUPHAR_FAMILY', 'http://identifiers.org/iuphar.family/')
KEGG = CurieNamespace('KEGG', 'http://www.kegg.jp/entry/')
KEGG_BRITE = CurieNamespace('KEGG_BRITE', 'https://bioregistry.io/kegg.brite:')
KEGG_COMPOUND = CurieNamespace('KEGG_COMPOUND', 'http://identifiers.org/kegg.compound/')
KEGG_DISEASE = CurieNamespace('KEGG_DISEASE', 'http://identifiers.org/kegg.disease/')
KEGG_DRUG = CurieNamespace('KEGG_DRUG', 'http://identifiers.org/kegg.drug/')
KEGG_ENVIRON = CurieNamespace('KEGG_ENVIRON', 'http://identifiers.org/kegg.environ/')
KEGG_GENES = CurieNamespace('KEGG_GENES', 'https://bioregistry.io/kegg.genes:bsu:')
KEGG_GLYCAN = CurieNamespace('KEGG_GLYCAN', 'http://identifiers.org/kegg.glycan/')
KEGG_MODULE = CurieNamespace('KEGG_MODULE', 'http://identifiers.org/kegg.module/')
KEGG_ORTHOLOGY = CurieNamespace('KEGG_ORTHOLOGY', 'http://identifiers.org/kegg.orthology/')
KEGG_PATHWAY = CurieNamespace('KEGG_PATHWAY', 'https://bioregistry.io/kegg.pathway:')
KEGG_RCLASS = CurieNamespace('KEGG_RCLASS', 'https://www.genome.jp/dbget-bin/www_bget?rc:')
KEGG_REACTION = CurieNamespace('KEGG_REACTION', 'http://identifiers.org/kegg.reaction/')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
MA = CurieNamespace('MA', 'http://purl.obolibrary.org/obo/MA_')
MAXO = CurieNamespace('MAXO', 'http://purl.obolibrary.org/obo/MAXO_')
MEDDRA = CurieNamespace('MEDDRA', 'http://identifiers.org/meddra/')
MESH = CurieNamespace('MESH', 'http://id.nlm.nih.gov/mesh/')
METANETX_REACTION = CurieNamespace('METANETX_REACTION', 'https://www.metanetx.org/equa_info/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
MI = CurieNamespace('MI', 'http://purl.obolibrary.org/obo/MI_')
MIR = CurieNamespace('MIR', 'http://identifiers.org/mir/')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
MP = CurieNamespace('MP', 'http://purl.obolibrary.org/obo/MP_')
MPATH = CurieNamespace('MPATH', 'http://purl.obolibrary.org/obo/MPATH_')
MSIGDB = CurieNamespace('MSigDB', 'https://www.gsea-msigdb.org/gsea/msigdb/')
MMUSDV = CurieNamespace('MmusDv', 'http://purl.obolibrary.org/obo/MMUSDV_')
NBO = CurieNamespace('NBO', 'http://purl.obolibrary.org/obo/NBO_')
NBO_PROPERTY = CurieNamespace('NBO-PROPERTY', 'http://purl.obolibrary.org/obo/nbo#')
NCBIGENE = CurieNamespace('NCBIGene', 'http://identifiers.org/ncbigene/')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
NCIT_OBO = CurieNamespace('NCIT-OBO', 'http://purl.obolibrary.org/obo/ncit#')
NDC = CurieNamespace('NDC', 'http://identifiers.org/ndc/')
NDDF = CurieNamespace('NDDF', 'http://purl.bioontology.org/ontology/NDDF/')
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
OBAN = CurieNamespace('OBAN', 'http://purl.org/oban/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
OGMS = CurieNamespace('OGMS', 'http://purl.obolibrary.org/obo/OGMS_')
OMIM = CurieNamespace('OMIM', 'http://purl.obolibrary.org/obo/OMIM_')
OMIM_PS = CurieNamespace('OMIM_PS', 'https://www.omim.org/phenotypicSeries/')
OMIT = CurieNamespace('OMIT', 'http://purl.obolibrary.org/obo/OMIT_')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PANTHER_FAMILY = CurieNamespace('PANTHER_FAMILY', 'http://www.pantherdb.org/panther/family.do?clsAccession=')
PANTHER_PATHWAY = CurieNamespace('PANTHER_PATHWAY', 'http://identifiers.org/panther.pathway/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PCO = CurieNamespace('PCO', 'http://purl.obolibrary.org/obo/PCO_')
PFAM = CurieNamespace('PFAM', 'http://identifiers.org/pfam/')
PHARMGKB_DISEASE = CurieNamespace('PHARMGKB_DISEASE', 'https://www.pharmgkb.org/disease/')
PHARMGKB_DRUG = CurieNamespace('PHARMGKB_DRUG', 'https://www.pharmgkb.org/chemical/')
PHARMGKB_GENE = CurieNamespace('PHARMGKB_GENE', 'https://www.pharmgkb.org/gene/')
PHARMGKB_PATHWAYS = CurieNamespace('PHARMGKB_PATHWAYS', 'https://www.pharmgkb.org/pathway/')
PHARMGKB_VARIANT = CurieNamespace('PHARMGKB_VARIANT', 'https://www.pharmgkb.org/variant/')
PHAROS = CurieNamespace('PHAROS', 'http://pharos.nih.gov')
PIRSF = CurieNamespace('PIRSF', 'http://identifiers.org/pirsf/')
PMC = CurieNamespace('PMC', 'http://europepmc.org/articles/PMC')
PMCID = CurieNamespace('PMCID', 'http://www.ncbi.nlm.nih.gov/pmc/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PRINTS = CurieNamespace('PRINTS', 'http://identifiers.org/prints/')
PRODOM = CurieNamespace('PRODOM', 'http://identifiers.org/prodom/')
PROSITE = CurieNamespace('PROSITE', 'http://identifiers.org/prosite/')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
PUBCHEM_SUBSTANCE = CurieNamespace('PUBCHEM_SUBSTANCE', 'http://identifiers.org/pubchem.substance/')
PW = CurieNamespace('PW', 'http://purl.obolibrary.org/obo/PW_')
PATHWHIZ = CurieNamespace('PathWhiz', 'http://smpdb.ca/pathways/#')
POMBASE = CurieNamespace('PomBase', 'https://www.pombase.org/gene/')
REACT = CurieNamespace('REACT', 'http://www.reactome.org/PathwayBrowser/#/')
REPODB = CurieNamespace('REPODB', 'http://apps.chiragjpgroup.org/repoDB/')
RFAM = CurieNamespace('RFAM', 'http://identifiers.org/rfam/')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
RHEA = CurieNamespace('RHEA', 'http://identifiers.org/rhea/')
RNACENTRAL = CurieNamespace('RNACENTRAL', 'http://identifiers.org/rnacentral/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RXCUI = CurieNamespace('RXCUI', 'https://mor.nlm.nih.gov/RxNav/search?searchBy=RXCUI&searchTerm=')
RXNORM = CurieNamespace('RXNORM', 'http://purl.bioontology.org/ontology/RXNORM/')
RESEARCHID = CurieNamespace('ResearchID', 'https://publons.com/researcher/')
SEED_REACTION = CurieNamespace('SEED_REACTION', 'https://modelseed.org/biochem/reactions/')
SEMMEDDB = CurieNamespace('SEMMEDDB', 'https://skr3.nlm.nih.gov/SemMedDB')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
SIDER_DRUG = CurieNamespace('SIDER_DRUG', 'http://identifiers.org/sider.drug/')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SMART = CurieNamespace('SMART', 'http://identifiers.org/smart/')
SMPDB = CurieNamespace('SMPDB', 'http://identifiers.org/smpdb/')
SNOMED = CurieNamespace('SNOMED', 'http://purl.obolibrary.org/obo/SNOMED_')
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://snomed.info/id/')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
SPDI = CurieNamespace('SPDI', 'https://api.ncbi.nlm.nih.gov/variation/v0/spdi/')
STATO = CurieNamespace('STATO', 'http://purl.obolibrary.org/obo/STATO_')
STY = CurieNamespace('STY', 'http://purl.bioontology.org/ontology/STY/')
SUPFAM = CurieNamespace('SUPFAM', 'http://identifiers.org/supfam/')
SCOPUSID = CurieNamespace('ScopusID', 'https://www.scopus.com/authid/detail.uri?authorId=')
TAXRANK = CurieNamespace('TAXRANK', 'http://purl.obolibrary.org/obo/TAXRANK_')
TCDB = CurieNamespace('TCDB', 'http://identifiers.org/tcdb/')
TIGRFAM = CurieNamespace('TIGRFAM', 'http://identifiers.org/tigrfam/')
TO = CurieNamespace('TO', 'http://purl.obolibrary.org/obo/TO_')
UBERGRAPH = CurieNamespace('UBERGRAPH', 'http://translator.renci.org/ubergraph-axioms.ofn#')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UBERON_CORE = CurieNamespace('UBERON_CORE', 'http://purl.obolibrary.org/obo/uberon/core#')
UBERON_NONAMESPACE = CurieNamespace('UBERON_NONAMESPACE', 'http://purl.obolibrary.org/obo/core#')
UMLS = CurieNamespace('UMLS', 'http://identifiers.org/umls/')
UMLSSG = CurieNamespace('UMLSSG', 'https://lhncbc.nlm.nih.gov/semanticnetwork/download/sg_archive/SemGroups-v04.txt')
UNII = CurieNamespace('UNII', 'http://identifiers.org/unii/')
UNIPROT_ISOFORM = CurieNamespace('UNIPROT_ISOFORM', 'http://purl.uniprot.org/isoforms/')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
UO_PROPERTY = CurieNamespace('UO-PROPERTY', 'http://purl.obolibrary.org/obo/uo#')
UPHENO = CurieNamespace('UPHENO', 'http://purl.obolibrary.org/obo/UPHENO_')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://purl.uniprot.org/uniprot/')
VANDF = CurieNamespace('VANDF', 'https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/VANDF/')
VMC = CurieNamespace('VMC', 'https://github.com/ga4gh/vr-spec/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
WBPHENOTYPE = CurieNamespace('WBPhenotype', 'http://purl.obolibrary.org/obo/WBPhenotype_')
WBVOCAB = CurieNamespace('WBVocab', 'http://bio2rdf.org/wormbase_vocabulary')
WBBT = CurieNamespace('WBbt', 'http://purl.obolibrary.org/obo/WBbt_')
WBLS = CurieNamespace('WBls', 'http://purl.obolibrary.org/obo/WBls_')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/entity/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/prop/')
WIKIPATHWAYS = CurieNamespace('WIKIPATHWAYS', 'http://identifiers.org/wikipathways/')
WORMBASE = CurieNamespace('WormBase', 'https://www.wormbase.org/get?name=')
XAO = CurieNamespace('XAO', 'http://purl.obolibrary.org/obo/XAO_')
XCO = CurieNamespace('XCO', 'http://purl.obolibrary.org/obo/XCO_')
XPO = CurieNamespace('XPO', 'http://purl.obolibrary.org/obo/XPO_')
XENBASE = CurieNamespace('Xenbase', 'http://www.xenbase.org/gene/showgene.do?method=display&geneId=')
ZFA = CurieNamespace('ZFA', 'http://purl.obolibrary.org/obo/ZFA_')
ZFIN = CurieNamespace('ZFIN', 'http://identifiers.org/zfin/')
ZFS = CurieNamespace('ZFS', 'http://purl.obolibrary.org/obo/ZFS_')
ZP = CurieNamespace('ZP', 'http://purl.obolibrary.org/obo/ZP_')
APOLLO = CurieNamespace('apollo', 'https://github.com/GMOD/Apollo')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
BIOSCHEMAS = CurieNamespace('bioschemas', 'https://bioschemas.org/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DCTYPES = CurieNamespace('dctypes', 'http://purl.org/dc/dcmitype/')
DICTYBASE = CurieNamespace('dictyBase', 'http://dictybase.org/gene/')
DOI = CurieNamespace('doi', 'https://doi.org/')
FABIO = CurieNamespace('fabio', 'http://purl.org/spar/fabio/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
FOODB_COMPOUND = CurieNamespace('foodb_compound', 'http://foodb.ca/compounds/')
FOODB_FOOD = CurieNamespace('foodb_food', 'http://foodb.ca/foods/')
GFF3 = CurieNamespace('gff3', 'https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md#')
GPI = CurieNamespace('gpi', 'https://github.com/geneontology/go-annotation/blob/master/specs/gpad-gpi-2-0.md#')
GTPO = CurieNamespace('gtpo', 'https://rdf.guidetopharmacology.org/ns/gtpo#')
ICD11 = CurieNamespace('icd11', 'http://id.who.int/icd/entity/')
ICD11_FOUNDATION = CurieNamespace('icd11_foundation', 'http://id.who.int/icd/entity/')
INTERPRO = CurieNamespace('interpro', 'https://www.ebi.ac.uk/interpro/entry/')
ISBN = CurieNamespace('isbn', 'https://www.isbn-international.org/identifier/')
ISNI = CurieNamespace('isni', 'https://isni.org/isni/')
ISSN = CurieNamespace('issn', 'https://portal.issn.org/resource/ISSN/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MEDGEN = CurieNamespace('medgen', 'https://www.ncbi.nlm.nih.gov/medgen/')
METACYC_REACTION = CurieNamespace('metacyc_reaction', 'http://identifiers.org/metacyc.reaction:')
MIRBASE = CurieNamespace('mirbase', 'http://identifiers.org/mirbase')
MMMP_BIOMAPS = CurieNamespace('mmmp_biomaps', 'https://bioregistry.io/mmmp.biomaps:')
NCATS_BIOPLANET = CurieNamespace('ncats_bioplanet', 'https://tripod.nih.gov/bioplanet/detail.jsp?pid=')
NCATS_DRUG = CurieNamespace('ncats_drug', 'https://drugs.ncats.io/drug/')
OBOINOWL = CurieNamespace('oboInOwl', 'http://www.geneontology.org/formats/oboInOwl#')
ORPHANET = CurieNamespace('orphanet', 'http://www.orpha.net/ORDO/Orphanet_')
OS = CurieNamespace('os', 'https://github.com/cmungall/owlstar/blob/master/owlstar.ttl')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
REGULATES = CurieNamespace('regulates', 'http://example.org/UNKNOWN/regulates/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BIOLINK


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "chemical formula value"
    type_model_uri = BIOLINK.ChemicalFormulaValue


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "iri type"
    type_model_uri = BIOLINK.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = BIOLINK.LabelType


class PredicateType(Uriorcurie):
    """ A CURIE from the biolink related_to hierarchy. For example, biolink:related_to, biolink:causes, biolink:treats. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "predicate type"
    type_model_uri = BIOLINK.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = BIOLINK.NarrativeText


class SymbolType(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = BIOLINK.SymbolType


class FrequencyValue(String):
    type_class_uri = UO["0000105"]
    type_class_curie = "UO:0000105"
    type_name = "frequency value"
    type_model_uri = BIOLINK.FrequencyValue


class PercentageFrequencyValue(Double):
    type_class_uri = UO["0000187"]
    type_class_curie = "UO:0000187"
    type_name = "percentage frequency value"
    type_model_uri = BIOLINK.PercentageFrequencyValue


class Quotient(Double):
    type_class_uri = UO["0010006"]
    type_class_curie = "UO:0010006"
    type_name = "quotient"
    type_model_uri = BIOLINK.Quotient


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = BIOLINK.Unit


class TimeType(Time):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "time type"
    type_model_uri = BIOLINK.TimeType


class BiologicalSequence(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "biological sequence"
    type_model_uri = BIOLINK.BiologicalSequence


# Class references
class OntologyClassId(extended_str):
    pass


class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class AttributeId(NamedThingId):
    pass


class ChemicalRoleId(AttributeId):
    pass


class BiologicalSexId(AttributeId):
    pass


class PhenotypicSexId(BiologicalSexId):
    pass


class GenotypicSexId(BiologicalSexId):
    pass


class SeverityValueId(AttributeId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class TaxonomicRankId(OntologyClassId):
    pass


class OrganismTaxonId(NamedThingId):
    pass


class EventId(NamedThingId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class AgentId(AdministrativeEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class StudyResultId(InformationContentEntityId):
    pass


class StudyVariableId(InformationContentEntityId):
    pass


class CommonDataElementId(InformationContentEntityId):
    pass


class ConceptCountAnalysisResultId(StudyResultId):
    pass


class ObservedExpectedFrequencyAnalysisResultId(StudyResultId):
    pass


class RelativeFrequencyAnalysisResultId(StudyResultId):
    pass


class TextMiningResultId(StudyResultId):
    pass


class ChiSquaredAnalysisResultId(StudyResultId):
    pass


class LogOddsAnalysisResultId(StudyResultId):
    pass


class DatasetId(InformationContentEntityId):
    pass


class DatasetDistributionId(InformationContentEntityId):
    pass


class DatasetVersionId(InformationContentEntityId):
    pass


class DatasetSummaryId(InformationContentEntityId):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class BookId(PublicationId):
    pass


class BookChapterId(PublicationId):
    pass


class SerialId(PublicationId):
    pass


class ArticleId(PublicationId):
    pass


class JournalArticleId(ArticleId):
    pass


class PatentId(PublicationId):
    pass


class WebPageId(PublicationId):
    pass


class PreprintPublicationId(PublicationId):
    pass


class DrugLabelId(PublicationId):
    pass


class RetrievalSourceId(InformationContentEntityId):
    pass


class PhysicalEntityId(NamedThingId):
    pass


class ActivityId(NamedThingId):
    pass


class StudyId(ActivityId):
    pass


class ProcedureId(NamedThingId):
    pass


class PhenomenonId(NamedThingId):
    pass


class DeviceId(NamedThingId):
    pass


class DiagnosticAidId(NamedThingId):
    pass


class MaterialSampleId(PhysicalEntityId):
    pass


class PlanetaryEntityId(NamedThingId):
    pass


class EnvironmentalProcessId(PlanetaryEntityId):
    pass


class EnvironmentalFeatureId(PlanetaryEntityId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class BiologicalEntityId(NamedThingId):
    pass


class ChemicalEntityId(NamedThingId):
    pass


class MolecularEntityId(ChemicalEntityId):
    pass


class SmallMoleculeId(MolecularEntityId):
    pass


class ChemicalMixtureId(ChemicalEntityId):
    pass


class NucleicAcidEntityId(MolecularEntityId):
    pass


class RegulatoryRegionId(BiologicalEntityId):
    pass


class AccessibleDnaRegionId(RegulatoryRegionId):
    pass


class TranscriptionFactorBindingSiteId(RegulatoryRegionId):
    pass


class MolecularMixtureId(ChemicalMixtureId):
    pass


class ComplexMolecularMixtureId(ChemicalMixtureId):
    pass


class BiologicalProcessOrActivityId(BiologicalEntityId):
    pass


class MolecularActivityId(BiologicalProcessOrActivityId):
    pass


class BiologicalProcessId(BiologicalProcessOrActivityId):
    pass


class PathwayId(BiologicalProcessId):
    pass


class PhysiologicalProcessId(BiologicalProcessId):
    pass


class BehaviorId(BiologicalProcessId):
    pass


class ProcessedMaterialId(ChemicalMixtureId):
    pass


class DrugId(MolecularMixtureId):
    pass


class EnvironmentalFoodContaminantId(ChemicalEntityId):
    pass


class FoodAdditiveId(ChemicalEntityId):
    pass


class FoodId(ChemicalMixtureId):
    pass


class OrganismAttributeId(AttributeId):
    pass


class PhenotypicQualityId(OrganismAttributeId):
    pass


class GeneticInheritanceId(BiologicalEntityId):
    pass


class OrganismalEntityId(BiologicalEntityId):
    pass


class BacteriumId(OrganismalEntityId):
    pass


class VirusId(OrganismalEntityId):
    pass


class CellularOrganismId(OrganismalEntityId):
    pass


class MammalId(CellularOrganismId):
    pass


class HumanId(MammalId):
    pass


class PlantId(CellularOrganismId):
    pass


class InvertebrateId(CellularOrganismId):
    pass


class VertebrateId(CellularOrganismId):
    pass


class FungusId(CellularOrganismId):
    pass


class LifeStageId(OrganismalEntityId):
    pass


class IndividualOrganismId(OrganismalEntityId):
    pass


class PopulationOfIndividualOrganismsId(OrganismalEntityId):
    pass


class StudyPopulationId(PopulationOfIndividualOrganismsId):
    pass


class DiseaseOrPhenotypicFeatureId(BiologicalEntityId):
    pass


class DiseaseId(DiseaseOrPhenotypicFeatureId):
    pass


class PhenotypicFeatureId(DiseaseOrPhenotypicFeatureId):
    pass


class BehavioralFeatureId(PhenotypicFeatureId):
    pass


class AnatomicalEntityId(OrganismalEntityId):
    pass


class CellularComponentId(AnatomicalEntityId):
    pass


class CellId(AnatomicalEntityId):
    pass


class CellLineId(OrganismalEntityId):
    pass


class GrossAnatomicalStructureId(AnatomicalEntityId):
    pass


class GeneId(BiologicalEntityId):
    pass


class MacromolecularComplexId(BiologicalEntityId):
    pass


class NucleosomeModificationId(BiologicalEntityId):
    pass


class GenomeId(BiologicalEntityId):
    pass


class ExonId(BiologicalEntityId):
    pass


class TranscriptId(BiologicalEntityId):
    pass


class CodingSequenceId(BiologicalEntityId):
    pass


class PolypeptideId(BiologicalEntityId):
    pass


class ProteinId(PolypeptideId):
    pass


class ProteinIsoformId(ProteinId):
    pass


class ProteinDomainId(BiologicalEntityId):
    pass


class PosttranslationalModificationId(BiologicalEntityId):
    pass


class ProteinFamilyId(BiologicalEntityId):
    pass


class NucleicAcidSequenceMotifId(BiologicalEntityId):
    pass


class RNAProductId(TranscriptId):
    pass


class RNAProductIsoformId(RNAProductId):
    pass


class NoncodingRNAProductId(RNAProductId):
    pass


class MicroRNAId(NoncodingRNAProductId):
    pass


class SiRNAId(NoncodingRNAProductId):
    pass


class GeneFamilyId(BiologicalEntityId):
    pass


class ZygosityId(AttributeId):
    pass


class GenotypeId(BiologicalEntityId):
    pass


class HaplotypeId(BiologicalEntityId):
    pass


class SequenceVariantId(BiologicalEntityId):
    pass


class SnvId(SequenceVariantId):
    pass


class ReagentTargetedGeneId(BiologicalEntityId):
    pass


class ClinicalAttributeId(AttributeId):
    pass


class ClinicalMeasurementId(ClinicalAttributeId):
    pass


class ClinicalModifierId(ClinicalAttributeId):
    pass


class ClinicalCourseId(ClinicalAttributeId):
    pass


class OnsetId(ClinicalCourseId):
    pass


class ClinicalEntityId(NamedThingId):
    pass


class ClinicalTrialId(StudyId):
    pass


class ClinicalInterventionId(ClinicalEntityId):
    pass


class ClinicalFindingId(PhenotypicFeatureId):
    pass


class HospitalizationId(ClinicalInterventionId):
    pass


class SocioeconomicAttributeId(AttributeId):
    pass


class CaseId(IndividualOrganismId):
    pass


class CohortId(StudyPopulationId):
    pass


class ExposureEventId(OntologyClassId):
    pass


class GenomicBackgroundExposureId(AttributeId):
    pass


class PathologicalProcessId(BiologicalProcessId):
    pass


class PathologicalProcessExposureId(AttributeId):
    pass


class PathologicalAnatomicalStructureId(AnatomicalEntityId):
    pass


class PathologicalAnatomicalExposureId(AttributeId):
    pass


class DiseaseOrPhenotypicFeatureExposureId(AttributeId):
    pass


class ChemicalExposureId(AttributeId):
    pass


class ComplexChemicalExposureId(AttributeId):
    pass


class DrugExposureId(ChemicalExposureId):
    pass


class DrugToGeneInteractionExposureId(DrugExposureId):
    pass


class TreatmentId(NamedThingId):
    pass


class BioticExposureId(AttributeId):
    pass


class EnvironmentalExposureId(AttributeId):
    pass


class GeographicExposureId(EnvironmentalExposureId):
    pass


class BehavioralExposureId(AttributeId):
    pass


class SocioeconomicExposureId(AttributeId):
    pass


class AssociationId(EntityId):
    pass


class DiseaseAssociatedWithResponseToChemicalEntityAssociationId(AssociationId):
    pass


class ChemicalEntityAssessesNamedThingAssociationId(AssociationId):
    pass


class ContributorAssociationId(AssociationId):
    pass


class GenotypeToGenotypePartAssociationId(AssociationId):
    pass


class GenotypeToGeneAssociationId(AssociationId):
    pass


class GenotypeToVariantAssociationId(AssociationId):
    pass


class GeneToGeneAssociationId(AssociationId):
    pass


class GeneToGeneHomologyAssociationId(GeneToGeneAssociationId):
    pass


class GeneToGeneFamilyAssociationId(AssociationId):
    pass


class GeneToGeneCoexpressionAssociationId(GeneToGeneAssociationId):
    pass


class PairwiseGeneToGeneInteractionId(GeneToGeneAssociationId):
    pass


class PairwiseMolecularInteractionId(PairwiseGeneToGeneInteractionId):
    pass


class CellLineToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToChemicalAssociationId(AssociationId):
    pass


class ReactionToParticipantAssociationId(ChemicalToChemicalAssociationId):
    pass


class ReactionToCatalystAssociationId(ReactionToParticipantAssociationId):
    pass


class ChemicalToChemicalDerivationAssociationId(ChemicalToChemicalAssociationId):
    pass


class ChemicalToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociationId(ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociationId):
    pass


class GeneToPathwayAssociationId(AssociationId):
    pass


class MolecularActivityToPathwayAssociationId(AssociationId):
    pass


class ChemicalToPathwayAssociationId(AssociationId):
    pass


class NamedThingAssociatedWithLikelihoodOfNamedThingAssociationId(AssociationId):
    pass


class ChemicalGeneInteractionAssociationId(AssociationId):
    pass


class GeneRegulatesGeneAssociationId(AssociationId):
    pass


class ProcessRegulatesProcessAssociationId(AssociationId):
    pass


class ChemicalAffectsGeneAssociationId(AssociationId):
    pass


class GeneAffectsChemicalAssociationId(AssociationId):
    pass


class DrugToGeneAssociationId(AssociationId):
    pass


class MaterialSampleDerivationAssociationId(AssociationId):
    pass


class MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToExposureEventAssociationId(AssociationId):
    pass


class ExposureEventToOutcomeAssociationId(AssociationId):
    pass


class PhenotypicFeatureToPhenotypicFeatureAssociationId(AssociationId):
    pass


class InformationContentEntityToNamedThingAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureToLocationAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociationId(AssociationId):
    pass


class GenotypeToPhenotypicFeatureAssociationId(AssociationId):
    pass


class ExposureEventToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class CaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class CaseToDiseaseAssociationId(AssociationId):
    pass


class CaseToVariantAssociationId(AssociationId):
    pass


class CaseToGeneAssociationId(AssociationId):
    pass


class BehaviorToBehavioralFeatureAssociationId(AssociationId):
    pass


class GeneToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToPhenotypicFeatureAssociationId(GeneToDiseaseOrPhenotypicFeatureAssociationId):
    pass


class GeneToDiseaseAssociationId(GeneToDiseaseOrPhenotypicFeatureAssociationId):
    pass


class CausalGeneToDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class CorrelatedGeneToDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class DruggableGeneToDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class PhenotypicFeatureToDiseaseAssociationId(AssociationId):
    pass


class VariantToGeneAssociationId(AssociationId):
    pass


class VariantToGeneExpressionAssociationId(VariantToGeneAssociationId):
    pass


class VariantToPopulationAssociationId(AssociationId):
    pass


class PopulationToPopulationAssociationId(AssociationId):
    pass


class VariantToPhenotypicFeatureAssociationId(AssociationId):
    pass


class VariantToDiseaseAssociationId(AssociationId):
    pass


class GenotypeToDiseaseAssociationId(AssociationId):
    pass


class GeneAsAModelOfDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class VariantAsAModelOfDiseaseAssociationId(VariantToDiseaseAssociationId):
    pass


class GenotypeAsAModelOfDiseaseAssociationId(GenotypeToDiseaseAssociationId):
    pass


class CellLineAsAModelOfDiseaseAssociationId(CellLineToDiseaseOrPhenotypicFeatureAssociationId):
    pass


class OrganismalEntityAsAModelOfDiseaseAssociationId(AssociationId):
    pass


class OrganismToOrganismAssociationId(AssociationId):
    pass


class TaxonToTaxonAssociationId(AssociationId):
    pass


class GeneHasVariantThatContributesToDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class GeneToExpressionSiteAssociationId(AssociationId):
    pass


class SequenceVariantModulatesTreatmentAssociationId(AssociationId):
    pass


class FunctionalAssociationId(AssociationId):
    pass


class MacromolecularMachineToMolecularActivityAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToBiologicalProcessAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToCellularComponentAssociationId(FunctionalAssociationId):
    pass


class MolecularActivityToChemicalEntityAssociationId(AssociationId):
    pass


class MolecularActivityToMolecularActivityAssociationId(AssociationId):
    pass


class GeneToGoTermAssociationId(FunctionalAssociationId):
    pass


class EntityToDiseaseAssociationId(AssociationId):
    pass


class EntityToPhenotypicFeatureAssociationId(AssociationId):
    pass


class SequenceAssociationId(AssociationId):
    pass


class GenomicSequenceLocalizationId(SequenceAssociationId):
    pass


class SequenceFeatureRelationshipId(AssociationId):
    pass


class TranscriptToGeneRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneToGeneProductRelationshipId(SequenceFeatureRelationshipId):
    pass


class ExonToTranscriptRelationshipId(SequenceFeatureRelationshipId):
    pass


class ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociationId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityAssociationId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityPartOfAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class OrganismTaxonToOrganismTaxonAssociationId(AssociationId):
    pass


class OrganismTaxonToOrganismTaxonSpecializationId(OrganismTaxonToOrganismTaxonAssociationId):
    pass


class OrganismTaxonToOrganismTaxonInteractionId(OrganismTaxonToOrganismTaxonAssociationId):
    pass


class OrganismTaxonToEnvironmentAssociationId(AssociationId):
    pass


@dataclass(repr=False)
class MappingCollection(YAMLRoot):
    """
    A collection of deprecated mappings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MappingCollection"]
    class_class_curie: ClassVar[str] = "biolink:MappingCollection"
    class_name: ClassVar[str] = "mapping collection"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MappingCollection

    predicate_mappings: Optional[Union[Union[dict, "PredicateMapping"], list[Union[dict, "PredicateMapping"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.predicate_mappings, list):
            self.predicate_mappings = [self.predicate_mappings] if self.predicate_mappings is not None else []
        self.predicate_mappings = [v if isinstance(v, PredicateMapping) else PredicateMapping(**as_dict(v)) for v in self.predicate_mappings]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PredicateMapping(YAMLRoot):
    """
    A deprecated predicate mapping object contains the deprecated predicate and an example of the rewiring that should
    be done to use a qualified statement in its place.
    """
    _inherited_slots: ClassVar[list[str]] = ["exact_match", "narrow_match", "broad_match"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["PredicateMapping"]
    class_class_curie: ClassVar[str] = "biolink:PredicateMapping"
    class_name: ClassVar[str] = "predicate mapping"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PredicateMapping

    predicate: Union[str, PredicateType] = None
    mapped_predicate: Optional[str] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    subject_form_or_variant_qualifier: Optional[str] = None
    subject_part_qualifier: Optional[str] = None
    subject_derivative_qualifier: Optional[str] = None
    subject_context_qualifier: Optional[str] = None
    qualified_predicate: Optional[str] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_form_or_variant_qualifier: Optional[str] = None
    object_part_qualifier: Optional[str] = None
    object_derivative_qualifier: Optional[str] = None
    object_context_qualifier: Optional[str] = None
    causal_mechanism_qualifier: Optional[Union[str, "CausalMechanismQualifierEnum"]] = None
    anatomical_context_qualifier: Optional[str] = None
    species_context_qualifier: Optional[Union[str, OrganismTaxonId]] = None
    exact_match: Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]] = empty_list()
    narrow_match: Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]] = empty_list()
    broad_match: Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.mapped_predicate is not None and not isinstance(self.mapped_predicate, str):
            self.mapped_predicate = str(self.mapped_predicate)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.subject_form_or_variant_qualifier is not None and not isinstance(self.subject_form_or_variant_qualifier, str):
            self.subject_form_or_variant_qualifier = str(self.subject_form_or_variant_qualifier)

        if self.subject_part_qualifier is not None and not isinstance(self.subject_part_qualifier, str):
            self.subject_part_qualifier = str(self.subject_part_qualifier)

        if self.subject_derivative_qualifier is not None and not isinstance(self.subject_derivative_qualifier, str):
            self.subject_derivative_qualifier = str(self.subject_derivative_qualifier)

        if self.subject_context_qualifier is not None and not isinstance(self.subject_context_qualifier, str):
            self.subject_context_qualifier = str(self.subject_context_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.object_form_or_variant_qualifier is not None and not isinstance(self.object_form_or_variant_qualifier, str):
            self.object_form_or_variant_qualifier = str(self.object_form_or_variant_qualifier)

        if self.object_part_qualifier is not None and not isinstance(self.object_part_qualifier, str):
            self.object_part_qualifier = str(self.object_part_qualifier)

        if self.object_derivative_qualifier is not None and not isinstance(self.object_derivative_qualifier, str):
            self.object_derivative_qualifier = str(self.object_derivative_qualifier)

        if self.object_context_qualifier is not None and not isinstance(self.object_context_qualifier, str):
            self.object_context_qualifier = str(self.object_context_qualifier)

        if self.causal_mechanism_qualifier is not None and not isinstance(self.causal_mechanism_qualifier, CausalMechanismQualifierEnum):
            self.causal_mechanism_qualifier = CausalMechanismQualifierEnum(self.causal_mechanism_qualifier)

        if self.anatomical_context_qualifier is not None and not isinstance(self.anatomical_context_qualifier, str):
            self.anatomical_context_qualifier = str(self.anatomical_context_qualifier)

        if self.species_context_qualifier is not None and not isinstance(self.species_context_qualifier, OrganismTaxonId):
            self.species_context_qualifier = OrganismTaxonId(self.species_context_qualifier)

        if not isinstance(self.exact_match, list):
            self.exact_match = [self.exact_match] if self.exact_match is not None else []
        self.exact_match = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.exact_match]

        if not isinstance(self.narrow_match, list):
            self.narrow_match = [self.narrow_match] if self.narrow_match is not None else []
        self.narrow_match = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.narrow_match]

        if not isinstance(self.broad_match, list):
            self.broad_match = [self.broad_match] if self.broad_match is not None else []
        self.broad_match = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.broad_match]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologyClass(YAMLRoot):
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be
    considered both instances of biolink classes, and OWL classes in their own right. In general you should not need
    to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of
    endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["OntologyClass"]
    class_class_curie: ClassVar[str] = "biolink:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OntologyClass

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


class Annotation(YAMLRoot):
    """
    Biolink Model root class for entity annotations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Annotation"]
    class_class_curie: ClassVar[str] = "biolink:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Annotation


@dataclass(repr=False)
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["QuantityValue"]
    class_class_curie: ClassVar[str] = "biolink:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = BIOLINK.QuantityValue

    has_unit: Optional[Union[str, Unit]] = None
    has_numeric_value: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_unit is not None and not isinstance(self.has_unit, Unit):
            self.has_unit = Unit(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        super().__post_init__(**kwargs)


class RelationshipQuantifier(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["RelationshipQuantifier"]
    class_class_curie: ClassVar[str] = "biolink:RelationshipQuantifier"
    class_name: ClassVar[str] = "relationship quantifier"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RelationshipQuantifier


class SensitivityQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SensitivityQuantifier"]
    class_class_curie: ClassVar[str] = "biolink:SensitivityQuantifier"
    class_name: ClassVar[str] = "sensitivity quantifier"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SensitivityQuantifier


class SpecificityQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SpecificityQuantifier"]
    class_class_curie: ClassVar[str] = "biolink:SpecificityQuantifier"
    class_name: ClassVar[str] = "specificity quantifier"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SpecificityQuantifier


class PathognomonicityQuantifier(SpecificityQuantifier):
    """
    A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the
    feature implies the existence of the disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PathognomonicityQuantifier"]
    class_class_curie: ClassVar[str] = "biolink:PathognomonicityQuantifier"
    class_name: ClassVar[str] = "pathognomonicity quantifier"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PathognomonicityQuantifier


@dataclass(repr=False)
class FrequencyQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["FrequencyQuantifier"]
    class_class_curie: ClassVar[str] = "biolink:FrequencyQuantifier"
    class_name: ClassVar[str] = "frequency quantifier"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FrequencyQuantifier

    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None
    has_percentage: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        super().__post_init__(**kwargs)


class ChemicalOrDrugOrTreatment(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalOrDrugOrTreatment"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalOrDrugOrTreatment"
    class_name: ClassVar[str] = "chemical or drug or treatment"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalOrDrugOrTreatment


@dataclass(repr=False)
class Entity(YAMLRoot):
    """
    Root Biolink Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Entity"]
    class_class_curie: ClassVar[str] = "biolink:Entity"
    class_name: ClassVar[str] = "entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Entity

    id: Union[str, EntityId] = None
    iri: Optional[Union[str, IriType]] = None
    category: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    type: Optional[Union[str, list[str]]] = empty_list()
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    has_attribute: Optional[Union[Union[str, AttributeId], list[Union[str, AttributeId]]]] = empty_list()
    deprecated: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]

        if not isinstance(self.type, list):
            self.type = [self.type] if self.type is not None else []
        self.type = [v if isinstance(v, str) else str(v) for v in self.type]

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, AttributeId) else AttributeId(v) for v in self.has_attribute]

        if self.deprecated is not None and not isinstance(self.deprecated, Bool):
            self.deprecated = Bool(self.deprecated)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "category"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["NamedThing"]
    class_class_curie: ClassVar[str] = "biolink:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NamedThing

    id: Union[str, NamedThingId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    provided_by: Optional[Union[str, list[str]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    synonym: Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]

        if not isinstance(self.provided_by, list):
            self.provided_by = [self.provided_by] if self.provided_by is not None else []
        self.provided_by = [v if isinstance(v, str) else str(v) for v in self.provided_by]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if self.full_name is not None and not isinstance(self.full_name, LabelType):
            self.full_name = LabelType(self.full_name)

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


    def __new__(cls, *args, **kwargs):

        type_designator = "category"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class Attribute(NamedThing):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Attribute"]
    class_class_curie: ClassVar[str] = "biolink:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Attribute

    id: Union[str, AttributeId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    name: Optional[Union[str, LabelType]] = None
    has_quantitative_value: Optional[Union[Union[dict, QuantityValue], list[Union[dict, QuantityValue]]]] = empty_list()
    has_qualitative_value: Optional[Union[str, NamedThingId]] = None
    iri: Optional[Union[str, IriType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)

        if self._is_empty(self.has_attribute_type):
            self.MissingRequiredField("has_attribute_type")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.has_quantitative_value, list):
            self.has_quantitative_value = [self.has_quantitative_value] if self.has_quantitative_value is not None else []
        self.has_quantitative_value = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.has_quantitative_value]

        if self.has_qualitative_value is not None and not isinstance(self.has_qualitative_value, NamedThingId):
            self.has_qualitative_value = NamedThingId(self.has_qualitative_value)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalRole(Attribute):
    """
    A role played by the molecular entity or part thereof within a chemical context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalRole"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalRole"
    class_name: ClassVar[str] = "chemical role"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalRole

    id: Union[str, ChemicalRoleId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalRoleId):
            self.id = ChemicalRoleId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class BiologicalSex(Attribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["BiologicalSex"]
    class_class_curie: ClassVar[str] = "biolink:BiologicalSex"
    class_name: ClassVar[str] = "biological sex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalSex

    id: Union[str, BiologicalSexId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhenotypicSex"]
    class_class_curie: ClassVar[str] = "biolink:PhenotypicSex"
    class_name: ClassVar[str] = "phenotypic sex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicSex

    id: Union[str, PhenotypicSexId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypicSexId):
            self.id = PhenotypicSexId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex
    chromosomes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenotypicSex"]
    class_class_curie: ClassVar[str] = "biolink:GenotypicSex"
    class_name: ClassVar[str] = "genotypic sex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypicSex

    id: Union[str, GenotypicSexId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenotypicSexId):
            self.id = GenotypicSexId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SeverityValue"]
    class_class_curie: ClassVar[str] = "biolink:SeverityValue"
    class_name: ClassVar[str] = "severity value"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SeverityValue

    id: Union[str, SeverityValueId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SeverityValueId):
            self.id = SeverityValueId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["RelationshipType"]
    class_class_curie: ClassVar[str] = "biolink:RelationshipType"
    class_name: ClassVar[str] = "relationship type"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RelationshipType

    id: Union[str, RelationshipTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["TaxonomicRank"]
    class_class_curie: ClassVar[str] = "biolink:TaxonomicRank"
    class_name: ClassVar[str] = "taxonomic rank"
    class_model_uri: ClassVar[URIRef] = BIOLINK.TaxonomicRank

    id: Union[str, TaxonomicRankId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TaxonomicRankId):
            self.id = TaxonomicRankId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganismTaxon(NamedThing):
    """
    A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria).
    Can also be used to represent strains or subspecies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["OrganismTaxon"]
    class_class_curie: ClassVar[str] = "biolink:OrganismTaxon"
    class_name: ClassVar[str] = "organism taxon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxon

    id: Union[str, OrganismTaxonId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_taxonomic_rank: Optional[Union[str, TaxonomicRankId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)

        if self.has_taxonomic_rank is not None and not isinstance(self.has_taxonomic_rank, TaxonomicRankId):
            self.has_taxonomic_rank = TaxonomicRankId(self.has_taxonomic_rank)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Event(NamedThing):
    """
    Something that happens at a given place and time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Event"]
    class_class_curie: ClassVar[str] = "biolink:Event"
    class_name: ClassVar[str] = "event"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Event

    id: Union[str, EventId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["AdministrativeEntity"]
    class_class_curie: ClassVar[str] = "biolink:AdministrativeEntity"
    class_name: ClassVar[str] = "administrative entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Agent(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Agent"]
    class_class_curie: ClassVar[str] = "biolink:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Agent

    id: Union[str, AgentId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    affiliation: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    address: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation] if self.affiliation is not None else []
        self.affiliation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.affiliation]

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["InformationContentEntity"]
    class_class_curie: ClassVar[str] = "biolink:InformationContentEntity"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    license: Optional[str] = None
    rights: Optional[str] = None
    format: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class StudyResult(InformationContentEntity):
    """
    A collection of data items from a study that are about a particular study subject or experimental unit (the
    'focus' of the Result) - optionally with context/provenance metadata that may be relevant to the interpretation of
    this data as evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["StudyResult"]
    class_class_curie: ClassVar[str] = "biolink:StudyResult"
    class_name: ClassVar[str] = "study result"
    class_model_uri: ClassVar[URIRef] = BIOLINK.StudyResult

    id: Union[str, StudyResultId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class StudyVariable(InformationContentEntity):
    """
    a variable that is used as a measure in the investigation of a study
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["StudyVariable"]
    class_class_curie: ClassVar[str] = "biolink:StudyVariable"
    class_name: ClassVar[str] = "study variable"
    class_model_uri: ClassVar[URIRef] = BIOLINK.StudyVariable

    id: Union[str, StudyVariableId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyVariableId):
            self.id = StudyVariableId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CommonDataElement(InformationContentEntity):
    """
    A Common Data Element (CDE) is a standardized, precisely defined question, paired with a set of allowable
    responses, used systematically across different sites, studies, or clinical trials to ensure consistent data
    collection. Multiple CDEs (from one or more Collections) can be curated into Forms. (https://cde.nlm.nih.gov/home)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CommonDataElement"]
    class_class_curie: ClassVar[str] = "biolink:CommonDataElement"
    class_name: ClassVar[str] = "common data element"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CommonDataElement

    id: Union[str, CommonDataElementId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommonDataElementId):
            self.id = CommonDataElementId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ConceptCountAnalysisResult(StudyResult):
    """
    A result of a concept count analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ConceptCountAnalysisResult"]
    class_class_curie: ClassVar[str] = "biolink:ConceptCountAnalysisResult"
    class_name: ClassVar[str] = "concept count analysis result"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ConceptCountAnalysisResult

    id: Union[str, ConceptCountAnalysisResultId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConceptCountAnalysisResultId):
            self.id = ConceptCountAnalysisResultId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ObservedExpectedFrequencyAnalysisResult(StudyResult):
    """
    A result of a observed expected frequency analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ObservedExpectedFrequencyAnalysisResult"]
    class_class_curie: ClassVar[str] = "biolink:ObservedExpectedFrequencyAnalysisResult"
    class_name: ClassVar[str] = "observed expected frequency analysis result"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ObservedExpectedFrequencyAnalysisResult

    id: Union[str, ObservedExpectedFrequencyAnalysisResultId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservedExpectedFrequencyAnalysisResultId):
            self.id = ObservedExpectedFrequencyAnalysisResultId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class RelativeFrequencyAnalysisResult(StudyResult):
    """
    A result of a relative frequency analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["RelativeFrequencyAnalysisResult"]
    class_class_curie: ClassVar[str] = "biolink:RelativeFrequencyAnalysisResult"
    class_name: ClassVar[str] = "relative frequency analysis result"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RelativeFrequencyAnalysisResult

    id: Union[str, RelativeFrequencyAnalysisResultId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelativeFrequencyAnalysisResultId):
            self.id = RelativeFrequencyAnalysisResultId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class TextMiningResult(StudyResult):
    """
    A result of text mining.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["TextMiningResult"]
    class_class_curie: ClassVar[str] = "biolink:TextMiningResult"
    class_name: ClassVar[str] = "text mining result"
    class_model_uri: ClassVar[URIRef] = BIOLINK.TextMiningResult

    id: Union[str, TextMiningResultId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TextMiningResultId):
            self.id = TextMiningResultId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChiSquaredAnalysisResult(StudyResult):
    """
    A result of a chi squared analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChiSquaredAnalysisResult"]
    class_class_curie: ClassVar[str] = "biolink:ChiSquaredAnalysisResult"
    class_name: ClassVar[str] = "chi squared analysis result"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChiSquaredAnalysisResult

    id: Union[str, ChiSquaredAnalysisResultId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChiSquaredAnalysisResultId):
            self.id = ChiSquaredAnalysisResultId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class LogOddsAnalysisResult(StudyResult):
    """
    A result of a log odds ratio analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["LogOddsAnalysisResult"]
    class_class_curie: ClassVar[str] = "biolink:LogOddsAnalysisResult"
    class_name: ClassVar[str] = "log odds analysis result"
    class_model_uri: ClassVar[URIRef] = BIOLINK.LogOddsAnalysisResult

    id: Union[str, LogOddsAnalysisResultId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LogOddsAnalysisResultId):
            self.id = LogOddsAnalysisResultId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Dataset"]
    class_class_curie: ClassVar[str] = "biolink:Dataset"
    class_name: ClassVar[str] = "dataset"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Dataset

    id: Union[str, DatasetId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DatasetDistribution(InformationContentEntity):
    """
    an item that holds distribution level information about a dataset.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DatasetDistribution"]
    class_class_curie: ClassVar[str] = "biolink:DatasetDistribution"
    class_name: ClassVar[str] = "dataset distribution"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DatasetDistribution

    id: Union[str, DatasetDistributionId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    distribution_download_url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetDistributionId):
            self.id = DatasetDistributionId(self.id)

        if self.distribution_download_url is not None and not isinstance(self.distribution_download_url, str):
            self.distribution_download_url = str(self.distribution_download_url)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DatasetVersion(InformationContentEntity):
    """
    an item that holds version level information about a dataset.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DatasetVersion"]
    class_class_curie: ClassVar[str] = "biolink:DatasetVersion"
    class_name: ClassVar[str] = "dataset version"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DatasetVersion

    id: Union[str, DatasetVersionId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_dataset: Optional[Union[str, DatasetId]] = None
    ingest_date: Optional[str] = None
    has_distribution: Optional[Union[str, DatasetDistributionId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetVersionId):
            self.id = DatasetVersionId(self.id)

        if self.has_dataset is not None and not isinstance(self.has_dataset, DatasetId):
            self.has_dataset = DatasetId(self.has_dataset)

        if self.ingest_date is not None and not isinstance(self.ingest_date, str):
            self.ingest_date = str(self.ingest_date)

        if self.has_distribution is not None and not isinstance(self.has_distribution, DatasetDistributionId):
            self.has_distribution = DatasetDistributionId(self.has_distribution)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DatasetSummary(InformationContentEntity):
    """
    an item that holds summary level information about a dataset.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DatasetSummary"]
    class_class_curie: ClassVar[str] = "biolink:DatasetSummary"
    class_name: ClassVar[str] = "dataset summary"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DatasetSummary

    id: Union[str, DatasetSummaryId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    source_web_page: Optional[str] = None
    source_logo: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetSummaryId):
            self.id = DatasetSummaryId(self.id)

        if self.source_web_page is not None and not isinstance(self.source_web_page, str):
            self.source_web_page = str(self.source_web_page)

        if self.source_logo is not None and not isinstance(self.source_logo, str):
            self.source_logo = str(self.source_logo)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ConfidenceLevel"]
    class_class_curie: ClassVar[str] = "biolink:ConfidenceLevel"
    class_name: ClassVar[str] = "confidence level"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ConfidenceLevel

    id: Union[str, ConfidenceLevelId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EvidenceType"]
    class_class_curie: ClassVar[str] = "biolink:EvidenceType"
    class_name: ClassVar[str] = "evidence type"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EvidenceType

    id: Union[str, EvidenceTypeId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Publication(InformationContentEntity):
    """
    Any ‘published’ piece of information. Publications are considered broadly to include any document or document part
    made available in print or on the web - which may include scientific journal issues, individual articles, and
    books - as well as things like pre-prints, white papers, patents, drug labels, web pages, protocol documents, and
    even a part of a publication if of significant knowledge scope (e.g. a figure, figure legend, or section
    highlighted by NLP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Publication"]
    class_class_curie: ClassVar[str] = "biolink:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Publication

    id: Union[str, PublicationId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    publication_type: Union[str, list[str]] = None
    authors: Optional[Union[Union[str, AgentId], list[Union[str, AgentId]]]] = empty_list()
    pages: Optional[Union[str, list[str]]] = empty_list()
    summary: Optional[str] = None
    keywords: Optional[Union[str, list[str]]] = empty_list()
    mesh_terms: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self._is_empty(self.publication_type):
            self.MissingRequiredField("publication_type")
        if not isinstance(self.publication_type, list):
            self.publication_type = [self.publication_type] if self.publication_type is not None else []
        self.publication_type = [v if isinstance(v, str) else str(v) for v in self.publication_type]

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, AgentId) else AgentId(v) for v in self.authors]

        if not isinstance(self.pages, list):
            self.pages = [self.pages] if self.pages is not None else []
        self.pages = [v if isinstance(v, str) else str(v) for v in self.pages]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if not isinstance(self.mesh_terms, list):
            self.mesh_terms = [self.mesh_terms] if self.mesh_terms is not None else []
        self.mesh_terms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.mesh_terms]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Book(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Book"]
    class_class_curie: ClassVar[str] = "biolink:Book"
    class_name: ClassVar[str] = "book"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Book

    id: Union[str, BookId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    publication_type: Union[str, list[str]] = None
    type: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookId):
            self.id = BookId(self.id)

        if not isinstance(self.type, list):
            self.type = [self.type] if self.type is not None else []
        self.type = [v if isinstance(v, str) else str(v) for v in self.type]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class BookChapter(Publication):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["BookChapter"]
    class_class_curie: ClassVar[str] = "biolink:BookChapter"
    class_name: ClassVar[str] = "book chapter"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BookChapter

    id: Union[str, BookChapterId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    publication_type: Union[str, list[str]] = None
    published_in: Union[str, URIorCURIE] = None
    volume: Optional[str] = None
    chapter: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookChapterId):
            self.id = BookChapterId(self.id)

        if self._is_empty(self.published_in):
            self.MissingRequiredField("published_in")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.chapter is not None and not isinstance(self.chapter, str):
            self.chapter = str(self.chapter)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Serial(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Serial"]
    class_class_curie: ClassVar[str] = "biolink:Serial"
    class_name: ClassVar[str] = "serial"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Serial

    id: Union[str, SerialId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    publication_type: Union[str, list[str]] = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    type: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SerialId):
            self.id = SerialId(self.id)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if not isinstance(self.type, list):
            self.type = [self.type] if self.type is not None else []
        self.type = [v if isinstance(v, str) else str(v) for v in self.type]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Article(Publication):
    """
    a piece of writing on a particular topic presented as a stand-alone section of a larger publication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Article"]
    class_class_curie: ClassVar[str] = "biolink:Article"
    class_name: ClassVar[str] = "article"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Article

    id: Union[str, ArticleId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    publication_type: Union[str, list[str]] = None
    published_in: Union[str, URIorCURIE] = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArticleId):
            self.id = ArticleId(self.id)

        if self._is_empty(self.published_in):
            self.MissingRequiredField("published_in")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class JournalArticle(Article):
    """
    an article, typically presenting results of research, that is published in an issue of a scientific journal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["JournalArticle"]
    class_class_curie: ClassVar[str] = "biolink:JournalArticle"
    class_name: ClassVar[str] = "journal article"
    class_model_uri: ClassVar[URIRef] = BIOLINK.JournalArticle

    id: Union[str, JournalArticleId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    publication_type: Union[str, list[str]] = None
    published_in: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JournalArticleId):
            self.id = JournalArticleId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Patent(Publication):
    """
    a legal document granted by a patent issuing authority which confers upon the patenter the sole right to make, use
    and sell an invention for a set period of time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Patent"]
    class_class_curie: ClassVar[str] = "biolink:Patent"
    class_name: ClassVar[str] = "patent"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Patent

    id: Union[str, PatentId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    publication_type: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PatentId):
            self.id = PatentId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class WebPage(Publication):
    """
    a document that is published according to World Wide Web standards, which may incorporate text, graphics, sound,
    and/or other features.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["WebPage"]
    class_class_curie: ClassVar[str] = "biolink:WebPage"
    class_name: ClassVar[str] = "web page"
    class_model_uri: ClassVar[URIRef] = BIOLINK.WebPage

    id: Union[str, WebPageId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    publication_type: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WebPageId):
            self.id = WebPageId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PreprintPublication(Publication):
    """
    a document reresenting an early version of an author's original scholarly work, such as a research paper or a
    review, prior to formal peer review and publication in a peer-reviewed scholarly or scientific journal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PreprintPublication"]
    class_class_curie: ClassVar[str] = "biolink:PreprintPublication"
    class_name: ClassVar[str] = "preprint publication"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PreprintPublication

    id: Union[str, PreprintPublicationId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    publication_type: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PreprintPublicationId):
            self.id = PreprintPublicationId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DrugLabel(Publication):
    """
    a document accompanying a drug or its container that provides written, printed or graphic information about the
    drug, including drug contents, specific instructions or warnings for administration, storage and disposal
    instructions, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DrugLabel"]
    class_class_curie: ClassVar[str] = "biolink:DrugLabel"
    class_name: ClassVar[str] = "drug label"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DrugLabel

    id: Union[str, DrugLabelId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    publication_type: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DrugLabelId):
            self.id = DrugLabelId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class RetrievalSource(InformationContentEntity):
    """
    Provides information about how a particular InformationResource served as a source from which knowledge expressed
    in an Edge, or data used to generate this knowledge, was retrieved.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["RetrievalSource"]
    class_class_curie: ClassVar[str] = "biolink:RetrievalSource"
    class_name: ClassVar[str] = "retrieval source"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RetrievalSource

    id: Union[str, RetrievalSourceId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    resource_id: Union[str, URIorCURIE] = None
    resource_role: Union[str, "ResourceRoleEnum"] = None
    upstream_resource_ids: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    source_record_urls: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RetrievalSourceId):
            self.id = RetrievalSourceId(self.id)

        if self._is_empty(self.resource_id):
            self.MissingRequiredField("resource_id")
        if not isinstance(self.resource_id, URIorCURIE):
            self.resource_id = URIorCURIE(self.resource_id)

        if self._is_empty(self.resource_role):
            self.MissingRequiredField("resource_role")
        if not isinstance(self.resource_role, ResourceRoleEnum):
            self.resource_role = ResourceRoleEnum(self.resource_role)

        if not isinstance(self.upstream_resource_ids, list):
            self.upstream_resource_ids = [self.upstream_resource_ids] if self.upstream_resource_ids is not None else []
        self.upstream_resource_ids = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.upstream_resource_ids]

        if not isinstance(self.source_record_urls, list):
            self.source_record_urls = [self.source_record_urls] if self.source_record_urls is not None else []
        self.source_record_urls = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.source_record_urls]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


class PhysicalEssenceOrOccurrent(YAMLRoot):
    """
    Either a physical or processual entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhysicalEssenceOrOccurrent"]
    class_class_curie: ClassVar[str] = "biolink:PhysicalEssenceOrOccurrent"
    class_name: ClassVar[str] = "physical essence or occurrent"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhysicalEssenceOrOccurrent


class PhysicalEssence(PhysicalEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhysicalEssence"]
    class_class_curie: ClassVar[str] = "biolink:PhysicalEssence"
    class_name: ClassVar[str] = "physical essence"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhysicalEssence


@dataclass(repr=False)
class PhysicalEntity(NamedThing):
    """
    An entity that has material reality (a.k.a. physical essence).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhysicalEntity"]
    class_class_curie: ClassVar[str] = "biolink:PhysicalEntity"
    class_name: ClassVar[str] = "physical entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhysicalEntity

    id: Union[str, PhysicalEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalEntityId):
            self.id = PhysicalEntityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


class Occurrent(PhysicalEssenceOrOccurrent):
    """
    A processual entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Occurrent"]
    class_class_curie: ClassVar[str] = "biolink:Occurrent"
    class_name: ClassVar[str] = "occurrent"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Occurrent


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ActivityAndBehavior"]
    class_class_curie: ClassVar[str] = "biolink:ActivityAndBehavior"
    class_name: ClassVar[str] = "activity and behavior"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ActivityAndBehavior


@dataclass(repr=False)
class Activity(NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include
    consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Activity"]
    class_class_curie: ClassVar[str] = "biolink:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Activity

    id: Union[str, ActivityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Study(Activity):
    """
    a detailed investigation and/or analysis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Study"]
    class_class_curie: ClassVar[str] = "biolink:Study"
    class_name: ClassVar[str] = "study"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Study

    id: Union[str, StudyId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Procedure(NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Procedure"]
    class_class_curie: ClassVar[str] = "biolink:Procedure"
    class_name: ClassVar[str] = "procedure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Procedure

    id: Union[str, ProcedureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Phenomenon(NamedThing):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Phenomenon"]
    class_class_curie: ClassVar[str] = "biolink:Phenomenon"
    class_name: ClassVar[str] = "phenomenon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Phenomenon

    id: Union[str, PhenomenonId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Device"]
    class_class_curie: ClassVar[str] = "biolink:Device"
    class_name: ClassVar[str] = "device"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Device

    id: Union[str, DeviceId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DiagnosticAid(NamedThing):
    """
    A device or substance used to help diagnose disease or injury
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiagnosticAid"]
    class_class_curie: ClassVar[str] = "biolink:DiagnosticAid"
    class_name: ClassVar[str] = "diagnostic aid"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiagnosticAid

    id: Union[str, DiagnosticAidId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiagnosticAidId):
            self.id = DiagnosticAidId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


class SubjectOfInvestigation(YAMLRoot):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SubjectOfInvestigation"]
    class_class_curie: ClassVar[str] = "biolink:SubjectOfInvestigation"
    class_name: ClassVar[str] = "subject of investigation"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SubjectOfInvestigation


@dataclass(repr=False)
class MaterialSample(PhysicalEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    [SIO]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MaterialSample"]
    class_class_curie: ClassVar[str] = "biolink:MaterialSample"
    class_name: ClassVar[str] = "material sample"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSample

    id: Union[str, MaterialSampleId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialSampleId):
            self.id = MaterialSampleId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PlanetaryEntity"]
    class_class_curie: ClassVar[str] = "biolink:PlanetaryEntity"
    class_name: ClassVar[str] = "planetary entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PlanetaryEntity

    id: Union[str, PlanetaryEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class EnvironmentalProcess(PlanetaryEntity):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EnvironmentalProcess"]
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalProcess"
    class_name: ClassVar[str] = "environmental process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalProcess

    id: Union[str, EnvironmentalProcessId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class EnvironmentalFeature(PlanetaryEntity):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EnvironmentalFeature"]
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalFeature"
    class_name: ClassVar[str] = "environmental feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalFeature

    id: Union[str, EnvironmentalFeatureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeographicLocation"]
    class_class_curie: ClassVar[str] = "biolink:GeographicLocation"
    class_name: ClassVar[str] = "geographic location"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeographicLocation

    id: Union[str, GeographicLocationId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeographicLocationAtTime"]
    class_class_curie: ClassVar[str] = "biolink:GeographicLocationAtTime"
    class_name: ClassVar[str] = "geographic location at time"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeographicLocationAtTime

    id: Union[str, GeographicLocationAtTimeId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ThingWithTaxon(YAMLRoot):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms;
    genes, their products and other molecular entities; body parts; biological processes
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["ThingWithTaxon"]
    class_class_curie: ClassVar[str] = "biolink:ThingWithTaxon"
    class_name: ClassVar[str] = "thing with taxon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ThingWithTaxon

    in_taxon: Optional[Union[Union[str, OrganismTaxonId], list[Union[str, OrganismTaxonId]]]] = empty_list()
    in_taxon_label: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        if self.in_taxon_label is not None and not isinstance(self.in_taxon_label, LabelType):
            self.in_taxon_label = LabelType(self.in_taxon_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalEntity(NamedThing):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["BiologicalEntity"]
    class_class_curie: ClassVar[str] = "biolink:BiologicalEntity"
    class_name: ClassVar[str] = "biological entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalEntity

    id: Union[str, BiologicalEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    in_taxon: Optional[Union[Union[str, OrganismTaxonId], list[Union[str, OrganismTaxonId]]]] = empty_list()
    in_taxon_label: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        if self.in_taxon_label is not None and not isinstance(self.in_taxon_label, LabelType):
            self.in_taxon_label = LabelType(self.in_taxon_label)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GenomicEntity(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenomicEntity"]
    class_class_curie: ClassVar[str] = "biolink:GenomicEntity"
    class_name: ClassVar[str] = "genomic entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenomicEntity

    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EpigenomicEntity(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EpigenomicEntity"]
    class_class_curie: ClassVar[str] = "biolink:EpigenomicEntity"
    class_name: ClassVar[str] = "epigenomic entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EpigenomicEntity

    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntity(NamedThing):
    """
    A chemical entity is a physical entity that pertains to chemistry or biochemistry.
    """
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalEntity"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalEntity"
    class_name: ClassVar[str] = "chemical entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    trade_name: Optional[str] = None
    available_from: Optional[Union[Union[str, "DrugAvailabilityEnum"], list[Union[str, "DrugAvailabilityEnum"]]]] = empty_list()
    max_tolerated_dose: Optional[str] = None
    is_toxic: Optional[Union[bool, Bool]] = None
    has_chemical_role: Optional[Union[Union[str, ChemicalRoleId], list[Union[str, ChemicalRoleId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        if self.trade_name is not None and not isinstance(self.trade_name, str):
            self.trade_name = str(self.trade_name)

        if not isinstance(self.available_from, list):
            self.available_from = [self.available_from] if self.available_from is not None else []
        self.available_from = [v if isinstance(v, DrugAvailabilityEnum) else DrugAvailabilityEnum(v) for v in self.available_from]

        if self.max_tolerated_dose is not None and not isinstance(self.max_tolerated_dose, str):
            self.max_tolerated_dose = str(self.max_tolerated_dose)

        if self.is_toxic is not None and not isinstance(self.is_toxic, Bool):
            self.is_toxic = Bool(self.is_toxic)

        if not isinstance(self.has_chemical_role, list):
            self.has_chemical_role = [self.has_chemical_role] if self.has_chemical_role is not None else []
        self.has_chemical_role = [v if isinstance(v, ChemicalRoleId) else ChemicalRoleId(v) for v in self.has_chemical_role]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MolecularEntity(ChemicalEntity):
    """
    A molecular entity is a chemical entity composed of individual or covalently bonded atoms.
    """
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["MolecularEntity"]
    class_class_curie: ClassVar[str] = "biolink:MolecularEntity"
    class_name: ClassVar[str] = "molecular entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularEntity

    id: Union[str, MolecularEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    is_metabolite: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularEntityId):
            self.id = MolecularEntityId(self.id)

        if self.is_metabolite is not None and not isinstance(self.is_metabolite, Bool):
            self.is_metabolite = Bool(self.is_metabolite)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class SmallMolecule(MolecularEntity):
    """
    A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES,
    InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of
    representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium
    ion).
    """
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["SmallMolecule"]
    class_class_curie: ClassVar[str] = "biolink:SmallMolecule"
    class_name: ClassVar[str] = "small molecule"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SmallMolecule

    id: Union[str, SmallMoleculeId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SmallMoleculeId):
            self.id = SmallMoleculeId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalMixture(ChemicalEntity):
    """
    A chemical mixture is a chemical entity composed of two or more molecular entities.
    """
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalMixture"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalMixture"
    class_name: ClassVar[str] = "chemical mixture"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalMixture

    id: Union[str, ChemicalMixtureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    is_supplement: Optional[str] = None
    highest_FDA_approval_status: Optional[Union[str, "ApprovalStatusEnum"]] = None
    drug_regulatory_status_world_wide: Optional[Union[str, "ApprovalStatusEnum"]] = None
    routes_of_delivery: Optional[Union[Union[str, "DrugDeliveryEnum"], list[Union[str, "DrugDeliveryEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalMixtureId):
            self.id = ChemicalMixtureId(self.id)

        if self.is_supplement is not None and not isinstance(self.is_supplement, str):
            self.is_supplement = str(self.is_supplement)

        if self.highest_FDA_approval_status is not None and not isinstance(self.highest_FDA_approval_status, ApprovalStatusEnum):
            self.highest_FDA_approval_status = ApprovalStatusEnum(self.highest_FDA_approval_status)

        if self.drug_regulatory_status_world_wide is not None and not isinstance(self.drug_regulatory_status_world_wide, ApprovalStatusEnum):
            self.drug_regulatory_status_world_wide = ApprovalStatusEnum(self.drug_regulatory_status_world_wide)

        if not isinstance(self.routes_of_delivery, list):
            self.routes_of_delivery = [self.routes_of_delivery] if self.routes_of_delivery is not None else []
        self.routes_of_delivery = [v if isinstance(v, DrugDeliveryEnum) else DrugDeliveryEnum(v) for v in self.routes_of_delivery]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class NucleicAcidEntity(MolecularEntity):
    """
    A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based
    sequence representations of its precise sequence; for convenience of representation, partial sequences of various
    kinds are included.
    """
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["NucleicAcidEntity"]
    class_class_curie: ClassVar[str] = "biolink:NucleicAcidEntity"
    class_name: ClassVar[str] = "nucleic acid entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NucleicAcidEntity

    id: Union[str, NucleicAcidEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None
    in_taxon: Optional[Union[Union[str, OrganismTaxonId], list[Union[str, OrganismTaxonId]]]] = empty_list()
    in_taxon_label: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NucleicAcidEntityId):
            self.id = NucleicAcidEntityId(self.id)

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        if self.in_taxon_label is not None and not isinstance(self.in_taxon_label, LabelType):
            self.in_taxon_label = LabelType(self.in_taxon_label)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class RegulatoryRegion(BiologicalEntity):
    """
    A region (or regions) of the genome that contains known or putative regulatory elements that act in cis- or trans-
    to affect the transcription of gene
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["RegulatoryRegion"]
    class_class_curie: ClassVar[str] = "biolink:RegulatoryRegion"
    class_name: ClassVar[str] = "regulatory region"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RegulatoryRegion

    id: Union[str, RegulatoryRegionId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegulatoryRegionId):
            self.id = RegulatoryRegionId(self.id)

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class AccessibleDnaRegion(RegulatoryRegion):
    """
    A region (or regions) of a chromatinized genome that has been measured to be more accessible to an enzyme such as
    DNase-I or Tn5 Transpose
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["AccessibleDnaRegion"]
    class_class_curie: ClassVar[str] = "biolink:AccessibleDnaRegion"
    class_name: ClassVar[str] = "accessible dna region"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AccessibleDnaRegion

    id: Union[str, AccessibleDnaRegionId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AccessibleDnaRegionId):
            self.id = AccessibleDnaRegionId(self.id)

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class TranscriptionFactorBindingSite(RegulatoryRegion):
    """
    A region (or regions) of the genome that contains a region of DNA known or predicted to bind a protein that
    modulates gene transcription
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["TranscriptionFactorBindingSite"]
    class_class_curie: ClassVar[str] = "biolink:TranscriptionFactorBindingSite"
    class_name: ClassVar[str] = "transcription factor binding site"
    class_model_uri: ClassVar[URIRef] = BIOLINK.TranscriptionFactorBindingSite

    id: Union[str, TranscriptionFactorBindingSiteId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TranscriptionFactorBindingSiteId):
            self.id = TranscriptionFactorBindingSiteId(self.id)

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MolecularMixture(ChemicalMixture):
    """
    A molecular mixture is a chemical mixture composed of two or more molecular entities with known concentration and
    stoichiometry.
    """
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["MolecularMixture"]
    class_class_curie: ClassVar[str] = "biolink:MolecularMixture"
    class_name: ClassVar[str] = "molecular mixture"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularMixture

    id: Union[str, MolecularMixtureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularMixtureId):
            self.id = MolecularMixtureId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ComplexMolecularMixture(ChemicalMixture):
    """
    A complex molecular mixture is a chemical mixture composed of two or more molecular entities with unknown
    concentration and stoichiometry.
    """
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["ComplexMolecularMixture"]
    class_class_curie: ClassVar[str] = "biolink:ComplexMolecularMixture"
    class_name: ClassVar[str] = "complex molecular mixture"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ComplexMolecularMixture

    id: Union[str, ComplexMolecularMixtureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComplexMolecularMixtureId):
            self.id = ComplexMolecularMixtureId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities in a
    biological system.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["BiologicalProcessOrActivity"]
    class_class_curie: ClassVar[str] = "biolink:BiologicalProcessOrActivity"
    class_name: ClassVar[str] = "biological process or activity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcessOrActivity

    id: Union[str, BiologicalProcessOrActivityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_input: Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]] = empty_list()
    enabled_by: Optional[Union[Union[str, PhysicalEntityId], list[Union[str, PhysicalEntityId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalProcessOrActivityId):
            self.id = BiologicalProcessOrActivityId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by] if self.enabled_by is not None else []
        self.enabled_by = [v if isinstance(v, PhysicalEntityId) else PhysicalEntityId(v) for v in self.enabled_by]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["MolecularActivity"]
    class_class_curie: ClassVar[str] = "biolink:MolecularActivity"
    class_name: ClassVar[str] = "molecular activity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularActivity

    id: Union[str, MolecularActivityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_input: Optional[Union[Union[str, MolecularEntityId], list[Union[str, MolecularEntityId]]]] = empty_list()
    has_output: Optional[Union[Union[str, MolecularEntityId], list[Union[str, MolecularEntityId]]]] = empty_list()
    enabled_by: Optional[Union[Union[dict, "MacromolecularMachineMixin"], list[Union[dict, "MacromolecularMachineMixin"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, MolecularEntityId) else MolecularEntityId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, MolecularEntityId) else MolecularEntityId(v) for v in self.has_output]

        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by] if self.enabled_by is not None else []
        self.enabled_by = [v if isinstance(v, MacromolecularMachineMixin) else MacromolecularMachineMixin(**as_dict(v)) for v in self.enabled_by]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["BiologicalProcess"]
    class_class_curie: ClassVar[str] = "biolink:BiologicalProcess"
    class_name: ClassVar[str] = "biological process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcess

    id: Union[str, BiologicalProcessId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Pathway(BiologicalProcess):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Pathway"]
    class_class_curie: ClassVar[str] = "biolink:Pathway"
    class_name: ClassVar[str] = "pathway"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Pathway

    id: Union[str, PathwayId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PhysiologicalProcess(BiologicalProcess):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhysiologicalProcess"]
    class_class_curie: ClassVar[str] = "biolink:PhysiologicalProcess"
    class_name: ClassVar[str] = "physiological process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhysiologicalProcess

    id: Union[str, PhysiologicalProcessId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysiologicalProcessId):
            self.id = PhysiologicalProcessId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Behavior(BiologicalProcess):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Behavior"]
    class_class_curie: ClassVar[str] = "biolink:Behavior"
    class_name: ClassVar[str] = "behavior"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Behavior

    id: Union[str, BehaviorId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehaviorId):
            self.id = BehaviorId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ProcessedMaterial(ChemicalMixture):
    """
    A chemical entity (often a mixture) processed for consumption for nutritional, medical or technical use. Is a
    material entity that is created or changed during material processing.
    """
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["ProcessedMaterial"]
    class_class_curie: ClassVar[str] = "biolink:ProcessedMaterial"
    class_name: ClassVar[str] = "processed material"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ProcessedMaterial

    id: Union[str, ProcessedMaterialId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessedMaterialId):
            self.id = ProcessedMaterialId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Drug(MolecularMixture):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Drug"]
    class_class_curie: ClassVar[str] = "biolink:Drug"
    class_name: ClassVar[str] = "drug"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Drug

    id: Union[str, DrugId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class EnvironmentalFoodContaminant(ChemicalEntity):
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["EnvironmentalFoodContaminant"]
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalFoodContaminant"
    class_name: ClassVar[str] = "environmental food contaminant"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalFoodContaminant

    id: Union[str, EnvironmentalFoodContaminantId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalFoodContaminantId):
            self.id = EnvironmentalFoodContaminantId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class FoodAdditive(ChemicalEntity):
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["FoodAdditive"]
    class_class_curie: ClassVar[str] = "biolink:FoodAdditive"
    class_name: ClassVar[str] = "food additive"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FoodAdditive

    id: Union[str, FoodAdditiveId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoodAdditiveId):
            self.id = FoodAdditiveId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Food(ChemicalMixture):
    """
    A substance consumed by a living organism as a source of nutrition
    """
    _inherited_slots: ClassVar[list[str]] = ["has_chemical_role"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Food"]
    class_class_curie: ClassVar[str] = "biolink:Food"
    class_name: ClassVar[str] = "food"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Food

    id: Union[str, FoodId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoodId):
            self.id = FoodId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class OrganismAttribute(Attribute):
    """
    describes a characteristic of an organismal entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["OrganismAttribute"]
    class_class_curie: ClassVar[str] = "biolink:OrganismAttribute"
    class_name: ClassVar[str] = "organism attribute"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismAttribute

    id: Union[str, OrganismAttributeId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismAttributeId):
            self.id = OrganismAttributeId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PhenotypicQuality(OrganismAttribute):
    """
    A property of a phenotype
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhenotypicQuality"]
    class_class_curie: ClassVar[str] = "biolink:PhenotypicQuality"
    class_name: ClassVar[str] = "phenotypic quality"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicQuality

    id: Union[str, PhenotypicQualityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypicQualityId):
            self.id = PhenotypicQualityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneticInheritance(BiologicalEntity):
    """
    The pattern or 'mode' in which a particular genetic trait or disorder is passed from one generation to the next,
    e.g. autosomal dominant, autosomal recessive, etc.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneticInheritance"]
    class_class_curie: ClassVar[str] = "biolink:GeneticInheritance"
    class_name: ClassVar[str] = "genetic inheritance"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneticInheritance

    id: Union[str, GeneticInheritanceId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneticInheritanceId):
            self.id = GeneticInheritanceId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding
    chemical entities
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["OrganismalEntity"]
    class_class_curie: ClassVar[str] = "biolink:OrganismalEntity"
    class_name: ClassVar[str] = "organismal entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismalEntity

    id: Union[str, OrganismalEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute: Optional[Union[Union[str, AttributeId], list[Union[str, AttributeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, AttributeId) else AttributeId(v) for v in self.has_attribute]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Bacterium(OrganismalEntity):
    """
    A member of a group of unicellular microorganisms lacking a nuclear membrane, that reproduce by binary fission and
    are often motile.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Bacterium"]
    class_class_curie: ClassVar[str] = "biolink:Bacterium"
    class_name: ClassVar[str] = "bacterium"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Bacterium

    id: Union[str, BacteriumId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BacteriumId):
            self.id = BacteriumId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Virus(OrganismalEntity):
    """
    A virus is a microorganism that replicates itself as a microRNA and infects the host cell.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Virus"]
    class_class_curie: ClassVar[str] = "biolink:Virus"
    class_name: ClassVar[str] = "virus"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Virus

    id: Union[str, VirusId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirusId):
            self.id = VirusId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CellularOrganism(OrganismalEntity):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["CellularOrganism"]
    class_class_curie: ClassVar[str] = "biolink:CellularOrganism"
    class_name: ClassVar[str] = "cellular organism"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellularOrganism

    id: Union[str, CellularOrganismId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellularOrganismId):
            self.id = CellularOrganismId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Mammal(CellularOrganism):
    """
    A member of the class Mammalia, a clade of endothermic amniotes distinguished from reptiles and birds by the
    possession of hair, three middle ear bones, mammary glands, and a neocortex
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Mammal"]
    class_class_curie: ClassVar[str] = "biolink:Mammal"
    class_name: ClassVar[str] = "mammal"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Mammal

    id: Union[str, MammalId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MammalId):
            self.id = MammalId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Human(Mammal):
    """
    A member of the the species Homo sapiens.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Human"]
    class_class_curie: ClassVar[str] = "biolink:Human"
    class_name: ClassVar[str] = "human"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Human

    id: Union[str, HumanId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanId):
            self.id = HumanId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Plant(CellularOrganism):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Plant"]
    class_class_curie: ClassVar[str] = "biolink:Plant"
    class_name: ClassVar[str] = "plant"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Plant

    id: Union[str, PlantId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlantId):
            self.id = PlantId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Invertebrate(CellularOrganism):
    """
    An animal lacking a vertebral column. This group consists of 98% of all animal species.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Invertebrate"]
    class_class_curie: ClassVar[str] = "biolink:Invertebrate"
    class_name: ClassVar[str] = "invertebrate"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Invertebrate

    id: Union[str, InvertebrateId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvertebrateId):
            self.id = InvertebrateId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Vertebrate(CellularOrganism):
    """
    A sub-phylum of animals consisting of those having a bony or cartilaginous vertebral column.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Vertebrate"]
    class_class_curie: ClassVar[str] = "biolink:Vertebrate"
    class_name: ClassVar[str] = "vertebrate"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Vertebrate

    id: Union[str, VertebrateId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VertebrateId):
            self.id = VertebrateId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Fungus(CellularOrganism):
    """
    A kingdom of eukaryotic, heterotrophic organisms that live as saprobes or parasites, including mushrooms, yeasts,
    smuts, molds, etc. They reproduce either sexually or asexually, and have life cycles that range from simple to
    complex. Filamentous fungi refer to those that grow as multicellular colonies (mushrooms and molds).
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Fungus"]
    class_class_curie: ClassVar[str] = "biolink:Fungus"
    class_name: ClassVar[str] = "fungus"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Fungus

    id: Union[str, FungusId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FungusId):
            self.id = FungusId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["LifeStage"]
    class_class_curie: ClassVar[str] = "biolink:LifeStage"
    class_name: ClassVar[str] = "life stage"
    class_model_uri: ClassVar[URIRef] = BIOLINK.LifeStage

    id: Union[str, LifeStageId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LifeStageId):
            self.id = LifeStageId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class IndividualOrganism(OrganismalEntity):
    """
    An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID:
    ORCID:0000-0002-5355-2576
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["IndividualOrganism"]
    class_class_curie: ClassVar[str] = "biolink:IndividualOrganism"
    class_name: ClassVar[str] = "individual organism"
    class_model_uri: ClassVar[URIRef] = BIOLINK.IndividualOrganism

    id: Union[str, IndividualOrganismId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IndividualOrganismId):
            self.id = IndividualOrganismId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PopulationOfIndividualOrganisms(OrganismalEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["PopulationOfIndividualOrganisms"]
    class_class_curie: ClassVar[str] = "biolink:PopulationOfIndividualOrganisms"
    class_name: ClassVar[str] = "population of individual organisms"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PopulationOfIndividualOrganisms

    id: Union[str, PopulationOfIndividualOrganismsId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulationOfIndividualOrganismsId):
            self.id = PopulationOfIndividualOrganismsId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class StudyPopulation(PopulationOfIndividualOrganisms):
    """
    A group of people banded together or treated as a group as participants in a research study.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["StudyPopulation"]
    class_class_curie: ClassVar[str] = "biolink:StudyPopulation"
    class_name: ClassVar[str] = "study population"
    class_model_uri: ClassVar[URIRef] = BIOLINK.StudyPopulation

    id: Union[str, StudyPopulationId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyPopulationId):
            self.id = StudyPopulationId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these
    as distinct, others such as MESH conflate. Please see definitions of phenotypic feature and disease in this model
    for their independent descriptions. This class is helpful to enforce domains and ranges that may involve either a
    disease or a phenotypic feature.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseOrPhenotypicFeature"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeature"
    class_name: ClassVar[str] = "disease or phenotypic feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeature

    id: Union[str, DiseaseOrPhenotypicFeatureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Disease(DiseaseOrPhenotypicFeature):
    """
    A disorder of structure or function, especially one that produces specific signs, phenotypes or symptoms or that
    affects a specific location and is not simply a direct result of physical injury. A disposition to undergo
    pathological processes that exists in an organism because of one or more disorders in that organism.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Disease"]
    class_class_curie: ClassVar[str] = "biolink:Disease"
    class_name: ClassVar[str] = "disease"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Disease

    id: Union[str, DiseaseId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    """
    A combination of entity and quality that makes up a phenotyping statement. An observable characteristic of an
    individual resulting from the interaction of its genotype with its molecular and physical environment.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhenotypicFeature"]
    class_class_curie: ClassVar[str] = "biolink:PhenotypicFeature"
    class_name: ClassVar[str] = "phenotypic feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicFeature

    id: Union[str, PhenotypicFeatureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypicFeatureId):
            self.id = PhenotypicFeatureId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class BehavioralFeature(PhenotypicFeature):
    """
    A phenotypic feature which is behavioral in nature.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["BehavioralFeature"]
    class_class_curie: ClassVar[str] = "biolink:BehavioralFeature"
    class_name: ClassVar[str] = "behavioral feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BehavioralFeature

    id: Union[str, BehavioralFeatureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehavioralFeatureId):
            self.id = BehavioralFeatureId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["AnatomicalEntity"]
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntity"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["CellularComponent"]
    class_class_curie: ClassVar[str] = "biolink:CellularComponent"
    class_name: ClassVar[str] = "cellular component"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellularComponent

    id: Union[str, CellularComponentId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Cell(AnatomicalEntity):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Cell"]
    class_class_curie: ClassVar[str] = "biolink:Cell"
    class_name: ClassVar[str] = "cell"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Cell

    id: Union[str, CellId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellId):
            self.id = CellId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CellLine(OrganismalEntity):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["CellLine"]
    class_class_curie: ClassVar[str] = "biolink:CellLine"
    class_name: ClassVar[str] = "cell line"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLine

    id: Union[str, CellLineId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GrossAnatomicalStructure(AnatomicalEntity):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["GrossAnatomicalStructure"]
    class_class_curie: ClassVar[str] = "biolink:GrossAnatomicalStructure"
    class_name: ClassVar[str] = "gross anatomical structure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GrossAnatomicalStructure

    id: Union[str, GrossAnatomicalStructureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GrossAnatomicalStructureId):
            self.id = GrossAnatomicalStructureId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


class ChemicalEntityOrGeneOrGeneProduct(YAMLRoot):
    """
    A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching
    across chemical entities that must include genes and their children as chemical entities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalEntityOrGeneOrGeneProduct"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalEntityOrGeneOrGeneProduct"
    class_name: ClassVar[str] = "chemical entity or gene or gene product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalEntityOrGeneOrGeneProduct


class ChemicalEntityOrProteinOrPolypeptide(YAMLRoot):
    """
    A union of chemical entities and children, and protein and polypeptide. This mixin is helpful to use when
    searching across chemical entities that must include genes and their children as chemical entities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalEntityOrProteinOrPolypeptide"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalEntityOrProteinOrPolypeptide"
    class_name: ClassVar[str] = "chemical entity or protein or polypeptide"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalEntityOrProteinOrPolypeptide


@dataclass(repr=False)
class MacromolecularMachineMixin(YAMLRoot):
    """
    A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell.
    They either carry out individual biological activities, or they encode molecules which do this.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MacromolecularMachineMixin"]
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineMixin"
    class_name: ClassVar[str] = "macromolecular machine mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineMixin

    name: Optional[Union[str, SymbolType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)

        super().__post_init__(**kwargs)


class GeneOrGeneProduct(MacromolecularMachineMixin):
    """
    A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneOrGeneProduct"]
    class_class_curie: ClassVar[str] = "biolink:GeneOrGeneProduct"
    class_name: ClassVar[str] = "gene or gene product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneOrGeneProduct


@dataclass(repr=False)
class Gene(BiologicalEntity):
    """
    A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A
    gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Gene"]
    class_class_curie: ClassVar[str] = "biolink:Gene"
    class_name: ClassVar[str] = "gene"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Gene

    id: Union[str, GeneId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    name: Optional[Union[str, LabelType]] = None
    symbol: Optional[str] = None
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneProductMixin(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA
    molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneProductMixin"]
    class_class_curie: ClassVar[str] = "biolink:GeneProductMixin"
    class_name: ClassVar[str] = "gene product mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneProductMixin

    synonym: Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


class GeneProductIsoformMixin(GeneProductMixin):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene
    product is intended to represent a specific isoform rather than a canonical or reference or generic product. The
    designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneProductIsoformMixin"]
    class_class_curie: ClassVar[str] = "biolink:GeneProductIsoformMixin"
    class_name: ClassVar[str] = "gene product isoform mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneProductIsoformMixin


@dataclass(repr=False)
class MacromolecularComplex(BiologicalEntity):
    """
    A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which
    at least one component is a protein and the constituent parts function together.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["MacromolecularComplex"]
    class_class_curie: ClassVar[str] = "biolink:MacromolecularComplex"
    class_name: ClassVar[str] = "macromolecular complex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularComplex

    id: Union[str, MacromolecularComplexId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MacromolecularComplexId):
            self.id = MacromolecularComplexId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class NucleosomeModification(BiologicalEntity):
    """
    A chemical modification of a histone protein within a nucleosome octomer or a substitution of a histone with a
    variant histone isoform. e.g. Histone 4 Lysine 20 methylation (H4K20me), histone variant H2AZ substituting H2A.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["NucleosomeModification"]
    class_class_curie: ClassVar[str] = "biolink:NucleosomeModification"
    class_name: ClassVar[str] = "nucleosome modification"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NucleosomeModification

    id: Union[str, NucleosomeModificationId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    name: Optional[Union[str, LabelType]] = None
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    synonym: Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NucleosomeModificationId):
            self.id = NucleosomeModificationId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Genome(BiologicalEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Genome"]
    class_class_curie: ClassVar[str] = "biolink:Genome"
    class_name: ClassVar[str] = "genome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Genome

    id: Union[str, GenomeId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenomeId):
            self.id = GenomeId(self.id)

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Exon(BiologicalEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA
    splicing.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Exon"]
    class_class_curie: ClassVar[str] = "biolink:Exon"
    class_name: ClassVar[str] = "exon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Exon

    id: Union[str, ExonId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExonId):
            self.id = ExonId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Transcript(BiologicalEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Transcript"]
    class_class_curie: ClassVar[str] = "biolink:Transcript"
    class_name: ClassVar[str] = "transcript"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Transcript

    id: Union[str, TranscriptId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TranscriptId):
            self.id = TranscriptId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CodingSequence(BiologicalEntity):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["CodingSequence"]
    class_class_curie: ClassVar[str] = "biolink:CodingSequence"
    class_name: ClassVar[str] = "coding sequence"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CodingSequence

    id: Union[str, CodingSequenceId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Polypeptide(BiologicalEntity):
    """
    A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based
    sequence representations of its precise primary structure; for convenience of representation, partial sequences of
    various kinds are included, even if they do not represent a physical molecule.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Polypeptide"]
    class_class_curie: ClassVar[str] = "biolink:Polypeptide"
    class_name: ClassVar[str] = "polypeptide"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Polypeptide

    id: Union[str, PolypeptideId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolypeptideId):
            self.id = PolypeptideId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Protein(Polypeptide):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated
    translation of mRNA
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Protein"]
    class_class_curie: ClassVar[str] = "biolink:Protein"
    class_name: ClassVar[str] = "protein"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Protein

    id: Union[str, ProteinId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    name: Optional[Union[str, LabelType]] = None
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    synonym: Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["ProteinIsoform"]
    class_class_curie: ClassVar[str] = "biolink:ProteinIsoform"
    class_name: ClassVar[str] = "protein isoform"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ProteinIsoform

    id: Union[str, ProteinIsoformId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    name: Optional[Union[str, LabelType]] = None
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    synonym: Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinIsoformId):
            self.id = ProteinIsoformId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ProteinDomain(BiologicalEntity):
    """
    A conserved part of protein sequence and (tertiary) structure that can evolve, function, and exist independently
    of the rest of the protein chain. Protein domains maintain their structure and function independently of the
    proteins in which they are found. e.g. an SH3 domain.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["ProteinDomain"]
    class_class_curie: ClassVar[str] = "biolink:ProteinDomain"
    class_name: ClassVar[str] = "protein domain"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ProteinDomain

    id: Union[str, ProteinDomainId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_gene_or_gene_product: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinDomainId):
            self.id = ProteinDomainId(self.id)

        if not isinstance(self.has_gene_or_gene_product, list):
            self.has_gene_or_gene_product = [self.has_gene_or_gene_product] if self.has_gene_or_gene_product is not None else []
        self.has_gene_or_gene_product = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene_or_gene_product]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PosttranslationalModification(BiologicalEntity):
    """
    A chemical modification of a polypeptide or protein that occurs after translation. e.g. polypeptide cleavage to
    form separate proteins, methylation or acetylation of histone tail amino acids, protein ubiquitination.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["PosttranslationalModification"]
    class_class_curie: ClassVar[str] = "biolink:PosttranslationalModification"
    class_name: ClassVar[str] = "posttranslational modification"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PosttranslationalModification

    id: Union[str, PosttranslationalModificationId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    name: Optional[Union[str, LabelType]] = None
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    synonym: Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PosttranslationalModificationId):
            self.id = PosttranslationalModificationId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ProteinFamily(BiologicalEntity):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["ProteinFamily"]
    class_class_curie: ClassVar[str] = "biolink:ProteinFamily"
    class_name: ClassVar[str] = "protein family"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ProteinFamily

    id: Union[str, ProteinFamilyId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_gene_or_gene_product: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinFamilyId):
            self.id = ProteinFamilyId(self.id)

        if not isinstance(self.has_gene_or_gene_product, list):
            self.has_gene_or_gene_product = [self.has_gene_or_gene_product] if self.has_gene_or_gene_product is not None else []
        self.has_gene_or_gene_product = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene_or_gene_product]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class NucleicAcidSequenceMotif(BiologicalEntity):
    """
    A linear nucleotide sequence pattern that is widespread and has, or is conjectured to have, a biological
    significance. e.g. the TATA box promoter motif, transcription factor binding consensus sequences.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["NucleicAcidSequenceMotif"]
    class_class_curie: ClassVar[str] = "biolink:NucleicAcidSequenceMotif"
    class_name: ClassVar[str] = "nucleic acid sequence motif"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NucleicAcidSequenceMotif

    id: Union[str, NucleicAcidSequenceMotifId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NucleicAcidSequenceMotifId):
            self.id = NucleicAcidSequenceMotifId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class RNAProduct(Transcript):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["RNAProduct"]
    class_class_curie: ClassVar[str] = "biolink:RNAProduct"
    class_name: ClassVar[str] = "RNA product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RNAProduct

    id: Union[str, RNAProductId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    name: Optional[Union[str, LabelType]] = None
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    synonym: Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RNAProductId):
            self.id = RNAProductId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class RNAProductIsoform(RNAProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["RNAProductIsoform"]
    class_class_curie: ClassVar[str] = "biolink:RNAProductIsoform"
    class_name: ClassVar[str] = "RNA product isoform"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RNAProductIsoform

    id: Union[str, RNAProductIsoformId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    name: Optional[Union[str, LabelType]] = None
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    synonym: Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RNAProductIsoformId):
            self.id = RNAProductIsoformId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class NoncodingRNAProduct(RNAProduct):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["NoncodingRNAProduct"]
    class_class_curie: ClassVar[str] = "biolink:NoncodingRNAProduct"
    class_name: ClassVar[str] = "noncoding RNA product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NoncodingRNAProduct

    id: Union[str, NoncodingRNAProductId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoncodingRNAProductId):
            self.id = NoncodingRNAProductId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MicroRNA(NoncodingRNAProduct):
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["MicroRNA"]
    class_class_curie: ClassVar[str] = "biolink:MicroRNA"
    class_name: ClassVar[str] = "microRNA"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MicroRNA

    id: Union[str, MicroRNAId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicroRNAId):
            self.id = MicroRNAId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class SiRNA(NoncodingRNAProduct):
    """
    A small RNA molecule that is the product of a longer exogenous or endogenous dsRNA, which is either a bimolecular
    duplex or very long hairpin, processed (via the Dicer pathway) such that numerous siRNAs accumulate from both
    strands of the dsRNA. SRNAs trigger the cleavage of their target molecules.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["SiRNA"]
    class_class_curie: ClassVar[str] = "biolink:SiRNA"
    class_name: ClassVar[str] = "siRNA"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SiRNA

    id: Union[str, SiRNAId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SiRNAId):
            self.id = SiRNAId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneGroupingMixin(YAMLRoot):
    """
    any grouping of multiple genes or gene products
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneGroupingMixin"]
    class_class_curie: ClassVar[str] = "biolink:GeneGroupingMixin"
    class_name: ClassVar[str] = "gene grouping mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneGroupingMixin

    has_gene_or_gene_product: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.has_gene_or_gene_product, list):
            self.has_gene_or_gene_product = [self.has_gene_or_gene_product] if self.has_gene_or_gene_product is not None else []
        self.has_gene_or_gene_product = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene_or_gene_product]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneFamily(BiologicalEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneFamily"]
    class_class_curie: ClassVar[str] = "biolink:GeneFamily"
    class_name: ClassVar[str] = "gene family"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneFamily

    id: Union[str, GeneFamilyId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_gene_or_gene_product: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneFamilyId):
            self.id = GeneFamilyId(self.id)

        if not isinstance(self.has_gene_or_gene_product, list):
            self.has_gene_or_gene_product = [self.has_gene_or_gene_product] if self.has_gene_or_gene_product is not None else []
        self.has_gene_or_gene_product = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene_or_gene_product]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Zygosity(Attribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Zygosity"]
    class_class_curie: ClassVar[str] = "biolink:Zygosity"
    class_name: ClassVar[str] = "zygosity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Zygosity

    id: Union[str, ZygosityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ZygosityId):
            self.id = ZygosityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Genotype(BiologicalEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or
    gene expression, relative to some established background
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Genotype"]
    class_class_curie: ClassVar[str] = "biolink:Genotype"
    class_name: ClassVar[str] = "genotype"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Genotype

    id: Union[str, GenotypeId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_zygosity: Optional[Union[str, ZygosityId]] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenotypeId):
            self.id = GenotypeId(self.id)

        if self.has_zygosity is not None and not isinstance(self.has_zygosity, ZygosityId):
            self.has_zygosity = ZygosityId(self.has_zygosity)

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Haplotype(BiologicalEntity):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Haplotype"]
    class_class_curie: ClassVar[str] = "biolink:Haplotype"
    class_name: ClassVar[str] = "haplotype"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Haplotype

    id: Union[str, HaplotypeId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HaplotypeId):
            self.id = HaplotypeId(self.id)

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class SequenceVariant(BiologicalEntity):
    """
    A sequence_variant is a non exact copy of a sequence_feature or genome exhibiting one or more sequence_alteration.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["SequenceVariant"]
    class_class_curie: ClassVar[str] = "biolink:SequenceVariant"
    class_name: ClassVar[str] = "sequence variant"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SequenceVariant

    id: Union[str, SequenceVariantId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_gene: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()
    hgvs_nomenclature: Optional[Union[str, list[str]]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)

        if not isinstance(self.has_gene, list):
            self.has_gene = [self.has_gene] if self.has_gene is not None else []
        self.has_gene = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene]

        if not isinstance(self.hgvs_nomenclature, list):
            self.hgvs_nomenclature = [self.hgvs_nomenclature] if self.hgvs_nomenclature is not None else []
        self.hgvs_nomenclature = [v if isinstance(v, str) else str(v) for v in self.hgvs_nomenclature]

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Snv(SequenceVariant):
    """
    SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Snv"]
    class_class_curie: ClassVar[str] = "biolink:Snv"
    class_name: ClassVar[str] = "snv"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Snv

    id: Union[str, SnvId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SnvId):
            self.id = SnvId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ReagentTargetedGene(BiologicalEntity):
    """
    A gene altered in its expression level in the context of some experiment as a result of being targeted by
    gene-knockdown reagent(s) such as a morpholino or RNAi.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["ReagentTargetedGene"]
    class_class_curie: ClassVar[str] = "biolink:ReagentTargetedGene"
    class_name: ClassVar[str] = "reagent targeted gene"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ReagentTargetedGene

    id: Union[str, ReagentTargetedGeneId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReagentTargetedGeneId):
            self.id = ReagentTargetedGeneId(self.id)

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ClinicalAttribute(Attribute):
    """
    Attributes relating to a clinical manifestation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ClinicalAttribute"]
    class_class_curie: ClassVar[str] = "biolink:ClinicalAttribute"
    class_name: ClassVar[str] = "clinical attribute"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalAttribute

    id: Union[str, ClinicalAttributeId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalAttributeId):
            self.id = ClinicalAttributeId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ClinicalMeasurement(ClinicalAttribute):
    """
    A clinical measurement is a special kind of attribute which results from a laboratory observation from a subject
    individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ClinicalMeasurement"]
    class_class_curie: ClassVar[str] = "biolink:ClinicalMeasurement"
    class_name: ClassVar[str] = "clinical measurement"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalMeasurement

    id: Union[str, ClinicalMeasurementId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalMeasurementId):
            self.id = ClinicalMeasurementId(self.id)

        if self._is_empty(self.has_attribute_type):
            self.MissingRequiredField("has_attribute_type")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ClinicalModifier(ClinicalAttribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the phenotypic abnormality sub-ontology,
    with respect to severity, laterality, and other aspects
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ClinicalModifier"]
    class_class_curie: ClassVar[str] = "biolink:ClinicalModifier"
    class_name: ClassVar[str] = "clinical modifier"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalModifier

    id: Union[str, ClinicalModifierId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalModifierId):
            self.id = ClinicalModifierId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ClinicalCourse(ClinicalAttribute):
    """
    The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the
    affected individual
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ClinicalCourse"]
    class_class_curie: ClassVar[str] = "biolink:ClinicalCourse"
    class_name: ClassVar[str] = "clinical course"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalCourse

    id: Union[str, ClinicalCourseId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalCourseId):
            self.id = ClinicalCourseId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Onset(ClinicalCourse):
    """
    The age group in which (disease) symptom manifestations appear.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Onset"]
    class_class_curie: ClassVar[str] = "biolink:Onset"
    class_name: ClassVar[str] = "onset"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Onset

    id: Union[str, OnsetId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OnsetId):
            self.id = OnsetId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed
    under biological entities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ClinicalEntity"]
    class_class_curie: ClassVar[str] = "biolink:ClinicalEntity"
    class_name: ClassVar[str] = "clinical entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalEntity

    id: Union[str, ClinicalEntityId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalEntityId):
            self.id = ClinicalEntityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ClinicalTrial(Study):
    """
    A clinical trial is a research study that prospectively assigns human participants or groups of humans to one or
    more health-related interventions to evaluate the effects on health outcomes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ClinicalTrial"]
    class_class_curie: ClassVar[str] = "biolink:ClinicalTrial"
    class_name: ClassVar[str] = "clinical trial"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalTrial

    id: Union[str, ClinicalTrialId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    clinical_trial_phase: Optional[Union[str, "ResearchPhaseEnum"]] = None
    clinical_trial_primary_purpose: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalTrialId):
            self.id = ClinicalTrialId(self.id)

        if self.clinical_trial_phase is not None and not isinstance(self.clinical_trial_phase, ResearchPhaseEnum):
            self.clinical_trial_phase = ResearchPhaseEnum(self.clinical_trial_phase)

        if self.clinical_trial_primary_purpose is not None and not isinstance(self.clinical_trial_primary_purpose, str):
            self.clinical_trial_primary_purpose = str(self.clinical_trial_primary_purpose)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ClinicalIntervention(ClinicalEntity):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ClinicalIntervention"]
    class_class_curie: ClassVar[str] = "biolink:ClinicalIntervention"
    class_name: ClassVar[str] = "clinical intervention"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalIntervention

    id: Union[str, ClinicalInterventionId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalInterventionId):
            self.id = ClinicalInterventionId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ClinicalFinding(PhenotypicFeature):
    """
    this category is currently considered broad enough to tag clinical lab measurements and other biological
    attributes taken as 'clinical traits' with some statistical score, for example, a p value in genetic associations.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["ClinicalFinding"]
    class_class_curie: ClassVar[str] = "biolink:ClinicalFinding"
    class_name: ClassVar[str] = "clinical finding"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalFinding

    id: Union[str, ClinicalFindingId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute: Optional[Union[Union[str, ClinicalAttributeId], list[Union[str, ClinicalAttributeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalFindingId):
            self.id = ClinicalFindingId(self.id)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, ClinicalAttributeId) else ClinicalAttributeId(v) for v in self.has_attribute]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Hospitalization(ClinicalIntervention):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Hospitalization"]
    class_class_curie: ClassVar[str] = "biolink:Hospitalization"
    class_name: ClassVar[str] = "hospitalization"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Hospitalization

    id: Union[str, HospitalizationId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HospitalizationId):
            self.id = HospitalizationId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class SocioeconomicAttribute(Attribute):
    """
    Attributes relating to a socioeconomic manifestation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SocioeconomicAttribute"]
    class_class_curie: ClassVar[str] = "biolink:SocioeconomicAttribute"
    class_name: ClassVar[str] = "socioeconomic attribute"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SocioeconomicAttribute

    id: Union[str, SocioeconomicAttributeId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SocioeconomicAttributeId):
            self.id = SocioeconomicAttributeId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Case(IndividualOrganism):
    """
    An individual (human) organism that has a patient role in some clinical context.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Case"]
    class_class_curie: ClassVar[str] = "biolink:Case"
    class_name: ClassVar[str] = "case"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Case

    id: Union[str, CaseId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_biological_sex: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)

        if self.has_biological_sex is not None and not isinstance(self.has_biological_sex, BiologicalSexId):
            self.has_biological_sex = BiologicalSexId(self.has_biological_sex)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Cohort(StudyPopulation):
    """
    A group of people banded together or treated as a group who share common characteristics. A cohort 'study' is a
    particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["Cohort"]
    class_class_curie: ClassVar[str] = "biolink:Cohort"
    class_name: ClassVar[str] = "cohort"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Cohort

    id: Union[str, CohortId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ExposureEvent(OntologyClass):
    """
    A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more
    phenotypic features of that organism, potentially mediated by genes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ExposureEvent"]
    class_class_curie: ClassVar[str] = "biolink:ExposureEvent"
    class_name: ClassVar[str] = "exposure event"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ExposureEvent

    id: Union[str, ExposureEventId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GenomicBackgroundExposure(Attribute):
    """
    A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or
    other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing
    an outcome.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenomicBackgroundExposure"]
    class_class_curie: ClassVar[str] = "biolink:GenomicBackgroundExposure"
    class_name: ClassVar[str] = "genomic background exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenomicBackgroundExposure

    id: Union[str, GenomicBackgroundExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None
    has_gene_or_gene_product: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None
    in_taxon: Optional[Union[Union[str, OrganismTaxonId], list[Union[str, OrganismTaxonId]]]] = empty_list()
    in_taxon_label: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenomicBackgroundExposureId):
            self.id = GenomicBackgroundExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        if not isinstance(self.has_gene_or_gene_product, list):
            self.has_gene_or_gene_product = [self.has_gene_or_gene_product] if self.has_gene_or_gene_product is not None else []
        self.has_gene_or_gene_product = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene_or_gene_product]

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        if self.in_taxon_label is not None and not isinstance(self.in_taxon_label, LabelType):
            self.in_taxon_label = LabelType(self.in_taxon_label)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


class PathologicalEntityMixin(YAMLRoot):
    """
    A pathological (abnormal) structure or process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PathologicalEntityMixin"]
    class_class_curie: ClassVar[str] = "biolink:PathologicalEntityMixin"
    class_name: ClassVar[str] = "pathological entity mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PathologicalEntityMixin


@dataclass(repr=False)
class PathologicalProcess(BiologicalProcess):
    """
    A biologic function or a process having an abnormal or deleterious effect at the subcellular, cellular,
    multicellular, or organismal level.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon", "has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["PathologicalProcess"]
    class_class_curie: ClassVar[str] = "biolink:PathologicalProcess"
    class_name: ClassVar[str] = "pathological process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PathologicalProcess

    id: Union[str, PathologicalProcessId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathologicalProcessId):
            self.id = PathologicalProcessId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PathologicalProcessExposure(Attribute):
    """
    A pathological process, when viewed as an exposure, representing a precondition, leading to or influencing an
    outcome, e.g. autoimmunity leading to disease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PathologicalProcessExposure"]
    class_class_curie: ClassVar[str] = "biolink:PathologicalProcessExposure"
    class_name: ClassVar[str] = "pathological process exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PathologicalProcessExposure

    id: Union[str, PathologicalProcessExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathologicalProcessExposureId):
            self.id = PathologicalProcessExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PathologicalAnatomicalStructure(AnatomicalEntity):
    """
    An anatomical structure with the potential of have an abnormal or deleterious effect at the subcellular, cellular,
    multicellular, or organismal level.
    """
    _inherited_slots: ClassVar[list[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK["PathologicalAnatomicalStructure"]
    class_class_curie: ClassVar[str] = "biolink:PathologicalAnatomicalStructure"
    class_name: ClassVar[str] = "pathological anatomical structure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PathologicalAnatomicalStructure

    id: Union[str, PathologicalAnatomicalStructureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathologicalAnatomicalStructureId):
            self.id = PathologicalAnatomicalStructureId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PathologicalAnatomicalExposure(Attribute):
    """
    An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or
    influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PathologicalAnatomicalExposure"]
    class_class_curie: ClassVar[str] = "biolink:PathologicalAnatomicalExposure"
    class_name: ClassVar[str] = "pathological anatomical exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PathologicalAnatomicalExposure

    id: Union[str, PathologicalAnatomicalExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathologicalAnatomicalExposureId):
            self.id = PathologicalAnatomicalExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DiseaseOrPhenotypicFeatureExposure(Attribute):
    """
    A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or
    influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin
    pigmentation predisposing an individual to skin cancer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseOrPhenotypicFeatureExposure"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureExposure"
    class_name: ClassVar[str] = "disease or phenotypic feature exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureExposure

    id: Union[str, DiseaseOrPhenotypicFeatureExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureExposureId):
            self.id = DiseaseOrPhenotypicFeatureExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalExposure(Attribute):
    """
    A chemical exposure is an intake of a particular chemical entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalExposure"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalExposure"
    class_name: ClassVar[str] = "chemical exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalExposure

    id: Union[str, ChemicalExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    has_quantitative_value: Optional[Union[Union[dict, QuantityValue], list[Union[dict, QuantityValue]]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalExposureId):
            self.id = ChemicalExposureId(self.id)

        if not isinstance(self.has_quantitative_value, list):
            self.has_quantitative_value = [self.has_quantitative_value] if self.has_quantitative_value is not None else []
        self.has_quantitative_value = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.has_quantitative_value]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ComplexChemicalExposure(Attribute):
    """
    A complex chemical exposure is an intake of a chemical mixture (e.g. gasoline), other than a drug.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ComplexChemicalExposure"]
    class_class_curie: ClassVar[str] = "biolink:ComplexChemicalExposure"
    class_name: ClassVar[str] = "complex chemical exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ComplexChemicalExposure

    id: Union[str, ComplexChemicalExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComplexChemicalExposureId):
            self.id = ComplexChemicalExposureId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DrugExposure(ChemicalExposure):
    """
    A drug exposure is an intake of a particular drug.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DrugExposure"]
    class_class_curie: ClassVar[str] = "biolink:DrugExposure"
    class_name: ClassVar[str] = "drug exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DrugExposure

    id: Union[str, DrugExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DrugExposureId):
            self.id = DrugExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DrugToGeneInteractionExposure(DrugExposure):
    """
    drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are
    known to constitute an 'exposure' to the organism, leading to or influencing an outcome.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DrugToGeneInteractionExposure"]
    class_class_curie: ClassVar[str] = "biolink:DrugToGeneInteractionExposure"
    class_name: ClassVar[str] = "drug to gene interaction exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DrugToGeneInteractionExposure

    id: Union[str, DrugToGeneInteractionExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    has_gene_or_gene_product: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DrugToGeneInteractionExposureId):
            self.id = DrugToGeneInteractionExposureId(self.id)

        if not isinstance(self.has_gene_or_gene_product, list):
            self.has_gene_or_gene_product = [self.has_gene_or_gene_product] if self.has_gene_or_gene_product is not None else []
        self.has_gene_or_gene_product = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene_or_gene_product]

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class Treatment(NamedThing):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices
    and/or procedures
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Treatment"]
    class_class_curie: ClassVar[str] = "biolink:Treatment"
    class_name: ClassVar[str] = "treatment"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Treatment

    id: Union[str, TreatmentId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_drug: Optional[Union[Union[str, DrugId], list[Union[str, DrugId]]]] = empty_list()
    has_device: Optional[Union[Union[str, DeviceId], list[Union[str, DeviceId]]]] = empty_list()
    has_procedure: Optional[Union[Union[str, ProcedureId], list[Union[str, ProcedureId]]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TreatmentId):
            self.id = TreatmentId(self.id)

        if not isinstance(self.has_drug, list):
            self.has_drug = [self.has_drug] if self.has_drug is not None else []
        self.has_drug = [v if isinstance(v, DrugId) else DrugId(v) for v in self.has_drug]

        if not isinstance(self.has_device, list):
            self.has_device = [self.has_device] if self.has_device is not None else []
        self.has_device = [v if isinstance(v, DeviceId) else DeviceId(v) for v in self.has_device]

        if not isinstance(self.has_procedure, list):
            self.has_procedure = [self.has_procedure] if self.has_procedure is not None else []
        self.has_procedure = [v if isinstance(v, ProcedureId) else ProcedureId(v) for v in self.has_procedure]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class BioticExposure(Attribute):
    """
    An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["BioticExposure"]
    class_class_curie: ClassVar[str] = "biolink:BioticExposure"
    class_name: ClassVar[str] = "biotic exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BioticExposure

    id: Union[str, BioticExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BioticExposureId):
            self.id = BioticExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class EnvironmentalExposure(Attribute):
    """
    A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B),
    atmospheric (heat, cold, general pollution) and water-born contaminants.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EnvironmentalExposure"]
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalExposure"
    class_name: ClassVar[str] = "environmental exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalExposure

    id: Union[str, EnvironmentalExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalExposureId):
            self.id = EnvironmentalExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeographicExposure(EnvironmentalExposure):
    """
    A geographic exposure is a factor relating to geographic proximity to some impactful entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeographicExposure"]
    class_class_curie: ClassVar[str] = "biolink:GeographicExposure"
    class_name: ClassVar[str] = "geographic exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeographicExposure

    id: Union[str, GeographicExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicExposureId):
            self.id = GeographicExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class BehavioralExposure(Attribute):
    """
    A behavioral exposure is a factor relating to behavior impacting an individual.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["BehavioralExposure"]
    class_class_curie: ClassVar[str] = "biolink:BehavioralExposure"
    class_name: ClassVar[str] = "behavioral exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BehavioralExposure

    id: Union[str, BehavioralExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehavioralExposureId):
            self.id = BehavioralExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class SocioeconomicExposure(Attribute):
    """
    A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g.
    poverty).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SocioeconomicExposure"]
    class_class_curie: ClassVar[str] = "biolink:SocioeconomicExposure"
    class_name: ClassVar[str] = "socioeconomic exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SocioeconomicExposure

    id: Union[str, SocioeconomicExposureId] = None
    category: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    has_attribute: Union[Union[str, SocioeconomicAttributeId], list[Union[str, SocioeconomicAttributeId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SocioeconomicExposureId):
            self.id = SocioeconomicExposureId(self.id)

        if self._is_empty(self.has_attribute):
            self.MissingRequiredField("has_attribute")
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, SocioeconomicAttributeId) else SocioeconomicAttributeId(v) for v in self.has_attribute]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


class Outcome(YAMLRoot):
    """
    An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of
    various categories of possible biological or non-biological (e.g. clinical) outcomes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Outcome"]
    class_class_curie: ClassVar[str] = "biolink:Outcome"
    class_name: ClassVar[str] = "outcome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Outcome


class PathologicalProcessOutcome(YAMLRoot):
    """
    An outcome resulting from an exposure event which is the manifestation of a pathological process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PathologicalProcessOutcome"]
    class_class_curie: ClassVar[str] = "biolink:PathologicalProcessOutcome"
    class_name: ClassVar[str] = "pathological process outcome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PathologicalProcessOutcome


class PathologicalAnatomicalOutcome(YAMLRoot):
    """
    An outcome resulting from an exposure event which is the manifestation of an abnormal anatomical structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PathologicalAnatomicalOutcome"]
    class_class_curie: ClassVar[str] = "biolink:PathologicalAnatomicalOutcome"
    class_name: ClassVar[str] = "pathological anatomical outcome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PathologicalAnatomicalOutcome


class DiseaseOrPhenotypicFeatureOutcome(YAMLRoot):
    """
    Physiological outcomes resulting from an exposure event which is the manifestation of a disease or other
    characteristic phenotype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseOrPhenotypicFeatureOutcome"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureOutcome"
    class_name: ClassVar[str] = "disease or phenotypic feature outcome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureOutcome


class BehavioralOutcome(YAMLRoot):
    """
    An outcome resulting from an exposure event which is the manifestation of human behavior.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["BehavioralOutcome"]
    class_class_curie: ClassVar[str] = "biolink:BehavioralOutcome"
    class_name: ClassVar[str] = "behavioral outcome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BehavioralOutcome


class HospitalizationOutcome(YAMLRoot):
    """
    An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room
    visit) or chronic (inpatient) hospitalization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["HospitalizationOutcome"]
    class_class_curie: ClassVar[str] = "biolink:HospitalizationOutcome"
    class_name: ClassVar[str] = "hospitalization outcome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.HospitalizationOutcome


class MortalityOutcome(YAMLRoot):
    """
    An outcome of death from resulting from an exposure event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MortalityOutcome"]
    class_class_curie: ClassVar[str] = "biolink:MortalityOutcome"
    class_name: ClassVar[str] = "mortality outcome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MortalityOutcome


class EpidemiologicalOutcome(YAMLRoot):
    """
    An epidemiological outcome, such as societal disease burden, resulting from an exposure event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EpidemiologicalOutcome"]
    class_class_curie: ClassVar[str] = "biolink:EpidemiologicalOutcome"
    class_name: ClassVar[str] = "epidemiological outcome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EpidemiologicalOutcome


class SocioeconomicOutcome(YAMLRoot):
    """
    An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure
    event
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SocioeconomicOutcome"]
    class_class_curie: ClassVar[str] = "biolink:SocioeconomicOutcome"
    class_name: ClassVar[str] = "socioeconomic outcome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SocioeconomicOutcome


@dataclass(repr=False)
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Association"]
    class_class_curie: ClassVar[str] = "biolink:Association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Association

    id: Union[str, AssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    negated: Optional[Union[bool, Bool]] = None
    qualifier: Optional[str] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]] = empty_list()
    publications: Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]] = empty_list()
    sources: Optional[Union[dict[Union[str, RetrievalSourceId], Union[dict, RetrievalSource]], list[Union[dict, RetrievalSource]]]] = empty_dict()
    has_evidence: Optional[Union[Union[str, EvidenceTypeId], list[Union[str, EvidenceTypeId]]]] = empty_list()
    knowledge_source: Optional[str] = None
    primary_knowledge_source: Optional[str] = None
    aggregator_knowledge_source: Optional[Union[str, list[str]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None
    original_subject: Optional[str] = None
    original_predicate: Optional[Union[str, URIorCURIE]] = None
    original_object: Optional[str] = None
    subject_category: Optional[Union[str, OntologyClassId]] = None
    object_category: Optional[Union[str, OntologyClassId]] = None
    subject_closure: Optional[Union[str, list[str]]] = empty_list()
    object_closure: Optional[Union[str, list[str]]] = empty_list()
    subject_category_closure: Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]] = empty_list()
    object_category_closure: Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]] = empty_list()
    subject_namespace: Optional[str] = None
    object_namespace: Optional[str] = None
    subject_label_closure: Optional[Union[str, list[str]]] = empty_list()
    object_label_closure: Optional[Union[str, list[str]]] = empty_list()
    retrieval_source_ids: Optional[Union[Union[str, RetrievalSourceId], list[Union[str, RetrievalSourceId]]]] = empty_list()
    p_value: Optional[float] = None
    adjusted_p_value: Optional[float] = None
    has_supporting_studies: Optional[Union[Union[str, StudyId], list[Union[str, StudyId]]]] = empty_list()
    type: Optional[Union[str, list[str]]] = empty_list()
    category: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.knowledge_level):
            self.MissingRequiredField("knowledge_level")
        if not isinstance(self.knowledge_level, KnowledgeLevelEnum):
            self.knowledge_level = KnowledgeLevelEnum(self.knowledge_level)

        if self._is_empty(self.agent_type):
            self.MissingRequiredField("agent_type")
        if not isinstance(self.agent_type, AgentTypeEnum):
            self.agent_type = AgentTypeEnum(self.agent_type)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.qualifier is not None and not isinstance(self.qualifier, str):
            self.qualifier = str(self.qualifier)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.publications]

        self._normalize_inlined_as_list(slot_name="sources", slot_type=RetrievalSource, key_name="id", keyed=True)

        if not isinstance(self.has_evidence, list):
            self.has_evidence = [self.has_evidence] if self.has_evidence is not None else []
        self.has_evidence = [v if isinstance(v, EvidenceTypeId) else EvidenceTypeId(v) for v in self.has_evidence]

        if self.knowledge_source is not None and not isinstance(self.knowledge_source, str):
            self.knowledge_source = str(self.knowledge_source)

        if self.primary_knowledge_source is not None and not isinstance(self.primary_knowledge_source, str):
            self.primary_knowledge_source = str(self.primary_knowledge_source)

        if not isinstance(self.aggregator_knowledge_source, list):
            self.aggregator_knowledge_source = [self.aggregator_knowledge_source] if self.aggregator_knowledge_source is not None else []
        self.aggregator_knowledge_source = [v if isinstance(v, str) else str(v) for v in self.aggregator_knowledge_source]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        if self.original_subject is not None and not isinstance(self.original_subject, str):
            self.original_subject = str(self.original_subject)

        if self.original_predicate is not None and not isinstance(self.original_predicate, URIorCURIE):
            self.original_predicate = URIorCURIE(self.original_predicate)

        if self.original_object is not None and not isinstance(self.original_object, str):
            self.original_object = str(self.original_object)

        if self.subject_category is not None and not isinstance(self.subject_category, OntologyClassId):
            self.subject_category = OntologyClassId(self.subject_category)

        if self.object_category is not None and not isinstance(self.object_category, OntologyClassId):
            self.object_category = OntologyClassId(self.object_category)

        if not isinstance(self.subject_closure, list):
            self.subject_closure = [self.subject_closure] if self.subject_closure is not None else []
        self.subject_closure = [v if isinstance(v, str) else str(v) for v in self.subject_closure]

        if not isinstance(self.object_closure, list):
            self.object_closure = [self.object_closure] if self.object_closure is not None else []
        self.object_closure = [v if isinstance(v, str) else str(v) for v in self.object_closure]

        if not isinstance(self.subject_category_closure, list):
            self.subject_category_closure = [self.subject_category_closure] if self.subject_category_closure is not None else []
        self.subject_category_closure = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subject_category_closure]

        if not isinstance(self.object_category_closure, list):
            self.object_category_closure = [self.object_category_closure] if self.object_category_closure is not None else []
        self.object_category_closure = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.object_category_closure]

        if self.subject_namespace is not None and not isinstance(self.subject_namespace, str):
            self.subject_namespace = str(self.subject_namespace)

        if self.object_namespace is not None and not isinstance(self.object_namespace, str):
            self.object_namespace = str(self.object_namespace)

        if not isinstance(self.subject_label_closure, list):
            self.subject_label_closure = [self.subject_label_closure] if self.subject_label_closure is not None else []
        self.subject_label_closure = [v if isinstance(v, str) else str(v) for v in self.subject_label_closure]

        if not isinstance(self.object_label_closure, list):
            self.object_label_closure = [self.object_label_closure] if self.object_label_closure is not None else []
        self.object_label_closure = [v if isinstance(v, str) else str(v) for v in self.object_label_closure]

        if not isinstance(self.retrieval_source_ids, list):
            self.retrieval_source_ids = [self.retrieval_source_ids] if self.retrieval_source_ids is not None else []
        self.retrieval_source_ids = [v if isinstance(v, RetrievalSourceId) else RetrievalSourceId(v) for v in self.retrieval_source_ids]

        if self.p_value is not None and not isinstance(self.p_value, float):
            self.p_value = float(self.p_value)

        if self.adjusted_p_value is not None and not isinstance(self.adjusted_p_value, float):
            self.adjusted_p_value = float(self.adjusted_p_value)

        if not isinstance(self.has_supporting_studies, list):
            self.has_supporting_studies = [self.has_supporting_studies] if self.has_supporting_studies is not None else []
        self.has_supporting_studies = [v if isinstance(v, StudyId) else StudyId(v) for v in self.has_supporting_studies]

        if not isinstance(self.type, list):
            self.type = [self.type] if self.type is not None else []
        self.type = [v if isinstance(v, str) else str(v) for v in self.type]

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


    def __new__(cls, *args, **kwargs):

        type_designator = "category"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class DiseaseAssociatedWithResponseToChemicalEntityAssociation(Association):
    """
    A statistical association between a disease and a chemical entity where the chemical entity has a therapeutic or
    adverse effect on the disease progression, symptoms or outcomes in a patient, cell line, or any model system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseAssociatedWithResponseToChemicalEntityAssociation"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseAssociatedWithResponseToChemicalEntityAssociation"
    class_name: ClassVar[str] = "disease associated with response to chemical entity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseAssociatedWithResponseToChemicalEntityAssociation

    id: Union[str, DiseaseAssociatedWithResponseToChemicalEntityAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, DiseaseId] = None
    object: Union[str, ChemicalEntityId] = None
    predicate: Union[str, PredicateType] = None
    response_context_qualifier: Optional[Union[str, "ResponseEnum"]] = None
    response_target_context_qualifier: Optional[Union[str, "ResponseTargetEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseAssociatedWithResponseToChemicalEntityAssociationId):
            self.id = DiseaseAssociatedWithResponseToChemicalEntityAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ChemicalEntityId):
            self.object = ChemicalEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.response_context_qualifier is not None and not isinstance(self.response_context_qualifier, ResponseEnum):
            self.response_context_qualifier = ResponseEnum(self.response_context_qualifier)

        if self.response_target_context_qualifier is not None and not isinstance(self.response_target_context_qualifier, ResponseTargetEnum):
            self.response_target_context_qualifier = ResponseTargetEnum(self.response_target_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalEntityAssessesNamedThingAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalEntityAssessesNamedThingAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalEntityAssessesNamedThingAssociation"
    class_name: ClassVar[str] = "chemical entity assesses named thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalEntityAssessesNamedThingAssociation

    id: Union[str, ChemicalEntityAssessesNamedThingAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, ChemicalEntityId] = None
    object: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityAssessesNamedThingAssociationId):
            self.id = ChemicalEntityAssessesNamedThingAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ChemicalEntityId):
            self.subject = ChemicalEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ContributorAssociation(Association):
    """
    Any association between an entity (such as a publication) and various agents that contribute to its realisation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ContributorAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ContributorAssociation"
    class_name: ClassVar[str] = "contributor association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ContributorAssociation

    id: Union[str, ContributorAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, InformationContentEntityId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, AgentId] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContributorAssociationId):
            self.id = ContributorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, InformationContentEntityId):
            self.subject = InformationContentEntityId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AgentId):
            self.object = AgentId(self.object)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenotypeToGenotypePartAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GenotypeToGenotypePartAssociation"
    class_name: ClassVar[str] = "genotype to genotype part association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToGenotypePartAssociation

    id: Union[str, GenotypeToGenotypePartAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, GenotypeId] = None
    object: Union[str, GenotypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenotypeToGenotypePartAssociationId):
            self.id = GenotypeToGenotypePartAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GenotypeId):
            self.object = GenotypeId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single
    one. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenotypeToGeneAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GenotypeToGeneAssociation"
    class_name: ClassVar[str] = "genotype to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToGeneAssociation

    id: Union[str, GenotypeToGeneAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, GenotypeId] = None
    object: Union[str, GeneId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenotypeToGeneAssociationId):
            self.id = GenotypeToGeneAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenotypeToVariantAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GenotypeToVariantAssociation"
    class_name: ClassVar[str] = "genotype to variant association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToVariantAssociation

    id: Union[str, GenotypeToVariantAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, GenotypeId] = None
    object: Union[str, SequenceVariantId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenotypeToVariantAssociationId):
            self.id = GenotypeToVariantAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToGeneAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneAssociation"
    class_name: ClassVar[str] = "gene to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneAssociation

    id: Union[str, GeneToGeneAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[dict, GeneOrGeneProduct] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneOrGeneProduct):
            self.object = GeneOrGeneProduct(**as_dict(self.object))

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should
    differ) or paralogy (in which case the species may be the same)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToGeneHomologyAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneHomologyAssociation"
    class_name: ClassVar[str] = "gene to gene homology association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneHomologyAssociation

    id: Union[str, GeneToGeneHomologyAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    predicate: Union[str, PredicateType] = None
    object: Union[dict, GeneOrGeneProduct] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToGeneHomologyAssociationId):
            self.id = GeneToGeneHomologyAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneOrGeneProduct):
            self.object = GeneOrGeneProduct(**as_dict(self.object))

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneToGeneFamilyAssociation(Association):
    """
    Set membership of a gene in a family of genes related by common evolutionary ancestry usually inferred by sequence
    comparisons. The genes in a given family generally share common sequence motifs which generally map onto shared
    gene product structure-function relationships.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToGeneFamilyAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneFamilyAssociation"
    class_name: ClassVar[str] = "gene to gene family association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneFamilyAssociation

    id: Union[str, GeneToGeneFamilyAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, GeneId] = None
    object: Union[str, GeneFamilyId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToGeneFamilyAssociationId):
            self.id = GeneToGeneFamilyAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneFamilyId):
            self.object = GeneFamilyId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneExpressionMixin(YAMLRoot):
    """
    Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the
    expression occurs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneExpressionMixin"]
    class_class_curie: ClassVar[str] = "biolink:GeneExpressionMixin"
    class_name: ClassVar[str] = "gene expression mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneExpressionMixin

    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    expression_site: Optional[Union[str, AnatomicalEntityId]] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    phenotypic_state: Optional[Union[str, DiseaseOrPhenotypicFeatureId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.expression_site is not None and not isinstance(self.expression_site, AnatomicalEntityId):
            self.expression_site = AnatomicalEntityId(self.expression_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)

        if self.phenotypic_state is not None and not isinstance(self.phenotypic_state, DiseaseOrPhenotypicFeatureId):
            self.phenotypic_state = DiseaseOrPhenotypicFeatureId(self.phenotypic_state)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneToGeneCoexpressionAssociation(GeneToGeneAssociation):
    """
    Indicates that two genes are co-expressed, generally under the same conditions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToGeneCoexpressionAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneCoexpressionAssociation"
    class_name: ClassVar[str] = "gene to gene coexpression association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneCoexpressionAssociation

    id: Union[str, GeneToGeneCoexpressionAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[dict, GeneOrGeneProduct] = None
    predicate: Union[str, PredicateType] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    expression_site: Optional[Union[str, AnatomicalEntityId]] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    phenotypic_state: Optional[Union[str, DiseaseOrPhenotypicFeatureId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToGeneCoexpressionAssociationId):
            self.id = GeneToGeneCoexpressionAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.expression_site is not None and not isinstance(self.expression_site, AnatomicalEntityId):
            self.expression_site = AnatomicalEntityId(self.expression_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)

        if self.phenotypic_state is not None and not isinstance(self.phenotypic_state, DiseaseOrPhenotypicFeatureId):
            self.phenotypic_state = DiseaseOrPhenotypicFeatureId(self.phenotypic_state)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between
    genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PairwiseGeneToGeneInteraction"]
    class_class_curie: ClassVar[str] = "biolink:PairwiseGeneToGeneInteraction"
    class_name: ClassVar[str] = "pairwise gene to gene interaction"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PairwiseGeneToGeneInteraction

    id: Union[str, PairwiseGeneToGeneInteractionId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[dict, GeneOrGeneProduct] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PairwiseGeneToGeneInteractionId):
            self.id = PairwiseGeneToGeneInteractionId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PairwiseMolecularInteraction(PairwiseGeneToGeneInteraction):
    """
    An interaction at the molecular level between two physical entities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PairwiseMolecularInteraction"]
    class_class_curie: ClassVar[str] = "biolink:PairwiseMolecularInteraction"
    class_name: ClassVar[str] = "pairwise molecular interaction"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PairwiseMolecularInteraction

    id: Union[str, PairwiseMolecularInteractionId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, MolecularEntityId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, MolecularEntityId] = None
    interacting_molecules_category: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PairwiseMolecularInteractionId):
            self.id = PairwiseMolecularInteractionId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, MolecularEntityId):
            self.object = MolecularEntityId(self.object)

        if self.interacting_molecules_category is not None and not isinstance(self.interacting_molecules_category, OntologyClassId):
            self.interacting_molecules_category = OntologyClassId(self.interacting_molecules_category)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CellLineToEntityAssociationMixin(YAMLRoot):
    """
    An relationship between a cell line and another entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CellLineToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:CellLineToEntityAssociationMixin"
    class_name: ClassVar[str] = "cell line to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLineToEntityAssociationMixin

    subject: Union[str, CellLineId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellLineToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an
    individual with that disease or phenotype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CellLineToDiseaseOrPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:CellLineToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "cell line to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLineToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, CellLineToDiseaseOrPhenotypicFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    subject_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    object_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    anatomical_context_qualifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellLineToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = CellLineToDiseaseOrPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.subject_specialization_qualifier is not None and not isinstance(self.subject_specialization_qualifier, URIorCURIE):
            self.subject_specialization_qualifier = URIorCURIE(self.subject_specialization_qualifier)

        if self.object_specialization_qualifier is not None and not isinstance(self.object_specialization_qualifier, URIorCURIE):
            self.object_specialization_qualifier = URIorCURIE(self.object_specialization_qualifier)

        if self.anatomical_context_qualifier is not None and not isinstance(self.anatomical_context_qualifier, str):
            self.anatomical_context_qualifier = str(self.anatomical_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalEntityToEntityAssociationMixin(YAMLRoot):
    """
    An interaction between a chemical entity and another entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalEntityToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalEntityToEntityAssociationMixin"
    class_name: ClassVar[str] = "chemical entity to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalEntityToEntityAssociationMixin

    subject: Union[dict, ChemicalEntityOrGeneOrGeneProduct] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ChemicalEntityOrGeneOrGeneProduct):
            self.subject = ChemicalEntityOrGeneOrGeneProduct()

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugToEntityAssociationMixin(ChemicalEntityToEntityAssociationMixin):
    """
    An interaction between a drug and another entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DrugToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:DrugToEntityAssociationMixin"
    class_name: ClassVar[str] = "drug to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DrugToEntityAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalToEntityAssociationMixin(ChemicalEntityToEntityAssociationMixin):
    """
    An interaction between a chemical entity and another entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalToEntityAssociationMixin"
    class_name: ClassVar[str] = "chemical to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToEntityAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ChemicalEntityOrGeneOrGeneProduct):
            self.subject = ChemicalEntityOrGeneOrGeneProduct()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CaseToEntityAssociationMixin(YAMLRoot):
    """
    An abstract association for use where the case is the subject
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CaseToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:CaseToEntityAssociationMixin"
    class_name: ClassVar[str] = "case to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CaseToEntityAssociationMixin

    subject: Union[str, CaseId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalToChemicalAssociation(Association):
    """
    A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal
    edges, e.g. one chemical converted to another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalToChemicalAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalToChemicalAssociation"
    class_name: ClassVar[str] = "chemical to chemical association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToChemicalAssociation

    id: Union[str, ChemicalToChemicalAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ChemicalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalToChemicalAssociationId):
            self.id = ChemicalToChemicalAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ChemicalEntityId):
            self.object = ChemicalEntityId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ReactionToParticipantAssociation(ChemicalToChemicalAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ReactionToParticipantAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ReactionToParticipantAssociation"
    class_name: ClassVar[str] = "reaction to participant association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ReactionToParticipantAssociation

    id: Union[str, ReactionToParticipantAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ChemicalEntityId] = None
    subject: Union[str, MolecularEntityId] = None
    stoichiometry: Optional[int] = None
    reaction_direction: Optional[Union[str, "ReactionDirectionEnum"]] = None
    reaction_side: Optional[Union[str, "ReactionSideEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionToParticipantAssociationId):
            self.id = ReactionToParticipantAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)

        if self.stoichiometry is not None and not isinstance(self.stoichiometry, int):
            self.stoichiometry = int(self.stoichiometry)

        if self.reaction_direction is not None and not isinstance(self.reaction_direction, ReactionDirectionEnum):
            self.reaction_direction = ReactionDirectionEnum(self.reaction_direction)

        if self.reaction_side is not None and not isinstance(self.reaction_side, ReactionSideEnum):
            self.reaction_side = ReactionSideEnum(self.reaction_side)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ReactionToCatalystAssociation(ReactionToParticipantAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ReactionToCatalystAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ReactionToCatalystAssociation"
    class_name: ClassVar[str] = "reaction to catalyst association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ReactionToCatalystAssociation

    id: Union[str, ReactionToCatalystAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, MolecularEntityId] = None
    object: Union[dict, GeneOrGeneProduct] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionToCatalystAssociationId):
            self.id = ReactionToCatalystAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneOrGeneProduct):
            self.object = GeneOrGeneProduct(**as_dict(self.object))

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalToChemicalDerivationAssociation(ChemicalToChemicalAssociation):
    """
    A causal relationship between two chemical entities, where the subject represents the upstream entity and the
    object represents the downstream. For any such association there is an implicit reaction: IF R has-input C1 AND R
    has-output C2 AND R enabled-by P AND R type Reaction THEN C1 derives-into C2 catalyst qualifier P
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalToChemicalDerivationAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalToChemicalDerivationAssociation"
    class_name: ClassVar[str] = "chemical to chemical derivation association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToChemicalDerivationAssociation

    id: Union[str, ChemicalToChemicalDerivationAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, ChemicalEntityId] = None
    object: Union[str, ChemicalEntityId] = None
    predicate: Union[str, PredicateType] = None
    catalyst_qualifier: Optional[Union[Union[dict, MacromolecularMachineMixin], list[Union[dict, MacromolecularMachineMixin]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalToChemicalDerivationAssociationId):
            self.id = ChemicalToChemicalDerivationAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ChemicalEntityId):
            self.subject = ChemicalEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ChemicalEntityId):
            self.object = ChemicalEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if not isinstance(self.catalyst_qualifier, list):
            self.catalyst_qualifier = [self.catalyst_qualifier] if self.catalyst_qualifier is not None else []
        self.catalyst_qualifier = [v if isinstance(v, MacromolecularMachineMixin) else MacromolecularMachineMixin(**as_dict(v)) for v in self.catalyst_qualifier]

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise
    to or exacerbates the phenotype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalToDiseaseOrPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "chemical to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, ChemicalToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    subject_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    object_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    anatomical_context_qualifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = ChemicalToDiseaseOrPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.subject_specialization_qualifier is not None and not isinstance(self.subject_specialization_qualifier, URIorCURIE):
            self.subject_specialization_qualifier = URIorCURIE(self.subject_specialization_qualifier)

        if self.object_specialization_qualifier is not None and not isinstance(self.object_specialization_qualifier, URIorCURIE):
            self.object_specialization_qualifier = URIorCURIE(self.object_specialization_qualifier)

        if self.anatomical_context_qualifier is not None and not isinstance(self.anatomical_context_qualifier, str):
            self.anatomical_context_qualifier = str(self.anatomical_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic
    feature where the disease or phenotypic feature is a secondary undesirable effect.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "chemical or drug or treatment to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    FDA_adverse_event_level: Optional[Union[str, "FDAIDAAdverseEventEnum"]] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    subject_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    object_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    anatomical_context_qualifier: Optional[str] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.FDA_adverse_event_level is not None and not isinstance(self.FDA_adverse_event_level, FDAIDAAdverseEventEnum):
            self.FDA_adverse_event_level = FDAIDAAdverseEventEnum(self.FDA_adverse_event_level)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.subject_specialization_qualifier is not None and not isinstance(self.subject_specialization_qualifier, URIorCURIE):
            self.subject_specialization_qualifier = URIorCURIE(self.subject_specialization_qualifier)

        if self.object_specialization_qualifier is not None and not isinstance(self.object_specialization_qualifier, URIorCURIE):
            self.object_specialization_qualifier = URIorCURIE(self.object_specialization_qualifier)

        if self.anatomical_context_qualifier is not None and not isinstance(self.anatomical_context_qualifier, str):
            self.anatomical_context_qualifier = str(self.anatomical_context_qualifier)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation(ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation):
    """
    This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic
    feature where the disesae or phenotypic feature is a secondary, typically (but not always) undesirable effect.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "chemical or drug or treatment side effect disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    subject_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    object_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    anatomical_context_qualifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociationId):
            self.id = ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.subject_specialization_qualifier is not None and not isinstance(self.subject_specialization_qualifier, URIorCURIE):
            self.subject_specialization_qualifier = URIorCURIE(self.subject_specialization_qualifier)

        if self.object_specialization_qualifier is not None and not isinstance(self.object_specialization_qualifier, URIorCURIE):
            self.object_specialization_qualifier = URIorCURIE(self.object_specialization_qualifier)

        if self.anatomical_context_qualifier is not None and not isinstance(self.anatomical_context_qualifier, str):
            self.anatomical_context_qualifier = str(self.anatomical_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneToPathwayAssociation(Association):
    """
    An interaction between a gene or gene product and a biological process or pathway.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToPathwayAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneToPathwayAssociation"
    class_name: ClassVar[str] = "gene to pathway association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToPathwayAssociation

    id: Union[str, GeneToPathwayAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[str, PathwayId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToPathwayAssociationId):
            self.id = GeneToPathwayAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MolecularActivityToPathwayAssociation(Association):
    """
    Association that holds the relationship between a reaction and the pathway it participates in.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MolecularActivityToPathwayAssociation"]
    class_class_curie: ClassVar[str] = "biolink:MolecularActivityToPathwayAssociation"
    class_name: ClassVar[str] = "molecular activity to pathway association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularActivityToPathwayAssociation

    id: Union[str, MolecularActivityToPathwayAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, MolecularActivityId] = None
    object: Union[str, PathwayId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularActivityToPathwayAssociationId):
            self.id = MolecularActivityToPathwayAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, MolecularActivityId):
            self.subject = MolecularActivityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalToPathwayAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalToPathwayAssociation"
    class_name: ClassVar[str] = "chemical to pathway association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToPathwayAssociation

    id: Union[str, ChemicalToPathwayAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, ChemicalEntityId] = None
    object: Union[str, PathwayId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalToPathwayAssociationId):
            self.id = ChemicalToPathwayAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ChemicalEntityId):
            self.subject = ChemicalEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class NamedThingAssociatedWithLikelihoodOfNamedThingAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["NamedThingAssociatedWithLikelihoodOfNamedThingAssociation"]
    class_class_curie: ClassVar[str] = "biolink:NamedThingAssociatedWithLikelihoodOfNamedThingAssociation"
    class_name: ClassVar[str] = "named thing associated with likelihood of named thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NamedThingAssociatedWithLikelihoodOfNamedThingAssociation

    id: Union[str, NamedThingAssociatedWithLikelihoodOfNamedThingAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_context_qualifier: Optional[Union[str, OntologyClassId]] = None
    object_aspect_qualifier: Optional[str] = None
    object_context_qualifier: Optional[Union[str, OntologyClassId]] = None
    population_context_qualifier: Optional[Union[str, PopulationOfIndividualOrganismsId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingAssociatedWithLikelihoodOfNamedThingAssociationId):
            self.id = NamedThingAssociatedWithLikelihoodOfNamedThingAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_context_qualifier is not None and not isinstance(self.subject_context_qualifier, OntologyClassId):
            self.subject_context_qualifier = OntologyClassId(self.subject_context_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_context_qualifier is not None and not isinstance(self.object_context_qualifier, OntologyClassId):
            self.object_context_qualifier = OntologyClassId(self.object_context_qualifier)

        if self.population_context_qualifier is not None and not isinstance(self.population_context_qualifier, PopulationOfIndividualOrganismsId):
            self.population_context_qualifier = PopulationOfIndividualOrganismsId(self.population_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalGeneInteractionAssociation(Association):
    """
    describes a physical interaction between a chemical entity and a gene or gene product. Any biological or chemical
    effect resulting from such an interaction are out of scope, and covered by the ChemicalAffectsGeneAssociation type
    (e.g. impact of a chemical on the abundance, activity, structure, etc, of either participant in the interaction)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalGeneInteractionAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalGeneInteractionAssociation"
    class_name: ClassVar[str] = "chemical gene interaction association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalGeneInteractionAssociation

    id: Union[str, ChemicalGeneInteractionAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, ChemicalEntityId] = None
    object: Union[dict, GeneOrGeneProduct] = None
    predicate: Union[str, PredicateType] = None
    subject_form_or_variant_qualifier: Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]] = None
    subject_part_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]] = None
    subject_derivative_qualifier: Optional[Union[str, "ChemicalEntityDerivativeEnum"]] = None
    subject_context_qualifier: Optional[Union[str, AnatomicalEntityId]] = None
    object_form_or_variant_qualifier: Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]] = None
    object_part_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]] = None
    object_context_qualifier: Optional[Union[str, AnatomicalEntityId]] = None
    anatomical_context_qualifier: Optional[Union[str, AnatomicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalGeneInteractionAssociationId):
            self.id = ChemicalGeneInteractionAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ChemicalEntityId):
            self.subject = ChemicalEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneOrGeneProduct):
            self.object = GeneOrGeneProduct(**as_dict(self.object))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject_form_or_variant_qualifier is not None and not isinstance(self.subject_form_or_variant_qualifier, ChemicalOrGeneOrGeneProductFormOrVariantEnum):
            self.subject_form_or_variant_qualifier = ChemicalOrGeneOrGeneProductFormOrVariantEnum(self.subject_form_or_variant_qualifier)

        if self.subject_part_qualifier is not None and not isinstance(self.subject_part_qualifier, GeneOrGeneProductOrChemicalPartQualifierEnum):
            self.subject_part_qualifier = GeneOrGeneProductOrChemicalPartQualifierEnum(self.subject_part_qualifier)

        if self.subject_derivative_qualifier is not None and not isinstance(self.subject_derivative_qualifier, ChemicalEntityDerivativeEnum):
            self.subject_derivative_qualifier = ChemicalEntityDerivativeEnum(self.subject_derivative_qualifier)

        if self.subject_context_qualifier is not None and not isinstance(self.subject_context_qualifier, AnatomicalEntityId):
            self.subject_context_qualifier = AnatomicalEntityId(self.subject_context_qualifier)

        if self.object_form_or_variant_qualifier is not None and not isinstance(self.object_form_or_variant_qualifier, ChemicalOrGeneOrGeneProductFormOrVariantEnum):
            self.object_form_or_variant_qualifier = ChemicalOrGeneOrGeneProductFormOrVariantEnum(self.object_form_or_variant_qualifier)

        if self.object_part_qualifier is not None and not isinstance(self.object_part_qualifier, GeneOrGeneProductOrChemicalPartQualifierEnum):
            self.object_part_qualifier = GeneOrGeneProductOrChemicalPartQualifierEnum(self.object_part_qualifier)

        if self.object_context_qualifier is not None and not isinstance(self.object_context_qualifier, AnatomicalEntityId):
            self.object_context_qualifier = AnatomicalEntityId(self.object_context_qualifier)

        if self.anatomical_context_qualifier is not None and not isinstance(self.anatomical_context_qualifier, AnatomicalEntityId):
            self.anatomical_context_qualifier = AnatomicalEntityId(self.anatomical_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneRegulatesGeneAssociation(Association):
    """
    Describes a regulatory relationship between two genes or gene products.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneRegulatesGeneAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneRegulatesGeneAssociation"
    class_name: ClassVar[str] = "gene regulates gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneRegulatesGeneAssociation

    id: Union[str, GeneRegulatesGeneAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    object_aspect_qualifier: Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"] = None
    object_direction_qualifier: Union[str, "DirectionQualifierEnum"] = None
    qualified_predicate: str = None
    subject: Union[dict, GeneOrGeneProduct] = None
    predicate: Union[str, PredicateType] = None
    object: Union[dict, GeneOrGeneProduct] = None
    species_context_qualifier: Optional[Union[str, OrganismTaxonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneRegulatesGeneAssociationId):
            self.id = GeneRegulatesGeneAssociationId(self.id)

        if self._is_empty(self.object_aspect_qualifier):
            self.MissingRequiredField("object_aspect_qualifier")
        if not isinstance(self.object_aspect_qualifier, GeneOrGeneProductOrChemicalEntityAspectEnum):
            self.object_aspect_qualifier = GeneOrGeneProductOrChemicalEntityAspectEnum(self.object_aspect_qualifier)

        if self._is_empty(self.object_direction_qualifier):
            self.MissingRequiredField("object_direction_qualifier")
        if not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self._is_empty(self.qualified_predicate):
            self.MissingRequiredField("qualified_predicate")
        if not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneOrGeneProduct):
            self.object = GeneOrGeneProduct(**as_dict(self.object))

        if self.species_context_qualifier is not None and not isinstance(self.species_context_qualifier, OrganismTaxonId):
            self.species_context_qualifier = OrganismTaxonId(self.species_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ProcessRegulatesProcessAssociation(Association):
    """
    Describes a regulatory relationship between two genes or gene products.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ProcessRegulatesProcessAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ProcessRegulatesProcessAssociation"
    class_name: ClassVar[str] = "process regulates process association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ProcessRegulatesProcessAssociation

    id: Union[str, ProcessRegulatesProcessAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, BiologicalProcessId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, BiologicalProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessRegulatesProcessAssociationId):
            self.id = ProcessRegulatesProcessAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, BiologicalProcessId):
            self.subject = BiologicalProcessId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalAffectsGeneAssociation(Association):
    """
    Describes an effect that a chemical has on a gene or gene product (e.g. an impact of on its abundance,
    activity,localization, processing, expression, etc.)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalAffectsGeneAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalAffectsGeneAssociation"
    class_name: ClassVar[str] = "chemical affects gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalAffectsGeneAssociation

    id: Union[str, ChemicalAffectsGeneAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, ChemicalEntityId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[dict, GeneOrGeneProduct] = None
    subject_form_or_variant_qualifier: Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]] = None
    subject_part_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]] = None
    subject_derivative_qualifier: Optional[Union[str, "ChemicalEntityDerivativeEnum"]] = None
    subject_aspect_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"]] = None
    subject_context_qualifier: Optional[Union[str, AnatomicalEntityId]] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_form_or_variant_qualifier: Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]] = None
    object_part_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]] = None
    object_aspect_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"]] = None
    object_context_qualifier: Optional[Union[str, AnatomicalEntityId]] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    causal_mechanism_qualifier: Optional[Union[str, "CausalMechanismQualifierEnum"]] = None
    anatomical_context_qualifier: Optional[Union[str, AnatomicalEntityId]] = None
    qualified_predicate: Optional[str] = None
    species_context_qualifier: Optional[Union[str, OrganismTaxonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalAffectsGeneAssociationId):
            self.id = ChemicalAffectsGeneAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ChemicalEntityId):
            self.subject = ChemicalEntityId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneOrGeneProduct):
            self.object = GeneOrGeneProduct(**as_dict(self.object))

        if self.subject_form_or_variant_qualifier is not None and not isinstance(self.subject_form_or_variant_qualifier, ChemicalOrGeneOrGeneProductFormOrVariantEnum):
            self.subject_form_or_variant_qualifier = ChemicalOrGeneOrGeneProductFormOrVariantEnum(self.subject_form_or_variant_qualifier)

        if self.subject_part_qualifier is not None and not isinstance(self.subject_part_qualifier, GeneOrGeneProductOrChemicalPartQualifierEnum):
            self.subject_part_qualifier = GeneOrGeneProductOrChemicalPartQualifierEnum(self.subject_part_qualifier)

        if self.subject_derivative_qualifier is not None and not isinstance(self.subject_derivative_qualifier, ChemicalEntityDerivativeEnum):
            self.subject_derivative_qualifier = ChemicalEntityDerivativeEnum(self.subject_derivative_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, GeneOrGeneProductOrChemicalEntityAspectEnum):
            self.subject_aspect_qualifier = GeneOrGeneProductOrChemicalEntityAspectEnum(self.subject_aspect_qualifier)

        if self.subject_context_qualifier is not None and not isinstance(self.subject_context_qualifier, AnatomicalEntityId):
            self.subject_context_qualifier = AnatomicalEntityId(self.subject_context_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_form_or_variant_qualifier is not None and not isinstance(self.object_form_or_variant_qualifier, ChemicalOrGeneOrGeneProductFormOrVariantEnum):
            self.object_form_or_variant_qualifier = ChemicalOrGeneOrGeneProductFormOrVariantEnum(self.object_form_or_variant_qualifier)

        if self.object_part_qualifier is not None and not isinstance(self.object_part_qualifier, GeneOrGeneProductOrChemicalPartQualifierEnum):
            self.object_part_qualifier = GeneOrGeneProductOrChemicalPartQualifierEnum(self.object_part_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, GeneOrGeneProductOrChemicalEntityAspectEnum):
            self.object_aspect_qualifier = GeneOrGeneProductOrChemicalEntityAspectEnum(self.object_aspect_qualifier)

        if self.object_context_qualifier is not None and not isinstance(self.object_context_qualifier, AnatomicalEntityId):
            self.object_context_qualifier = AnatomicalEntityId(self.object_context_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.causal_mechanism_qualifier is not None and not isinstance(self.causal_mechanism_qualifier, CausalMechanismQualifierEnum):
            self.causal_mechanism_qualifier = CausalMechanismQualifierEnum(self.causal_mechanism_qualifier)

        if self.anatomical_context_qualifier is not None and not isinstance(self.anatomical_context_qualifier, AnatomicalEntityId):
            self.anatomical_context_qualifier = AnatomicalEntityId(self.anatomical_context_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.species_context_qualifier is not None and not isinstance(self.species_context_qualifier, OrganismTaxonId):
            self.species_context_qualifier = OrganismTaxonId(self.species_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneAffectsChemicalAssociation(Association):
    """
    Describes an effect that a gene or gene product has on a chemical entity (e.g. an impact of on its abundance,
    activity, localization, processing, transport, etc.)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneAffectsChemicalAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneAffectsChemicalAssociation"
    class_name: ClassVar[str] = "gene affects chemical association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneAffectsChemicalAssociation

    id: Union[str, GeneAffectsChemicalAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ChemicalEntityId] = None
    subject_form_or_variant_qualifier: Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]] = None
    subject_part_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]] = None
    subject_derivative_qualifier: Optional[str] = None
    subject_aspect_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"]] = None
    subject_context_qualifier: Optional[Union[str, AnatomicalEntityId]] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_form_or_variant_qualifier: Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]] = None
    object_part_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]] = None
    object_aspect_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"]] = None
    object_context_qualifier: Optional[Union[str, AnatomicalEntityId]] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_derivative_qualifier: Optional[Union[str, "ChemicalEntityDerivativeEnum"]] = None
    causal_mechanism_qualifier: Optional[Union[str, "CausalMechanismQualifierEnum"]] = None
    anatomical_context_qualifier: Optional[Union[str, AnatomicalEntityId]] = None
    qualified_predicate: Optional[str] = None
    species_context_qualifier: Optional[Union[str, OrganismTaxonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneAffectsChemicalAssociationId):
            self.id = GeneAffectsChemicalAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ChemicalEntityId):
            self.object = ChemicalEntityId(self.object)

        if self.subject_form_or_variant_qualifier is not None and not isinstance(self.subject_form_or_variant_qualifier, ChemicalOrGeneOrGeneProductFormOrVariantEnum):
            self.subject_form_or_variant_qualifier = ChemicalOrGeneOrGeneProductFormOrVariantEnum(self.subject_form_or_variant_qualifier)

        if self.subject_part_qualifier is not None and not isinstance(self.subject_part_qualifier, GeneOrGeneProductOrChemicalPartQualifierEnum):
            self.subject_part_qualifier = GeneOrGeneProductOrChemicalPartQualifierEnum(self.subject_part_qualifier)

        if self.subject_derivative_qualifier is not None and not isinstance(self.subject_derivative_qualifier, str):
            self.subject_derivative_qualifier = str(self.subject_derivative_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, GeneOrGeneProductOrChemicalEntityAspectEnum):
            self.subject_aspect_qualifier = GeneOrGeneProductOrChemicalEntityAspectEnum(self.subject_aspect_qualifier)

        if self.subject_context_qualifier is not None and not isinstance(self.subject_context_qualifier, AnatomicalEntityId):
            self.subject_context_qualifier = AnatomicalEntityId(self.subject_context_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_form_or_variant_qualifier is not None and not isinstance(self.object_form_or_variant_qualifier, ChemicalOrGeneOrGeneProductFormOrVariantEnum):
            self.object_form_or_variant_qualifier = ChemicalOrGeneOrGeneProductFormOrVariantEnum(self.object_form_or_variant_qualifier)

        if self.object_part_qualifier is not None and not isinstance(self.object_part_qualifier, GeneOrGeneProductOrChemicalPartQualifierEnum):
            self.object_part_qualifier = GeneOrGeneProductOrChemicalPartQualifierEnum(self.object_part_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, GeneOrGeneProductOrChemicalEntityAspectEnum):
            self.object_aspect_qualifier = GeneOrGeneProductOrChemicalEntityAspectEnum(self.object_aspect_qualifier)

        if self.object_context_qualifier is not None and not isinstance(self.object_context_qualifier, AnatomicalEntityId):
            self.object_context_qualifier = AnatomicalEntityId(self.object_context_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.object_derivative_qualifier is not None and not isinstance(self.object_derivative_qualifier, ChemicalEntityDerivativeEnum):
            self.object_derivative_qualifier = ChemicalEntityDerivativeEnum(self.object_derivative_qualifier)

        if self.causal_mechanism_qualifier is not None and not isinstance(self.causal_mechanism_qualifier, CausalMechanismQualifierEnum):
            self.causal_mechanism_qualifier = CausalMechanismQualifierEnum(self.causal_mechanism_qualifier)

        if self.anatomical_context_qualifier is not None and not isinstance(self.anatomical_context_qualifier, AnatomicalEntityId):
            self.anatomical_context_qualifier = AnatomicalEntityId(self.anatomical_context_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.species_context_qualifier is not None and not isinstance(self.species_context_qualifier, OrganismTaxonId):
            self.species_context_qualifier = OrganismTaxonId(self.species_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DrugToGeneAssociation(Association):
    """
    An interaction between a drug and a gene or gene product.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DrugToGeneAssociation"]
    class_class_curie: ClassVar[str] = "biolink:DrugToGeneAssociation"
    class_name: ClassVar[str] = "drug to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DrugToGeneAssociation

    id: Union[str, DrugToGeneAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    object: Union[dict, GeneOrGeneProduct] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DrugToGeneAssociationId):
            self.id = DrugToGeneAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneOrGeneProduct):
            self.object = GeneOrGeneProduct(**as_dict(self.object))

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MaterialSampleToEntityAssociationMixin(YAMLRoot):
    """
    An association between a material sample and something.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MaterialSampleToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:MaterialSampleToEntityAssociationMixin"
    class_name: ClassVar[str] = "material sample to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleToEntityAssociationMixin

    subject: Union[str, MaterialSampleId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, MaterialSampleId):
            self.subject = MaterialSampleId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialSampleDerivationAssociation(Association):
    """
    An association between a material sample and the material entity from which it is derived.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MaterialSampleDerivationAssociation"]
    class_class_curie: ClassVar[str] = "biolink:MaterialSampleDerivationAssociation"
    class_name: ClassVar[str] = "material sample derivation association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleDerivationAssociation

    id: Union[str, MaterialSampleDerivationAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, MaterialSampleId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialSampleDerivationAssociationId):
            self.id = MaterialSampleDerivationAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, MaterialSampleId):
            self.subject = MaterialSampleId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MaterialSampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a material sample and a disease or phenotype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MaterialSampleToDiseaseOrPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:MaterialSampleToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "material sample to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    subject_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    object_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    anatomical_context_qualifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.subject_specialization_qualifier is not None and not isinstance(self.subject_specialization_qualifier, URIorCURIE):
            self.subject_specialization_qualifier = URIorCURIE(self.subject_specialization_qualifier)

        if self.object_specialization_qualifier is not None and not isinstance(self.object_specialization_qualifier, URIorCURIE):
            self.object_specialization_qualifier = URIorCURIE(self.object_specialization_qualifier)

        if self.anatomical_context_qualifier is not None and not isinstance(self.anatomical_context_qualifier, str):
            self.anatomical_context_qualifier = str(self.anatomical_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DiseaseToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseToEntityAssociationMixin"
    class_name: ClassVar[str] = "disease to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseToEntityAssociationMixin

    subject: Union[str, DiseaseId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityToExposureEventAssociationMixin(YAMLRoot):
    """
    An association between some entity and an exposure event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EntityToExposureEventAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:EntityToExposureEventAssociationMixin"
    class_name: ClassVar[str] = "entity to exposure event association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToExposureEventAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ExposureEventId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ExposureEventId):
            self.object = ExposureEventId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseToExposureEventAssociation(Association):
    """
    An association between an exposure event and a disease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseToExposureEventAssociation"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseToExposureEventAssociation"
    class_name: ClassVar[str] = "disease to exposure event association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseToExposureEventAssociation

    id: Union[str, DiseaseToExposureEventAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseToExposureEventAssociationId):
            self.id = DiseaseToExposureEventAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class EntityToOutcomeAssociationMixin(YAMLRoot):
    """
    An association between some entity and an outcome
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EntityToOutcomeAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:EntityToOutcomeAssociationMixin"
    class_name: ClassVar[str] = "entity to outcome association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToOutcomeAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[dict, Outcome] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, Outcome):
            self.object = Outcome()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureEventToOutcomeAssociation(Association):
    """
    An association between an exposure event and an outcome.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ExposureEventToOutcomeAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ExposureEventToOutcomeAssociation"
    class_name: ClassVar[str] = "exposure event to outcome association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ExposureEventToOutcomeAssociation

    id: Union[str, ExposureEventToOutcomeAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    population_context_qualifier: Optional[Union[str, PopulationOfIndividualOrganismsId]] = None
    temporal_context_qualifier: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventToOutcomeAssociationId):
            self.id = ExposureEventToOutcomeAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.population_context_qualifier is not None and not isinstance(self.population_context_qualifier, PopulationOfIndividualOrganismsId):
            self.population_context_qualifier = PopulationOfIndividualOrganismsId(self.population_context_qualifier)

        if self.temporal_context_qualifier is not None and not isinstance(self.temporal_context_qualifier, TimeType):
            self.temporal_context_qualifier = TimeType(self.temporal_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class FrequencyQualifierMixin(YAMLRoot):
    """
    Qualifier for frequency type associations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["FrequencyQualifierMixin"]
    class_class_curie: ClassVar[str] = "biolink:FrequencyQualifierMixin"
    class_name: ClassVar[str] = "frequency qualifier mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FrequencyQualifierMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityToFeatureOrDiseaseQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to disease or phenotype associations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EntityToFeatureOrDiseaseQualifiersMixin"]
    class_class_curie: ClassVar[str] = "biolink:EntityToFeatureOrDiseaseQualifiersMixin"
    class_name: ClassVar[str] = "entity to feature or disease qualifiers mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToFeatureOrDiseaseQualifiersMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityToFeatureOrVariantQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to variant associations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EntityToFeatureOrVariantQualifiersMixin"]
    class_class_curie: ClassVar[str] = "biolink:EntityToFeatureOrVariantQualifiersMixin"
    class_name: ClassVar[str] = "entity to feature or variant qualifiers mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToFeatureOrVariantQualifiersMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityToFeatureOrGeneQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to gene associations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EntityToFeatureOrGeneQualifiersMixin"]
    class_class_curie: ClassVar[str] = "biolink:EntityToFeatureOrGeneQualifiersMixin"
    class_name: ClassVar[str] = "entity to feature or gene qualifiers mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToFeatureOrGeneQualifiersMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FeatureOrDiseaseQualifiersToEntityMixin(FrequencyQualifierMixin):
    """
    Qualifiers for disease or phenotype to entity associations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["FeatureOrDiseaseQualifiersToEntityMixin"]
    class_class_curie: ClassVar[str] = "biolink:FeatureOrDiseaseQualifiersToEntityMixin"
    class_name: ClassVar[str] = "feature or disease qualifiers to entity mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FeatureOrDiseaseQualifiersToEntityMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityToPhenotypicFeatureAssociationMixin(EntityToFeatureOrDiseaseQualifiersMixin):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EntityToPhenotypicFeatureAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:EntityToPhenotypicFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to phenotypic feature association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToPhenotypicFeatureAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, PhenotypicFeatureId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None
    has_percentage: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypicFeatureToEntityAssociationMixin(FeatureOrDiseaseQualifiersToEntityMixin):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhenotypicFeatureToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:PhenotypicFeatureToEntityAssociationMixin"
    class_name: ClassVar[str] = "phenotypic feature to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicFeatureToEntityAssociationMixin

    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, PhenotypicFeatureId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None
    has_percentage: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, PhenotypicFeatureId):
            self.subject = PhenotypicFeatureId(self.subject)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypicFeatureToPhenotypicFeatureAssociation(Association):
    """
    Association between two concept nodes of phenotypic character, qualified by the predicate used. This association
    may typically be used to specify 'similar_to' or 'member_of' relationships.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhenotypicFeatureToPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:PhenotypicFeatureToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "phenotypic feature to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicFeatureToPhenotypicFeatureAssociation

    id: Union[str, PhenotypicFeatureToPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypicFeatureToPhenotypicFeatureAssociationId):
            self.id = PhenotypicFeatureToPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class InformationContentEntityToNamedThingAssociation(Association):
    """
    association between a named thing and a information content entity where the specific context of the relationship
    between that named thing and the publication is unknown. For example, model organisms databases often capture the
    knowledge that a gene is found in a journal article, but not specifically the context in which that gene was
    documented in the article. In these cases, this association with the accompanying predicate 'mentions' could be
    used. Conversely, for more specific associations (like 'gene to disease association', the publication should be
    captured as an edge property).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["InformationContentEntityToNamedThingAssociation"]
    class_class_curie: ClassVar[str] = "biolink:InformationContentEntityToNamedThingAssociation"
    class_name: ClassVar[str] = "information content entity to named thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.InformationContentEntityToNamedThingAssociation

    id: Union[str, InformationContentEntityToNamedThingAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, NamedThingId] = None
    object: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationContentEntityToNamedThingAssociationId):
            self.id = InformationContentEntityToNamedThingAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class EntityToDiseaseAssociationMixin(EntityToFeatureOrDiseaseQualifiersMixin):
    """
    mixin class for any association whose object (target node) is a disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EntityToDiseaseAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:EntityToDiseaseAssociationMixin"
    class_name: ClassVar[str] = "entity to disease association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToDiseaseAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, DiseaseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseOrPhenotypicFeatureToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseOrPhenotypicFeatureToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureToEntityAssociationMixin"
    class_name: ClassVar[str] = "disease or phenotypic feature to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureToEntityAssociationMixin

    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseOrPhenotypicFeatureToLocationAssociation(Association):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the
    disease/feature manifests in that site.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseOrPhenotypicFeatureToLocationAssociation"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureToLocationAssociation"
    class_name: ClassVar[str] = "disease or phenotypic feature to location association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureToLocationAssociation

    id: Union[str, DiseaseOrPhenotypicFeatureToLocationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureToLocationAssociationId):
            self.id = DiseaseOrPhenotypicFeatureToLocationAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation(Association):
    """
    An association between either a disease or a phenotypic feature and its mode of (genetic) inheritance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation"
    class_name: ClassVar[str] = "disease or phenotypic feature to genetic inheritance association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation

    id: Union[str, DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, GeneticInheritanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociationId):
            self.id = DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneticInheritanceId):
            self.object = GeneticInheritanceId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class EntityToDiseaseOrPhenotypicFeatureAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EntityToDiseaseOrPhenotypicFeatureAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:EntityToDiseaseOrPhenotypicFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to disease or phenotypic feature association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToDiseaseOrPhenotypicFeatureAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    subject_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    object_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None
    anatomical_context_qualifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.subject_specialization_qualifier is not None and not isinstance(self.subject_specialization_qualifier, URIorCURIE):
            self.subject_specialization_qualifier = URIorCURIE(self.subject_specialization_qualifier)

        if self.object_specialization_qualifier is not None and not isinstance(self.object_specialization_qualifier, URIorCURIE):
            self.object_specialization_qualifier = URIorCURIE(self.object_specialization_qualifier)

        if self.anatomical_context_qualifier is not None and not isinstance(self.anatomical_context_qualifier, str):
            self.anatomical_context_qualifier = str(self.anatomical_context_qualifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GenotypeToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenotypeToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:GenotypeToEntityAssociationMixin"
    class_name: ClassVar[str] = "genotype to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToEntityAssociationMixin

    subject: Union[str, GenotypeId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype,
    either in isolation or through environment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenotypeToPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GenotypeToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "genotype to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToPhenotypicFeatureAssociation

    id: Union[str, GenotypeToPhenotypicFeatureAssociationId] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, GenotypeId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenotypeToPhenotypicFeatureAssociationId):
            self.id = GenotypeToPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ExposureEventToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ExposureEventToPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ExposureEventToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "exposure event to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ExposureEventToPhenotypicFeatureAssociation

    id: Union[str, ExposureEventToPhenotypicFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, ExposureEventId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventToPhenotypicFeatureAssociationId):
            self.id = ExposureEventToPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ExposureEventId):
            self.subject = ExposureEventId(self.subject)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the
    disease in some way.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseToPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "disease to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseToPhenotypicFeatureAssociation

    id: Union[str, DiseaseToPhenotypicFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, DiseaseId] = None
    object: Union[str, PhenotypicFeatureId] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None
    has_percentage: Optional[float] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseToPhenotypicFeatureAssociationId):
            self.id = DiseaseToPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)

        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)

        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or
    has had the phenotype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CaseToPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:CaseToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "case to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CaseToPhenotypicFeatureAssociation

    id: Union[str, CaseToPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    negated: Optional[Union[bool, Bool]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CaseToPhenotypicFeatureAssociationId):
            self.id = CaseToPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CaseToDiseaseAssociation(Association):
    """
    An association between a Case (patient) and a Disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CaseToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:CaseToDiseaseAssociation"
    class_name: ClassVar[str] = "case to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CaseToDiseaseAssociation

    id: Union[str, CaseToDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, DiseaseId] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CaseToDiseaseAssociationId):
            self.id = CaseToDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CaseToVariantAssociation(Association):
    """
    Association between a Case and a Genetic Variant
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CaseToVariantAssociation"]
    class_class_curie: ClassVar[str] = "biolink:CaseToVariantAssociation"
    class_name: ClassVar[str] = "case to variant association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CaseToVariantAssociation

    id: Union[str, CaseToVariantAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, SequenceVariantId] = None
    has_zygosity: Optional[Union[str, ZygosityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CaseToVariantAssociationId):
            self.id = CaseToVariantAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)

        if self.has_zygosity is not None and not isinstance(self.has_zygosity, ZygosityId):
            self.has_zygosity = ZygosityId(self.has_zygosity)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CaseToGeneAssociation(Association):
    """
    Association between a Case and a Gene (e.g., indicating a gene of interest for the case)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CaseToGeneAssociation"]
    class_class_curie: ClassVar[str] = "biolink:CaseToGeneAssociation"
    class_name: ClassVar[str] = "case to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CaseToGeneAssociation

    id: Union[str, CaseToGeneAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[dict, GeneOrGeneProduct] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CaseToGeneAssociationId):
            self.id = CaseToGeneAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneOrGeneProduct):
            self.object = GeneOrGeneProduct(**as_dict(self.object))

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class BehaviorToBehavioralFeatureAssociation(Association):
    """
    An association between an mixture behavior and a behavioral feature manifested by the individual exhibited or has
    exhibited the behavior.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["BehaviorToBehavioralFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:BehaviorToBehavioralFeatureAssociation"
    class_name: ClassVar[str] = "behavior to behavioral feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BehaviorToBehavioralFeatureAssociation

    id: Union[str, BehaviorToBehavioralFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, BehaviorId] = None
    object: Union[str, BehavioralFeatureId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehaviorToBehavioralFeatureAssociationId):
            self.id = BehaviorToBehavioralFeatureAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, BehaviorId):
            self.subject = BehaviorId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BehavioralFeatureId):
            self.object = BehavioralFeatureId(self.object)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:GeneToEntityAssociationMixin"
    class_name: ClassVar[str] = "gene to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToEntityAssociationMixin

    subject: Union[dict, GeneOrGeneProduct] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VariantToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["VariantToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:VariantToEntityAssociationMixin"
    class_name: ClassVar[str] = "variant to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToEntityAssociationMixin

    subject: Union[str, SequenceVariantId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneToDiseaseOrPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToDiseaseOrPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "gene to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, GeneToDiseaseOrPhenotypicFeatureAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None
    predicate: Union[str, PredicateType] = None
    subject_aspect_qualifier: Optional[Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"]] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = GeneToDiseaseOrPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, GeneOrGeneProductOrChemicalEntityAspectEnum):
            self.subject_aspect_qualifier = GeneOrGeneProductOrChemicalEntityAspectEnum(self.subject_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneToPhenotypicFeatureAssociation(GeneToDiseaseOrPhenotypicFeatureAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "gene to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToPhenotypicFeatureAssociation

    id: Union[str, GeneToPhenotypicFeatureAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[str, PhenotypicFeatureId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToPhenotypicFeatureAssociationId):
            self.id = GeneToPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneToDiseaseAssociation(GeneToDiseaseOrPhenotypicFeatureAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneToDiseaseAssociation"
    class_name: ClassVar[str] = "gene to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToDiseaseAssociation

    id: Union[str, GeneToDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[str, DiseaseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToDiseaseAssociationId):
            self.id = GeneToDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CausalGeneToDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CausalGeneToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:CausalGeneToDiseaseAssociation"
    class_name: ClassVar[str] = "causal gene to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CausalGeneToDiseaseAssociation

    id: Union[str, CausalGeneToDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[str, DiseaseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CausalGeneToDiseaseAssociationId):
            self.id = CausalGeneToDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CorrelatedGeneToDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CorrelatedGeneToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:CorrelatedGeneToDiseaseAssociation"
    class_name: ClassVar[str] = "correlated gene to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CorrelatedGeneToDiseaseAssociation

    id: Union[str, CorrelatedGeneToDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[str, DiseaseId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CorrelatedGeneToDiseaseAssociationId):
            self.id = CorrelatedGeneToDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class DruggableGeneToDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DruggableGeneToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:DruggableGeneToDiseaseAssociation"
    class_name: ClassVar[str] = "druggable gene to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DruggableGeneToDiseaseAssociation

    id: Union[str, DruggableGeneToDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    object: Union[str, DiseaseId] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    predicate: Union[str, PredicateType] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    has_evidence: Optional[Union[Union[str, "DruggableGeneCategoryEnum"], list[Union[str, "DruggableGeneCategoryEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DruggableGeneToDiseaseAssociationId):
            self.id = DruggableGeneToDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if not isinstance(self.has_evidence, list):
            self.has_evidence = [self.has_evidence] if self.has_evidence is not None else []
        self.has_evidence = [v if isinstance(v, DruggableGeneCategoryEnum) else DruggableGeneCategoryEnum(v) for v in self.has_evidence]

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PhenotypicFeatureToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhenotypicFeatureToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:PhenotypicFeatureToDiseaseAssociation"
    class_name: ClassVar[str] = "phenotypic feature to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicFeatureToDiseaseAssociation

    id: Union[str, PhenotypicFeatureToDiseaseAssociationId] = None
    subject: Union[str, NamedThingId] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypicFeatureToDiseaseAssociationId):
            self.id = PhenotypicFeatureToDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class VariantToGeneAssociation(Association):
    """
    An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in
    linkage disequilibrium)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["VariantToGeneAssociation"]
    class_class_curie: ClassVar[str] = "biolink:VariantToGeneAssociation"
    class_name: ClassVar[str] = "variant to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToGeneAssociation

    id: Union[str, VariantToGeneAssociationId] = None
    subject: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    object: Union[str, GeneId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantToGeneAssociationId):
            self.id = VariantToGeneAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class VariantToGeneExpressionAssociation(VariantToGeneAssociation):
    """
    An association between a variant and expression of a gene (i.e. e-QTL)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["VariantToGeneExpressionAssociation"]
    class_class_curie: ClassVar[str] = "biolink:VariantToGeneExpressionAssociation"
    class_name: ClassVar[str] = "variant to gene expression association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToGeneExpressionAssociation

    id: Union[str, VariantToGeneExpressionAssociationId] = None
    subject: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    object: Union[str, GeneId] = None
    predicate: Union[str, PredicateType] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    expression_site: Optional[Union[str, AnatomicalEntityId]] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    phenotypic_state: Optional[Union[str, DiseaseOrPhenotypicFeatureId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantToGeneExpressionAssociationId):
            self.id = VariantToGeneExpressionAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.expression_site is not None and not isinstance(self.expression_site, AnatomicalEntityId):
            self.expression_site = AnatomicalEntityId(self.expression_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)

        if self.phenotypic_state is not None and not isinstance(self.phenotypic_state, DiseaseOrPhenotypicFeatureId):
            self.phenotypic_state = DiseaseOrPhenotypicFeatureId(self.phenotypic_state)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["VariantToPopulationAssociation"]
    class_class_curie: ClassVar[str] = "biolink:VariantToPopulationAssociation"
    class_name: ClassVar[str] = "variant to population association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToPopulationAssociation

    id: Union[str, VariantToPopulationAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None
    has_quotient: Optional[float] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_percentage: Optional[float] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantToPopulationAssociationId):
            self.id = VariantToPopulationAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PopulationToPopulationAssociation"]
    class_class_curie: ClassVar[str] = "biolink:PopulationToPopulationAssociation"
    class_name: ClassVar[str] = "population to population association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PopulationToPopulationAssociation

    id: Union[str, PopulationToPopulationAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, PopulationOfIndividualOrganismsId] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, PopulationOfIndividualOrganismsId):
            self.subject = PopulationOfIndividualOrganismsId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class VariantToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["VariantToPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:VariantToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "variant to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToPhenotypicFeatureAssociation

    id: Union[str, VariantToPhenotypicFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, SequenceVariantId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantToPhenotypicFeatureAssociationId):
            self.id = VariantToPhenotypicFeatureAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class VariantToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["VariantToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:VariantToDiseaseAssociation"
    class_name: ClassVar[str] = "variant to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToDiseaseAssociation

    id: Union[str, VariantToDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantToDiseaseAssociationId):
            self.id = VariantToDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GenotypeToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenotypeToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GenotypeToDiseaseAssociation"
    class_name: ClassVar[str] = "genotype to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToDiseaseAssociation

    id: Union[str, GenotypeToDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenotypeToDiseaseAssociationId):
            self.id = GenotypeToDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ModelToDiseaseAssociationMixin(YAMLRoot):
    """
    This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in
    that it recapitulates some features of the disease in a way that is useful for studying the disease outside a
    patient carrying the disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ModelToDiseaseAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:ModelToDiseaseAssociationMixin"
    class_name: ClassVar[str] = "model to disease association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ModelToDiseaseAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneAsAModelOfDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "gene as a model of disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneAsAModelOfDiseaseAssociation

    id: Union[str, GeneAsAModelOfDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, DiseaseId] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneAsAModelOfDiseaseAssociationId):
            self.id = GeneAsAModelOfDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class VariantAsAModelOfDiseaseAssociation(VariantToDiseaseAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["VariantAsAModelOfDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:VariantAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "variant as a model of disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantAsAModelOfDiseaseAssociation

    id: Union[str, VariantAsAModelOfDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, SequenceVariantId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantAsAModelOfDiseaseAssociationId):
            self.id = VariantAsAModelOfDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GenotypeAsAModelOfDiseaseAssociation(GenotypeToDiseaseAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenotypeAsAModelOfDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GenotypeAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "genotype as a model of disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeAsAModelOfDiseaseAssociation

    id: Union[str, GenotypeAsAModelOfDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, GenotypeId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenotypeAsAModelOfDiseaseAssociationId):
            self.id = GenotypeAsAModelOfDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class CellLineAsAModelOfDiseaseAssociation(CellLineToDiseaseOrPhenotypicFeatureAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CellLineAsAModelOfDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:CellLineAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "cell line as a model of disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLineAsAModelOfDiseaseAssociation

    id: Union[str, CellLineAsAModelOfDiseaseAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, CellLineId] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellLineAsAModelOfDiseaseAssociationId):
            self.id = CellLineAsAModelOfDiseaseAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class OrganismalEntityAsAModelOfDiseaseAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["OrganismalEntityAsAModelOfDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:OrganismalEntityAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "organismal entity as a model of disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismalEntityAsAModelOfDiseaseAssociation

    id: Union[str, OrganismalEntityAsAModelOfDiseaseAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, OrganismalEntityId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None
    qualified_predicate: Optional[str] = None
    disease_context_qualifier: Optional[Union[str, DiseaseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismalEntityAsAModelOfDiseaseAssociationId):
            self.id = OrganismalEntityAsAModelOfDiseaseAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OrganismalEntityId):
            self.subject = OrganismalEntityId(self.subject)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(self.frequency_qualifier)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, DirectionQualifierEnum):
            self.subject_direction_qualifier = DirectionQualifierEnum(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        if self.qualified_predicate is not None and not isinstance(self.qualified_predicate, str):
            self.qualified_predicate = str(self.qualified_predicate)

        if self.disease_context_qualifier is not None and not isinstance(self.disease_context_qualifier, DiseaseId):
            self.disease_context_qualifier = DiseaseId(self.disease_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class OrganismToOrganismAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["OrganismToOrganismAssociation"]
    class_class_curie: ClassVar[str] = "biolink:OrganismToOrganismAssociation"
    class_name: ClassVar[str] = "organism to organism association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismToOrganismAssociation

    id: Union[str, OrganismToOrganismAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, IndividualOrganismId] = None
    object: Union[str, IndividualOrganismId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismToOrganismAssociationId):
            self.id = OrganismToOrganismAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, IndividualOrganismId):
            self.subject = IndividualOrganismId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, IndividualOrganismId):
            self.object = IndividualOrganismId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class TaxonToTaxonAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["TaxonToTaxonAssociation"]
    class_class_curie: ClassVar[str] = "biolink:TaxonToTaxonAssociation"
    class_name: ClassVar[str] = "taxon to taxon association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.TaxonToTaxonAssociation

    id: Union[str, TaxonToTaxonAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, OrganismTaxonId] = None
    object: Union[str, OrganismTaxonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TaxonToTaxonAssociationId):
            self.id = TaxonToTaxonAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OrganismTaxonId):
            self.subject = OrganismTaxonId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OrganismTaxonId):
            self.object = OrganismTaxonId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneHasVariantThatContributesToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneHasVariantThatContributesToDiseaseAssociation"
    class_name: ClassVar[str] = "gene has variant that contributes to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneHasVariantThatContributesToDiseaseAssociation

    id: Union[str, GeneHasVariantThatContributesToDiseaseAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[str, DiseaseId] = None
    predicate: Union[str, PredicateType] = None
    subject_form_or_variant_qualifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneHasVariantThatContributesToDiseaseAssociationId):
            self.id = GeneHasVariantThatContributesToDiseaseAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject_form_or_variant_qualifier is not None and not isinstance(self.subject_form_or_variant_qualifier, str):
            self.subject_form_or_variant_qualifier = str(self.subject_form_or_variant_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and a gene expression site, possibly qualified by stage/timing info.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToExpressionSiteAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneToExpressionSiteAssociation"
    class_name: ClassVar[str] = "gene to expression site association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToExpressionSiteAssociation

    id: Union[str, GeneToExpressionSiteAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, GeneOrGeneProduct] = None
    object: Union[str, AnatomicalEntityId] = None
    predicate: Union[str, PredicateType] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    object_specialization_qualifier: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToExpressionSiteAssociationId):
            self.id = GeneToExpressionSiteAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneOrGeneProduct):
            self.subject = GeneOrGeneProduct(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.object_specialization_qualifier is not None and not isinstance(self.object_specialization_qualifier, URIorCURIE):
            self.object_specialization_qualifier = URIorCURIE(self.object_specialization_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself
    encompasses both the disease and the drug used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SequenceVariantModulatesTreatmentAssociation"]
    class_class_curie: ClassVar[str] = "biolink:SequenceVariantModulatesTreatmentAssociation"
    class_name: ClassVar[str] = "sequence variant modulates treatment association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SequenceVariantModulatesTreatmentAssociation

    id: Union[str, SequenceVariantModulatesTreatmentAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, TreatmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, TreatmentId):
            self.object = TreatmentId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine mixin (gene, gene product or complex of gene products) and either
    a molecular activity, a biological process or a cellular location in which a function is executed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["FunctionalAssociation"]
    class_class_curie: ClassVar[str] = "biolink:FunctionalAssociation"
    class_name: ClassVar[str] = "functional association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FunctionalAssociation

    id: Union[str, FunctionalAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, MacromolecularMachineMixin] = None
    object: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, MacromolecularMachineMixin):
            self.subject = MacromolecularMachineMixin(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OntologyClassId):
            self.object = OntologyClassId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MacromolecularMachineToEntityAssociationMixin(YAMLRoot):
    """
    an association which has a macromolecular machine mixin as a subject
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MacromolecularMachineToEntityAssociationMixin"]
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineToEntityAssociationMixin"
    class_name: ClassVar[str] = "macromolecular machine to entity association mixin"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToEntityAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    species_context_qualifier: Optional[Union[str, OrganismTaxonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.species_context_qualifier is not None and not isinstance(self.species_context_qualifier, OrganismTaxonId):
            self.species_context_qualifier = OrganismTaxonId(self.species_context_qualifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MacromolecularMachineToMolecularActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity
    (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to
    its execution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MacromolecularMachineToMolecularActivityAssociation"]
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineToMolecularActivityAssociation"
    class_name: ClassVar[str] = "macromolecular machine to molecular activity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToMolecularActivityAssociation

    id: Union[str, MacromolecularMachineToMolecularActivityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, MacromolecularMachineMixin] = None
    object: Union[str, MolecularActivityId] = None
    species_context_qualifier: Optional[Union[str, OrganismTaxonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MacromolecularMachineToMolecularActivityAssociationId):
            self.id = MacromolecularMachineToMolecularActivityAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)

        if self.species_context_qualifier is not None and not isinstance(self.species_context_qualifier, OrganismTaxonId):
            self.species_context_qualifier = OrganismTaxonId(self.species_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MacromolecularMachineToBiologicalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process
    or pathway (as represented in the GO biological process branch), where the entity carries out some part of the
    process, regulates it, or acts upstream of it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MacromolecularMachineToBiologicalProcessAssociation"]
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineToBiologicalProcessAssociation"
    class_name: ClassVar[str] = "macromolecular machine to biological process association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToBiologicalProcessAssociation

    id: Union[str, MacromolecularMachineToBiologicalProcessAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, MacromolecularMachineMixin] = None
    object: Union[str, BiologicalProcessId] = None
    species_context_qualifier: Optional[Union[str, OrganismTaxonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MacromolecularMachineToBiologicalProcessAssociationId):
            self.id = MacromolecularMachineToBiologicalProcessAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        if self.species_context_qualifier is not None and not isinstance(self.species_context_qualifier, OrganismTaxonId):
            self.species_context_qualifier = OrganismTaxonId(self.species_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MacromolecularMachineToCellularComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component
    (as represented in the GO cellular component branch), where the entity carries out its function in the cellular
    component.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MacromolecularMachineToCellularComponentAssociation"]
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineToCellularComponentAssociation"
    class_name: ClassVar[str] = "macromolecular machine to cellular component association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToCellularComponentAssociation

    id: Union[str, MacromolecularMachineToCellularComponentAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[dict, MacromolecularMachineMixin] = None
    object: Union[str, CellularComponentId] = None
    species_context_qualifier: Optional[Union[str, OrganismTaxonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MacromolecularMachineToCellularComponentAssociationId):
            self.id = MacromolecularMachineToCellularComponentAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)

        if self.species_context_qualifier is not None and not isinstance(self.species_context_qualifier, OrganismTaxonId):
            self.species_context_qualifier = OrganismTaxonId(self.species_context_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MolecularActivityToChemicalEntityAssociation(Association):
    """
    Added in response to capturing relationship between microbiome activities as measured via measurements of blood
    analytes as collected via blood and stool samples
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MolecularActivityToChemicalEntityAssociation"]
    class_class_curie: ClassVar[str] = "biolink:MolecularActivityToChemicalEntityAssociation"
    class_name: ClassVar[str] = "molecular activity to chemical entity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularActivityToChemicalEntityAssociation

    id: Union[str, MolecularActivityToChemicalEntityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, MolecularActivityId] = None
    object: Union[str, ChemicalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularActivityToChemicalEntityAssociationId):
            self.id = MolecularActivityToChemicalEntityAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, MolecularActivityId):
            self.subject = MolecularActivityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ChemicalEntityId):
            self.object = ChemicalEntityId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class MolecularActivityToMolecularActivityAssociation(Association):
    """
    Added in response to capturing relationship between microbiome activities as measured via measurements of blood
    analytes as collected via blood and stool samples
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MolecularActivityToMolecularActivityAssociation"]
    class_class_curie: ClassVar[str] = "biolink:MolecularActivityToMolecularActivityAssociation"
    class_name: ClassVar[str] = "molecular activity to molecular activity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularActivityToMolecularActivityAssociation

    id: Union[str, MolecularActivityToMolecularActivityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, MolecularActivityId] = None
    object: Union[str, MolecularActivityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularActivityToMolecularActivityAssociationId):
            self.id = MolecularActivityToMolecularActivityAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, MolecularActivityId):
            self.subject = MolecularActivityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneToGoTermAssociation(FunctionalAssociation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToGoTermAssociation"]
    class_class_curie: ClassVar[str] = "biolink:GeneToGoTermAssociation"
    class_name: ClassVar[str] = "gene to go term association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGoTermAssociation

    id: Union[str, GeneToGoTermAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, GeneId] = None
    object: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToGoTermAssociationId):
            self.id = GeneToGoTermAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OntologyClassId):
            self.object = OntologyClassId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class EntityToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EntityToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "biolink:EntityToDiseaseAssociation"
    class_name: ClassVar[str] = "entity to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToDiseaseAssociation

    id: Union[str, EntityToDiseaseAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    clinical_approval_status: Optional[Union[str, "ClinicalApprovalStatusEnum"]] = None
    max_research_phase: Optional[Union[str, "ResearchPhaseEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityToDiseaseAssociationId):
            self.id = EntityToDiseaseAssociationId(self.id)

        if self.clinical_approval_status is not None and not isinstance(self.clinical_approval_status, ClinicalApprovalStatusEnum):
            self.clinical_approval_status = ClinicalApprovalStatusEnum(self.clinical_approval_status)

        if self.max_research_phase is not None and not isinstance(self.max_research_phase, ResearchPhaseEnum):
            self.max_research_phase = ResearchPhaseEnum(self.max_research_phase)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class EntityToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EntityToPhenotypicFeatureAssociation"]
    class_class_curie: ClassVar[str] = "biolink:EntityToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "entity to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToPhenotypicFeatureAssociation

    id: Union[str, EntityToPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    clinical_approval_status: Optional[Union[str, "ClinicalApprovalStatusEnum"]] = None
    max_research_phase: Optional[Union[str, "ResearchPhaseEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityToPhenotypicFeatureAssociationId):
            self.id = EntityToPhenotypicFeatureAssociationId(self.id)

        if self.clinical_approval_status is not None and not isinstance(self.clinical_approval_status, ClinicalApprovalStatusEnum):
            self.clinical_approval_status = ClinicalApprovalStatusEnum(self.clinical_approval_status)

        if self.max_research_phase is not None and not isinstance(self.max_research_phase, ResearchPhaseEnum):
            self.max_research_phase = ResearchPhaseEnum(self.max_research_phase)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class SequenceAssociation(Association):
    """
    An association between a sequence feature and a nucleic acid entity it is localized to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SequenceAssociation"]
    class_class_curie: ClassVar[str] = "biolink:SequenceAssociation"
    class_name: ClassVar[str] = "sequence association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SequenceAssociation

    id: Union[str, SequenceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceAssociationId):
            self.id = SequenceAssociationId(self.id)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GenomicSequenceLocalization(SequenceAssociation):
    """
    A relationship between a sequence feature and a nucleic acid entity it is localized to. The reference entity may
    be a chromosome, chromosome region or information entity such as a contig.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GenomicSequenceLocalization"]
    class_class_curie: ClassVar[str] = "biolink:GenomicSequenceLocalization"
    class_name: ClassVar[str] = "genomic sequence localization"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenomicSequenceLocalization

    id: Union[str, GenomicSequenceLocalizationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, NucleicAcidEntityId] = None
    object: Union[str, NucleicAcidEntityId] = None
    predicate: Union[str, PredicateType] = None
    start_interbase_coordinate: Optional[int] = None
    end_interbase_coordinate: Optional[int] = None
    genome_build: Optional[Union[str, "StrandEnum"]] = None
    strand: Optional[Union[str, "StrandEnum"]] = None
    phase: Optional[Union[str, "PhaseEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenomicSequenceLocalizationId):
            self.id = GenomicSequenceLocalizationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NucleicAcidEntityId):
            self.subject = NucleicAcidEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NucleicAcidEntityId):
            self.object = NucleicAcidEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.start_interbase_coordinate is not None and not isinstance(self.start_interbase_coordinate, int):
            self.start_interbase_coordinate = int(self.start_interbase_coordinate)

        if self.end_interbase_coordinate is not None and not isinstance(self.end_interbase_coordinate, int):
            self.end_interbase_coordinate = int(self.end_interbase_coordinate)

        if self.genome_build is not None and not isinstance(self.genome_build, StrandEnum):
            self.genome_build = StrandEnum(self.genome_build)

        if self.strand is not None and not isinstance(self.strand, StrandEnum):
            self.strand = StrandEnum(self.strand)

        if self.phase is not None and not isinstance(self.phase, PhaseEnum):
            self.phase = PhaseEnum(self.phase)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SequenceFeatureRelationship"]
    class_class_curie: ClassVar[str] = "biolink:SequenceFeatureRelationship"
    class_name: ClassVar[str] = "sequence feature relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SequenceFeatureRelationship

    id: Union[str, SequenceFeatureRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, NucleicAcidEntityId] = None
    object: Union[str, NucleicAcidEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NucleicAcidEntityId):
            self.subject = NucleicAcidEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NucleicAcidEntityId):
            self.object = NucleicAcidEntityId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["TranscriptToGeneRelationship"]
    class_class_curie: ClassVar[str] = "biolink:TranscriptToGeneRelationship"
    class_name: ClassVar[str] = "transcript to gene relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.TranscriptToGeneRelationship

    id: Union[str, TranscriptToGeneRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, TranscriptId] = None
    object: Union[str, GeneId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TranscriptToGeneRelationshipId):
            self.id = TranscriptToGeneRelationshipId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, TranscriptId):
            self.subject = TranscriptId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["GeneToGeneProductRelationship"]
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneProductRelationship"
    class_name: ClassVar[str] = "gene to gene product relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneProductRelationship

    id: Union[str, GeneToGeneProductRelationshipId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, GeneId] = None
    object: Union[dict, GeneProductMixin] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToGeneProductRelationshipId):
            self.id = GeneToGeneProductRelationshipId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneProductMixin):
            self.object = GeneProductMixin(**as_dict(self.object))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ExonToTranscriptRelationship"]
    class_class_curie: ClassVar[str] = "biolink:ExonToTranscriptRelationship"
    class_name: ClassVar[str] = "exon to transcript relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ExonToTranscriptRelationship

    id: Union[str, ExonToTranscriptRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, ExonId] = None
    object: Union[str, TranscriptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExonToTranscriptRelationshipId):
            self.id = ExonToTranscriptRelationshipId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ExonId):
            self.subject = ExonId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation(Association):
    """
    A regulatory relationship between two genes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation"
    class_name: ClassVar[str] = "chemical entity or gene or gene product regulates gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation

    id: Union[str, ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, ChemicalEntityOrGeneOrGeneProduct] = None
    object: Union[dict, GeneOrGeneProduct] = None
    object_direction_qualifier: Optional[Union[str, "DirectionQualifierEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociationId):
            self.id = ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ChemicalEntityOrGeneOrGeneProduct):
            self.subject = ChemicalEntityOrGeneOrGeneProduct()

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneOrGeneProduct):
            self.object = GeneOrGeneProduct(**as_dict(self.object))

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, DirectionQualifierEnum):
            self.object_direction_qualifier = DirectionQualifierEnum(self.object_direction_qualifier)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["AnatomicalEntityToAnatomicalEntityAssociation"]
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, AnatomicalEntityId] = None
    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between cellular components and cells, between cells and tissues,
    tissues and whole organisms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["AnatomicalEntityToAnatomicalEntityPartOfAssociation"]
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityPartOfAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity part of association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityPartOfAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityPartOfAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, AnatomicalEntityId] = None
    object: Union[str, AnatomicalEntityId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityPartOfAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityPartOfAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e. the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["AnatomicalEntityToAnatomicalEntityOntogenicAssociation"]
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityOntogenicAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity ontogenic association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityOntogenicAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, AnatomicalEntityId] = None
    object: Union[str, AnatomicalEntityId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class OrganismTaxonToEntityAssociation(YAMLRoot):
    """
    An association between an organism taxon and another entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["OrganismTaxonToEntityAssociation"]
    class_class_curie: ClassVar[str] = "biolink:OrganismTaxonToEntityAssociation"
    class_name: ClassVar[str] = "organism taxon to entity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxonToEntityAssociation

    subject: Union[str, OrganismTaxonId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OrganismTaxonId):
            self.subject = OrganismTaxonId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganismTaxonToOrganismTaxonAssociation(Association):
    """
    A relationship between two organism taxon nodes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["OrganismTaxonToOrganismTaxonAssociation"]
    class_class_curie: ClassVar[str] = "biolink:OrganismTaxonToOrganismTaxonAssociation"
    class_name: ClassVar[str] = "organism taxon to organism taxon association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxonToOrganismTaxonAssociation

    id: Union[str, OrganismTaxonToOrganismTaxonAssociationId] = None
    predicate: Union[str, PredicateType] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, OrganismTaxonId] = None
    object: Union[str, OrganismTaxonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OrganismTaxonId):
            self.subject = OrganismTaxonId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OrganismTaxonId):
            self.object = OrganismTaxonId(self.object)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class OrganismTaxonToOrganismTaxonSpecialization(OrganismTaxonToOrganismTaxonAssociation):
    """
    A child-parent relationship between two taxa. For example: Homo sapiens subclass_of Homo
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["OrganismTaxonToOrganismTaxonSpecialization"]
    class_class_curie: ClassVar[str] = "biolink:OrganismTaxonToOrganismTaxonSpecialization"
    class_name: ClassVar[str] = "organism taxon to organism taxon specialization"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxonToOrganismTaxonSpecialization

    id: Union[str, OrganismTaxonToOrganismTaxonSpecializationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, OrganismTaxonId] = None
    object: Union[str, OrganismTaxonId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismTaxonToOrganismTaxonSpecializationId):
            self.id = OrganismTaxonToOrganismTaxonSpecializationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OrganismTaxonId):
            self.subject = OrganismTaxonId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OrganismTaxonId):
            self.object = OrganismTaxonId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class OrganismTaxonToOrganismTaxonInteraction(OrganismTaxonToOrganismTaxonAssociation):
    """
    An interaction relationship between two taxa. This may be a symbiotic relationship (encompassing mutualism and
    parasitism), or it may be non-symbiotic. Example: plague transmitted_by flea; cattle domesticated_by Homo sapiens;
    plague infects Homo sapiens
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["OrganismTaxonToOrganismTaxonInteraction"]
    class_class_curie: ClassVar[str] = "biolink:OrganismTaxonToOrganismTaxonInteraction"
    class_name: ClassVar[str] = "organism taxon to organism taxon interaction"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxonToOrganismTaxonInteraction

    id: Union[str, OrganismTaxonToOrganismTaxonInteractionId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, OrganismTaxonId] = None
    object: Union[str, OrganismTaxonId] = None
    predicate: Union[str, PredicateType] = None
    associated_environmental_context: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismTaxonToOrganismTaxonInteractionId):
            self.id = OrganismTaxonToOrganismTaxonInteractionId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OrganismTaxonId):
            self.subject = OrganismTaxonId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OrganismTaxonId):
            self.object = OrganismTaxonId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.associated_environmental_context is not None and not isinstance(self.associated_environmental_context, str):
            self.associated_environmental_context = str(self.associated_environmental_context)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


@dataclass(repr=False)
class OrganismTaxonToEnvironmentAssociation(Association):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["OrganismTaxonToEnvironmentAssociation"]
    class_class_curie: ClassVar[str] = "biolink:OrganismTaxonToEnvironmentAssociation"
    class_name: ClassVar[str] = "organism taxon to environment association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxonToEnvironmentAssociation

    id: Union[str, OrganismTaxonToEnvironmentAssociationId] = None
    knowledge_level: Union[str, "KnowledgeLevelEnum"] = None
    agent_type: Union[str, "AgentTypeEnum"] = None
    subject: Union[str, OrganismTaxonId] = None
    object: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OrganismTaxonId):
            self.subject = OrganismTaxonId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.category]


# Enumerations
class ResponseEnum(EnumDefinitionImpl):
    """
    A response to a treatment or intervention
    """
    therapeutic_response = PermissibleValue(
        text="therapeutic_response",
        description="A positive response to a treatment or intervention")
    negative = PermissibleValue(
        text="negative",
        description="A negative response to a treatment or intervention")

    _defn = EnumDefinition(
        name="ResponseEnum",
        description="A response to a treatment or intervention",
    )

class ResponseTargetEnum(EnumDefinitionImpl):
    """
    The target of a treatment or intervention
    """
    cohort = PermissibleValue(
        text="cohort",
        description="A group of individuals that are the target of a treatment or intervention")
    individual = PermissibleValue(
        text="individual",
        description="An individual that is the target of a treatment or intervention")
    sample = PermissibleValue(
        text="sample",
        description="A biological materialsample that is the target of a treatment or intervention")

    _defn = EnumDefinition(
        name="ResponseTargetEnum",
        description="The target of a treatment or intervention",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cell line",
            PermissibleValue(
                text="cell line",
                description="A cell line that is the target of a treatment or intervention"))

class ClinicalTrialStatusEnum(EnumDefinitionImpl):
    """
    Enumeration of clinical trial statuses indicating the recruitment state, availability, or regulatory status of a
    clinical study or intervention.
    """
    ACTIVE_NOT_RECRUITING = PermissibleValue(
        text="ACTIVE_NOT_RECRUITING",
        description="The study is ongoing but not currently recruiting participants.")
    APPROVED_FOR_MARKETING = PermissibleValue(
        text="APPROVED_FOR_MARKETING",
        description="The intervention has received regulatory approval for marketing.")
    AVAILABLE = PermissibleValue(
        text="AVAILABLE",
        description="The intervention or data is available for use or distribution.")
    COMPLETED = PermissibleValue(
        text="COMPLETED",
        description="The study has ended normally and participants are no longer being examined or treated.")
    ENROLLING_BY_INVITATION = PermissibleValue(
        text="ENROLLING_BY_INVITATION",
        description="Participants are being enrolled by invitation only.")
    NO_LONGER_AVAILABLE = PermissibleValue(
        text="NO_LONGER_AVAILABLE",
        description="The intervention or data is no longer available.")
    NOT_YET_RECRUITING = PermissibleValue(
        text="NOT_YET_RECRUITING",
        description="The study has not yet started recruiting participants.")
    RECRUITING = PermissibleValue(
        text="RECRUITING",
        description="The study is currently recruiting participants.")
    SUSPENDED = PermissibleValue(
        text="SUSPENDED",
        description="The study has been temporarily halted but may resume.")
    TEMPORARILY_NOT_AVAILABLE = PermissibleValue(
        text="TEMPORARILY_NOT_AVAILABLE",
        description="The intervention or data is not currently available but may become available later.")
    TERMINATED = PermissibleValue(
        text="TERMINATED",
        description="The study has stopped prematurely and will not start again.")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="The recruitment or availability status is unknown.")
    WITHDRAWN = PermissibleValue(
        text="WITHDRAWN",
        description="The study was halted before enrolling its first participant.")

    _defn = EnumDefinition(
        name="ClinicalTrialStatusEnum",
        description="""Enumeration of clinical trial statuses indicating the recruitment state, availability, or regulatory status of a clinical study or intervention.""",
    )

class ApprovalStatusEnum(EnumDefinitionImpl):

    discovery_and_development_phase = PermissibleValue(
        text="discovery_and_development_phase",
        description="""Discovery & Development Phase. Discovery involves researchers finding new possibilities for medication through testing molecular compounds, noting unexpected effects from existing treatments, or the creation of new technology that allows novel ways of targeting medical products to sites in the body. Drug development occurs after researchers identify potential compounds for experiments.""")
    preclinical_research_phase = PermissibleValue(
        text="preclinical_research_phase",
        description="""Preclinical Research Phase.  Once researchers have examined the possibilities a new drug may contain, they must do preliminary research to determine its potential for harm (toxicity). This is categorized as preclinical research and can be one of two types: in vitro or in vivo.""")
    fda_clinical_research_phase = PermissibleValue(
        text="fda_clinical_research_phase",
        description="""Clinical Research Phase. Clinical research involves trials of the drug on people, and it is one of the most involved stages in the drug development and approval process. Clinical trials must answer specific questions and follow a protocol determined by the drug researcher or manufacturer.""")
    fda_review_phase_4 = PermissibleValue(
        text="fda_review_phase_4",
        description="FDA Review")
    fda_post_market_safety_review = PermissibleValue(
        text="fda_post_market_safety_review",
        description="""FDA Post-Market Safety Monitoring.  The last phase of drug approval is an ongoing one while the drug is on the marketplace. If a developer wants to change anything about the drug formulation or approve it for a new use, they must apply with the FDA. The FDA also frequently reviews the drug’s advertising and its manufacturing facility to make sure everything involved in its creation and marketing is in compliance with regulations.""")
    fda_clinical_research_phase_1 = PermissibleValue(
        text="fda_clinical_research_phase_1",
        description="""In the FDA Clinical Research Phase, the Clinical Research Phase 1 involves 20 – 100 study participants and lasts several months. This phase is used to determine the safety and dosage of the drug, and about 70% of these drugs move on to the next clinical research phase.""")
    fda_clinical_research_phase_2 = PermissibleValue(
        text="fda_clinical_research_phase_2",
        description="""In the FDA Clinical Research Phase, the Clinical Research Phase 2 involves up to several hundred people, who must have the disease or condition the drug supposes to treat. This phase can last from a few months to two years, and its purpose is to monitor the efficacy of the drug, as well as note side effects that may occur.""")
    fda_clinical_research_phase_3 = PermissibleValue(
        text="fda_clinical_research_phase_3",
        description="""In the FDA Clinical Research Phase, the Clinical Research Phase 3 involves 300 – 3000 volunteers and can last up to four years. It is used to continue monitoring the efficacy of the drug, as well as exploring any longer-term adverse reactions.""")
    fda_clinical_research_phase_4 = PermissibleValue(
        text="fda_clinical_research_phase_4",
        description="""In the FDA Clinical Research Phase, the Clinical Research Phase 4 involves several thousands of volunteers who have the disease or condition and continues to monitor safety and efficacy. If a drug passes this phase, it goes on to FDA review.""")
    fda_fast_track = PermissibleValue(
        text="fda_fast_track",
        description="""Fast track is a process designed to facilitate the development, and expedite the review of drugs to treat serious conditions and fill an unmet medical need. The purpose is to get important new drugs to the patient earlier. Fast Track addresses a broad range of serious conditions. For more information https://www.fda.gov/patients/fast-track-breakthrough-therapy-accelerated-approval-priority-review/fast-track""")
    fda_breakthrough_therapy = PermissibleValue(
        text="fda_breakthrough_therapy",
        description="""Breakthrough Therapy designation is a process designed to expedite the development and review of drugs that are intended to treat a serious condition and preliminary clinical evidence indicates that the drug may demonstrate substantial improvement over available therapy on a clinically significant endpoint(s). For more information https://www.fda.gov/patients/fast-track-breakthrough-therapy-accelerated-approval-priority-review/breakthrough-therapy""")
    fda_accelerated_approval = PermissibleValue(
        text="fda_accelerated_approval",
        description="""When studying a new drug, it can sometimes take many years to learn whether a drug actually provides a real effect on how a patient survives, feels, or functions. A positive therapeutic effect that is clinically meaningful in the context of a given disease is known as “clinical benefit”. Mindful of the fact that it may take an extended period of time to measure a drug’s intended clinical benefit, in 1992 FDA instituted the Accelerated Approval regulations. These regulations allowed drugs for serious conditions that filled an unmet medical need to be approved based on a surrogate endpoint. Using a surrogate endpoint enabled the FDA to approve these drugs faster. For more information https://www.fda.gov/patients/fast-track-breakthrough-therapy-accelerated-approval-priority-review/accelerated-approval""")
    fda_priority_review = PermissibleValue(
        text="fda_priority_review",
        description="""Prior to approval, each drug marketed in the United States must go through a detailed FDA review process. In 1992, under the Prescription Drug User Act (PDUFA), FDA agreed to specific goals for improving the drug review time and created a two-tiered system of review times – Standard Review and Priority Review. A Priority Review designation means FDA’s goal is to take action on an application within 6 months (compared to 10 months under standard review). For more information https://www.fda.gov/patients/fast-track-breakthrough-therapy-accelerated-approval-priority-review/priority-review""")
    regular_fda_approval = PermissibleValue(
        text="regular_fda_approval",
        description="""Regular FDA Approval.  The last phase of drug approval is an ongoing one while the drug is on the marketplace. If a developer wants to change anything about the drug formulation or approve it for a new use, they must apply with the FDA. The FDA also frequently reviews the drug’s advertising and its manufacturing facility to make sure everything involved in its creation and marketing is in compliance with regulations.""")
    post_approval_withdrawal = PermissibleValue(text="post_approval_withdrawal")

    _defn = EnumDefinition(
        name="ApprovalStatusEnum",
    )

class ClinicalApprovalStatusEnum(EnumDefinitionImpl):

    approved_for_condition = PermissibleValue(text="approved_for_condition")
    fda_approved_for_condition = PermissibleValue(text="fda_approved_for_condition")
    not_approved_for_condition = PermissibleValue(text="not_approved_for_condition")
    post_approval_withdrawal = PermissibleValue(text="post_approval_withdrawal")
    off_label_use = PermissibleValue(text="off_label_use")
    not_provided = PermissibleValue(text="not_provided")

    _defn = EnumDefinition(
        name="ClinicalApprovalStatusEnum",
    )

class ResearchPhaseEnum(EnumDefinitionImpl):

    pre_clinical_research_phase = PermissibleValue(
        text="pre_clinical_research_phase",
        description="""Biolink 'pre_clinical_research' is the union of both the `FDA discovery and development phase` and `FDA preclinical research phase`. Discovery involves researchers finding new possibilities for medication through testing molecular compounds, noting unexpected effects from existing treatments, or the creation of new technology that allows novel ways of targeting medical products to sites in the body. Drug development occurs after researchers identify potential compounds for experiments Preclinical Research Phase. Once researchers have examined the possibilities a new drug may contain, they must do preliminary research to determine its potential for harm (toxicity). This is categorized as preclinical research and can be one of two types: in vitro or in vivo.""")
    clinical_trial_phase = PermissibleValue(
        text="clinical_trial_phase",
        description="""Clinical research involves trials of the drug on people, and it is one of the most involved stages in the drug development and approval process. Clinical trials must answer specific questions and follow a protocol determined by the drug researcher or manufacturer.""")
    clinical_trial_phase_1 = PermissibleValue(
        text="clinical_trial_phase_1",
        description="""In the FDA Clinical Trial Phase, the Clinical Trial Phase 1 involves 20 – 100 study participants and lasts several months. This phase is used to determine the safety and dosage of the drug, and about 70% of these drugs move on to the next clinical research phase.""")
    clinical_trial_phase_2 = PermissibleValue(
        text="clinical_trial_phase_2",
        description="""In the FDA Clinical Trial Phase, the Clinical Trial Phase 2 involves up to several hundred people, who must have the disease or condition the drug supposes to treat. This phase can last from a few months to two years, and its purpose is to monitor the efficacy of the drug, as well as note side effects that may occur.""")
    clinical_trial_phase_3 = PermissibleValue(
        text="clinical_trial_phase_3",
        description="""In the FDA Clinical Trial Phase, the Clinical Trial Phase 3 involves 300 – 3000 volunteers and can last up to four years. It is used to continue monitoring the efficacy of the drug, as well as exploring any longer-term adverse reactions.""")
    clinical_trial_phase_4 = PermissibleValue(
        text="clinical_trial_phase_4",
        description="""In the FDA Clinical Trial Phase, the Clinical Trial Phase 4 involves several thousands of volunteers who have the disease or condition and continues to monitor safety and efficacy. If a drug passes this phase, it goes on to FDA review.""")
    not_provided = PermissibleValue(text="not_provided")

    _defn = EnumDefinition(
        name="ResearchPhaseEnum",
    )

class DirectionQualifierEnum(EnumDefinitionImpl):

    increased = PermissibleValue(text="increased")
    upregulated = PermissibleValue(text="upregulated")
    decreased = PermissibleValue(text="decreased")
    downregulated = PermissibleValue(text="downregulated")

    _defn = EnumDefinition(
        name="DirectionQualifierEnum",
    )

class ChemicalEntityDerivativeEnum(EnumDefinitionImpl):

    metabolite = PermissibleValue(text="metabolite")

    _defn = EnumDefinition(
        name="ChemicalEntityDerivativeEnum",
    )

class ChemicalOrGeneOrGeneProductFormOrVariantEnum(EnumDefinitionImpl):

    genetic_variant_form = PermissibleValue(text="genetic_variant_form")
    modified_form = PermissibleValue(text="modified_form")
    loss_of_function_variant_form = PermissibleValue(text="loss_of_function_variant_form")
    non_loss_of_function_variant_form = PermissibleValue(text="non_loss_of_function_variant_form")
    gain_of_function_variant_form = PermissibleValue(text="gain_of_function_variant_form")
    dominant_negative_variant_form = PermissibleValue(text="dominant_negative_variant_form")
    polymorphic_form = PermissibleValue(text="polymorphic_form")
    snp_form = PermissibleValue(text="snp_form")
    analog_form = PermissibleValue(text="analog_form")

    _defn = EnumDefinition(
        name="ChemicalOrGeneOrGeneProductFormOrVariantEnum",
    )

class GeneOrGeneProductOrChemicalPartQualifierEnum(EnumDefinitionImpl):

    polya_tail = PermissibleValue(text="polya_tail")
    promoter = PermissibleValue(text="promoter")
    enhancer = PermissibleValue(text="enhancer")
    exon = PermissibleValue(text="exon")
    intron = PermissibleValue(text="intron")

    _defn = EnumDefinition(
        name="GeneOrGeneProductOrChemicalPartQualifierEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "3_prime_utr",
            PermissibleValue(text="3_prime_utr"))
        setattr(cls, "5_prime_utr",
            PermissibleValue(text="5_prime_utr"))

class GeneOrGeneProductOrChemicalEntityAspectEnum(EnumDefinitionImpl):

    activity_or_abundance = PermissibleValue(
        text="activity_or_abundance",
        description="""Used in cases where the specificity of the relationship can not be determined to be either activity or abundance.  In general, a more specific value from this enumeration should be used.""")
    abundance = PermissibleValue(text="abundance")
    activity = PermissibleValue(text="activity")
    expression = PermissibleValue(text="expression")
    synthesis = PermissibleValue(text="synthesis")
    degradation = PermissibleValue(text="degradation")
    cleavage = PermissibleValue(text="cleavage")
    hydrolysis = PermissibleValue(text="hydrolysis")
    metabolic_processing = PermissibleValue(text="metabolic_processing")
    mutation_rate = PermissibleValue(text="mutation_rate")
    stability = PermissibleValue(text="stability")
    folding = PermissibleValue(text="folding")
    localization = PermissibleValue(text="localization")
    transport = PermissibleValue(text="transport")
    absorption = PermissibleValue(text="absorption")
    aggregation = PermissibleValue(text="aggregation")
    interaction = PermissibleValue(text="interaction")
    release = PermissibleValue(text="release")
    secretion = PermissibleValue(text="secretion")
    uptake = PermissibleValue(text="uptake")
    splicing = PermissibleValue(text="splicing")
    molecular_interaction = PermissibleValue(text="molecular_interaction")
    guanyl_nucleotide_exchange = PermissibleValue(text="guanyl_nucleotide_exchange")
    adenyl_nucleotide_exchange = PermissibleValue(text="adenyl_nucleotide_exchange")
    molecular_modification = PermissibleValue(text="molecular_modification")
    acetylation = PermissibleValue(text="acetylation")
    acylation = PermissibleValue(text="acylation")
    alkylation = PermissibleValue(text="alkylation")
    amination = PermissibleValue(text="amination")
    carbamoylation = PermissibleValue(text="carbamoylation")
    ethylation = PermissibleValue(text="ethylation")
    glutathionylation = PermissibleValue(text="glutathionylation")
    glycation = PermissibleValue(text="glycation")
    glycosylation = PermissibleValue(text="glycosylation")
    glucuronidation = PermissibleValue(text="glucuronidation")
    n_linked_glycosylation = PermissibleValue(text="n_linked_glycosylation")
    o_linked_glycosylation = PermissibleValue(text="o_linked_glycosylation")
    hydroxylation = PermissibleValue(text="hydroxylation")
    lipidation = PermissibleValue(text="lipidation")
    farnesylation = PermissibleValue(text="farnesylation")
    geranoylation = PermissibleValue(text="geranoylation")
    myristoylation = PermissibleValue(text="myristoylation")
    palmitoylation = PermissibleValue(text="palmitoylation")
    prenylation = PermissibleValue(text="prenylation")
    methylation = PermissibleValue(text="methylation")
    nitrosation = PermissibleValue(text="nitrosation")
    nucleotidylation = PermissibleValue(text="nucleotidylation")
    phosphorylation = PermissibleValue(text="phosphorylation")
    ribosylation = PermissibleValue(text="ribosylation")
    sulfation = PermissibleValue(text="sulfation")
    sumoylation = PermissibleValue(text="sumoylation")
    ubiquitination = PermissibleValue(text="ubiquitination")
    oxidation = PermissibleValue(text="oxidation")
    reduction = PermissibleValue(text="reduction")
    carboxylation = PermissibleValue(text="carboxylation")

    _defn = EnumDefinition(
        name="GeneOrGeneProductOrChemicalEntityAspectEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ADP-ribosylation",
            PermissibleValue(text="ADP-ribosylation"))

class CausalMechanismQualifierEnum(EnumDefinitionImpl):

    binding = PermissibleValue(
        text="binding",
        description="""A causal mechanism mediated by the direct contact between effector and target chemical or biomolecular entity, which form a stable physical interaction.""")
    inhibition = PermissibleValue(
        text="inhibition",
        description="""A causal mechanism in which the effector binds to the target and negatively effects its normal function, e.g. prevention of enzymatic reaction or activation of downstream pathway.""")
    antibody_inhibition = PermissibleValue(
        text="antibody_inhibition",
        description="A causal mechanism in which an antibody specifically binds to and interferes with the target.")
    antagonism = PermissibleValue(
        text="antagonism",
        description="""A causal mechanism in which the effector binds to a receptor and prevents activation by an agonist through competing for the binding site.""")
    molecular_channel_blockage = PermissibleValue(
        text="molecular_channel_blockage",
        description="""A causal mechanism in which the effector binds to a molecular channel and prevents or reduces transport of ions through it.""")
    inverse_agonism = PermissibleValue(
        text="inverse_agonism",
        description="""A causal mechanism in which the effector binds to the same receptor-binding site as an agonist and antagonizes its effects, often exerting the opposite effect of the agonist by suppressing spontaneous receptor signaling.""")
    negative_allosteric_modulation = PermissibleValue(
        text="negative_allosteric_modulation",
        description="""A causal mechanism in which the effector reduces or prevents the action of the endogenous ligand of a receptor by binding to a site distinct from that ligand (i.e. non-competitive inhibition)""")
    agonism = PermissibleValue(
        text="agonism",
        description="""A causal mechanism in which the effector binds and activates a receptor to mimic the effect of an endogenous ligand.""")
    molecular_channel_opening = PermissibleValue(
        text="molecular_channel_opening",
        description="""A causal mechanism in which the effector binds to a molecular channel and facilitates transport of ions through it.""")
    positive_allosteric_modulation = PermissibleValue(
        text="positive_allosteric_modulation",
        description="""A causal mechanism in which the effector enhances the action of the endogenous ligand of a receptor by binding to a site distinct from that ligand (i.e. non-competitive inhibition)""")
    potentiation = PermissibleValue(
        text="potentiation",
        description="""A causal mechanism in which the effector  binds to and enhances or intensifies the effect of some other chemical or drug on its target.""")
    activation = PermissibleValue(
        text="activation",
        description="""A causal mechanism in which the effector binds to and positively affects the normal functioning of its target.""")
    inducer = PermissibleValue(
        text="inducer",
        description="""A causal mechanism in which the effector binds to and increases the activity/rate of an enzyme that processes drugs in the body.""")
    transcriptional_regulation = PermissibleValue(
        text="transcriptional_regulation",
        description="A causal mechanism mediated by through the control of target gene transcription")
    signaling_mediated_control = PermissibleValue(
        text="signaling_mediated_control",
        description="""A causal mechanism mediated by the activation or control of signaling events that influence the some aspect of the target entity (e.g. its activity, processing, transport, etc)""")
    stabilization = PermissibleValue(text="stabilization")
    stimulation = PermissibleValue(text="stimulation")
    releasing_activity = PermissibleValue(text="releasing_activity")

    _defn = EnumDefinition(
        name="CausalMechanismQualifierEnum",
    )

class LogicalInterpretationEnum(EnumDefinitionImpl):

    some_some = PermissibleValue(
        text="some_some",
        description="A modifier on a triple that causes the triple to be interpreted as a some-some statement",
        meaning=OS["SomeSomeInterpretation"])
    all_some = PermissibleValue(
        text="all_some",
        description="A modifier on a triple that causes the triple to be interpreted as an all-some statement.",
        meaning=OS["AllSomeInterpretation"])
    inverse_all_some = PermissibleValue(text="inverse_all_some")

    _defn = EnumDefinition(
        name="LogicalInterpretationEnum",
    )

class ReactionDirectionEnum(EnumDefinitionImpl):

    left_to_right = PermissibleValue(text="left_to_right")
    right_to_left = PermissibleValue(text="right_to_left")
    bidirectional = PermissibleValue(text="bidirectional")
    neutral = PermissibleValue(text="neutral")

    _defn = EnumDefinition(
        name="ReactionDirectionEnum",
    )

class ReactionSideEnum(EnumDefinitionImpl):

    left = PermissibleValue(text="left")
    right = PermissibleValue(text="right")

    _defn = EnumDefinition(
        name="ReactionSideEnum",
    )

class PhaseEnum(EnumDefinitionImpl):
    """
    phase
    """
    _defn = EnumDefinition(
        name="PhaseEnum",
        description="phase",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
            PermissibleValue(text="0"))
        setattr(cls, "1",
            PermissibleValue(text="1"))
        setattr(cls, "2",
            PermissibleValue(text="2"))

class StrandEnum(EnumDefinitionImpl):
    """
    strand
    """
    _defn = EnumDefinition(
        name="StrandEnum",
        description="strand",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "+",
            PermissibleValue(
                text="+",
                description="Positive"))
        setattr(cls, "-",
            PermissibleValue(
                text="-",
                description="Negative"))
        setattr(cls, ".",
            PermissibleValue(
                text=".",
                description="Unstranded"))
        setattr(cls, "?",
            PermissibleValue(
                text="?",
                description="Unknown"))

class SequenceEnum(EnumDefinitionImpl):
    """
    type of sequence
    """
    na = PermissibleValue(
        text="na",
        description="nucleic acid")
    aa = PermissibleValue(
        text="aa",
        description="amino acid")

    _defn = EnumDefinition(
        name="SequenceEnum",
        description="type of sequence",
    )

class DruggableGeneCategoryEnum(EnumDefinitionImpl):

    tclin = PermissibleValue(
        text="tclin",
        description="""These targets have activities in DrugCentral (ie. approved drugs) with known mechanism of action.""")
    tbio = PermissibleValue(
        text="tbio",
        description="""These targets have activities in ChEMBL, Guide to Pharmacology or DrugCentral that satisfy the activity thresholds detailed below.""")
    tchem = PermissibleValue(
        text="tchem",
        description="""These targets do not have known drug or small molecule activities that satisfy the activity thresholds detailed below AND satisfy one or more of the following criteria: target is above the cutoff criteria for Tdark target is annotated with a Gene Ontology Molecular Function or Biological Process leaf term(s) with an Experimental Evidence code""")
    tdark = PermissibleValue(
        text="tdark",
        description="""These are targets about which virtually nothing is known. They do not have known drug or small molecule activities that satisfy the activity thresholds detailed below AND satisfy two or more of the following criteria: A PubMed text-mining score from Jensen Lab less than 5, greater than or equal TO 3 Gene RIFs, or less than or equal to 50 Antibodies available according to http://antibodypedia.com.""")

    _defn = EnumDefinition(
        name="DruggableGeneCategoryEnum",
    )

class DrugAvailabilityEnum(EnumDefinitionImpl):

    over_the_counter = PermissibleValue(
        text="over_the_counter",
        description="chemical entity is available over the counter without a prescription.")
    prescription = PermissibleValue(
        text="prescription",
        description="chemical entity is available by prescription.")

    _defn = EnumDefinition(
        name="DrugAvailabilityEnum",
    )

class DrugDeliveryEnum(EnumDefinitionImpl):

    inhalation = PermissibleValue(text="inhalation")
    oral = PermissibleValue(text="oral")
    absorption_through_the_skin = PermissibleValue(text="absorption_through_the_skin")
    intravenous_injection = PermissibleValue(text="intravenous_injection")

    _defn = EnumDefinition(
        name="DrugDeliveryEnum",
    )

class ResourceRoleEnum(EnumDefinitionImpl):
    """
    The role played by the information reource in serving as a source for an edge in a TRAPI message. Note that a
    given Edge should have one and only one 'primary' source, and may have any number of 'aggregator' or 'supporting
    data' sources. This enumeration is found in Biolink Model, but is repeated here for convenience.
    """
    primary_knowledge_source = PermissibleValue(text="primary_knowledge_source")
    aggregator_knowledge_source = PermissibleValue(text="aggregator_knowledge_source")
    supporting_data_source = PermissibleValue(text="supporting_data_source")

    _defn = EnumDefinition(
        name="ResourceRoleEnum",
        description="""The role played by the information reource in serving as a source for an edge in a TRAPI message. Note that a given Edge should have one and only one 'primary' source, and may have any number of 'aggregator' or 'supporting data' sources.  This enumeration is found in Biolink Model, but is repeated here for convenience.""",
    )

class AffinityParameterEnum(EnumDefinitionImpl):
    """
    The types of parameters that can be used to describe the affinity between two entities, characteristically
    chemicals and proteins.
    """
    pIC50 = PermissibleValue(
        text="pIC50",
        description="""Negative logarithm of the molar concentration of a chemical that produces a 50% inhibition of a function""")
    pEC50 = PermissibleValue(
        text="pEC50",
        description="""Negative logarithm of the molar concentration of a chemical that produces a 50% excitation of a function""")
    pAC50 = PermissibleValue(text="pAC50")
    pXC50 = PermissibleValue(text="pXC50")
    pKi = PermissibleValue(text="pKi")
    pKd = PermissibleValue(text="pKd")

    _defn = EnumDefinition(
        name="AffinityParameterEnum",
        description="""The types of parameters that can be used to describe the affinity between two entities, characteristically chemicals and proteins.""",
    )

class FDAIDAAdverseEventEnum(EnumDefinitionImpl):
    """
    please consult with the FDA guidelines as proposed in this document:
    https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm?fr=312.32
    """
    life_threatening_adverse_event = PermissibleValue(
        text="life_threatening_adverse_event",
        description="""An adverse event or suspected adverse reaction is considered 'life-threatening' if, in the view of either the investigator or sponsor, its occurrence places the patient or subject at immediate risk of death. It does not include an adverse event or suspected adverse reaction that, had it occurred in a more severe form, might have caused death.""")
    serious_adverse_event = PermissibleValue(
        text="serious_adverse_event",
        description="""An adverse event or suspected adverse reaction is considered 'serious' if, in the view of either the investigator or sponsor, it results in any of the following outcomes: Death, a life-threatening adverse event, inpatient hospitalization or prolongation of existing hospitalization, a persistent or significant incapacity or substantial disruption of the ability to conduct normal life functions, or a congenital anomaly/birth defect. Important medical events that may not result in death, be life-threatening, or require hospitalization may be considered serious when, based upon appropriate medical judgment, they may jeopardize the patient or subject and may require medical or surgical intervention to prevent one of the outcomes listed in this definition. Examples of such medical events include allergic bronchospasm requiring intensive treatment in an emergency room or at home, blood dyscrasias or convulsions that do not result in inpatient hospitalization, or the development of drug dependency or drug abuse.""")
    suspected_adverse_reaction = PermissibleValue(
        text="suspected_adverse_reaction",
        description="""means any adverse event for which there is a reasonable possibility that the drug caused the adverse event. For the purposes of IND safety reporting, 'reasonable possibility' means there is evidence to suggest a causal relationship between the drug and the adverse event. Suspected adverse reaction implies a lesser degree of certainty about causality than adverse reaction, which means any adverse event caused by a drug.""")
    unexpected_adverse_event = PermissibleValue(
        text="unexpected_adverse_event",
        description="""An adverse event or suspected adverse reaction is considered 'unexpected' if it is not listed in the investigator brochure or is not listed at the specificity or severity that has been observed; or, if an investigator brochure is not required or available, is not consistent with the risk information described in the general investigational plan or elsewhere in the current application, as amended. For example, under this definition, hepatic necrosis would be unexpected (by virtue of greater severity) if the investigator brochure referred only to elevated hepatic enzymes or hepatitis. Similarly, cerebral thromboembolism and cerebral vasculitis would be unexpected (by virtue of greater specificity) if the investigator brochure listed only cerebral vascular accidents. 'Unexpected', as used in this definition, also refers to adverse events or suspected adverse reactions that are mentioned in the investigator brochure as occurring with a class of drugs or as anticipated from the pharmacological properties of the drug, but are not specifically mentioned as occurring with the particular drug under investigation.""")

    _defn = EnumDefinition(
        name="FDAIDAAdverseEventEnum",
        description="""please consult with the FDA guidelines as proposed in this document: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm?fr=312.32""",
    )

class AgentTypeEnum(EnumDefinitionImpl):

    manual_agent = PermissibleValue(
        text="manual_agent",
        description="""A human agent who is responsible for generating a statement of knowledge. The human may utilize computationally generated information as evidence for the resulting knowledge,  but the human is the one who ultimately interprets/reasons with  this evidence to produce a statement of knowledge.""")
    automated_agent = PermissibleValue(
        text="automated_agent",
        description="""An automated agent, typically a software program or tool, that is  responsible for generating a statement of knowledge. Human contribution  to the knowledge creation process ends with the definition and coding of algorithms or analysis pipelines that get executed by the automated agent.""")
    data_analysis_pipeline = PermissibleValue(
        text="data_analysis_pipeline",
        description="""An automated agent that executes an analysis workflow over data and  reports the direct results of the analysis. These typically report  statistical associations/correlations between variables in the input dataset, and do not interpret/infer broader conclusions from associations the analysis reveals in the data.""")
    computational_model = PermissibleValue(
        text="computational_model",
        description="""An automated agent that generates knowledge statements (typically predictions) based on rules/logic explicitly encoded in an algorithm (e.g. heuristic models, supervised classifiers), or learned from patterns  observed in data (e.g. ML models, unsupervised classifiers).""")
    text_mining_agent = PermissibleValue(
        text="text_mining_agent",
        description="""An automated agent that uses Natural Language Processing to recognize concepts and/or relationships in text, and report them using formally encoded semantics (e.g. as an edge in a knowledge graph).""")
    image_processing_agent = PermissibleValue(
        text="image_processing_agent",
        description="""An automated agent that processes images to generate textual statements of  knowledge derived from the image and/or expressed in text the image  depicts (e.g. via OCR).""")
    manual_validation_of_automated_agent = PermissibleValue(
        text="manual_validation_of_automated_agent",
        description="""A human agent reviews and validates/approves the veracity of knowledge  that is initially generated by an automated agent.""")
    not_provided = PermissibleValue(
        text="not_provided",
        description="""The agent type is not provided, typically because it cannot be determined from available information if the agent that generated the knowledge is  manual or automated.""")

    _defn = EnumDefinition(
        name="AgentTypeEnum",
    )

class KnowledgeLevelEnum(EnumDefinitionImpl):

    knowledge_assertion = PermissibleValue(
        text="knowledge_assertion",
        description="""A statement of purported fact that is put forth by an agent as true, based on assessment of direct evidence. Assertions are likely but not  definitively true.""")
    logical_entailment = PermissibleValue(
        text="logical_entailment",
        description="""A statement reporting a conclusion that follows logically from premises representing established facts or knowledge assertions (e.g. fingernail part of finger, finger part of hand --> fingernail part of hand).""")
    prediction = PermissibleValue(
        text="prediction",
        description="""A statement of a possible fact based on probabilistic forms of reasoning over more indirect forms of evidence, that lead to more speculative conclusions.""")
    statistical_association = PermissibleValue(
        text="statistical_association",
        description="""A statement that reports concepts representing variables in a dataset to be statistically associated with each other in a particular cohort (e.g. 'Metformin Treatment (variable 1) is correlated with Diabetes Diagnosis (variable 2) in EHR dataset X').""")
    observation = PermissibleValue(
        text="observation",
        description="""A statement reporting (and possibly quantifying) a phenomenon that was observed to occur -  absent any analysis or interpretation that generates a statistical association or supports a broader conclusion or inference.""")
    not_provided = PermissibleValue(
        text="not_provided",
        description="""The knowledge level is not provided, typically because it cannot be determined from available. information.""")

    _defn = EnumDefinition(
        name="KnowledgeLevelEnum",
    )

# Slots
class slots:
    pass

slots.has_attribute = Slot(uri=BIOLINK.has_attribute, name="has attribute", curie=BIOLINK.curie('has_attribute'),
                   model_uri=BIOLINK.has_attribute, domain=Entity, range=Optional[Union[Union[str, AttributeId], list[Union[str, AttributeId]]]])

slots.has_attribute_type = Slot(uri=BIOLINK.has_attribute_type, name="has attribute type", curie=BIOLINK.curie('has_attribute_type'),
                   model_uri=BIOLINK.has_attribute_type, domain=Attribute, range=Union[str, OntologyClassId])

slots.has_qualitative_value = Slot(uri=BIOLINK.has_qualitative_value, name="has qualitative value", curie=BIOLINK.curie('has_qualitative_value'),
                   model_uri=BIOLINK.has_qualitative_value, domain=Attribute, range=Optional[Union[str, NamedThingId]])

slots.has_quantitative_value = Slot(uri=BIOLINK.has_quantitative_value, name="has quantitative value", curie=BIOLINK.curie('has_quantitative_value'),
                   model_uri=BIOLINK.has_quantitative_value, domain=Attribute, range=Optional[Union[Union[dict, QuantityValue], list[Union[dict, QuantityValue]]]])

slots.has_numeric_value = Slot(uri=BIOLINK.has_numeric_value, name="has numeric value", curie=BIOLINK.curie('has_numeric_value'),
                   model_uri=BIOLINK.has_numeric_value, domain=QuantityValue, range=Optional[float])

slots.has_unit = Slot(uri=BIOLINK.has_unit, name="has unit", curie=BIOLINK.curie('has_unit'),
                   model_uri=BIOLINK.has_unit, domain=QuantityValue, range=Optional[Union[str, Unit]])

slots.base_coordinate = Slot(uri=BIOLINK.base_coordinate, name="base coordinate", curie=BIOLINK.curie('base_coordinate'),
                   model_uri=BIOLINK.base_coordinate, domain=GenomicSequenceLocalization, range=Optional[int])

slots.node_property = Slot(uri=BIOLINK.node_property, name="node property", curie=BIOLINK.curie('node_property'),
                   model_uri=BIOLINK.node_property, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=BIOLINK.id, name="id", curie=BIOLINK.curie('id'),
                   model_uri=BIOLINK.id, domain=Entity, range=Union[str, EntityId])

slots.iri = Slot(uri=BIOLINK.iri, name="iri", curie=BIOLINK.curie('iri'),
                   model_uri=BIOLINK.iri, domain=None, range=Optional[Union[str, IriType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=BIOLINK.type, domain=Entity, range=Optional[Union[str, list[str]]])

slots.category = Slot(uri=BIOLINK.category, name="category", curie=BIOLINK.curie('category'),
                   model_uri=BIOLINK.category, domain=Entity, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.publication_type = Slot(uri=DCT.type, name="publication type", curie=DCT.curie('type'),
                   model_uri=BIOLINK.publication_type, domain=None, range=Optional[Union[str, list[str]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=BIOLINK.name, domain=Entity, range=Optional[Union[str, LabelType]])

slots.hgvs_nomenclature = Slot(uri=BIOLINK.hgvs_nomenclature, name="hgvs nomenclature", curie=BIOLINK.curie('hgvs_nomenclature'),
                   model_uri=BIOLINK.hgvs_nomenclature, domain=SequenceVariant, range=Optional[Union[str, list[str]]])

slots.stoichiometry = Slot(uri=BIOLINK.stoichiometry, name="stoichiometry", curie=BIOLINK.curie('stoichiometry'),
                   model_uri=BIOLINK.stoichiometry, domain=Association, range=Optional[int])

slots.reaction_direction = Slot(uri=BIOLINK.reaction_direction, name="reaction direction", curie=BIOLINK.curie('reaction_direction'),
                   model_uri=BIOLINK.reaction_direction, domain=Association, range=Optional[Union[str, "ReactionDirectionEnum"]])

slots.reaction_balanced = Slot(uri=BIOLINK.reaction_balanced, name="reaction balanced", curie=BIOLINK.curie('reaction_balanced'),
                   model_uri=BIOLINK.reaction_balanced, domain=Association, range=Optional[Union[bool, Bool]])

slots.reaction_side = Slot(uri=BIOLINK.reaction_side, name="reaction side", curie=BIOLINK.curie('reaction_side'),
                   model_uri=BIOLINK.reaction_side, domain=Association, range=Optional[Union[str, "ReactionSideEnum"]])

slots.symbol = Slot(uri=BIOLINK.symbol, name="symbol", curie=BIOLINK.curie('symbol'),
                   model_uri=BIOLINK.symbol, domain=NamedThing, range=Optional[str])

slots.synonym = Slot(uri=BIOLINK.synonym, name="synonym", curie=BIOLINK.curie('synonym'),
                   model_uri=BIOLINK.synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]])

slots.exact_synonym = Slot(uri=BIOLINK.exact_synonym, name="exact synonym", curie=BIOLINK.curie('exact_synonym'),
                   model_uri=BIOLINK.exact_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]])

slots.broad_synonym = Slot(uri=BIOLINK.broad_synonym, name="broad synonym", curie=BIOLINK.curie('broad_synonym'),
                   model_uri=BIOLINK.broad_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]])

slots.narrow_synonym = Slot(uri=BIOLINK.narrow_synonym, name="narrow synonym", curie=BIOLINK.curie('narrow_synonym'),
                   model_uri=BIOLINK.narrow_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]])

slots.related_synonym = Slot(uri=BIOLINK.related_synonym, name="related synonym", curie=BIOLINK.curie('related_synonym'),
                   model_uri=BIOLINK.related_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]])

slots.deprecated = Slot(uri=BIOLINK.deprecated, name="deprecated", curie=BIOLINK.curie('deprecated'),
                   model_uri=BIOLINK.deprecated, domain=None, range=Optional[Union[bool, Bool]])

slots.has_topic = Slot(uri=BIOLINK.has_topic, name="has topic", curie=BIOLINK.curie('has_topic'),
                   model_uri=BIOLINK.has_topic, domain=NamedThing, range=Optional[Union[str, OntologyClassId]])

slots.xref = Slot(uri=BIOLINK.xref, name="xref", curie=BIOLINK.curie('xref'),
                   model_uri=BIOLINK.xref, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.url = Slot(uri=BIOLINK.url, name="url", curie=BIOLINK.curie('url'),
                   model_uri=BIOLINK.url, domain=Entity, range=Optional[str])

slots.semmed_agreement_count = Slot(uri=BIOLINK.semmed_agreement_count, name="semmed agreement count", curie=BIOLINK.curie('semmed_agreement_count'),
                   model_uri=BIOLINK.semmed_agreement_count, domain=Association, range=Optional[int])

slots.support_graphs = Slot(uri=BIOLINK.support_graphs, name="support graphs", curie=BIOLINK.curie('support_graphs'),
                   model_uri=BIOLINK.support_graphs, domain=Association, range=Optional[Union[str, list[str]]])

slots.resource_id = Slot(uri=BIOLINK.resource_id, name="resource id", curie=BIOLINK.curie('resource_id'),
                   model_uri=BIOLINK.resource_id, domain=RetrievalSource, range=Optional[Union[str, URIorCURIE]])

slots.resource_role = Slot(uri=BIOLINK.resource_role, name="resource role", curie=BIOLINK.curie('resource_role'),
                   model_uri=BIOLINK.resource_role, domain=RetrievalSource, range=Optional[Union[str, "ResourceRoleEnum"]])

slots.retrieval_source_ids = Slot(uri=BIOLINK.retrieval_source_ids, name="retrieval source ids", curie=BIOLINK.curie('retrieval_source_ids'),
                   model_uri=BIOLINK.retrieval_source_ids, domain=None, range=Optional[Union[Union[str, RetrievalSourceId], list[Union[str, RetrievalSourceId]]]])

slots.full_name = Slot(uri=BIOLINK.full_name, name="full name", curie=BIOLINK.curie('full_name'),
                   model_uri=BIOLINK.full_name, domain=NamedThing, range=Optional[Union[str, LabelType]])

slots.upstream_resource_ids = Slot(uri=BIOLINK.upstream_resource_ids, name="upstream resource ids", curie=BIOLINK.curie('upstream_resource_ids'),
                   model_uri=BIOLINK.upstream_resource_ids, domain=RetrievalSource, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.source_record_urls = Slot(uri=BIOLINK.source_record_urls, name="source record urls", curie=BIOLINK.curie('source_record_urls'),
                   model_uri=BIOLINK.source_record_urls, domain=RetrievalSource, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=BIOLINK.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.systematic_synonym = Slot(uri=GOP.systematic_synonym, name="systematic synonym", curie=GOP.curie('systematic_synonym'),
                   model_uri=BIOLINK.systematic_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], list[Union[str, LabelType]]]])

slots.affiliation = Slot(uri=BIOLINK.affiliation, name="affiliation", curie=BIOLINK.curie('affiliation'),
                   model_uri=BIOLINK.affiliation, domain=Agent, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.address = Slot(uri=BIOLINK.address, name="address", curie=BIOLINK.curie('address'),
                   model_uri=BIOLINK.address, domain=NamedThing, range=Optional[str])

slots.latitude = Slot(uri=BIOLINK.latitude, name="latitude", curie=BIOLINK.curie('latitude'),
                   model_uri=BIOLINK.latitude, domain=NamedThing, range=Optional[float])

slots.longitude = Slot(uri=BIOLINK.longitude, name="longitude", curie=BIOLINK.curie('longitude'),
                   model_uri=BIOLINK.longitude, domain=NamedThing, range=Optional[float])

slots.timepoint = Slot(uri=BIOLINK.timepoint, name="timepoint", curie=BIOLINK.curie('timepoint'),
                   model_uri=BIOLINK.timepoint, domain=None, range=Optional[Union[str, TimeType]])

slots.creation_date = Slot(uri=BIOLINK.creation_date, name="creation date", curie=BIOLINK.curie('creation_date'),
                   model_uri=BIOLINK.creation_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.update_date = Slot(uri=BIOLINK.update_date, name="update date", curie=BIOLINK.curie('update_date'),
                   model_uri=BIOLINK.update_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.aggregate_statistic = Slot(uri=BIOLINK.aggregate_statistic, name="aggregate statistic", curie=BIOLINK.curie('aggregate_statistic'),
                   model_uri=BIOLINK.aggregate_statistic, domain=NamedThing, range=Optional[str])

slots.has_count = Slot(uri=BIOLINK.has_count, name="has count", curie=BIOLINK.curie('has_count'),
                   model_uri=BIOLINK.has_count, domain=NamedThing, range=Optional[int])

slots.has_total = Slot(uri=BIOLINK.has_total, name="has total", curie=BIOLINK.curie('has_total'),
                   model_uri=BIOLINK.has_total, domain=NamedThing, range=Optional[int])

slots.has_quotient = Slot(uri=BIOLINK.has_quotient, name="has quotient", curie=BIOLINK.curie('has_quotient'),
                   model_uri=BIOLINK.has_quotient, domain=NamedThing, range=Optional[float])

slots.has_percentage = Slot(uri=BIOLINK.has_percentage, name="has percentage", curie=BIOLINK.curie('has_percentage'),
                   model_uri=BIOLINK.has_percentage, domain=NamedThing, range=Optional[float])

slots.has_taxonomic_rank = Slot(uri=BIOLINK.has_taxonomic_rank, name="has taxonomic rank", curie=BIOLINK.curie('has_taxonomic_rank'),
                   model_uri=BIOLINK.has_taxonomic_rank, domain=NamedThing, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA["P105"]])

slots.has_dataset = Slot(uri=BIOLINK.has_dataset, name="has dataset", curie=BIOLINK.curie('has_dataset'),
                   model_uri=BIOLINK.has_dataset, domain=DatasetVersion, range=Optional[Union[str, DatasetId]])

slots.source_web_page = Slot(uri=BIOLINK.source_web_page, name="source web page", curie=BIOLINK.curie('source_web_page'),
                   model_uri=BIOLINK.source_web_page, domain=DatasetSummary, range=Optional[str])

slots.source_logo = Slot(uri=SCHEMA.logo, name="source logo", curie=SCHEMA.curie('logo'),
                   model_uri=BIOLINK.source_logo, domain=DatasetSummary, range=Optional[str])

slots.retrieved_on = Slot(uri=BIOLINK.retrieved_on, name="retrieved on", curie=BIOLINK.curie('retrieved_on'),
                   model_uri=BIOLINK.retrieved_on, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.version_of = Slot(uri=BIOLINK.version_of, name="version of", curie=BIOLINK.curie('version_of'),
                   model_uri=BIOLINK.version_of, domain=DatasetVersion, range=Optional[Union[str, DatasetSummaryId]])

slots.version = Slot(uri=BIOLINK.version, name="version", curie=BIOLINK.curie('version'),
                   model_uri=BIOLINK.version, domain=Dataset, range=Optional[str])

slots.license = Slot(uri=BIOLINK.license, name="license", curie=BIOLINK.curie('license'),
                   model_uri=BIOLINK.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=BIOLINK.rights, name="rights", curie=BIOLINK.curie('rights'),
                   model_uri=BIOLINK.rights, domain=InformationContentEntity, range=Optional[str])

slots.format = Slot(uri=BIOLINK.format, name="format", curie=BIOLINK.curie('format'),
                   model_uri=BIOLINK.format, domain=InformationContentEntity, range=Optional[str])

slots.created_with = Slot(uri=BIOLINK.created_with, name="created with", curie=BIOLINK.curie('created_with'),
                   model_uri=BIOLINK.created_with, domain=Dataset, range=Optional[str])

slots.download_url = Slot(uri=DCAT.downloadURL, name="download url", curie=DCAT.curie('downloadURL'),
                   model_uri=BIOLINK.download_url, domain=InformationContentEntity, range=Optional[str])

slots.dataset_download_url = Slot(uri=DCAT.downloadURL, name="dataset download url", curie=DCAT.curie('downloadURL'),
                   model_uri=BIOLINK.dataset_download_url, domain=Dataset, range=Optional[str])

slots.distribution_download_url = Slot(uri=BIOLINK.distribution_download_url, name="distribution download url", curie=BIOLINK.curie('distribution_download_url'),
                   model_uri=BIOLINK.distribution_download_url, domain=DatasetDistribution, range=Optional[str])

slots.ingest_date = Slot(uri=BIOLINK.ingest_date, name="ingest date", curie=BIOLINK.curie('ingest_date'),
                   model_uri=BIOLINK.ingest_date, domain=DatasetVersion, range=Optional[str])

slots.has_distribution = Slot(uri=DCT.distribution, name="has distribution", curie=DCT.curie('distribution'),
                   model_uri=BIOLINK.has_distribution, domain=DatasetVersion, range=Optional[Union[str, DatasetDistributionId]])

slots.published_in = Slot(uri=BIOLINK.published_in, name="published in", curie=BIOLINK.curie('published_in'),
                   model_uri=BIOLINK.published_in, domain=Publication, range=Optional[Union[str, URIorCURIE]])

slots.iso_abbreviation = Slot(uri=BIOLINK.iso_abbreviation, name="iso abbreviation", curie=BIOLINK.curie('iso_abbreviation'),
                   model_uri=BIOLINK.iso_abbreviation, domain=Publication, range=Optional[str])

slots.authors = Slot(uri=BIOLINK.authors, name="authors", curie=BIOLINK.curie('authors'),
                   model_uri=BIOLINK.authors, domain=Publication, range=Optional[Union[Union[str, AgentId], list[Union[str, AgentId]]]])

slots.volume = Slot(uri=BIOLINK.volume, name="volume", curie=BIOLINK.curie('volume'),
                   model_uri=BIOLINK.volume, domain=Publication, range=Optional[str])

slots.chapter = Slot(uri=BIOLINK.chapter, name="chapter", curie=BIOLINK.curie('chapter'),
                   model_uri=BIOLINK.chapter, domain=BookChapter, range=Optional[str])

slots.issue = Slot(uri=BIOLINK.issue, name="issue", curie=BIOLINK.curie('issue'),
                   model_uri=BIOLINK.issue, domain=Publication, range=Optional[str])

slots.pages = Slot(uri=BIOLINK.pages, name="pages", curie=BIOLINK.curie('pages'),
                   model_uri=BIOLINK.pages, domain=Publication, range=Optional[Union[str, list[str]]])

slots.summary = Slot(uri=BIOLINK.summary, name="summary", curie=BIOLINK.curie('summary'),
                   model_uri=BIOLINK.summary, domain=Publication, range=Optional[str])

slots.keywords = Slot(uri=BIOLINK.keywords, name="keywords", curie=BIOLINK.curie('keywords'),
                   model_uri=BIOLINK.keywords, domain=Publication, range=Optional[Union[str, list[str]]])

slots.mesh_terms = Slot(uri=BIOLINK.mesh_terms, name="mesh terms", curie=BIOLINK.curie('mesh_terms'),
                   model_uri=BIOLINK.mesh_terms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.clinical_trial_phase = Slot(uri=BIOLINK.clinical_trial_phase, name="clinical trial phase", curie=BIOLINK.curie('clinical_trial_phase'),
                   model_uri=BIOLINK.clinical_trial_phase, domain=NamedThing, range=Optional[Union[str, "ResearchPhaseEnum"]])

slots.clinical_trial_primary_purpose = Slot(uri=BIOLINK.clinical_trial_primary_purpose, name="clinical trial primary purpose", curie=BIOLINK.curie('clinical_trial_primary_purpose'),
                   model_uri=BIOLINK.clinical_trial_primary_purpose, domain=ClinicalTrial, range=Optional[str])

slots.clinical_trial_intervention_model = Slot(uri=BIOLINK.clinical_trial_intervention_model, name="clinical trial intervention model", curie=BIOLINK.curie('clinical_trial_intervention_model'),
                   model_uri=BIOLINK.clinical_trial_intervention_model, domain=ClinicalTrial, range=Optional[str])

slots.clinical_trial_time_perspective = Slot(uri=BIOLINK.clinical_trial_time_perspective, name="clinical trial time perspective", curie=BIOLINK.curie('clinical_trial_time_perspective'),
                   model_uri=BIOLINK.clinical_trial_time_perspective, domain=ClinicalTrial, range=Optional[str])

slots.clinical_trial_overall_status = Slot(uri=BIOLINK.clinical_trial_overall_status, name="clinical trial overall status", curie=BIOLINK.curie('clinical_trial_overall_status'),
                   model_uri=BIOLINK.clinical_trial_overall_status, domain=ClinicalTrial, range=Optional[Union[str, "ClinicalTrialStatusEnum"]])

slots.clinical_trial_intervention_boxed_warning = Slot(uri=BIOLINK.clinical_trial_intervention_boxed_warning, name="clinical trial intervention boxed warning", curie=BIOLINK.curie('clinical_trial_intervention_boxed_warning'),
                   model_uri=BIOLINK.clinical_trial_intervention_boxed_warning, domain=Association, range=Optional[Union[bool, Bool]])

slots.clinical_trial_tested_intervention = Slot(uri=BIOLINK.clinical_trial_tested_intervention, name="clinical trial tested intervention", curie=BIOLINK.curie('clinical_trial_tested_intervention'),
                   model_uri=BIOLINK.clinical_trial_tested_intervention, domain=Association, range=Optional[str])

slots.has_biological_sequence = Slot(uri=BIOLINK.has_biological_sequence, name="has biological sequence", curie=BIOLINK.curie('has_biological_sequence'),
                   model_uri=BIOLINK.has_biological_sequence, domain=NamedThing, range=Optional[Union[str, BiologicalSequence]])

slots.has_gene_or_gene_product = Slot(uri=BIOLINK.has_gene_or_gene_product, name="has gene or gene product", curie=BIOLINK.curie('has_gene_or_gene_product'),
                   model_uri=BIOLINK.has_gene_or_gene_product, domain=NamedThing, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.has_gene = Slot(uri=BIOLINK.has_gene, name="has gene", curie=BIOLINK.curie('has_gene'),
                   model_uri=BIOLINK.has_gene, domain=NamedThing, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.has_zygosity = Slot(uri=BIOLINK.has_zygosity, name="has zygosity", curie=BIOLINK.curie('has_zygosity'),
                   model_uri=BIOLINK.has_zygosity, domain=NucleicAcidEntity, range=Optional[Union[str, ZygosityId]])

slots.has_chemical_formula = Slot(uri=BIOLINK.has_chemical_formula, name="has chemical formula", curie=BIOLINK.curie('has_chemical_formula'),
                   model_uri=BIOLINK.has_chemical_formula, domain=NamedThing, range=Optional[str])

slots.is_metabolite = Slot(uri=BIOLINK.is_metabolite, name="is metabolite", curie=BIOLINK.curie('is_metabolite'),
                   model_uri=BIOLINK.is_metabolite, domain=MolecularEntity, range=Optional[Union[bool, Bool]])

slots.has_constituent = Slot(uri=BIOLINK.has_constituent, name="has constituent", curie=BIOLINK.curie('has_constituent'),
                   model_uri=BIOLINK.has_constituent, domain=NamedThing, range=Optional[Union[Union[str, MolecularEntityId], list[Union[str, MolecularEntityId]]]])

slots.has_drug = Slot(uri=BIOLINK.has_drug, name="has drug", curie=BIOLINK.curie('has_drug'),
                   model_uri=BIOLINK.has_drug, domain=NamedThing, range=Optional[Union[Union[str, DrugId], list[Union[str, DrugId]]]])

slots.has_device = Slot(uri=BIOLINK.has_device, name="has device", curie=BIOLINK.curie('has_device'),
                   model_uri=BIOLINK.has_device, domain=NamedThing, range=Optional[Union[Union[str, DeviceId], list[Union[str, DeviceId]]]])

slots.has_procedure = Slot(uri=BIOLINK.has_procedure, name="has procedure", curie=BIOLINK.curie('has_procedure'),
                   model_uri=BIOLINK.has_procedure, domain=NamedThing, range=Optional[Union[Union[str, ProcedureId], list[Union[str, ProcedureId]]]])

slots.has_receptor = Slot(uri=BIOLINK.has_receptor, name="has receptor", curie=BIOLINK.curie('has_receptor'),
                   model_uri=BIOLINK.has_receptor, domain=None, range=Optional[Union[str, OrganismalEntityId]])

slots.has_stressor = Slot(uri=BIOLINK.has_stressor, name="has stressor", curie=BIOLINK.curie('has_stressor'),
                   model_uri=BIOLINK.has_stressor, domain=None, range=Optional[str])

slots.has_route = Slot(uri=BIOLINK.has_route, name="has route", curie=BIOLINK.curie('has_route'),
                   model_uri=BIOLINK.has_route, domain=None, range=Optional[str])

slots.response_context_qualifier = Slot(uri=BIOLINK.response_context_qualifier, name="response context qualifier", curie=BIOLINK.curie('response_context_qualifier'),
                   model_uri=BIOLINK.response_context_qualifier, domain=Association, range=Optional[Union[str, "ResponseEnum"]])

slots.response_target_context_qualifier = Slot(uri=BIOLINK.response_target_context_qualifier, name="response target context qualifier", curie=BIOLINK.curie('response_target_context_qualifier'),
                   model_uri=BIOLINK.response_target_context_qualifier, domain=Association, range=Optional[Union[str, "ResponseTargetEnum"]])

slots.population_context_qualifier = Slot(uri=BIOLINK.population_context_qualifier, name="population context qualifier", curie=BIOLINK.curie('population_context_qualifier'),
                   model_uri=BIOLINK.population_context_qualifier, domain=Association, range=Optional[Union[str, PopulationOfIndividualOrganismsId]])

slots.temporal_context_qualifier = Slot(uri=BIOLINK.temporal_context_qualifier, name="temporal context qualifier", curie=BIOLINK.curie('temporal_context_qualifier'),
                   model_uri=BIOLINK.temporal_context_qualifier, domain=Association, range=Optional[Union[str, TimeType]])

slots.temporal_interval_qualifier = Slot(uri=BIOLINK.temporal_interval_qualifier, name="temporal interval qualifier", curie=BIOLINK.curie('temporal_interval_qualifier'),
                   model_uri=BIOLINK.temporal_interval_qualifier, domain=Association, range=Optional[Union[str, TimeType]])

slots.is_supplement = Slot(uri=BIOLINK.is_supplement, name="is supplement", curie=BIOLINK.curie('is_supplement'),
                   model_uri=BIOLINK.is_supplement, domain=ChemicalMixture, range=Optional[str])

slots.trade_name = Slot(uri=BIOLINK.trade_name, name="trade name", curie=BIOLINK.curie('trade_name'),
                   model_uri=BIOLINK.trade_name, domain=ChemicalEntity, range=Optional[str])

slots.available_from = Slot(uri=BIOLINK.available_from, name="available from", curie=BIOLINK.curie('available_from'),
                   model_uri=BIOLINK.available_from, domain=NamedThing, range=Optional[Union[Union[str, "DrugAvailabilityEnum"], list[Union[str, "DrugAvailabilityEnum"]]]])

slots.is_toxic = Slot(uri=BIOLINK.is_toxic, name="is toxic", curie=BIOLINK.curie('is_toxic'),
                   model_uri=BIOLINK.is_toxic, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.has_chemical_role = Slot(uri=BIOLINK.has_chemical_role, name="has chemical role", curie=BIOLINK.curie('has_chemical_role'),
                   model_uri=BIOLINK.has_chemical_role, domain=NamedThing, range=Optional[Union[Union[str, ChemicalRoleId], list[Union[str, ChemicalRoleId]]]])

slots.max_tolerated_dose = Slot(uri=BIOLINK.max_tolerated_dose, name="max tolerated dose", curie=BIOLINK.curie('max_tolerated_dose'),
                   model_uri=BIOLINK.max_tolerated_dose, domain=NamedThing, range=Optional[str])

slots.animal_model_available_from = Slot(uri=BIOLINK.animal_model_available_from, name="animal model available from", curie=BIOLINK.curie('animal_model_available_from'),
                   model_uri=BIOLINK.animal_model_available_from, domain=NamedThing, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.affinity = Slot(uri=BIOLINK.affinity, name="affinity", curie=BIOLINK.curie('affinity'),
                   model_uri=BIOLINK.affinity, domain=Association, range=Optional[float])

slots.affinity_parameter = Slot(uri=BIOLINK.affinity_parameter, name="affinity parameter", curie=BIOLINK.curie('affinity_parameter'),
                   model_uri=BIOLINK.affinity_parameter, domain=Association, range=Optional[Union[str, "AffinityParameterEnum"]])

slots.FDA_adverse_event_level = Slot(uri=BIOLINK.FDA_adverse_event_level, name="FDA adverse event level", curie=BIOLINK.curie('FDA_adverse_event_level'),
                   model_uri=BIOLINK.FDA_adverse_event_level, domain=Association, range=Optional[Union[str, "FDAIDAAdverseEventEnum"]])

slots.highest_FDA_approval_status = Slot(uri=BIOLINK.highest_FDA_approval_status, name="highest FDA approval status", curie=BIOLINK.curie('highest_FDA_approval_status'),
                   model_uri=BIOLINK.highest_FDA_approval_status, domain=None, range=Optional[Union[str, "ApprovalStatusEnum"]])

slots.drug_regulatory_status_world_wide = Slot(uri=BIOLINK.drug_regulatory_status_world_wide, name="drug regulatory status world wide", curie=BIOLINK.curie('drug_regulatory_status_world_wide'),
                   model_uri=BIOLINK.drug_regulatory_status_world_wide, domain=None, range=Optional[Union[str, "ApprovalStatusEnum"]])

slots.routes_of_delivery = Slot(uri=BIOLINK.routes_of_delivery, name="routes of delivery", curie=BIOLINK.curie('routes_of_delivery'),
                   model_uri=BIOLINK.routes_of_delivery, domain=None, range=Optional[Union[Union[str, "DrugDeliveryEnum"], list[Union[str, "DrugDeliveryEnum"]]]])

slots.form_or_variant_qualifier = Slot(uri=BIOLINK.form_or_variant_qualifier, name="form or variant qualifier", curie=BIOLINK.curie('form_or_variant_qualifier'),
                   model_uri=BIOLINK.form_or_variant_qualifier, domain=Association, range=Optional[str])

slots.specialization_qualifier = Slot(uri=BIOLINK.specialization_qualifier, name="specialization qualifier", curie=BIOLINK.curie('specialization_qualifier'),
                   model_uri=BIOLINK.specialization_qualifier, domain=Association, range=Optional[str])

slots.aspect_qualifier = Slot(uri=BIOLINK.aspect_qualifier, name="aspect qualifier", curie=BIOLINK.curie('aspect_qualifier'),
                   model_uri=BIOLINK.aspect_qualifier, domain=Association, range=Optional[str])

slots.derivative_qualifier = Slot(uri=BIOLINK.derivative_qualifier, name="derivative qualifier", curie=BIOLINK.curie('derivative_qualifier'),
                   model_uri=BIOLINK.derivative_qualifier, domain=Association, range=Optional[str])

slots.part_qualifier = Slot(uri=BIOLINK.part_qualifier, name="part qualifier", curie=BIOLINK.curie('part_qualifier'),
                   model_uri=BIOLINK.part_qualifier, domain=Association, range=Optional[str])

slots.context_qualifier = Slot(uri=BIOLINK.context_qualifier, name="context qualifier", curie=BIOLINK.curie('context_qualifier'),
                   model_uri=BIOLINK.context_qualifier, domain=Association, range=Optional[str])

slots.direction_qualifier = Slot(uri=BIOLINK.direction_qualifier, name="direction qualifier", curie=BIOLINK.curie('direction_qualifier'),
                   model_uri=BIOLINK.direction_qualifier, domain=Association, range=Optional[str])

slots.mapped_predicate = Slot(uri=BIOLINK.mapped_predicate, name="mapped predicate", curie=BIOLINK.curie('mapped_predicate'),
                   model_uri=BIOLINK.mapped_predicate, domain=None, range=Optional[str])

slots.predicate_mappings = Slot(uri=BIOLINK.predicate_mappings, name="predicate mappings", curie=BIOLINK.curie('predicate_mappings'),
                   model_uri=BIOLINK.predicate_mappings, domain=None, range=Optional[Union[Union[dict, PredicateMapping], list[Union[dict, PredicateMapping]]]])

slots.exact_matches = Slot(uri=BIOLINK.exact_matches, name="exact matches", curie=BIOLINK.curie('exact_matches'),
                   model_uri=BIOLINK.exact_matches, domain=None, range=Optional[Union[str, list[str]]])

slots.narrow_matches = Slot(uri=BIOLINK.narrow_matches, name="narrow matches", curie=BIOLINK.curie('narrow_matches'),
                   model_uri=BIOLINK.narrow_matches, domain=None, range=Optional[Union[str, list[str]]])

slots.broad_matches = Slot(uri=BIOLINK.broad_matches, name="broad matches", curie=BIOLINK.curie('broad_matches'),
                   model_uri=BIOLINK.broad_matches, domain=None, range=Optional[Union[str, list[str]]])

slots.subject_aspect_qualifier = Slot(uri=BIOLINK.subject_aspect_qualifier, name="subject aspect qualifier", curie=BIOLINK.curie('subject_aspect_qualifier'),
                   model_uri=BIOLINK.subject_aspect_qualifier, domain=Association, range=Optional[str])

slots.subject_specialization_qualifier = Slot(uri=BIOLINK.subject_specialization_qualifier, name="subject specialization qualifier", curie=BIOLINK.curie('subject_specialization_qualifier'),
                   model_uri=BIOLINK.subject_specialization_qualifier, domain=Association, range=Optional[Union[str, URIorCURIE]])

slots.subject_form_or_variant_qualifier = Slot(uri=BIOLINK.subject_form_or_variant_qualifier, name="subject form or variant qualifier", curie=BIOLINK.curie('subject_form_or_variant_qualifier'),
                   model_uri=BIOLINK.subject_form_or_variant_qualifier, domain=Association, range=Optional[str])

slots.subject_part_qualifier = Slot(uri=BIOLINK.subject_part_qualifier, name="subject part qualifier", curie=BIOLINK.curie('subject_part_qualifier'),
                   model_uri=BIOLINK.subject_part_qualifier, domain=Association, range=Optional[str])

slots.subject_derivative_qualifier = Slot(uri=BIOLINK.subject_derivative_qualifier, name="subject derivative qualifier", curie=BIOLINK.curie('subject_derivative_qualifier'),
                   model_uri=BIOLINK.subject_derivative_qualifier, domain=Association, range=Optional[str])

slots.subject_context_qualifier = Slot(uri=BIOLINK.subject_context_qualifier, name="subject context qualifier", curie=BIOLINK.curie('subject_context_qualifier'),
                   model_uri=BIOLINK.subject_context_qualifier, domain=Association, range=Optional[str])

slots.subject_direction_qualifier = Slot(uri=BIOLINK.subject_direction_qualifier, name="subject direction qualifier", curie=BIOLINK.curie('subject_direction_qualifier'),
                   model_uri=BIOLINK.subject_direction_qualifier, domain=Association, range=Optional[Union[str, "DirectionQualifierEnum"]])

slots.object_aspect_qualifier = Slot(uri=BIOLINK.object_aspect_qualifier, name="object aspect qualifier", curie=BIOLINK.curie('object_aspect_qualifier'),
                   model_uri=BIOLINK.object_aspect_qualifier, domain=Association, range=Optional[str])

slots.object_specialization_qualifier = Slot(uri=BIOLINK.object_specialization_qualifier, name="object specialization qualifier", curie=BIOLINK.curie('object_specialization_qualifier'),
                   model_uri=BIOLINK.object_specialization_qualifier, domain=Association, range=Optional[Union[str, URIorCURIE]])

slots.object_form_or_variant_qualifier = Slot(uri=BIOLINK.object_form_or_variant_qualifier, name="object form or variant qualifier", curie=BIOLINK.curie('object_form_or_variant_qualifier'),
                   model_uri=BIOLINK.object_form_or_variant_qualifier, domain=Association, range=Optional[str])

slots.object_part_qualifier = Slot(uri=BIOLINK.object_part_qualifier, name="object part qualifier", curie=BIOLINK.curie('object_part_qualifier'),
                   model_uri=BIOLINK.object_part_qualifier, domain=Association, range=Optional[str])

slots.object_derivative_qualifier = Slot(uri=BIOLINK.object_derivative_qualifier, name="object derivative qualifier", curie=BIOLINK.curie('object_derivative_qualifier'),
                   model_uri=BIOLINK.object_derivative_qualifier, domain=Association, range=Optional[str])

slots.object_context_qualifier = Slot(uri=BIOLINK.object_context_qualifier, name="object context qualifier", curie=BIOLINK.curie('object_context_qualifier'),
                   model_uri=BIOLINK.object_context_qualifier, domain=Association, range=Optional[str])

slots.object_direction_qualifier = Slot(uri=BIOLINK.object_direction_qualifier, name="object direction qualifier", curie=BIOLINK.curie('object_direction_qualifier'),
                   model_uri=BIOLINK.object_direction_qualifier, domain=Association, range=Optional[Union[str, "DirectionQualifierEnum"]])

slots.qualified_predicate = Slot(uri=BIOLINK.qualified_predicate, name="qualified predicate", curie=BIOLINK.curie('qualified_predicate'),
                   model_uri=BIOLINK.qualified_predicate, domain=Association, range=Optional[str])

slots.statement_qualifier = Slot(uri=BIOLINK.statement_qualifier, name="statement qualifier", curie=BIOLINK.curie('statement_qualifier'),
                   model_uri=BIOLINK.statement_qualifier, domain=Association, range=Optional[str])

slots.causal_mechanism_qualifier = Slot(uri=BIOLINK.causal_mechanism_qualifier, name="causal mechanism qualifier", curie=BIOLINK.curie('causal_mechanism_qualifier'),
                   model_uri=BIOLINK.causal_mechanism_qualifier, domain=Association, range=Optional[Union[str, "CausalMechanismQualifierEnum"]])

slots.anatomical_context_qualifier = Slot(uri=BIOLINK.anatomical_context_qualifier, name="anatomical context qualifier", curie=BIOLINK.curie('anatomical_context_qualifier'),
                   model_uri=BIOLINK.anatomical_context_qualifier, domain=Association, range=Optional[str])

slots.species_context_qualifier = Slot(uri=BIOLINK.species_context_qualifier, name="species context qualifier", curie=BIOLINK.curie('species_context_qualifier'),
                   model_uri=BIOLINK.species_context_qualifier, domain=Association, range=Optional[Union[str, OrganismTaxonId]])

slots.disease_context_qualifier = Slot(uri=BIOLINK.disease_context_qualifier, name="disease context qualifier", curie=BIOLINK.curie('disease_context_qualifier'),
                   model_uri=BIOLINK.disease_context_qualifier, domain=Association, range=Optional[Union[str, DiseaseId]])

slots.qualifiers = Slot(uri=BIOLINK.qualifiers, name="qualifiers", curie=BIOLINK.curie('qualifiers'),
                   model_uri=BIOLINK.qualifiers, domain=Association, range=Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]])

slots.frequency_qualifier = Slot(uri=BIOLINK.frequency_qualifier, name="frequency qualifier", curie=BIOLINK.curie('frequency_qualifier'),
                   model_uri=BIOLINK.frequency_qualifier, domain=Association, range=Optional[Union[str, FrequencyValue]])

slots.severity_qualifier = Slot(uri=BIOLINK.severity_qualifier, name="severity qualifier", curie=BIOLINK.curie('severity_qualifier'),
                   model_uri=BIOLINK.severity_qualifier, domain=Association, range=Optional[Union[str, SeverityValueId]])

slots.sex_qualifier = Slot(uri=BIOLINK.sex_qualifier, name="sex qualifier", curie=BIOLINK.curie('sex_qualifier'),
                   model_uri=BIOLINK.sex_qualifier, domain=Association, range=Optional[Union[str, BiologicalSexId]])

slots.onset_qualifier = Slot(uri=BIOLINK.onset_qualifier, name="onset qualifier", curie=BIOLINK.curie('onset_qualifier'),
                   model_uri=BIOLINK.onset_qualifier, domain=Association, range=Optional[Union[str, OnsetId]])

slots.clinical_modifier_qualifier = Slot(uri=BIOLINK.clinical_modifier_qualifier, name="clinical modifier qualifier", curie=BIOLINK.curie('clinical_modifier_qualifier'),
                   model_uri=BIOLINK.clinical_modifier_qualifier, domain=Association, range=Optional[Union[str, ClinicalModifierId]])

slots.sequence_variant_qualifier = Slot(uri=BIOLINK.sequence_variant_qualifier, name="sequence variant qualifier", curie=BIOLINK.curie('sequence_variant_qualifier'),
                   model_uri=BIOLINK.sequence_variant_qualifier, domain=Association, range=Optional[Union[str, SequenceVariantId]])

slots.quantifier_qualifier = Slot(uri=BIOLINK.quantifier_qualifier, name="quantifier qualifier", curie=BIOLINK.curie('quantifier_qualifier'),
                   model_uri=BIOLINK.quantifier_qualifier, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.catalyst_qualifier = Slot(uri=BIOLINK.catalyst_qualifier, name="catalyst qualifier", curie=BIOLINK.curie('catalyst_qualifier'),
                   model_uri=BIOLINK.catalyst_qualifier, domain=Association, range=Optional[Union[Union[dict, MacromolecularMachineMixin], list[Union[dict, MacromolecularMachineMixin]]]])

slots.stage_qualifier = Slot(uri=BIOLINK.stage_qualifier, name="stage qualifier", curie=BIOLINK.curie('stage_qualifier'),
                   model_uri=BIOLINK.stage_qualifier, domain=Association, range=Optional[Union[str, LifeStageId]])

slots.related_to = Slot(uri=BIOLINK.related_to, name="related to", curie=BIOLINK.curie('related_to'),
                   model_uri=BIOLINK.related_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.related_to_at_concept_level = Slot(uri=BIOLINK.related_to_at_concept_level, name="related to at concept level", curie=BIOLINK.curie('related_to_at_concept_level'),
                   model_uri=BIOLINK.related_to_at_concept_level, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.related_to_at_instance_level = Slot(uri=BIOLINK.related_to_at_instance_level, name="related to at instance level", curie=BIOLINK.curie('related_to_at_instance_level'),
                   model_uri=BIOLINK.related_to_at_instance_level, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.associated_with = Slot(uri=BIOLINK.associated_with, name="associated with", curie=BIOLINK.curie('associated_with'),
                   model_uri=BIOLINK.associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.superclass_of = Slot(uri=BIOLINK.superclass_of, name="superclass of", curie=BIOLINK.curie('superclass_of'),
                   model_uri=BIOLINK.superclass_of, domain=None, range=Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]])

slots.subclass_of = Slot(uri=BIOLINK.subclass_of, name="subclass of", curie=BIOLINK.curie('subclass_of'),
                   model_uri=BIOLINK.subclass_of, domain=None, range=Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]])

slots.same_as = Slot(uri=BIOLINK.same_as, name="same as", curie=BIOLINK.curie('same_as'),
                   model_uri=BIOLINK.same_as, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.close_match = Slot(uri=BIOLINK.close_match, name="close match", curie=BIOLINK.curie('close_match'),
                   model_uri=BIOLINK.close_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.exact_match = Slot(uri=BIOLINK.exact_match, name="exact match", curie=BIOLINK.curie('exact_match'),
                   model_uri=BIOLINK.exact_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.broad_match = Slot(uri=BIOLINK.broad_match, name="broad match", curie=BIOLINK.curie('broad_match'),
                   model_uri=BIOLINK.broad_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.narrow_match = Slot(uri=BIOLINK.narrow_match, name="narrow match", curie=BIOLINK.curie('narrow_match'),
                   model_uri=BIOLINK.narrow_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.member_of = Slot(uri=BIOLINK.member_of, name="member of", curie=BIOLINK.curie('member_of'),
                   model_uri=BIOLINK.member_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.has_member = Slot(uri=BIOLINK.has_member, name="has member", curie=BIOLINK.curie('has_member'),
                   model_uri=BIOLINK.has_member, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.opposite_of = Slot(uri=BIOLINK.opposite_of, name="opposite of", curie=BIOLINK.curie('opposite_of'),
                   model_uri=BIOLINK.opposite_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.affects_likelihood_of = Slot(uri=BIOLINK.affects_likelihood_of, name="affects likelihood of", curie=BIOLINK.curie('affects_likelihood_of'),
                   model_uri=BIOLINK.affects_likelihood_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.likelihood_affected_by = Slot(uri=BIOLINK.likelihood_affected_by, name="likelihood affected by", curie=BIOLINK.curie('likelihood_affected_by'),
                   model_uri=BIOLINK.likelihood_affected_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.associated_with_likelihood_of = Slot(uri=BIOLINK.associated_with_likelihood_of, name="associated with likelihood of", curie=BIOLINK.curie('associated_with_likelihood_of'),
                   model_uri=BIOLINK.associated_with_likelihood_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.likelihood_associated_with = Slot(uri=BIOLINK.likelihood_associated_with, name="likelihood associated with", curie=BIOLINK.curie('likelihood_associated_with'),
                   model_uri=BIOLINK.likelihood_associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.associated_with_increased_likelihood_of = Slot(uri=BIOLINK.associated_with_increased_likelihood_of, name="associated with increased likelihood of", curie=BIOLINK.curie('associated_with_increased_likelihood_of'),
                   model_uri=BIOLINK.associated_with_increased_likelihood_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.increased_likelihood_associated_with = Slot(uri=BIOLINK.increased_likelihood_associated_with, name="increased likelihood associated with", curie=BIOLINK.curie('increased_likelihood_associated_with'),
                   model_uri=BIOLINK.increased_likelihood_associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.associated_with_decreased_likelihood_of = Slot(uri=BIOLINK.associated_with_decreased_likelihood_of, name="associated with decreased likelihood of", curie=BIOLINK.curie('associated_with_decreased_likelihood_of'),
                   model_uri=BIOLINK.associated_with_decreased_likelihood_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.decreased_likelihood_associated_with = Slot(uri=BIOLINK.decreased_likelihood_associated_with, name="decreased likelihood associated with", curie=BIOLINK.curie('decreased_likelihood_associated_with'),
                   model_uri=BIOLINK.decreased_likelihood_associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.target_for = Slot(uri=BIOLINK.target_for, name="target for", curie=BIOLINK.curie('target_for'),
                   model_uri=BIOLINK.target_for, domain=Gene, range=Optional[Union[Union[str, DiseaseId], list[Union[str, DiseaseId]]]])

slots.has_target = Slot(uri=BIOLINK.has_target, name="has target", curie=BIOLINK.curie('has_target'),
                   model_uri=BIOLINK.has_target, domain=Disease, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.active_in = Slot(uri=BIOLINK.active_in, name="active in", curie=BIOLINK.curie('active_in'),
                   model_uri=BIOLINK.active_in, domain=None, range=Optional[Union[Union[str, CellularComponentId], list[Union[str, CellularComponentId]]]])

slots.has_active_component = Slot(uri=BIOLINK.has_active_component, name="has active component", curie=BIOLINK.curie('has_active_component'),
                   model_uri=BIOLINK.has_active_component, domain=CellularComponent, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.acts_upstream_of = Slot(uri=BIOLINK.acts_upstream_of, name="acts upstream of", curie=BIOLINK.curie('acts_upstream_of'),
                   model_uri=BIOLINK.acts_upstream_of, domain=None, range=Optional[Union[Union[str, BiologicalProcessId], list[Union[str, BiologicalProcessId]]]])

slots.has_upstream_actor = Slot(uri=BIOLINK.has_upstream_actor, name="has upstream actor", curie=BIOLINK.curie('has_upstream_actor'),
                   model_uri=BIOLINK.has_upstream_actor, domain=BiologicalProcess, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.acts_upstream_of_positive_effect = Slot(uri=BIOLINK.acts_upstream_of_positive_effect, name="acts upstream of positive effect", curie=BIOLINK.curie('acts_upstream_of_positive_effect'),
                   model_uri=BIOLINK.acts_upstream_of_positive_effect, domain=None, range=Optional[Union[Union[str, BiologicalProcessId], list[Union[str, BiologicalProcessId]]]])

slots.has_positive_upstream_actor = Slot(uri=BIOLINK.has_positive_upstream_actor, name="has positive upstream actor", curie=BIOLINK.curie('has_positive_upstream_actor'),
                   model_uri=BIOLINK.has_positive_upstream_actor, domain=BiologicalProcess, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.acts_upstream_of_negative_effect = Slot(uri=BIOLINK.acts_upstream_of_negative_effect, name="acts upstream of negative effect", curie=BIOLINK.curie('acts_upstream_of_negative_effect'),
                   model_uri=BIOLINK.acts_upstream_of_negative_effect, domain=None, range=Optional[Union[Union[str, BiologicalProcessId], list[Union[str, BiologicalProcessId]]]])

slots.has_negative_upstream_actor = Slot(uri=BIOLINK.has_negative_upstream_actor, name="has negative upstream actor", curie=BIOLINK.curie('has_negative_upstream_actor'),
                   model_uri=BIOLINK.has_negative_upstream_actor, domain=BiologicalProcess, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.acts_upstream_of_or_within = Slot(uri=BIOLINK.acts_upstream_of_or_within, name="acts upstream of or within", curie=BIOLINK.curie('acts_upstream_of_or_within'),
                   model_uri=BIOLINK.acts_upstream_of_or_within, domain=None, range=Optional[Union[Union[str, BiologicalProcessId], list[Union[str, BiologicalProcessId]]]])

slots.has_upstream_or_within_actor = Slot(uri=BIOLINK.has_upstream_or_within_actor, name="has upstream or within actor", curie=BIOLINK.curie('has_upstream_or_within_actor'),
                   model_uri=BIOLINK.has_upstream_or_within_actor, domain=BiologicalProcess, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.acts_upstream_of_or_within_positive_effect = Slot(uri=BIOLINK.acts_upstream_of_or_within_positive_effect, name="acts upstream of or within positive effect", curie=BIOLINK.curie('acts_upstream_of_or_within_positive_effect'),
                   model_uri=BIOLINK.acts_upstream_of_or_within_positive_effect, domain=None, range=Optional[Union[Union[str, BiologicalProcessId], list[Union[str, BiologicalProcessId]]]])

slots.has_positive_upstream_or_within_actor = Slot(uri=BIOLINK.has_positive_upstream_or_within_actor, name="has positive upstream or within actor", curie=BIOLINK.curie('has_positive_upstream_or_within_actor'),
                   model_uri=BIOLINK.has_positive_upstream_or_within_actor, domain=BiologicalProcess, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.acts_upstream_of_or_within_negative_effect = Slot(uri=BIOLINK.acts_upstream_of_or_within_negative_effect, name="acts upstream of or within negative effect", curie=BIOLINK.curie('acts_upstream_of_or_within_negative_effect'),
                   model_uri=BIOLINK.acts_upstream_of_or_within_negative_effect, domain=None, range=Optional[Union[Union[str, BiologicalProcessId], list[Union[str, BiologicalProcessId]]]])

slots.has_negative_upstream_or_within_actor = Slot(uri=BIOLINK.has_negative_upstream_or_within_actor, name="has negative upstream or within actor", curie=BIOLINK.curie('has_negative_upstream_or_within_actor'),
                   model_uri=BIOLINK.has_negative_upstream_or_within_actor, domain=BiologicalProcess, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.mentions = Slot(uri=BIOLINK.mentions, name="mentions", curie=BIOLINK.curie('mentions'),
                   model_uri=BIOLINK.mentions, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.mentioned_by = Slot(uri=BIOLINK.mentioned_by, name="mentioned by", curie=BIOLINK.curie('mentioned_by'),
                   model_uri=BIOLINK.mentioned_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.contributor = Slot(uri=BIOLINK.contributor, name="contributor", curie=BIOLINK.curie('contributor'),
                   model_uri=BIOLINK.contributor, domain=Agent, range=Optional[Union[Union[str, InformationContentEntityId], list[Union[str, InformationContentEntityId]]]])

slots.has_contributor = Slot(uri=BIOLINK.has_contributor, name="has contributor", curie=BIOLINK.curie('has_contributor'),
                   model_uri=BIOLINK.has_contributor, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], list[Union[str, AgentId]]]])

slots.provider = Slot(uri=BIOLINK.provider, name="provider", curie=BIOLINK.curie('provider'),
                   model_uri=BIOLINK.provider, domain=Agent, range=Optional[Union[Union[str, InformationContentEntityId], list[Union[str, InformationContentEntityId]]]])

slots.has_provider = Slot(uri=BIOLINK.has_provider, name="has provider", curie=BIOLINK.curie('has_provider'),
                   model_uri=BIOLINK.has_provider, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], list[Union[str, AgentId]]]])

slots.publisher = Slot(uri=BIOLINK.publisher, name="publisher", curie=BIOLINK.curie('publisher'),
                   model_uri=BIOLINK.publisher, domain=Agent, range=Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]])

slots.has_publisher = Slot(uri=BIOLINK.has_publisher, name="has publisher", curie=BIOLINK.curie('has_publisher'),
                   model_uri=BIOLINK.has_publisher, domain=Publication, range=Optional[Union[Union[str, AgentId], list[Union[str, AgentId]]]])

slots.editor = Slot(uri=BIOLINK.editor, name="editor", curie=BIOLINK.curie('editor'),
                   model_uri=BIOLINK.editor, domain=Agent, range=Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]])

slots.has_editor = Slot(uri=BIOLINK.has_editor, name="has editor", curie=BIOLINK.curie('has_editor'),
                   model_uri=BIOLINK.has_editor, domain=Publication, range=Optional[Union[Union[str, AgentId], list[Union[str, AgentId]]]])

slots.author = Slot(uri=BIOLINK.author, name="author", curie=BIOLINK.curie('author'),
                   model_uri=BIOLINK.author, domain=Agent, range=Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]])

slots.has_author = Slot(uri=BIOLINK.has_author, name="has author", curie=BIOLINK.curie('has_author'),
                   model_uri=BIOLINK.has_author, domain=Publication, range=Optional[Union[Union[str, AgentId], list[Union[str, AgentId]]]])

slots.assesses = Slot(uri=BIOLINK.assesses, name="assesses", curie=BIOLINK.curie('assesses'),
                   model_uri=BIOLINK.assesses, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.is_assessed_by = Slot(uri=BIOLINK.is_assessed_by, name="is assessed by", curie=BIOLINK.curie('is_assessed_by'),
                   model_uri=BIOLINK.is_assessed_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.interacts_with = Slot(uri=BIOLINK.interacts_with, name="interacts with", curie=BIOLINK.curie('interacts_with'),
                   model_uri=BIOLINK.interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.physically_interacts_with = Slot(uri=BIOLINK.physically_interacts_with, name="physically interacts with", curie=BIOLINK.curie('physically_interacts_with'),
                   model_uri=BIOLINK.physically_interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.directly_physically_interacts_with = Slot(uri=BIOLINK.directly_physically_interacts_with, name="directly physically interacts with", curie=BIOLINK.curie('directly_physically_interacts_with'),
                   model_uri=BIOLINK.directly_physically_interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.binds = Slot(uri=BIOLINK.binds, name="binds", curie=BIOLINK.curie('binds'),
                   model_uri=BIOLINK.binds, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.indirectly_physically_interacts_with = Slot(uri=BIOLINK.indirectly_physically_interacts_with, name="indirectly physically interacts with", curie=BIOLINK.curie('indirectly_physically_interacts_with'),
                   model_uri=BIOLINK.indirectly_physically_interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.genetically_interacts_with = Slot(uri=BIOLINK.genetically_interacts_with, name="genetically interacts with", curie=BIOLINK.curie('genetically_interacts_with'),
                   model_uri=BIOLINK.genetically_interacts_with, domain=Gene, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.gene_fusion_with = Slot(uri=BIOLINK.gene_fusion_with, name="gene_fusion_with", curie=BIOLINK.curie('gene_fusion_with'),
                   model_uri=BIOLINK.gene_fusion_with, domain=Gene, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.genetic_neighborhood_of = Slot(uri=BIOLINK.genetic_neighborhood_of, name="genetic_neighborhood_of", curie=BIOLINK.curie('genetic_neighborhood_of'),
                   model_uri=BIOLINK.genetic_neighborhood_of, domain=Gene, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.affects = Slot(uri=BIOLINK.affects, name="affects", curie=BIOLINK.curie('affects'),
                   model_uri=BIOLINK.affects, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.affected_by = Slot(uri=BIOLINK.affected_by, name="affected by", curie=BIOLINK.curie('affected_by'),
                   model_uri=BIOLINK.affected_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.associated_with_response_to = Slot(uri=BIOLINK.associated_with_response_to, name="associated with response to", curie=BIOLINK.curie('associated_with_response_to'),
                   model_uri=BIOLINK.associated_with_response_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.response_associated_with = Slot(uri=BIOLINK.response_associated_with, name="response associated with", curie=BIOLINK.curie('response_associated_with'),
                   model_uri=BIOLINK.response_associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.associated_with_sensitivity_to = Slot(uri=BIOLINK.associated_with_sensitivity_to, name="associated with sensitivity to", curie=BIOLINK.curie('associated_with_sensitivity_to'),
                   model_uri=BIOLINK.associated_with_sensitivity_to, domain=NamedThing, range=Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]])

slots.sensitivity_associated_with = Slot(uri=BIOLINK.sensitivity_associated_with, name="sensitivity associated with", curie=BIOLINK.curie('sensitivity_associated_with'),
                   model_uri=BIOLINK.sensitivity_associated_with, domain=ChemicalEntity, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.associated_with_resistance_to = Slot(uri=BIOLINK.associated_with_resistance_to, name="associated with resistance to", curie=BIOLINK.curie('associated_with_resistance_to'),
                   model_uri=BIOLINK.associated_with_resistance_to, domain=NamedThing, range=Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]])

slots.resistance_associated_with = Slot(uri=BIOLINK.resistance_associated_with, name="resistance associated with", curie=BIOLINK.curie('resistance_associated_with'),
                   model_uri=BIOLINK.resistance_associated_with, domain=ChemicalEntity, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.diagnoses = Slot(uri=BIOLINK.diagnoses, name="diagnoses", curie=BIOLINK.curie('diagnoses'),
                   model_uri=BIOLINK.diagnoses, domain=DiagnosticAid, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.is_diagnosed_by = Slot(uri=BIOLINK.is_diagnosed_by, name="is diagnosed by", curie=BIOLINK.curie('is_diagnosed_by'),
                   model_uri=BIOLINK.is_diagnosed_by, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[str, DiagnosticAidId], list[Union[str, DiagnosticAidId]]]])

slots.increases_amount_or_activity_of = Slot(uri=BIOLINK.increases_amount_or_activity_of, name="increases amount or activity of", curie=BIOLINK.curie('increases_amount_or_activity_of'),
                   model_uri=BIOLINK.increases_amount_or_activity_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.amount_or_activity_increased_by = Slot(uri=BIOLINK.amount_or_activity_increased_by, name="amount or activity increased by", curie=BIOLINK.curie('amount_or_activity_increased_by'),
                   model_uri=BIOLINK.amount_or_activity_increased_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.decreases_amount_or_activity_of = Slot(uri=BIOLINK.decreases_amount_or_activity_of, name="decreases amount or activity of", curie=BIOLINK.curie('decreases_amount_or_activity_of'),
                   model_uri=BIOLINK.decreases_amount_or_activity_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.amount_or_activity_decreased_by = Slot(uri=BIOLINK.amount_or_activity_decreased_by, name="amount or activity decreased by", curie=BIOLINK.curie('amount_or_activity_decreased_by'),
                   model_uri=BIOLINK.amount_or_activity_decreased_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.chemical_role_mixin = Slot(uri=BIOLINK.chemical_role_mixin, name="chemical role mixin", curie=BIOLINK.curie('chemical_role_mixin'),
                   model_uri=BIOLINK.chemical_role_mixin, domain=None, range=Optional[str])

slots.biological_role_mixin = Slot(uri=BIOLINK.biological_role_mixin, name="biological role mixin", curie=BIOLINK.curie('biological_role_mixin'),
                   model_uri=BIOLINK.biological_role_mixin, domain=None, range=Optional[str])

slots.affects_response_to = Slot(uri=BIOLINK.affects_response_to, name="affects response to", curie=BIOLINK.curie('affects_response_to'),
                   model_uri=BIOLINK.affects_response_to, domain=None, range=Optional[Union[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"], list[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"]]]])

slots.response_affected_by = Slot(uri=BIOLINK.response_affected_by, name="response affected by", curie=BIOLINK.curie('response_affected_by'),
                   model_uri=BIOLINK.response_affected_by, domain=None, range=Optional[Union[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"], list[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"]]]])

slots.increases_response_to = Slot(uri=BIOLINK.increases_response_to, name="increases response to", curie=BIOLINK.curie('increases_response_to'),
                   model_uri=BIOLINK.increases_response_to, domain=None, range=Optional[Union[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"], list[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"]]]])

slots.response_increased_by = Slot(uri=BIOLINK.response_increased_by, name="response increased by", curie=BIOLINK.curie('response_increased_by'),
                   model_uri=BIOLINK.response_increased_by, domain=None, range=Optional[Union[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"], list[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"]]]])

slots.decreases_response_to = Slot(uri=BIOLINK.decreases_response_to, name="decreases response to", curie=BIOLINK.curie('decreases_response_to'),
                   model_uri=BIOLINK.decreases_response_to, domain=None, range=Optional[Union[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"], list[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"]]]])

slots.response_decreased_by = Slot(uri=BIOLINK.response_decreased_by, name="response decreased by", curie=BIOLINK.curie('response_decreased_by'),
                   model_uri=BIOLINK.response_decreased_by, domain=None, range=Optional[Union[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"], list[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"]]]])

slots.regulates = Slot(uri=BIOLINK.regulates, name="regulates", curie=BIOLINK.curie('regulates'),
                   model_uri=BIOLINK.regulates, domain=None, range=Optional[Union[Union[dict, "PhysicalEssenceOrOccurrent"], list[Union[dict, "PhysicalEssenceOrOccurrent"]]]])

slots.regulated_by = Slot(uri=BIOLINK.regulated_by, name="regulated by", curie=BIOLINK.curie('regulated_by'),
                   model_uri=BIOLINK.regulated_by, domain=None, range=Optional[Union[Union[dict, "PhysicalEssenceOrOccurrent"], list[Union[dict, "PhysicalEssenceOrOccurrent"]]]])

slots.disrupts = Slot(uri=BIOLINK.disrupts, name="disrupts", curie=BIOLINK.curie('disrupts'),
                   model_uri=BIOLINK.disrupts, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.disrupted_by = Slot(uri=BIOLINK.disrupted_by, name="disrupted by", curie=BIOLINK.curie('disrupted_by'),
                   model_uri=BIOLINK.disrupted_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.gene_product_of = Slot(uri=BIOLINK.gene_product_of, name="gene product of", curie=BIOLINK.curie('gene_product_of'),
                   model_uri=BIOLINK.gene_product_of, domain=None, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.has_gene_product = Slot(uri=BIOLINK.has_gene_product, name="has gene product", curie=BIOLINK.curie('has_gene_product'),
                   model_uri=BIOLINK.has_gene_product, domain=Gene, range=Optional[Union[Union[dict, "GeneProductMixin"], list[Union[dict, "GeneProductMixin"]]]])

slots.transcribed_to = Slot(uri=BIOLINK.transcribed_to, name="transcribed to", curie=BIOLINK.curie('transcribed_to'),
                   model_uri=BIOLINK.transcribed_to, domain=Gene, range=Optional[Union[Union[str, TranscriptId], list[Union[str, TranscriptId]]]])

slots.transcribed_from = Slot(uri=BIOLINK.transcribed_from, name="transcribed from", curie=BIOLINK.curie('transcribed_from'),
                   model_uri=BIOLINK.transcribed_from, domain=Transcript, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.translates_to = Slot(uri=BIOLINK.translates_to, name="translates to", curie=BIOLINK.curie('translates_to'),
                   model_uri=BIOLINK.translates_to, domain=Transcript, range=Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]])

slots.translation_of = Slot(uri=BIOLINK.translation_of, name="translation of", curie=BIOLINK.curie('translation_of'),
                   model_uri=BIOLINK.translation_of, domain=Protein, range=Optional[Union[Union[str, TranscriptId], list[Union[str, TranscriptId]]]])

slots.homologous_to = Slot(uri=BIOLINK.homologous_to, name="homologous to", curie=BIOLINK.curie('homologous_to'),
                   model_uri=BIOLINK.homologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.paralogous_to = Slot(uri=BIOLINK.paralogous_to, name="paralogous to", curie=BIOLINK.curie('paralogous_to'),
                   model_uri=BIOLINK.paralogous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.orthologous_to = Slot(uri=BIOLINK.orthologous_to, name="orthologous to", curie=BIOLINK.curie('orthologous_to'),
                   model_uri=BIOLINK.orthologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.xenologous_to = Slot(uri=BIOLINK.xenologous_to, name="xenologous to", curie=BIOLINK.curie('xenologous_to'),
                   model_uri=BIOLINK.xenologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.coexists_with = Slot(uri=BIOLINK.coexists_with, name="coexists with", curie=BIOLINK.curie('coexists_with'),
                   model_uri=BIOLINK.coexists_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.in_pathway_with = Slot(uri=BIOLINK.in_pathway_with, name="in pathway with", curie=BIOLINK.curie('in_pathway_with'),
                   model_uri=BIOLINK.in_pathway_with, domain=None, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.in_complex_with = Slot(uri=BIOLINK.in_complex_with, name="in complex with", curie=BIOLINK.curie('in_complex_with'),
                   model_uri=BIOLINK.in_complex_with, domain=None, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.in_cell_population_with = Slot(uri=BIOLINK.in_cell_population_with, name="in cell population with", curie=BIOLINK.curie('in_cell_population_with'),
                   model_uri=BIOLINK.in_cell_population_with, domain=None, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.colocalizes_with = Slot(uri=BIOLINK.colocalizes_with, name="colocalizes with", curie=BIOLINK.curie('colocalizes_with'),
                   model_uri=BIOLINK.colocalizes_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.genetic_association = Slot(uri=BIOLINK.genetic_association, name="genetic association", curie=BIOLINK.curie('genetic_association'),
                   model_uri=BIOLINK.genetic_association, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.genetically_associated_with = Slot(uri=BIOLINK.genetically_associated_with, name="genetically associated with", curie=BIOLINK.curie('genetically_associated_with'),
                   model_uri=BIOLINK.genetically_associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.gene_associated_with_condition = Slot(uri=BIOLINK.gene_associated_with_condition, name="gene associated with condition", curie=BIOLINK.curie('gene_associated_with_condition'),
                   model_uri=BIOLINK.gene_associated_with_condition, domain=Gene, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.condition_associated_with_gene = Slot(uri=BIOLINK.condition_associated_with_gene, name="condition associated with gene", curie=BIOLINK.curie('condition_associated_with_gene'),
                   model_uri=BIOLINK.condition_associated_with_gene, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.contributes_to = Slot(uri=BIOLINK.contributes_to, name="contributes to", curie=BIOLINK.curie('contributes_to'),
                   model_uri=BIOLINK.contributes_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.contribution_from = Slot(uri=BIOLINK.contribution_from, name="contribution from", curie=BIOLINK.curie('contribution_from'),
                   model_uri=BIOLINK.contribution_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.causes = Slot(uri=BIOLINK.causes, name="causes", curie=BIOLINK.curie('causes'),
                   model_uri=BIOLINK.causes, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.caused_by = Slot(uri=BIOLINK.caused_by, name="caused by", curie=BIOLINK.curie('caused_by'),
                   model_uri=BIOLINK.caused_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.ameliorates_condition = Slot(uri=BIOLINK.ameliorates_condition, name="ameliorates condition", curie=BIOLINK.curie('ameliorates_condition'),
                   model_uri=BIOLINK.ameliorates_condition, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.condition_ameliorated_by = Slot(uri=BIOLINK.condition_ameliorated_by, name="condition ameliorated by", curie=BIOLINK.curie('condition_ameliorated_by'),
                   model_uri=BIOLINK.condition_ameliorated_by, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.preventative_for_condition = Slot(uri=BIOLINK.preventative_for_condition, name="preventative for condition", curie=BIOLINK.curie('preventative_for_condition'),
                   model_uri=BIOLINK.preventative_for_condition, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.condition_prevented_by = Slot(uri=BIOLINK.condition_prevented_by, name="condition prevented by", curie=BIOLINK.curie('condition_prevented_by'),
                   model_uri=BIOLINK.condition_prevented_by, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.promotes_condition = Slot(uri=BIOLINK.promotes_condition, name="promotes condition", curie=BIOLINK.curie('promotes_condition'),
                   model_uri=BIOLINK.promotes_condition, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.condition_promoted_by = Slot(uri=BIOLINK.condition_promoted_by, name="condition promoted by", curie=BIOLINK.curie('condition_promoted_by'),
                   model_uri=BIOLINK.condition_promoted_by, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.predisposes_to_condition = Slot(uri=BIOLINK.predisposes_to_condition, name="predisposes to condition", curie=BIOLINK.curie('predisposes_to_condition'),
                   model_uri=BIOLINK.predisposes_to_condition, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.condition_predisposed_by = Slot(uri=BIOLINK.condition_predisposed_by, name="condition predisposed by", curie=BIOLINK.curie('condition_predisposed_by'),
                   model_uri=BIOLINK.condition_predisposed_by, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.exacerbates_condition = Slot(uri=BIOLINK.exacerbates_condition, name="exacerbates condition", curie=BIOLINK.curie('exacerbates_condition'),
                   model_uri=BIOLINK.exacerbates_condition, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.condition_exacerbated_by = Slot(uri=BIOLINK.condition_exacerbated_by, name="condition exacerbated by", curie=BIOLINK.curie('condition_exacerbated_by'),
                   model_uri=BIOLINK.condition_exacerbated_by, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.treats = Slot(uri=BIOLINK.treats, name="treats", curie=BIOLINK.curie('treats'),
                   model_uri=BIOLINK.treats, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.treated_by = Slot(uri=BIOLINK.treated_by, name="treated by", curie=BIOLINK.curie('treated_by'),
                   model_uri=BIOLINK.treated_by, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.studied_to_treat = Slot(uri=BIOLINK.studied_to_treat, name="studied to treat", curie=BIOLINK.curie('studied_to_treat'),
                   model_uri=BIOLINK.studied_to_treat, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.in_clinical_trials_for = Slot(uri=BIOLINK.in_clinical_trials_for, name="in clinical trials for", curie=BIOLINK.curie('in_clinical_trials_for'),
                   model_uri=BIOLINK.in_clinical_trials_for, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.tested_by_clinical_trials_of = Slot(uri=BIOLINK.tested_by_clinical_trials_of, name="tested by clinical trials of", curie=BIOLINK.curie('tested_by_clinical_trials_of'),
                   model_uri=BIOLINK.tested_by_clinical_trials_of, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.treated_in_studies_by = Slot(uri=BIOLINK.treated_in_studies_by, name="treated in studies by", curie=BIOLINK.curie('treated_in_studies_by'),
                   model_uri=BIOLINK.treated_in_studies_by, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.tested_by_preclinical_trials_of = Slot(uri=BIOLINK.tested_by_preclinical_trials_of, name="tested by preclinical trials of", curie=BIOLINK.curie('tested_by_preclinical_trials_of'),
                   model_uri=BIOLINK.tested_by_preclinical_trials_of, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.in_preclinical_trials_for = Slot(uri=BIOLINK.in_preclinical_trials_for, name="in preclinical trials for", curie=BIOLINK.curie('in_preclinical_trials_for'),
                   model_uri=BIOLINK.in_preclinical_trials_for, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.beneficial_in_models_for = Slot(uri=BIOLINK.beneficial_in_models_for, name="beneficial in models for", curie=BIOLINK.curie('beneficial_in_models_for'),
                   model_uri=BIOLINK.beneficial_in_models_for, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.models_demonstrating_benefits_for = Slot(uri=BIOLINK.models_demonstrating_benefits_for, name="models demonstrating benefits for", curie=BIOLINK.curie('models_demonstrating_benefits_for'),
                   model_uri=BIOLINK.models_demonstrating_benefits_for, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.applied_to_treat = Slot(uri=BIOLINK.applied_to_treat, name="applied to treat", curie=BIOLINK.curie('applied_to_treat'),
                   model_uri=BIOLINK.applied_to_treat, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.treatment_applications_from = Slot(uri=BIOLINK.treatment_applications_from, name="treatment applications from", curie=BIOLINK.curie('treatment_applications_from'),
                   model_uri=BIOLINK.treatment_applications_from, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.treats_or_applied_or_studied_to_treat = Slot(uri=BIOLINK.treats_or_applied_or_studied_to_treat, name="treats or applied or studied to treat", curie=BIOLINK.curie('treats_or_applied_or_studied_to_treat'),
                   model_uri=BIOLINK.treats_or_applied_or_studied_to_treat, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.subject_of_treatment_application_or_study_for_treatment_by = Slot(uri=BIOLINK.subject_of_treatment_application_or_study_for_treatment_by, name="subject of treatment application or study for treatment by", curie=BIOLINK.curie('subject_of_treatment_application_or_study_for_treatment_by'),
                   model_uri=BIOLINK.subject_of_treatment_application_or_study_for_treatment_by, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.correlated_with = Slot(uri=BIOLINK.correlated_with, name="correlated with", curie=BIOLINK.curie('correlated_with'),
                   model_uri=BIOLINK.correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.positively_correlated_with = Slot(uri=BIOLINK.positively_correlated_with, name="positively correlated with", curie=BIOLINK.curie('positively_correlated_with'),
                   model_uri=BIOLINK.positively_correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.negatively_correlated_with = Slot(uri=BIOLINK.negatively_correlated_with, name="negatively correlated with", curie=BIOLINK.curie('negatively_correlated_with'),
                   model_uri=BIOLINK.negatively_correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.occurs_together_in_literature_with = Slot(uri=BIOLINK.occurs_together_in_literature_with, name="occurs together in literature with", curie=BIOLINK.curie('occurs_together_in_literature_with'),
                   model_uri=BIOLINK.occurs_together_in_literature_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.coexpressed_with = Slot(uri=BIOLINK.coexpressed_with, name="coexpressed with", curie=BIOLINK.curie('coexpressed_with'),
                   model_uri=BIOLINK.coexpressed_with, domain=None, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.has_biomarker = Slot(uri=BIOLINK.has_biomarker, name="has biomarker", curie=BIOLINK.curie('has_biomarker'),
                   model_uri=BIOLINK.has_biomarker, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"], list[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"]]]])

slots.biomarker_for = Slot(uri=BIOLINK.biomarker_for, name="biomarker for", curie=BIOLINK.curie('biomarker_for'),
                   model_uri=BIOLINK.biomarker_for, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.expressed_in = Slot(uri=BIOLINK.expressed_in, name="expressed in", curie=BIOLINK.curie('expressed_in'),
                   model_uri=BIOLINK.expressed_in, domain=None, range=Optional[Union[Union[str, AnatomicalEntityId], list[Union[str, AnatomicalEntityId]]]])

slots.expresses = Slot(uri=BIOLINK.expresses, name="expresses", curie=BIOLINK.curie('expresses'),
                   model_uri=BIOLINK.expresses, domain=AnatomicalEntity, range=Optional[Union[Union[dict, "GeneOrGeneProduct"], list[Union[dict, "GeneOrGeneProduct"]]]])

slots.has_phenotype = Slot(uri=BIOLINK.has_phenotype, name="has phenotype", curie=BIOLINK.curie('has_phenotype'),
                   model_uri=BIOLINK.has_phenotype, domain=BiologicalEntity, range=Optional[Union[Union[str, PhenotypicFeatureId], list[Union[str, PhenotypicFeatureId]]]])

slots.phenotype_of = Slot(uri=BIOLINK.phenotype_of, name="phenotype of", curie=BIOLINK.curie('phenotype_of'),
                   model_uri=BIOLINK.phenotype_of, domain=PhenotypicFeature, range=Optional[Union[Union[str, BiologicalEntityId], list[Union[str, BiologicalEntityId]]]])

slots.occurs_in = Slot(uri=BIOLINK.occurs_in, name="occurs in", curie=BIOLINK.curie('occurs_in'),
                   model_uri=BIOLINK.occurs_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.contains_process = Slot(uri=BIOLINK.contains_process, name="contains process", curie=BIOLINK.curie('contains_process'),
                   model_uri=BIOLINK.contains_process, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.located_in = Slot(uri=BIOLINK.located_in, name="located in", curie=BIOLINK.curie('located_in'),
                   model_uri=BIOLINK.located_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.location_of = Slot(uri=BIOLINK.location_of, name="location of", curie=BIOLINK.curie('location_of'),
                   model_uri=BIOLINK.location_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.disease_has_location = Slot(uri=BIOLINK.disease_has_location, name="disease has location", curie=BIOLINK.curie('disease_has_location'),
                   model_uri=BIOLINK.disease_has_location, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.location_of_disease = Slot(uri=BIOLINK.location_of_disease, name="location of disease", curie=BIOLINK.curie('location_of_disease'),
                   model_uri=BIOLINK.location_of_disease, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.similar_to = Slot(uri=BIOLINK.similar_to, name="similar to", curie=BIOLINK.curie('similar_to'),
                   model_uri=BIOLINK.similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.chemically_similar_to = Slot(uri=BIOLINK.chemically_similar_to, name="chemically similar to", curie=BIOLINK.curie('chemically_similar_to'),
                   model_uri=BIOLINK.chemically_similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.has_sequence_location = Slot(uri=BIOLINK.has_sequence_location, name="has sequence location", curie=BIOLINK.curie('has_sequence_location'),
                   model_uri=BIOLINK.has_sequence_location, domain=NucleicAcidEntity, range=Optional[Union[Union[str, NucleicAcidEntityId], list[Union[str, NucleicAcidEntityId]]]])

slots.sequence_location_of = Slot(uri=BIOLINK.sequence_location_of, name="sequence location of", curie=BIOLINK.curie('sequence_location_of'),
                   model_uri=BIOLINK.sequence_location_of, domain=NucleicAcidEntity, range=Optional[Union[Union[str, NucleicAcidEntityId], list[Union[str, NucleicAcidEntityId]]]])

slots.model_of = Slot(uri=BIOLINK.model_of, name="model of", curie=BIOLINK.curie('model_of'),
                   model_uri=BIOLINK.model_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.models = Slot(uri=BIOLINK.models, name="models", curie=BIOLINK.curie('models'),
                   model_uri=BIOLINK.models, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.overlaps = Slot(uri=BIOLINK.overlaps, name="overlaps", curie=BIOLINK.curie('overlaps'),
                   model_uri=BIOLINK.overlaps, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.has_part = Slot(uri=BIOLINK.has_part, name="has part", curie=BIOLINK.curie('has_part'),
                   model_uri=BIOLINK.has_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.has_plasma_membrane_part = Slot(uri=BIOLINK.has_plasma_membrane_part, name="has plasma membrane part", curie=BIOLINK.curie('has_plasma_membrane_part'),
                   model_uri=BIOLINK.has_plasma_membrane_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.composed_primarily_of = Slot(uri=BIOLINK.composed_primarily_of, name="composed primarily of", curie=BIOLINK.curie('composed_primarily_of'),
                   model_uri=BIOLINK.composed_primarily_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.primarily_composed_of = Slot(uri=BIOLINK.primarily_composed_of, name="primarily composed of", curie=BIOLINK.curie('primarily_composed_of'),
                   model_uri=BIOLINK.primarily_composed_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.plasma_membrane_part_of = Slot(uri=BIOLINK.plasma_membrane_part_of, name="plasma membrane part of", curie=BIOLINK.curie('plasma_membrane_part_of'),
                   model_uri=BIOLINK.plasma_membrane_part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.part_of = Slot(uri=BIOLINK.part_of, name="part of", curie=BIOLINK.curie('part_of'),
                   model_uri=BIOLINK.part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.has_input = Slot(uri=BIOLINK.has_input, name="has input", curie=BIOLINK.curie('has_input'),
                   model_uri=BIOLINK.has_input, domain=BiologicalProcessOrActivity, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.is_input_of = Slot(uri=BIOLINK.is_input_of, name="is input of", curie=BIOLINK.curie('is_input_of'),
                   model_uri=BIOLINK.is_input_of, domain=NamedThing, range=Optional[Union[Union[str, BiologicalProcessOrActivityId], list[Union[str, BiologicalProcessOrActivityId]]]])

slots.has_output = Slot(uri=BIOLINK.has_output, name="has output", curie=BIOLINK.curie('has_output'),
                   model_uri=BIOLINK.has_output, domain=BiologicalProcessOrActivity, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.is_output_of = Slot(uri=BIOLINK.is_output_of, name="is output of", curie=BIOLINK.curie('is_output_of'),
                   model_uri=BIOLINK.is_output_of, domain=NamedThing, range=Optional[Union[Union[str, BiologicalProcessOrActivityId], list[Union[str, BiologicalProcessOrActivityId]]]])

slots.has_participant = Slot(uri=BIOLINK.has_participant, name="has participant", curie=BIOLINK.curie('has_participant'),
                   model_uri=BIOLINK.has_participant, domain=BiologicalProcessOrActivity, range=Optional[Union[Union[dict, Occurrent], list[Union[dict, Occurrent]]]])

slots.catalyzes = Slot(uri=BIOLINK.catalyzes, name="catalyzes", curie=BIOLINK.curie('catalyzes'),
                   model_uri=BIOLINK.catalyzes, domain=None, range=Optional[Union[Union[str, BiologicalProcessOrActivityId], list[Union[str, BiologicalProcessOrActivityId]]]])

slots.has_catalyst = Slot(uri=BIOLINK.has_catalyst, name="has catalyst", curie=BIOLINK.curie('has_catalyst'),
                   model_uri=BIOLINK.has_catalyst, domain=BiologicalProcessOrActivity, range=Optional[Union[Union[dict, Occurrent], list[Union[dict, Occurrent]]]])

slots.has_substrate = Slot(uri=BIOLINK.has_substrate, name="has substrate", curie=BIOLINK.curie('has_substrate'),
                   model_uri=BIOLINK.has_substrate, domain=None, range=Optional[Union[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"], list[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"]]]])

slots.is_substrate_of = Slot(uri=BIOLINK.is_substrate_of, name="is substrate of", curie=BIOLINK.curie('is_substrate_of'),
                   model_uri=BIOLINK.is_substrate_of, domain=None, range=Optional[Union[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"], list[Union[dict, "ChemicalEntityOrGeneOrGeneProduct"]]]])

slots.participates_in = Slot(uri=BIOLINK.participates_in, name="participates in", curie=BIOLINK.curie('participates_in'),
                   model_uri=BIOLINK.participates_in, domain=None, range=Optional[Union[Union[str, BiologicalProcessOrActivityId], list[Union[str, BiologicalProcessOrActivityId]]]])

slots.actively_involved_in = Slot(uri=BIOLINK.actively_involved_in, name="actively involved in", curie=BIOLINK.curie('actively_involved_in'),
                   model_uri=BIOLINK.actively_involved_in, domain=NamedThing, range=Optional[Union[Union[str, BiologicalProcessOrActivityId], list[Union[str, BiologicalProcessOrActivityId]]]])

slots.actively_involves = Slot(uri=BIOLINK.actively_involves, name="actively involves", curie=BIOLINK.curie('actively_involves'),
                   model_uri=BIOLINK.actively_involves, domain=BiologicalProcessOrActivity, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.capable_of = Slot(uri=BIOLINK.capable_of, name="capable of", curie=BIOLINK.curie('capable_of'),
                   model_uri=BIOLINK.capable_of, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], list[Union[dict, "Occurrent"]]]])

slots.can_be_carried_out_by = Slot(uri=BIOLINK.can_be_carried_out_by, name="can be carried out by", curie=BIOLINK.curie('can_be_carried_out_by'),
                   model_uri=BIOLINK.can_be_carried_out_by, domain=None, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.enables = Slot(uri=BIOLINK.enables, name="enables", curie=BIOLINK.curie('enables'),
                   model_uri=BIOLINK.enables, domain=PhysicalEntity, range=Optional[Union[Union[str, BiologicalProcessOrActivityId], list[Union[str, BiologicalProcessOrActivityId]]]])

slots.enabled_by = Slot(uri=BIOLINK.enabled_by, name="enabled by", curie=BIOLINK.curie('enabled_by'),
                   model_uri=BIOLINK.enabled_by, domain=BiologicalProcessOrActivity, range=Optional[Union[Union[str, PhysicalEntityId], list[Union[str, PhysicalEntityId]]]])

slots.derives_into = Slot(uri=BIOLINK.derives_into, name="derives into", curie=BIOLINK.curie('derives_into'),
                   model_uri=BIOLINK.derives_into, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.derives_from = Slot(uri=BIOLINK.derives_from, name="derives from", curie=BIOLINK.curie('derives_from'),
                   model_uri=BIOLINK.derives_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.is_metabolite_of = Slot(uri=BIOLINK.is_metabolite_of, name="is metabolite of", curie=BIOLINK.curie('is_metabolite_of'),
                   model_uri=BIOLINK.is_metabolite_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], list[Union[str, MolecularEntityId]]]])

slots.has_metabolite = Slot(uri=BIOLINK.has_metabolite, name="has metabolite", curie=BIOLINK.curie('has_metabolite'),
                   model_uri=BIOLINK.has_metabolite, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], list[Union[str, MolecularEntityId]]]])

slots.food_component_of = Slot(uri=BIOLINK.food_component_of, name="food component of", curie=BIOLINK.curie('food_component_of'),
                   model_uri=BIOLINK.food_component_of, domain=ChemicalEntity, range=Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]])

slots.has_food_component = Slot(uri=BIOLINK.has_food_component, name="has food component", curie=BIOLINK.curie('has_food_component'),
                   model_uri=BIOLINK.has_food_component, domain=ChemicalEntity, range=Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]])

slots.nutrient_of = Slot(uri=BIOLINK.nutrient_of, name="nutrient of", curie=BIOLINK.curie('nutrient_of'),
                   model_uri=BIOLINK.nutrient_of, domain=ChemicalEntity, range=Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]])

slots.has_nutrient = Slot(uri=BIOLINK.has_nutrient, name="has nutrient", curie=BIOLINK.curie('has_nutrient'),
                   model_uri=BIOLINK.has_nutrient, domain=ChemicalEntity, range=Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]])

slots.is_active_ingredient_of = Slot(uri=BIOLINK.is_active_ingredient_of, name="is active ingredient of", curie=BIOLINK.curie('is_active_ingredient_of'),
                   model_uri=BIOLINK.is_active_ingredient_of, domain=MolecularEntity, range=Optional[Union[Union[str, DrugId], list[Union[str, DrugId]]]], mappings = [RO["0002249"]])

slots.has_active_ingredient = Slot(uri=BIOLINK.has_active_ingredient, name="has active ingredient", curie=BIOLINK.curie('has_active_ingredient'),
                   model_uri=BIOLINK.has_active_ingredient, domain=Drug, range=Optional[Union[Union[str, MolecularEntityId], list[Union[str, MolecularEntityId]]]], mappings = [RO["0002248"]])

slots.is_excipient_of = Slot(uri=BIOLINK.is_excipient_of, name="is excipient of", curie=BIOLINK.curie('is_excipient_of'),
                   model_uri=BIOLINK.is_excipient_of, domain=MolecularEntity, range=Optional[Union[Union[str, DrugId], list[Union[str, DrugId]]]], mappings = [WIKIDATA["Q902638"]])

slots.has_excipient = Slot(uri=BIOLINK.has_excipient, name="has excipient", curie=BIOLINK.curie('has_excipient'),
                   model_uri=BIOLINK.has_excipient, domain=Drug, range=Optional[Union[Union[str, MolecularEntityId], list[Union[str, MolecularEntityId]]]], mappings = [WIKIDATA["Q902638"]])

slots.manifestation_of = Slot(uri=BIOLINK.manifestation_of, name="manifestation of", curie=BIOLINK.curie('manifestation_of'),
                   model_uri=BIOLINK.manifestation_of, domain=NamedThing, range=Optional[Union[Union[str, DiseaseId], list[Union[str, DiseaseId]]]])

slots.has_manifestation = Slot(uri=BIOLINK.has_manifestation, name="has manifestation", curie=BIOLINK.curie('has_manifestation'),
                   model_uri=BIOLINK.has_manifestation, domain=Disease, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.mode_of_inheritance_of = Slot(uri=BIOLINK.mode_of_inheritance_of, name="mode of inheritance of", curie=BIOLINK.curie('mode_of_inheritance_of'),
                   model_uri=BIOLINK.mode_of_inheritance_of, domain=GeneticInheritance, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.has_mode_of_inheritance = Slot(uri=BIOLINK.has_mode_of_inheritance, name="has mode of inheritance", curie=BIOLINK.curie('has_mode_of_inheritance'),
                   model_uri=BIOLINK.has_mode_of_inheritance, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[str, GeneticInheritanceId], list[Union[str, GeneticInheritanceId]]]])

slots.produces = Slot(uri=BIOLINK.produces, name="produces", curie=BIOLINK.curie('produces'),
                   model_uri=BIOLINK.produces, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.produced_by = Slot(uri=BIOLINK.produced_by, name="produced by", curie=BIOLINK.curie('produced_by'),
                   model_uri=BIOLINK.produced_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.consumes = Slot(uri=BIOLINK.consumes, name="consumes", curie=BIOLINK.curie('consumes'),
                   model_uri=BIOLINK.consumes, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.consumed_by = Slot(uri=BIOLINK.consumed_by, name="consumed by", curie=BIOLINK.curie('consumed_by'),
                   model_uri=BIOLINK.consumed_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.temporally_related_to = Slot(uri=BIOLINK.temporally_related_to, name="temporally related to", curie=BIOLINK.curie('temporally_related_to'),
                   model_uri=BIOLINK.temporally_related_to, domain=None, range=Optional[Union[Union[dict, "Occurrent"], list[Union[dict, "Occurrent"]]]])

slots.precedes = Slot(uri=BIOLINK.precedes, name="precedes", curie=BIOLINK.curie('precedes'),
                   model_uri=BIOLINK.precedes, domain=None, range=Optional[Union[Union[dict, "Occurrent"], list[Union[dict, "Occurrent"]]]])

slots.preceded_by = Slot(uri=BIOLINK.preceded_by, name="preceded by", curie=BIOLINK.curie('preceded_by'),
                   model_uri=BIOLINK.preceded_by, domain=None, range=Optional[Union[Union[dict, "Occurrent"], list[Union[dict, "Occurrent"]]]])

slots.has_variant_part = Slot(uri=BIOLINK.has_variant_part, name="has variant part", curie=BIOLINK.curie('has_variant_part'),
                   model_uri=BIOLINK.has_variant_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.variant_part_of = Slot(uri=BIOLINK.variant_part_of, name="variant part of", curie=BIOLINK.curie('variant_part_of'),
                   model_uri=BIOLINK.variant_part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.related_condition = Slot(uri=BIOLINK.related_condition, name="related condition", curie=BIOLINK.curie('related_condition'),
                   model_uri=BIOLINK.related_condition, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.is_sequence_variant_of = Slot(uri=BIOLINK.is_sequence_variant_of, name="is sequence variant of", curie=BIOLINK.curie('is_sequence_variant_of'),
                   model_uri=BIOLINK.is_sequence_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, GenomicEntity], list[Union[dict, GenomicEntity]]]])

slots.has_sequence_variant = Slot(uri=BIOLINK.has_sequence_variant, name="has sequence variant", curie=BIOLINK.curie('has_sequence_variant'),
                   model_uri=BIOLINK.has_sequence_variant, domain=None, range=Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]])

slots.is_missense_variant_of = Slot(uri=BIOLINK.is_missense_variant_of, name="is missense variant of", curie=BIOLINK.curie('is_missense_variant_of'),
                   model_uri=BIOLINK.is_missense_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, GenomicEntity], list[Union[dict, GenomicEntity]]]])

slots.has_missense_variant = Slot(uri=BIOLINK.has_missense_variant, name="has missense variant", curie=BIOLINK.curie('has_missense_variant'),
                   model_uri=BIOLINK.has_missense_variant, domain=None, range=Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]])

slots.is_synonymous_variant_of = Slot(uri=BIOLINK.is_synonymous_variant_of, name="is synonymous variant of", curie=BIOLINK.curie('is_synonymous_variant_of'),
                   model_uri=BIOLINK.is_synonymous_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, GenomicEntity], list[Union[dict, GenomicEntity]]]])

slots.has_synonymous_variant = Slot(uri=BIOLINK.has_synonymous_variant, name="has synonymous variant", curie=BIOLINK.curie('has_synonymous_variant'),
                   model_uri=BIOLINK.has_synonymous_variant, domain=None, range=Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]])

slots.is_nonsense_variant_of = Slot(uri=BIOLINK.is_nonsense_variant_of, name="is nonsense variant of", curie=BIOLINK.curie('is_nonsense_variant_of'),
                   model_uri=BIOLINK.is_nonsense_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, GenomicEntity], list[Union[dict, GenomicEntity]]]])

slots.has_nonsense_variant = Slot(uri=BIOLINK.has_nonsense_variant, name="has nonsense variant", curie=BIOLINK.curie('has_nonsense_variant'),
                   model_uri=BIOLINK.has_nonsense_variant, domain=None, range=Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]])

slots.is_frameshift_variant_of = Slot(uri=BIOLINK.is_frameshift_variant_of, name="is frameshift variant of", curie=BIOLINK.curie('is_frameshift_variant_of'),
                   model_uri=BIOLINK.is_frameshift_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, GenomicEntity], list[Union[dict, GenomicEntity]]]])

slots.has_frameshift_variant = Slot(uri=BIOLINK.has_frameshift_variant, name="has frameshift variant", curie=BIOLINK.curie('has_frameshift_variant'),
                   model_uri=BIOLINK.has_frameshift_variant, domain=None, range=Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]])

slots.is_splice_site_variant_of = Slot(uri=BIOLINK.is_splice_site_variant_of, name="is splice site variant of", curie=BIOLINK.curie('is_splice_site_variant_of'),
                   model_uri=BIOLINK.is_splice_site_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, GenomicEntity], list[Union[dict, GenomicEntity]]]])

slots.has_splice_site_variant = Slot(uri=BIOLINK.has_splice_site_variant, name="has splice site variant", curie=BIOLINK.curie('has_splice_site_variant'),
                   model_uri=BIOLINK.has_splice_site_variant, domain=None, range=Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]])

slots.is_nearby_variant_of = Slot(uri=BIOLINK.is_nearby_variant_of, name="is nearby variant of", curie=BIOLINK.curie('is_nearby_variant_of'),
                   model_uri=BIOLINK.is_nearby_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, GenomicEntity], list[Union[dict, GenomicEntity]]]])

slots.has_nearby_variant = Slot(uri=BIOLINK.has_nearby_variant, name="has nearby variant", curie=BIOLINK.curie('has_nearby_variant'),
                   model_uri=BIOLINK.has_nearby_variant, domain=None, range=Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]])

slots.is_non_coding_variant_of = Slot(uri=BIOLINK.is_non_coding_variant_of, name="is non coding variant of", curie=BIOLINK.curie('is_non_coding_variant_of'),
                   model_uri=BIOLINK.is_non_coding_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, GenomicEntity], list[Union[dict, GenomicEntity]]]])

slots.has_non_coding_variant = Slot(uri=BIOLINK.has_non_coding_variant, name="has non coding variant", curie=BIOLINK.curie('has_non_coding_variant'),
                   model_uri=BIOLINK.has_non_coding_variant, domain=None, range=Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]])

slots.disease_has_basis_in = Slot(uri=BIOLINK.disease_has_basis_in, name="disease has basis in", curie=BIOLINK.curie('disease_has_basis_in'),
                   model_uri=BIOLINK.disease_has_basis_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.occurs_in_disease = Slot(uri=BIOLINK.occurs_in_disease, name="occurs in disease", curie=BIOLINK.curie('occurs_in_disease'),
                   model_uri=BIOLINK.occurs_in_disease, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.has_adverse_event = Slot(uri=BIOLINK.has_adverse_event, name="has adverse event", curie=BIOLINK.curie('has_adverse_event'),
                   model_uri=BIOLINK.has_adverse_event, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.adverse_event_of = Slot(uri=BIOLINK.adverse_event_of, name="adverse event of", curie=BIOLINK.curie('adverse_event_of'),
                   model_uri=BIOLINK.adverse_event_of, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.has_side_effect = Slot(uri=BIOLINK.has_side_effect, name="has side effect", curie=BIOLINK.curie('has_side_effect'),
                   model_uri=BIOLINK.has_side_effect, domain=None, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], list[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.is_side_effect_of = Slot(uri=BIOLINK.is_side_effect_of, name="is side effect of", curie=BIOLINK.curie('is_side_effect_of'),
                   model_uri=BIOLINK.is_side_effect_of, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.contraindicated_in = Slot(uri=BIOLINK.contraindicated_in, name="contraindicated in", curie=BIOLINK.curie('contraindicated_in'),
                   model_uri=BIOLINK.contraindicated_in, domain=None, range=Optional[Union[Union[str, BiologicalEntityId], list[Union[str, BiologicalEntityId]]]])

slots.chemical_entity_or_drug_or_treatment = Slot(uri=BIOLINK.chemical_entity_or_drug_or_treatment, name="chemical entity or drug or treatment", curie=BIOLINK.curie('chemical_entity_or_drug_or_treatment'),
                   model_uri=BIOLINK.chemical_entity_or_drug_or_treatment, domain=None, range=Optional[str])

slots.has_contraindication = Slot(uri=BIOLINK.has_contraindication, name="has contraindication", curie=BIOLINK.curie('has_contraindication'),
                   model_uri=BIOLINK.has_contraindication, domain=BiologicalEntity, range=Optional[Union[Union[dict, ChemicalOrDrugOrTreatment], list[Union[dict, ChemicalOrDrugOrTreatment]]]])

slots.has_not_completed = Slot(uri=BIOLINK.has_not_completed, name="has not completed", curie=BIOLINK.curie('has_not_completed'),
                   model_uri=BIOLINK.has_not_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.not_completed_by = Slot(uri=BIOLINK.not_completed_by, name="not completed by", curie=BIOLINK.curie('not_completed_by'),
                   model_uri=BIOLINK.not_completed_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.has_completed = Slot(uri=BIOLINK.has_completed, name="has completed", curie=BIOLINK.curie('has_completed'),
                   model_uri=BIOLINK.has_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.completed_by = Slot(uri=BIOLINK.completed_by, name="completed by", curie=BIOLINK.curie('completed_by'),
                   model_uri=BIOLINK.completed_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.in_linkage_disequilibrium_with = Slot(uri=BIOLINK.in_linkage_disequilibrium_with, name="in linkage disequilibrium with", curie=BIOLINK.curie('in_linkage_disequilibrium_with'),
                   model_uri=BIOLINK.in_linkage_disequilibrium_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.has_increased_amount = Slot(uri=BIOLINK.has_increased_amount, name="has increased amount", curie=BIOLINK.curie('has_increased_amount'),
                   model_uri=BIOLINK.has_increased_amount, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.increased_amount_of = Slot(uri=BIOLINK.increased_amount_of, name="increased amount of", curie=BIOLINK.curie('increased_amount_of'),
                   model_uri=BIOLINK.increased_amount_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.has_decreased_amount = Slot(uri=BIOLINK.has_decreased_amount, name="has decreased amount", curie=BIOLINK.curie('has_decreased_amount'),
                   model_uri=BIOLINK.has_decreased_amount, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.decreased_amount_in = Slot(uri=BIOLINK.decreased_amount_in, name="decreased amount in", curie=BIOLINK.curie('decreased_amount_in'),
                   model_uri=BIOLINK.decreased_amount_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.lacks_part = Slot(uri=BIOLINK.lacks_part, name="lacks part", curie=BIOLINK.curie('lacks_part'),
                   model_uri=BIOLINK.lacks_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.missing_from = Slot(uri=BIOLINK.missing_from, name="missing from", curie=BIOLINK.curie('missing_from'),
                   model_uri=BIOLINK.missing_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.develops_from = Slot(uri=BIOLINK.develops_from, name="develops from", curie=BIOLINK.curie('develops_from'),
                   model_uri=BIOLINK.develops_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.develops_into = Slot(uri=BIOLINK.develops_into, name="develops into", curie=BIOLINK.curie('develops_into'),
                   model_uri=BIOLINK.develops_into, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.in_taxon = Slot(uri=BIOLINK.in_taxon, name="in taxon", curie=BIOLINK.curie('in_taxon'),
                   model_uri=BIOLINK.in_taxon, domain=None, range=Optional[Union[Union[str, OrganismTaxonId], list[Union[str, OrganismTaxonId]]]])

slots.in_taxon_label = Slot(uri=BIOLINK.in_taxon_label, name="in taxon label", curie=BIOLINK.curie('in_taxon_label'),
                   model_uri=BIOLINK.in_taxon_label, domain=None, range=Optional[Union[str, LabelType]])

slots.taxon_of = Slot(uri=BIOLINK.taxon_of, name="taxon of", curie=BIOLINK.curie('taxon_of'),
                   model_uri=BIOLINK.taxon_of, domain=OrganismTaxon, range=Optional[Union[Union[dict, "ThingWithTaxon"], list[Union[dict, "ThingWithTaxon"]]]])

slots.has_molecular_consequence = Slot(uri=BIOLINK.has_molecular_consequence, name="has molecular consequence", curie=BIOLINK.curie('has_molecular_consequence'),
                   model_uri=BIOLINK.has_molecular_consequence, domain=NamedThing, range=Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]])

slots.is_molecular_consequence_of = Slot(uri=BIOLINK.is_molecular_consequence_of, name="is molecular consequence of", curie=BIOLINK.curie('is_molecular_consequence_of'),
                   model_uri=BIOLINK.is_molecular_consequence_of, domain=None, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.association_slot = Slot(uri=BIOLINK.association_slot, name="association slot", curie=BIOLINK.curie('association_slot'),
                   model_uri=BIOLINK.association_slot, domain=Association, range=Optional[str])

slots.qualifier = Slot(uri=BIOLINK.qualifier, name="qualifier", curie=BIOLINK.curie('qualifier'),
                   model_uri=BIOLINK.qualifier, domain=Association, range=Optional[str])

slots.original_subject = Slot(uri=BIOLINK.original_subject, name="original subject", curie=BIOLINK.curie('original_subject'),
                   model_uri=BIOLINK.original_subject, domain=Association, range=Optional[str])

slots.original_object = Slot(uri=BIOLINK.original_object, name="original object", curie=BIOLINK.curie('original_object'),
                   model_uri=BIOLINK.original_object, domain=Association, range=Optional[str])

slots.original_predicate = Slot(uri=BIOLINK.original_predicate, name="original predicate", curie=BIOLINK.curie('original_predicate'),
                   model_uri=BIOLINK.original_predicate, domain=Association, range=Optional[Union[str, URIorCURIE]])

slots.subject_closure = Slot(uri=BIOLINK.subject_closure, name="subject closure", curie=BIOLINK.curie('subject_closure'),
                   model_uri=BIOLINK.subject_closure, domain=Association, range=Optional[Union[str, list[str]]])

slots.object_closure = Slot(uri=BIOLINK.object_closure, name="object closure", curie=BIOLINK.curie('object_closure'),
                   model_uri=BIOLINK.object_closure, domain=Association, range=Optional[Union[str, list[str]]])

slots.subject_category = Slot(uri=BIOLINK.subject_category, name="subject category", curie=BIOLINK.curie('subject_category'),
                   model_uri=BIOLINK.subject_category, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.object_category = Slot(uri=BIOLINK.object_category, name="object category", curie=BIOLINK.curie('object_category'),
                   model_uri=BIOLINK.object_category, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.subject_category_closure = Slot(uri=BIOLINK.subject_category_closure, name="subject category closure", curie=BIOLINK.curie('subject_category_closure'),
                   model_uri=BIOLINK.subject_category_closure, domain=Association, range=Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]])

slots.object_category_closure = Slot(uri=BIOLINK.object_category_closure, name="object category closure", curie=BIOLINK.curie('object_category_closure'),
                   model_uri=BIOLINK.object_category_closure, domain=Association, range=Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]])

slots.subject_label_closure = Slot(uri=BIOLINK.subject_label_closure, name="subject label closure", curie=BIOLINK.curie('subject_label_closure'),
                   model_uri=BIOLINK.subject_label_closure, domain=Association, range=Optional[Union[str, list[str]]])

slots.object_label_closure = Slot(uri=BIOLINK.object_label_closure, name="object label closure", curie=BIOLINK.curie('object_label_closure'),
                   model_uri=BIOLINK.object_label_closure, domain=Association, range=Optional[Union[str, list[str]]])

slots.subject_namespace = Slot(uri=BIOLINK.subject_namespace, name="subject namespace", curie=BIOLINK.curie('subject_namespace'),
                   model_uri=BIOLINK.subject_namespace, domain=Association, range=Optional[str])

slots.object_namespace = Slot(uri=BIOLINK.object_namespace, name="object namespace", curie=BIOLINK.curie('object_namespace'),
                   model_uri=BIOLINK.object_namespace, domain=Association, range=Optional[str])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.subject, domain=Association, range=Union[str, NamedThingId])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.object, domain=Association, range=Union[str, NamedThingId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.predicate, domain=Association, range=Union[str, PredicateType])

slots.logical_interpretation = Slot(uri=BIOLINK.logical_interpretation, name="logical interpretation", curie=BIOLINK.curie('logical_interpretation'),
                   model_uri=BIOLINK.logical_interpretation, domain=Association, range=Optional[Union[str, "LogicalInterpretationEnum"]])

slots.relation = Slot(uri=BIOLINK.relation, name="relation", curie=BIOLINK.curie('relation'),
                   model_uri=BIOLINK.relation, domain=None, range=Optional[str])

slots.negated = Slot(uri=BIOLINK.negated, name="negated", curie=BIOLINK.curie('negated'),
                   model_uri=BIOLINK.negated, domain=Association, range=Optional[Union[bool, Bool]])

slots.has_confidence_level = Slot(uri=BIOLINK.has_confidence_level, name="has confidence level", curie=BIOLINK.curie('has_confidence_level'),
                   model_uri=BIOLINK.has_confidence_level, domain=Association, range=Optional[str])

slots.has_confidence_score = Slot(uri=BIOLINK.has_confidence_score, name="has confidence score", curie=BIOLINK.curie('has_confidence_score'),
                   model_uri=BIOLINK.has_confidence_score, domain=Association, range=Optional[float])

slots.has_evidence = Slot(uri=BIOLINK.has_evidence, name="has evidence", curie=BIOLINK.curie('has_evidence'),
                   model_uri=BIOLINK.has_evidence, domain=Association, range=Optional[Union[Union[str, EvidenceTypeId], list[Union[str, EvidenceTypeId]]]])

slots.has_supporting_study_result = Slot(uri=BIOLINK.has_supporting_study_result, name="has supporting study result", curie=BIOLINK.curie('has_supporting_study_result'),
                   model_uri=BIOLINK.has_supporting_study_result, domain=Association, range=Optional[str])

slots.log_odds_ratio = Slot(uri=BIOLINK.log_odds_ratio, name="log odds ratio", curie=BIOLINK.curie('log_odds_ratio'),
                   model_uri=BIOLINK.log_odds_ratio, domain=Association, range=Optional[float])

slots.log_odds_ratio_95_ci = Slot(uri=BIOLINK.log_odds_ratio_95_ci, name="log odds ratio 95 ci", curie=BIOLINK.curie('log_odds_ratio_95_ci'),
                   model_uri=BIOLINK.log_odds_ratio_95_ci, domain=Association, range=Optional[float])

slots.total_sample_size = Slot(uri=BIOLINK.total_sample_size, name="total sample size", curie=BIOLINK.curie('total_sample_size'),
                   model_uri=BIOLINK.total_sample_size, domain=Association, range=Optional[int])

slots.mechanism_of_action = Slot(uri=BIOLINK.mechanism_of_action, name="mechanism of action", curie=BIOLINK.curie('mechanism_of_action'),
                   model_uri=BIOLINK.mechanism_of_action, domain=Association, range=Optional[Union[bool, Bool]])

slots.knowledge_source = Slot(uri=BIOLINK.knowledge_source, name="knowledge source", curie=BIOLINK.curie('knowledge_source'),
                   model_uri=BIOLINK.knowledge_source, domain=Association, range=Optional[str])

slots.provided_by = Slot(uri=BIOLINK.provided_by, name="provided by", curie=BIOLINK.curie('provided_by'),
                   model_uri=BIOLINK.provided_by, domain=NamedThing, range=Optional[Union[str, list[str]]])

slots.primary_knowledge_source = Slot(uri=BIOLINK.primary_knowledge_source, name="primary knowledge source", curie=BIOLINK.curie('primary_knowledge_source'),
                   model_uri=BIOLINK.primary_knowledge_source, domain=Association, range=Optional[str])

slots.aggregator_knowledge_source = Slot(uri=BIOLINK.aggregator_knowledge_source, name="aggregator knowledge source", curie=BIOLINK.curie('aggregator_knowledge_source'),
                   model_uri=BIOLINK.aggregator_knowledge_source, domain=Association, range=Optional[Union[str, list[str]]])

slots.supporting_data_source = Slot(uri=BIOLINK.supporting_data_source, name="supporting data source", curie=BIOLINK.curie('supporting_data_source'),
                   model_uri=BIOLINK.supporting_data_source, domain=Association, range=Optional[Union[str, list[str]]])

slots.supporting_data_set = Slot(uri=BIOLINK.supporting_data_set, name="supporting data set", curie=BIOLINK.curie('supporting_data_set'),
                   model_uri=BIOLINK.supporting_data_set, domain=Association, range=Optional[Union[str, list[str]]])

slots.chi_squared_statistic = Slot(uri=BIOLINK.chi_squared_statistic, name="chi squared statistic", curie=BIOLINK.curie('chi_squared_statistic'),
                   model_uri=BIOLINK.chi_squared_statistic, domain=Association, range=Optional[float])

slots.z_score = Slot(uri=BIOLINK.z_score, name="z score", curie=BIOLINK.curie('z_score'),
                   model_uri=BIOLINK.z_score, domain=Association, range=Optional[float])

slots.p_value = Slot(uri=BIOLINK.p_value, name="p value", curie=BIOLINK.curie('p_value'),
                   model_uri=BIOLINK.p_value, domain=Association, range=Optional[float])

slots.evidence_count = Slot(uri=BIOLINK.evidence_count, name="evidence count", curie=BIOLINK.curie('evidence_count'),
                   model_uri=BIOLINK.evidence_count, domain=Association, range=Optional[int])

slots.dataset_count = Slot(uri=BIOLINK.dataset_count, name="dataset count", curie=BIOLINK.curie('dataset_count'),
                   model_uri=BIOLINK.dataset_count, domain=Association, range=Optional[int])

slots.concept_count_subject = Slot(uri=BIOLINK.concept_count_subject, name="concept count subject", curie=BIOLINK.curie('concept_count_subject'),
                   model_uri=BIOLINK.concept_count_subject, domain=Association, range=Optional[int])

slots.concept_count_object = Slot(uri=BIOLINK.concept_count_object, name="concept count object", curie=BIOLINK.curie('concept_count_object'),
                   model_uri=BIOLINK.concept_count_object, domain=Association, range=Optional[int])

slots.concept_pair_count = Slot(uri=BIOLINK.concept_pair_count, name="concept pair count", curie=BIOLINK.curie('concept_pair_count'),
                   model_uri=BIOLINK.concept_pair_count, domain=Association, range=Optional[int])

slots.expected_count = Slot(uri=BIOLINK.expected_count, name="expected count", curie=BIOLINK.curie('expected_count'),
                   model_uri=BIOLINK.expected_count, domain=Association, range=Optional[str])

slots.relative_frequency_subject = Slot(uri=BIOLINK.relative_frequency_subject, name="relative frequency subject", curie=BIOLINK.curie('relative_frequency_subject'),
                   model_uri=BIOLINK.relative_frequency_subject, domain=Association, range=Optional[float])

slots.relative_frequency_object = Slot(uri=BIOLINK.relative_frequency_object, name="relative frequency object", curie=BIOLINK.curie('relative_frequency_object'),
                   model_uri=BIOLINK.relative_frequency_object, domain=Association, range=Optional[str])

slots.relative_frequency_subject_confidence_interval = Slot(uri=BIOLINK.relative_frequency_subject_confidence_interval, name="relative frequency subject confidence interval", curie=BIOLINK.curie('relative_frequency_subject_confidence_interval'),
                   model_uri=BIOLINK.relative_frequency_subject_confidence_interval, domain=Association, range=Optional[str])

slots.relative_frequency_object_confidence_interval = Slot(uri=BIOLINK.relative_frequency_object_confidence_interval, name="relative frequency object confidence interval", curie=BIOLINK.curie('relative_frequency_object_confidence_interval'),
                   model_uri=BIOLINK.relative_frequency_object_confidence_interval, domain=Association, range=Optional[str])

slots.adjusted_p_value = Slot(uri=BIOLINK.adjusted_p_value, name="adjusted p value", curie=BIOLINK.curie('adjusted_p_value'),
                   model_uri=BIOLINK.adjusted_p_value, domain=Association, range=Optional[float])

slots.bonferonni_adjusted_p_value = Slot(uri=BIOLINK.bonferonni_adjusted_p_value, name="bonferonni adjusted p value", curie=BIOLINK.curie('bonferonni_adjusted_p_value'),
                   model_uri=BIOLINK.bonferonni_adjusted_p_value, domain=Association, range=Optional[float])

slots.supporting_text = Slot(uri=BIOLINK.supporting_text, name="supporting text", curie=BIOLINK.curie('supporting_text'),
                   model_uri=BIOLINK.supporting_text, domain=Association, range=Optional[Union[str, list[str]]])

slots.supporting_documents = Slot(uri=BIOLINK.supporting_documents, name="supporting documents", curie=BIOLINK.curie('supporting_documents'),
                   model_uri=BIOLINK.supporting_documents, domain=Association, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.subject_location_in_text = Slot(uri=BIOLINK.subject_location_in_text, name="subject location in text", curie=BIOLINK.curie('subject_location_in_text'),
                   model_uri=BIOLINK.subject_location_in_text, domain=Association, range=Optional[Union[int, list[int]]])

slots.object_location_in_text = Slot(uri=BIOLINK.object_location_in_text, name="object location in text", curie=BIOLINK.curie('object_location_in_text'),
                   model_uri=BIOLINK.object_location_in_text, domain=Association, range=Optional[Union[int, list[int]]])

slots.extraction_confidence_score = Slot(uri=BIOLINK.extraction_confidence_score, name="extraction confidence score", curie=BIOLINK.curie('extraction_confidence_score'),
                   model_uri=BIOLINK.extraction_confidence_score, domain=Association, range=Optional[int])

slots.supporting_document_type = Slot(uri=BIOLINK.supporting_document_type, name="supporting document type", curie=BIOLINK.curie('supporting_document_type'),
                   model_uri=BIOLINK.supporting_document_type, domain=Association, range=Optional[str])

slots.supporting_document_year = Slot(uri=BIOLINK.supporting_document_year, name="supporting document year", curie=BIOLINK.curie('supporting_document_year'),
                   model_uri=BIOLINK.supporting_document_year, domain=Association, range=Optional[int])

slots.supporting_text_section_type = Slot(uri=BIOLINK.supporting_text_section_type, name="supporting text section type", curie=BIOLINK.curie('supporting_text_section_type'),
                   model_uri=BIOLINK.supporting_text_section_type, domain=Association, range=Optional[str])

slots.ln_ratio = Slot(uri=BIOLINK.ln_ratio, name="ln ratio", curie=BIOLINK.curie('ln_ratio'),
                   model_uri=BIOLINK.ln_ratio, domain=Association, range=Optional[float])

slots.ln_ratio_confidence_interval = Slot(uri=BIOLINK.ln_ratio_confidence_interval, name="ln ratio confidence interval", curie=BIOLINK.curie('ln_ratio_confidence_interval'),
                   model_uri=BIOLINK.ln_ratio_confidence_interval, domain=Association, range=Optional[float])

slots.interacting_molecules_category = Slot(uri=BIOLINK.interacting_molecules_category, name="interacting molecules category", curie=BIOLINK.curie('interacting_molecules_category'),
                   model_uri=BIOLINK.interacting_molecules_category, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.expression_site = Slot(uri=BIOLINK.expression_site, name="expression site", curie=BIOLINK.curie('expression_site'),
                   model_uri=BIOLINK.expression_site, domain=Association, range=Optional[Union[str, AnatomicalEntityId]])

slots.phenotypic_state = Slot(uri=BIOLINK.phenotypic_state, name="phenotypic state", curie=BIOLINK.curie('phenotypic_state'),
                   model_uri=BIOLINK.phenotypic_state, domain=Association, range=Optional[Union[str, DiseaseOrPhenotypicFeatureId]])

slots.publications = Slot(uri=BIOLINK.publications, name="publications", curie=BIOLINK.curie('publications'),
                   model_uri=BIOLINK.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]])

slots.sources = Slot(uri=BIOLINK.sources, name="sources", curie=BIOLINK.curie('sources'),
                   model_uri=BIOLINK.sources, domain=Association, range=Optional[Union[Union[str, RetrievalSourceId], list[Union[str, RetrievalSourceId]]]])

slots.associated_environmental_context = Slot(uri=BIOLINK.associated_environmental_context, name="associated environmental context", curie=BIOLINK.curie('associated_environmental_context'),
                   model_uri=BIOLINK.associated_environmental_context, domain=Association, range=Optional[str])

slots.sequence_localization_attribute = Slot(uri=BIOLINK.sequence_localization_attribute, name="sequence localization attribute", curie=BIOLINK.curie('sequence_localization_attribute'),
                   model_uri=BIOLINK.sequence_localization_attribute, domain=GenomicSequenceLocalization, range=Optional[str])

slots.interbase_coordinate = Slot(uri=BIOLINK.interbase_coordinate, name="interbase coordinate", curie=BIOLINK.curie('interbase_coordinate'),
                   model_uri=BIOLINK.interbase_coordinate, domain=GenomicSequenceLocalization, range=Optional[int])

slots.start_interbase_coordinate = Slot(uri=BIOLINK.start_interbase_coordinate, name="start interbase coordinate", curie=BIOLINK.curie('start_interbase_coordinate'),
                   model_uri=BIOLINK.start_interbase_coordinate, domain=GenomicSequenceLocalization, range=Optional[int])

slots.end_interbase_coordinate = Slot(uri=BIOLINK.end_interbase_coordinate, name="end interbase coordinate", curie=BIOLINK.curie('end_interbase_coordinate'),
                   model_uri=BIOLINK.end_interbase_coordinate, domain=GenomicSequenceLocalization, range=Optional[int])

slots.start_coordinate = Slot(uri=BIOLINK.start_coordinate, name="start coordinate", curie=BIOLINK.curie('start_coordinate'),
                   model_uri=BIOLINK.start_coordinate, domain=GenomicSequenceLocalization, range=Optional[int])

slots.end_coordinate = Slot(uri=BIOLINK.end_coordinate, name="end coordinate", curie=BIOLINK.curie('end_coordinate'),
                   model_uri=BIOLINK.end_coordinate, domain=GenomicSequenceLocalization, range=Optional[int])

slots.genome_build = Slot(uri=BIOLINK.genome_build, name="genome build", curie=BIOLINK.curie('genome_build'),
                   model_uri=BIOLINK.genome_build, domain=GenomicSequenceLocalization, range=Optional[Union[str, "StrandEnum"]])

slots.strand = Slot(uri=BIOLINK.strand, name="strand", curie=BIOLINK.curie('strand'),
                   model_uri=BIOLINK.strand, domain=GenomicSequenceLocalization, range=Optional[Union[str, "StrandEnum"]])

slots.phase = Slot(uri=BIOLINK.phase, name="phase", curie=BIOLINK.curie('phase'),
                   model_uri=BIOLINK.phase, domain=CodingSequence, range=Optional[Union[str, "PhaseEnum"]])

slots.clinical_approval_status = Slot(uri=BIOLINK.clinical_approval_status, name="clinical approval status", curie=BIOLINK.curie('clinical_approval_status'),
                   model_uri=BIOLINK.clinical_approval_status, domain=Association, range=Optional[Union[str, "ClinicalApprovalStatusEnum"]])

slots.max_research_phase = Slot(uri=BIOLINK.max_research_phase, name="max research phase", curie=BIOLINK.curie('max_research_phase'),
                   model_uri=BIOLINK.max_research_phase, domain=Association, range=Optional[Union[str, "ResearchPhaseEnum"]])

slots.has_supporting_studies = Slot(uri=BIOLINK.has_supporting_studies, name="has supporting studies", curie=BIOLINK.curie('has_supporting_studies'),
                   model_uri=BIOLINK.has_supporting_studies, domain=Association, range=Optional[Union[Union[str, StudyId], list[Union[str, StudyId]]]])

slots.supporting_study_metadata = Slot(uri=BIOLINK.supporting_study_metadata, name="supporting study metadata", curie=BIOLINK.curie('supporting_study_metadata'),
                   model_uri=BIOLINK.supporting_study_metadata, domain=Association, range=Optional[str])

slots.supporting_study_method_type = Slot(uri=BIOLINK.supporting_study_method_type, name="supporting study method type", curie=BIOLINK.curie('supporting_study_method_type'),
                   model_uri=BIOLINK.supporting_study_method_type, domain=Association, range=Optional[Union[str, URIorCURIE]])

slots.supporting_study_method_description = Slot(uri=BIOLINK.supporting_study_method_description, name="supporting study method description", curie=BIOLINK.curie('supporting_study_method_description'),
                   model_uri=BIOLINK.supporting_study_method_description, domain=Association, range=Optional[Union[str, URIorCURIE]])

slots.supporting_study_size = Slot(uri=BIOLINK.supporting_study_size, name="supporting study size", curie=BIOLINK.curie('supporting_study_size'),
                   model_uri=BIOLINK.supporting_study_size, domain=Association, range=Optional[int])

slots.supporting_study_cohort = Slot(uri=BIOLINK.supporting_study_cohort, name="supporting study cohort", curie=BIOLINK.curie('supporting_study_cohort'),
                   model_uri=BIOLINK.supporting_study_cohort, domain=Association, range=Optional[str])

slots.supporting_study_date_range = Slot(uri=BIOLINK.supporting_study_date_range, name="supporting study date range", curie=BIOLINK.curie('supporting_study_date_range'),
                   model_uri=BIOLINK.supporting_study_date_range, domain=Association, range=Optional[str])

slots.supporting_study_context = Slot(uri=BIOLINK.supporting_study_context, name="supporting study context", curie=BIOLINK.curie('supporting_study_context'),
                   model_uri=BIOLINK.supporting_study_context, domain=Association, range=Optional[str])

slots.knowledge_level = Slot(uri=BIOLINK.knowledge_level, name="knowledge level", curie=BIOLINK.curie('knowledge_level'),
                   model_uri=BIOLINK.knowledge_level, domain=Association, range=Union[str, "KnowledgeLevelEnum"])

slots.agent_type = Slot(uri=BIOLINK.agent_type, name="agent type", curie=BIOLINK.curie('agent_type'),
                   model_uri=BIOLINK.agent_type, domain=Association, range=Union[str, "AgentTypeEnum"])

slots.has_biological_sex = Slot(uri=BIOLINK.has_biological_sex, name="has biological sex", curie=BIOLINK.curie('has_biological_sex'),
                   model_uri=BIOLINK.has_biological_sex, domain=None, range=Optional[Union[str, BiologicalSexId]])

slots.attribute_name = Slot(uri=RDFS.label, name="attribute_name", curie=RDFS.curie('label'),
                   model_uri=BIOLINK.attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.named_thing_category = Slot(uri=BIOLINK.category, name="named thing_category", curie=BIOLINK.curie('category'),
                   model_uri=BIOLINK.named_thing_category, domain=NamedThing, range=Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]])

slots.organism_taxon_has_taxonomic_rank = Slot(uri=BIOLINK.has_taxonomic_rank, name="organism taxon_has taxonomic rank", curie=BIOLINK.curie('has_taxonomic_rank'),
                   model_uri=BIOLINK.organism_taxon_has_taxonomic_rank, domain=OrganismTaxon, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA["P105"]])

slots.agent_id = Slot(uri=BIOLINK.id, name="agent_id", curie=BIOLINK.curie('id'),
                   model_uri=BIOLINK.agent_id, domain=Agent, range=Union[str, AgentId])

slots.agent_name = Slot(uri=RDFS.label, name="agent_name", curie=RDFS.curie('label'),
                   model_uri=BIOLINK.agent_name, domain=Agent, range=Optional[Union[str, LabelType]])

slots.publication_id = Slot(uri=BIOLINK.id, name="publication_id", curie=BIOLINK.curie('id'),
                   model_uri=BIOLINK.publication_id, domain=Publication, range=Union[str, PublicationId])

slots.publication_name = Slot(uri=RDFS.label, name="publication_name", curie=RDFS.curie('label'),
                   model_uri=BIOLINK.publication_name, domain=Publication, range=Optional[Union[str, LabelType]])

slots.publication_publication_type = Slot(uri=DCT.type, name="publication_publication type", curie=DCT.curie('type'),
                   model_uri=BIOLINK.publication_publication_type, domain=Publication, range=Union[str, list[str]])

slots.publication_pages = Slot(uri=BIOLINK.pages, name="publication_pages", curie=BIOLINK.curie('pages'),
                   model_uri=BIOLINK.publication_pages, domain=Publication, range=Optional[Union[str, list[str]]])

slots.book_id = Slot(uri=BIOLINK.id, name="book_id", curie=BIOLINK.curie('id'),
                   model_uri=BIOLINK.book_id, domain=Book, range=Union[str, BookId])

slots.book_type = Slot(uri=RDF.type, name="book_type", curie=RDF.curie('type'),
                   model_uri=BIOLINK.book_type, domain=Book, range=Optional[Union[str, list[str]]])

slots.book_chapter_published_in = Slot(uri=BIOLINK.published_in, name="book chapter_published in", curie=BIOLINK.curie('published_in'),
                   model_uri=BIOLINK.book_chapter_published_in, domain=BookChapter, range=Union[str, URIorCURIE])

slots.serial_id = Slot(uri=BIOLINK.id, name="serial_id", curie=BIOLINK.curie('id'),
                   model_uri=BIOLINK.serial_id, domain=Serial, range=Union[str, SerialId])

slots.serial_type = Slot(uri=RDF.type, name="serial_type", curie=RDF.curie('type'),
                   model_uri=BIOLINK.serial_type, domain=Serial, range=Optional[Union[str, list[str]]])

slots.article_published_in = Slot(uri=BIOLINK.published_in, name="article_published in", curie=BIOLINK.curie('published_in'),
                   model_uri=BIOLINK.article_published_in, domain=Article, range=Union[str, URIorCURIE])

slots.article_iso_abbreviation = Slot(uri=BIOLINK.iso_abbreviation, name="article_iso abbreviation", curie=BIOLINK.curie('iso_abbreviation'),
                   model_uri=BIOLINK.article_iso_abbreviation, domain=Article, range=Optional[str])

slots.retrieval_source_resource_id = Slot(uri=BIOLINK.resource_id, name="retrieval source_resource id", curie=BIOLINK.curie('resource_id'),
                   model_uri=BIOLINK.retrieval_source_resource_id, domain=RetrievalSource, range=Union[str, URIorCURIE])

slots.retrieval_source_resource_role = Slot(uri=BIOLINK.resource_role, name="retrieval source_resource role", curie=BIOLINK.curie('resource_role'),
                   model_uri=BIOLINK.retrieval_source_resource_role, domain=RetrievalSource, range=Union[str, "ResourceRoleEnum"])

slots.retrieval_source_upstream_resource_ids = Slot(uri=BIOLINK.upstream_resource_ids, name="retrieval source_upstream resource ids", curie=BIOLINK.curie('upstream_resource_ids'),
                   model_uri=BIOLINK.retrieval_source_upstream_resource_ids, domain=RetrievalSource, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.retrieval_source_source_record_urls = Slot(uri=BIOLINK.source_record_urls, name="retrieval source_source record urls", curie=BIOLINK.curie('source_record_urls'),
                   model_uri=BIOLINK.retrieval_source_source_record_urls, domain=RetrievalSource, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.molecular_activity_has_input = Slot(uri=BIOLINK.has_input, name="molecular activity_has input", curie=BIOLINK.curie('has_input'),
                   model_uri=BIOLINK.molecular_activity_has_input, domain=MolecularActivity, range=Optional[Union[Union[str, MolecularEntityId], list[Union[str, MolecularEntityId]]]])

slots.molecular_activity_has_output = Slot(uri=BIOLINK.has_output, name="molecular activity_has output", curie=BIOLINK.curie('has_output'),
                   model_uri=BIOLINK.molecular_activity_has_output, domain=MolecularActivity, range=Optional[Union[Union[str, MolecularEntityId], list[Union[str, MolecularEntityId]]]])

slots.molecular_activity_enabled_by = Slot(uri=BIOLINK.enabled_by, name="molecular activity_enabled by", curie=BIOLINK.curie('enabled_by'),
                   model_uri=BIOLINK.molecular_activity_enabled_by, domain=MolecularActivity, range=Optional[Union[Union[dict, "MacromolecularMachineMixin"], list[Union[dict, "MacromolecularMachineMixin"]]]])

slots.organismal_entity_has_attribute = Slot(uri=BIOLINK.has_attribute, name="organismal entity_has attribute", curie=BIOLINK.curie('has_attribute'),
                   model_uri=BIOLINK.organismal_entity_has_attribute, domain=OrganismalEntity, range=Optional[Union[Union[str, AttributeId], list[Union[str, AttributeId]]]])

slots.macromolecular_machine_mixin_name = Slot(uri=RDFS.label, name="macromolecular machine mixin_name", curie=RDFS.curie('label'),
                   model_uri=BIOLINK.macromolecular_machine_mixin_name, domain=None, range=Optional[Union[str, SymbolType]])

slots.sequence_variant_has_gene = Slot(uri=BIOLINK.has_gene, name="sequence variant_has gene", curie=BIOLINK.curie('has_gene'),
                   model_uri=BIOLINK.sequence_variant_has_gene, domain=SequenceVariant, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.sequence_variant_has_biological_sequence = Slot(uri=BIOLINK.has_biological_sequence, name="sequence variant_has biological sequence", curie=BIOLINK.curie('has_biological_sequence'),
                   model_uri=BIOLINK.sequence_variant_has_biological_sequence, domain=SequenceVariant, range=Optional[Union[str, BiologicalSequence]])

slots.sequence_variant_id = Slot(uri=BIOLINK.id, name="sequence variant_id", curie=BIOLINK.curie('id'),
                   model_uri=BIOLINK.sequence_variant_id, domain=SequenceVariant, range=Union[str, SequenceVariantId])

slots.clinical_measurement_has_attribute_type = Slot(uri=BIOLINK.has_attribute_type, name="clinical measurement_has attribute type", curie=BIOLINK.curie('has_attribute_type'),
                   model_uri=BIOLINK.clinical_measurement_has_attribute_type, domain=ClinicalMeasurement, range=Union[str, OntologyClassId])

slots.clinical_finding_has_attribute = Slot(uri=BIOLINK.has_attribute, name="clinical finding_has attribute", curie=BIOLINK.curie('has_attribute'),
                   model_uri=BIOLINK.clinical_finding_has_attribute, domain=ClinicalFinding, range=Optional[Union[Union[str, ClinicalAttributeId], list[Union[str, ClinicalAttributeId]]]])

slots.socioeconomic_exposure_has_attribute = Slot(uri=BIOLINK.has_attribute, name="socioeconomic exposure_has attribute", curie=BIOLINK.curie('has_attribute'),
                   model_uri=BIOLINK.socioeconomic_exposure_has_attribute, domain=SocioeconomicExposure, range=Union[Union[str, SocioeconomicAttributeId], list[Union[str, SocioeconomicAttributeId]]])

slots.association_type = Slot(uri=RDF.type, name="association_type", curie=RDF.curie('type'),
                   model_uri=BIOLINK.association_type, domain=Association, range=Optional[Union[str, list[str]]])

slots.association_category = Slot(uri=BIOLINK.category, name="association_category", curie=BIOLINK.curie('category'),
                   model_uri=BIOLINK.association_category, domain=Association, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.association_sources = Slot(uri=BIOLINK.sources, name="association_sources", curie=BIOLINK.curie('sources'),
                   model_uri=BIOLINK.association_sources, domain=Association, range=Optional[Union[dict[Union[str, RetrievalSourceId], Union[dict, RetrievalSource]], list[Union[dict, RetrievalSource]]]])

slots.disease_associated_with_response_to_chemical_entity_association_subject = Slot(uri=RDF.subject, name="disease associated with response to chemical entity association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.disease_associated_with_response_to_chemical_entity_association_subject, domain=DiseaseAssociatedWithResponseToChemicalEntityAssociation, range=Union[str, DiseaseId])

slots.disease_associated_with_response_to_chemical_entity_association_object = Slot(uri=RDF.object, name="disease associated with response to chemical entity association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.disease_associated_with_response_to_chemical_entity_association_object, domain=DiseaseAssociatedWithResponseToChemicalEntityAssociation, range=Union[str, ChemicalEntityId])

slots.disease_associated_with_response_to_chemical_entity_association_predicate = Slot(uri=RDF.predicate, name="disease associated with response to chemical entity association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.disease_associated_with_response_to_chemical_entity_association_predicate, domain=DiseaseAssociatedWithResponseToChemicalEntityAssociation, range=Union[str, PredicateType])

slots.chemical_entity_assesses_named_thing_association_subject = Slot(uri=RDF.subject, name="chemical entity assesses named thing association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.chemical_entity_assesses_named_thing_association_subject, domain=ChemicalEntityAssessesNamedThingAssociation, range=Union[str, ChemicalEntityId])

slots.chemical_entity_assesses_named_thing_association_object = Slot(uri=RDF.object, name="chemical entity assesses named thing association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.chemical_entity_assesses_named_thing_association_object, domain=ChemicalEntityAssessesNamedThingAssociation, range=Union[str, NamedThingId])

slots.chemical_entity_assesses_named_thing_association_predicate = Slot(uri=RDF.predicate, name="chemical entity assesses named thing association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.chemical_entity_assesses_named_thing_association_predicate, domain=ChemicalEntityAssessesNamedThingAssociation, range=Union[str, PredicateType])

slots.contributor_association_subject = Slot(uri=RDF.subject, name="contributor association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.contributor_association_subject, domain=ContributorAssociation, range=Union[str, InformationContentEntityId])

slots.contributor_association_predicate = Slot(uri=RDF.predicate, name="contributor association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.contributor_association_predicate, domain=ContributorAssociation, range=Union[str, PredicateType])

slots.contributor_association_object = Slot(uri=RDF.object, name="contributor association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.contributor_association_object, domain=ContributorAssociation, range=Union[str, AgentId])

slots.contributor_association_qualifiers = Slot(uri=BIOLINK.qualifiers, name="contributor association_qualifiers", curie=BIOLINK.curie('qualifiers'),
                   model_uri=BIOLINK.contributor_association_qualifiers, domain=ContributorAssociation, range=Optional[Union[Union[str, OntologyClassId], list[Union[str, OntologyClassId]]]])

slots.genotype_to_genotype_part_association_predicate = Slot(uri=RDF.predicate, name="genotype to genotype part association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.genotype_to_genotype_part_association_predicate, domain=GenotypeToGenotypePartAssociation, range=Union[str, PredicateType])

slots.genotype_to_genotype_part_association_subject = Slot(uri=RDF.subject, name="genotype to genotype part association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.genotype_to_genotype_part_association_subject, domain=GenotypeToGenotypePartAssociation, range=Union[str, GenotypeId])

slots.genotype_to_genotype_part_association_object = Slot(uri=RDF.object, name="genotype to genotype part association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.genotype_to_genotype_part_association_object, domain=GenotypeToGenotypePartAssociation, range=Union[str, GenotypeId])

slots.genotype_to_gene_association_predicate = Slot(uri=RDF.predicate, name="genotype to gene association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.genotype_to_gene_association_predicate, domain=GenotypeToGeneAssociation, range=Union[str, PredicateType])

slots.genotype_to_gene_association_subject = Slot(uri=RDF.subject, name="genotype to gene association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.genotype_to_gene_association_subject, domain=GenotypeToGeneAssociation, range=Union[str, GenotypeId])

slots.genotype_to_gene_association_object = Slot(uri=RDF.object, name="genotype to gene association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.genotype_to_gene_association_object, domain=GenotypeToGeneAssociation, range=Union[str, GeneId])

slots.genotype_to_variant_association_predicate = Slot(uri=RDF.predicate, name="genotype to variant association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.genotype_to_variant_association_predicate, domain=GenotypeToVariantAssociation, range=Union[str, PredicateType])

slots.genotype_to_variant_association_subject = Slot(uri=RDF.subject, name="genotype to variant association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.genotype_to_variant_association_subject, domain=GenotypeToVariantAssociation, range=Union[str, GenotypeId])

slots.genotype_to_variant_association_object = Slot(uri=RDF.object, name="genotype to variant association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.genotype_to_variant_association_object, domain=GenotypeToVariantAssociation, range=Union[str, SequenceVariantId])

slots.gene_to_gene_association_subject = Slot(uri=RDF.subject, name="gene to gene association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_gene_association_subject, domain=GeneToGeneAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_to_gene_association_object = Slot(uri=RDF.object, name="gene to gene association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_to_gene_association_object, domain=GeneToGeneAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_to_gene_homology_association_subject = Slot(uri=RDF.subject, name="gene to gene homology association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_gene_homology_association_subject, domain=GeneToGeneHomologyAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_to_gene_homology_association_predicate = Slot(uri=RDF.predicate, name="gene to gene homology association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.gene_to_gene_homology_association_predicate, domain=GeneToGeneHomologyAssociation, range=Union[str, PredicateType])

slots.gene_to_gene_homology_association_object = Slot(uri=RDF.object, name="gene to gene homology association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_to_gene_homology_association_object, domain=GeneToGeneHomologyAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_to_gene_family_association_subject = Slot(uri=RDF.subject, name="gene to gene family association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_gene_family_association_subject, domain=GeneToGeneFamilyAssociation, range=Union[str, GeneId])

slots.gene_to_gene_family_association_object = Slot(uri=RDF.object, name="gene to gene family association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_to_gene_family_association_object, domain=GeneToGeneFamilyAssociation, range=Union[str, GeneFamilyId])

slots.gene_to_gene_family_association_predicate = Slot(uri=RDF.predicate, name="gene to gene family association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.gene_to_gene_family_association_predicate, domain=GeneToGeneFamilyAssociation, range=Union[str, PredicateType])

slots.gene_expression_mixin_quantifier_qualifier = Slot(uri=BIOLINK.quantifier_qualifier, name="gene expression mixin_quantifier qualifier", curie=BIOLINK.curie('quantifier_qualifier'),
                   model_uri=BIOLINK.gene_expression_mixin_quantifier_qualifier, domain=None, range=Optional[Union[str, OntologyClassId]])

slots.gene_to_gene_coexpression_association_predicate = Slot(uri=RDF.predicate, name="gene to gene coexpression association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.gene_to_gene_coexpression_association_predicate, domain=GeneToGeneCoexpressionAssociation, range=Union[str, PredicateType])

slots.pairwise_gene_to_gene_interaction_predicate = Slot(uri=RDF.predicate, name="pairwise gene to gene interaction_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.pairwise_gene_to_gene_interaction_predicate, domain=PairwiseGeneToGeneInteraction, range=Union[str, PredicateType])

slots.pairwise_molecular_interaction_subject = Slot(uri=RDF.subject, name="pairwise molecular interaction_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.pairwise_molecular_interaction_subject, domain=PairwiseMolecularInteraction, range=Union[str, MolecularEntityId])

slots.pairwise_molecular_interaction_id = Slot(uri=BIOLINK.id, name="pairwise molecular interaction_id", curie=BIOLINK.curie('id'),
                   model_uri=BIOLINK.pairwise_molecular_interaction_id, domain=PairwiseMolecularInteraction, range=Union[str, PairwiseMolecularInteractionId])

slots.pairwise_molecular_interaction_predicate = Slot(uri=RDF.predicate, name="pairwise molecular interaction_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.pairwise_molecular_interaction_predicate, domain=PairwiseMolecularInteraction, range=Union[str, PredicateType])

slots.pairwise_molecular_interaction_object = Slot(uri=RDF.object, name="pairwise molecular interaction_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.pairwise_molecular_interaction_object, domain=PairwiseMolecularInteraction, range=Union[str, MolecularEntityId])

slots.cell_line_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="cell line to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.cell_line_to_entity_association_mixin_subject, domain=None, range=Union[str, CellLineId])

slots.cell_line_to_disease_or_phenotypic_feature_association_subject = Slot(uri=RDF.subject, name="cell line to disease or phenotypic feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.cell_line_to_disease_or_phenotypic_feature_association_subject, domain=CellLineToDiseaseOrPhenotypicFeatureAssociation, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.chemical_entity_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="chemical entity to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.chemical_entity_to_entity_association_mixin_subject, domain=None, range=Union[dict, ChemicalEntityOrGeneOrGeneProduct])

slots.drug_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="drug to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.drug_to_entity_association_mixin_subject, domain=None, range=Union[str, DrugId])

slots.chemical_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="chemical to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.chemical_to_entity_association_mixin_subject, domain=None, range=Union[dict, ChemicalEntityOrGeneOrGeneProduct])

slots.case_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="case to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.case_to_entity_association_mixin_subject, domain=None, range=Union[str, CaseId])

slots.chemical_to_chemical_association_object = Slot(uri=RDF.object, name="chemical to chemical association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.chemical_to_chemical_association_object, domain=ChemicalToChemicalAssociation, range=Union[str, ChemicalEntityId])

slots.reaction_to_participant_association_subject = Slot(uri=RDF.subject, name="reaction to participant association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.reaction_to_participant_association_subject, domain=ReactionToParticipantAssociation, range=Union[str, MolecularEntityId])

slots.reaction_to_catalyst_association_object = Slot(uri=RDF.object, name="reaction to catalyst association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.reaction_to_catalyst_association_object, domain=ReactionToCatalystAssociation, range=Union[dict, GeneOrGeneProduct])

slots.chemical_to_chemical_derivation_association_subject = Slot(uri=RDF.subject, name="chemical to chemical derivation association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.chemical_to_chemical_derivation_association_subject, domain=ChemicalToChemicalDerivationAssociation, range=Union[str, ChemicalEntityId])

slots.chemical_to_chemical_derivation_association_object = Slot(uri=RDF.object, name="chemical to chemical derivation association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.chemical_to_chemical_derivation_association_object, domain=ChemicalToChemicalDerivationAssociation, range=Union[str, ChemicalEntityId])

slots.chemical_to_chemical_derivation_association_predicate = Slot(uri=RDF.predicate, name="chemical to chemical derivation association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.chemical_to_chemical_derivation_association_predicate, domain=ChemicalToChemicalDerivationAssociation, range=Union[str, PredicateType])

slots.chemical_to_chemical_derivation_association_catalyst_qualifier = Slot(uri=BIOLINK.catalyst_qualifier, name="chemical to chemical derivation association_catalyst qualifier", curie=BIOLINK.curie('catalyst_qualifier'),
                   model_uri=BIOLINK.chemical_to_chemical_derivation_association_catalyst_qualifier, domain=ChemicalToChemicalDerivationAssociation, range=Optional[Union[Union[dict, MacromolecularMachineMixin], list[Union[dict, MacromolecularMachineMixin]]]])

slots.chemical_to_disease_or_phenotypic_feature_association_object = Slot(uri=RDF.object, name="chemical to disease or phenotypic feature association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.chemical_to_disease_or_phenotypic_feature_association_object, domain=ChemicalToDiseaseOrPhenotypicFeatureAssociation, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_predicate = Slot(uri=RDF.predicate, name="chemical or drug or treatment to disease or phenotypic feature association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_predicate, domain=ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation, range=Union[str, PredicateType])

slots.chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_predicate = Slot(uri=RDF.predicate, name="chemical or drug or treatment side effect disease or phenotypic feature association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_predicate, domain=ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation, range=Union[str, PredicateType])

slots.gene_to_pathway_association_subject = Slot(uri=RDF.subject, name="gene to pathway association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_pathway_association_subject, domain=GeneToPathwayAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_to_pathway_association_object = Slot(uri=RDF.object, name="gene to pathway association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_to_pathway_association_object, domain=GeneToPathwayAssociation, range=Union[str, PathwayId])

slots.molecular_activity_to_pathway_association_subject = Slot(uri=RDF.subject, name="molecular activity to pathway association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.molecular_activity_to_pathway_association_subject, domain=MolecularActivityToPathwayAssociation, range=Union[str, MolecularActivityId])

slots.molecular_activity_to_pathway_association_object = Slot(uri=RDF.object, name="molecular activity to pathway association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.molecular_activity_to_pathway_association_object, domain=MolecularActivityToPathwayAssociation, range=Union[str, PathwayId])

slots.molecular_activity_to_pathway_association_predicate = Slot(uri=RDF.predicate, name="molecular activity to pathway association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.molecular_activity_to_pathway_association_predicate, domain=MolecularActivityToPathwayAssociation, range=Union[str, PredicateType])

slots.chemical_to_pathway_association_subject = Slot(uri=RDF.subject, name="chemical to pathway association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.chemical_to_pathway_association_subject, domain=ChemicalToPathwayAssociation, range=Union[str, ChemicalEntityId])

slots.chemical_to_pathway_association_object = Slot(uri=RDF.object, name="chemical to pathway association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.chemical_to_pathway_association_object, domain=ChemicalToPathwayAssociation, range=Union[str, PathwayId])

slots.named_thing_associated_with_likelihood_of_named_thing_association_predicate = Slot(uri=RDF.predicate, name="named thing associated with likelihood of named thing association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.named_thing_associated_with_likelihood_of_named_thing_association_predicate, domain=NamedThingAssociatedWithLikelihoodOfNamedThingAssociation, range=Union[str, PredicateType])

slots.named_thing_associated_with_likelihood_of_named_thing_association_subject_aspect_qualifier = Slot(uri=BIOLINK.subject_aspect_qualifier, name="named thing associated with likelihood of named thing association_subject aspect qualifier", curie=BIOLINK.curie('subject_aspect_qualifier'),
                   model_uri=BIOLINK.named_thing_associated_with_likelihood_of_named_thing_association_subject_aspect_qualifier, domain=NamedThingAssociatedWithLikelihoodOfNamedThingAssociation, range=Optional[str])

slots.named_thing_associated_with_likelihood_of_named_thing_association_subject_context_qualifier = Slot(uri=BIOLINK.subject_context_qualifier, name="named thing associated with likelihood of named thing association_subject context qualifier", curie=BIOLINK.curie('subject_context_qualifier'),
                   model_uri=BIOLINK.named_thing_associated_with_likelihood_of_named_thing_association_subject_context_qualifier, domain=NamedThingAssociatedWithLikelihoodOfNamedThingAssociation, range=Optional[Union[str, OntologyClassId]])

slots.named_thing_associated_with_likelihood_of_named_thing_association_object_aspect_qualifier = Slot(uri=BIOLINK.object_aspect_qualifier, name="named thing associated with likelihood of named thing association_object aspect qualifier", curie=BIOLINK.curie('object_aspect_qualifier'),
                   model_uri=BIOLINK.named_thing_associated_with_likelihood_of_named_thing_association_object_aspect_qualifier, domain=NamedThingAssociatedWithLikelihoodOfNamedThingAssociation, range=Optional[str])

slots.named_thing_associated_with_likelihood_of_named_thing_association_object_context_qualifier = Slot(uri=BIOLINK.object_context_qualifier, name="named thing associated with likelihood of named thing association_object context qualifier", curie=BIOLINK.curie('object_context_qualifier'),
                   model_uri=BIOLINK.named_thing_associated_with_likelihood_of_named_thing_association_object_context_qualifier, domain=NamedThingAssociatedWithLikelihoodOfNamedThingAssociation, range=Optional[Union[str, OntologyClassId]])

slots.chemical_gene_interaction_association_subject = Slot(uri=RDF.subject, name="chemical gene interaction association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_subject, domain=ChemicalGeneInteractionAssociation, range=Union[str, ChemicalEntityId])

slots.chemical_gene_interaction_association_object = Slot(uri=RDF.object, name="chemical gene interaction association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_object, domain=ChemicalGeneInteractionAssociation, range=Union[dict, GeneOrGeneProduct])

slots.chemical_gene_interaction_association_predicate = Slot(uri=RDF.predicate, name="chemical gene interaction association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_predicate, domain=ChemicalGeneInteractionAssociation, range=Union[str, PredicateType])

slots.chemical_gene_interaction_association_subject_form_or_variant_qualifier = Slot(uri=BIOLINK.subject_form_or_variant_qualifier, name="chemical gene interaction association_subject form or variant qualifier", curie=BIOLINK.curie('subject_form_or_variant_qualifier'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_subject_form_or_variant_qualifier, domain=ChemicalGeneInteractionAssociation, range=Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]])

slots.chemical_gene_interaction_association_subject_part_qualifier = Slot(uri=BIOLINK.subject_part_qualifier, name="chemical gene interaction association_subject part qualifier", curie=BIOLINK.curie('subject_part_qualifier'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_subject_part_qualifier, domain=ChemicalGeneInteractionAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]])

slots.chemical_gene_interaction_association_subject_derivative_qualifier = Slot(uri=BIOLINK.subject_derivative_qualifier, name="chemical gene interaction association_subject derivative qualifier", curie=BIOLINK.curie('subject_derivative_qualifier'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_subject_derivative_qualifier, domain=ChemicalGeneInteractionAssociation, range=Optional[Union[str, "ChemicalEntityDerivativeEnum"]])

slots.chemical_gene_interaction_association_subject_context_qualifier = Slot(uri=BIOLINK.subject_context_qualifier, name="chemical gene interaction association_subject context qualifier", curie=BIOLINK.curie('subject_context_qualifier'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_subject_context_qualifier, domain=ChemicalGeneInteractionAssociation, range=Optional[Union[str, AnatomicalEntityId]])

slots.chemical_gene_interaction_association_object_form_or_variant_qualifier = Slot(uri=BIOLINK.object_form_or_variant_qualifier, name="chemical gene interaction association_object form or variant qualifier", curie=BIOLINK.curie('object_form_or_variant_qualifier'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_object_form_or_variant_qualifier, domain=ChemicalGeneInteractionAssociation, range=Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]])

slots.chemical_gene_interaction_association_object_part_qualifier = Slot(uri=BIOLINK.object_part_qualifier, name="chemical gene interaction association_object part qualifier", curie=BIOLINK.curie('object_part_qualifier'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_object_part_qualifier, domain=ChemicalGeneInteractionAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]])

slots.chemical_gene_interaction_association_object_context_qualifier = Slot(uri=BIOLINK.object_context_qualifier, name="chemical gene interaction association_object context qualifier", curie=BIOLINK.curie('object_context_qualifier'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_object_context_qualifier, domain=ChemicalGeneInteractionAssociation, range=Optional[Union[str, AnatomicalEntityId]])

slots.chemical_gene_interaction_association_anatomical_context_qualifier = Slot(uri=BIOLINK.anatomical_context_qualifier, name="chemical gene interaction association_anatomical context qualifier", curie=BIOLINK.curie('anatomical_context_qualifier'),
                   model_uri=BIOLINK.chemical_gene_interaction_association_anatomical_context_qualifier, domain=ChemicalGeneInteractionAssociation, range=Optional[Union[str, AnatomicalEntityId]])

slots.gene_regulates_gene_association_subject = Slot(uri=RDF.subject, name="gene regulates gene association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_regulates_gene_association_subject, domain=GeneRegulatesGeneAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_regulates_gene_association_predicate = Slot(uri=RDF.predicate, name="gene regulates gene association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.gene_regulates_gene_association_predicate, domain=GeneRegulatesGeneAssociation, range=Union[str, PredicateType])

slots.gene_regulates_gene_association_object = Slot(uri=RDF.object, name="gene regulates gene association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_regulates_gene_association_object, domain=GeneRegulatesGeneAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_regulates_gene_association_object_aspect_qualifier = Slot(uri=BIOLINK.object_aspect_qualifier, name="gene regulates gene association_object aspect qualifier", curie=BIOLINK.curie('object_aspect_qualifier'),
                   model_uri=BIOLINK.gene_regulates_gene_association_object_aspect_qualifier, domain=GeneRegulatesGeneAssociation, range=Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"])

slots.gene_regulates_gene_association_object_direction_qualifier = Slot(uri=BIOLINK.object_direction_qualifier, name="gene regulates gene association_object direction qualifier", curie=BIOLINK.curie('object_direction_qualifier'),
                   model_uri=BIOLINK.gene_regulates_gene_association_object_direction_qualifier, domain=GeneRegulatesGeneAssociation, range=Union[str, "DirectionQualifierEnum"])

slots.gene_regulates_gene_association_qualified_predicate = Slot(uri=BIOLINK.qualified_predicate, name="gene regulates gene association_qualified predicate", curie=BIOLINK.curie('qualified_predicate'),
                   model_uri=BIOLINK.gene_regulates_gene_association_qualified_predicate, domain=GeneRegulatesGeneAssociation, range=str)

slots.process_regulates_process_association_subject = Slot(uri=RDF.subject, name="process regulates process association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.process_regulates_process_association_subject, domain=ProcessRegulatesProcessAssociation, range=Union[str, BiologicalProcessId])

slots.process_regulates_process_association_predicate = Slot(uri=RDF.predicate, name="process regulates process association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.process_regulates_process_association_predicate, domain=ProcessRegulatesProcessAssociation, range=Union[str, PredicateType])

slots.process_regulates_process_association_object = Slot(uri=RDF.object, name="process regulates process association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.process_regulates_process_association_object, domain=ProcessRegulatesProcessAssociation, range=Union[str, BiologicalProcessId])

slots.chemical_affects_gene_association_subject = Slot(uri=RDF.subject, name="chemical affects gene association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.chemical_affects_gene_association_subject, domain=ChemicalAffectsGeneAssociation, range=Union[str, ChemicalEntityId])

slots.chemical_affects_gene_association_subject_form_or_variant_qualifier = Slot(uri=BIOLINK.subject_form_or_variant_qualifier, name="chemical affects gene association_subject form or variant qualifier", curie=BIOLINK.curie('subject_form_or_variant_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_subject_form_or_variant_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]])

slots.chemical_affects_gene_association_subject_part_qualifier = Slot(uri=BIOLINK.subject_part_qualifier, name="chemical affects gene association_subject part qualifier", curie=BIOLINK.curie('subject_part_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_subject_part_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]])

slots.chemical_affects_gene_association_subject_derivative_qualifier = Slot(uri=BIOLINK.subject_derivative_qualifier, name="chemical affects gene association_subject derivative qualifier", curie=BIOLINK.curie('subject_derivative_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_subject_derivative_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, "ChemicalEntityDerivativeEnum"]])

slots.chemical_affects_gene_association_subject_aspect_qualifier = Slot(uri=BIOLINK.subject_aspect_qualifier, name="chemical affects gene association_subject aspect qualifier", curie=BIOLINK.curie('subject_aspect_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_subject_aspect_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"]])

slots.chemical_affects_gene_association_subject_context_qualifier = Slot(uri=BIOLINK.subject_context_qualifier, name="chemical affects gene association_subject context qualifier", curie=BIOLINK.curie('subject_context_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_subject_context_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, AnatomicalEntityId]])

slots.chemical_affects_gene_association_subject_direction_qualifier = Slot(uri=BIOLINK.subject_direction_qualifier, name="chemical affects gene association_subject direction qualifier", curie=BIOLINK.curie('subject_direction_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_subject_direction_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, "DirectionQualifierEnum"]])

slots.chemical_affects_gene_association_predicate = Slot(uri=RDF.predicate, name="chemical affects gene association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.chemical_affects_gene_association_predicate, domain=ChemicalAffectsGeneAssociation, range=Union[str, PredicateType])

slots.chemical_affects_gene_association_qualified_predicate = Slot(uri=BIOLINK.qualified_predicate, name="chemical affects gene association_qualified predicate", curie=BIOLINK.curie('qualified_predicate'),
                   model_uri=BIOLINK.chemical_affects_gene_association_qualified_predicate, domain=ChemicalAffectsGeneAssociation, range=Optional[str])

slots.chemical_affects_gene_association_object = Slot(uri=RDF.object, name="chemical affects gene association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.chemical_affects_gene_association_object, domain=ChemicalAffectsGeneAssociation, range=Union[dict, GeneOrGeneProduct])

slots.chemical_affects_gene_association_object_form_or_variant_qualifier = Slot(uri=BIOLINK.object_form_or_variant_qualifier, name="chemical affects gene association_object form or variant qualifier", curie=BIOLINK.curie('object_form_or_variant_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_object_form_or_variant_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]])

slots.chemical_affects_gene_association_object_part_qualifier = Slot(uri=BIOLINK.object_part_qualifier, name="chemical affects gene association_object part qualifier", curie=BIOLINK.curie('object_part_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_object_part_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]])

slots.chemical_affects_gene_association_object_aspect_qualifier = Slot(uri=BIOLINK.object_aspect_qualifier, name="chemical affects gene association_object aspect qualifier", curie=BIOLINK.curie('object_aspect_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_object_aspect_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"]])

slots.chemical_affects_gene_association_object_context_qualifier = Slot(uri=BIOLINK.object_context_qualifier, name="chemical affects gene association_object context qualifier", curie=BIOLINK.curie('object_context_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_object_context_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, AnatomicalEntityId]])

slots.chemical_affects_gene_association_object_direction_qualifier = Slot(uri=BIOLINK.object_direction_qualifier, name="chemical affects gene association_object direction qualifier", curie=BIOLINK.curie('object_direction_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_object_direction_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, "DirectionQualifierEnum"]])

slots.chemical_affects_gene_association_causal_mechanism_qualifier = Slot(uri=BIOLINK.causal_mechanism_qualifier, name="chemical affects gene association_causal mechanism qualifier", curie=BIOLINK.curie('causal_mechanism_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_causal_mechanism_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, "CausalMechanismQualifierEnum"]])

slots.chemical_affects_gene_association_anatomical_context_qualifier = Slot(uri=BIOLINK.anatomical_context_qualifier, name="chemical affects gene association_anatomical context qualifier", curie=BIOLINK.curie('anatomical_context_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_anatomical_context_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, AnatomicalEntityId]])

slots.chemical_affects_gene_association_species_context_qualifier = Slot(uri=BIOLINK.species_context_qualifier, name="chemical affects gene association_species context qualifier", curie=BIOLINK.curie('species_context_qualifier'),
                   model_uri=BIOLINK.chemical_affects_gene_association_species_context_qualifier, domain=ChemicalAffectsGeneAssociation, range=Optional[Union[str, OrganismTaxonId]])

slots.gene_affects_chemical_association_subject = Slot(uri=RDF.subject, name="gene affects chemical association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_affects_chemical_association_subject, domain=GeneAffectsChemicalAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_affects_chemical_association_subject_form_or_variant_qualifier = Slot(uri=BIOLINK.subject_form_or_variant_qualifier, name="gene affects chemical association_subject form or variant qualifier", curie=BIOLINK.curie('subject_form_or_variant_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_subject_form_or_variant_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]])

slots.gene_affects_chemical_association_subject_part_qualifier = Slot(uri=BIOLINK.subject_part_qualifier, name="gene affects chemical association_subject part qualifier", curie=BIOLINK.curie('subject_part_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_subject_part_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]])

slots.gene_affects_chemical_association_subject_aspect_qualifier = Slot(uri=BIOLINK.subject_aspect_qualifier, name="gene affects chemical association_subject aspect qualifier", curie=BIOLINK.curie('subject_aspect_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_subject_aspect_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"]])

slots.gene_affects_chemical_association_subject_context_qualifier = Slot(uri=BIOLINK.subject_context_qualifier, name="gene affects chemical association_subject context qualifier", curie=BIOLINK.curie('subject_context_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_subject_context_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, AnatomicalEntityId]])

slots.gene_affects_chemical_association_subject_direction_qualifier = Slot(uri=BIOLINK.subject_direction_qualifier, name="gene affects chemical association_subject direction qualifier", curie=BIOLINK.curie('subject_direction_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_subject_direction_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, "DirectionQualifierEnum"]])

slots.gene_affects_chemical_association_predicate = Slot(uri=RDF.predicate, name="gene affects chemical association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.gene_affects_chemical_association_predicate, domain=GeneAffectsChemicalAssociation, range=Union[str, PredicateType])

slots.gene_affects_chemical_association_qualified_predicate = Slot(uri=BIOLINK.qualified_predicate, name="gene affects chemical association_qualified predicate", curie=BIOLINK.curie('qualified_predicate'),
                   model_uri=BIOLINK.gene_affects_chemical_association_qualified_predicate, domain=GeneAffectsChemicalAssociation, range=Optional[str])

slots.gene_affects_chemical_association_object = Slot(uri=RDF.object, name="gene affects chemical association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_affects_chemical_association_object, domain=GeneAffectsChemicalAssociation, range=Union[str, ChemicalEntityId])

slots.gene_affects_chemical_association_object_form_or_variant_qualifier = Slot(uri=BIOLINK.object_form_or_variant_qualifier, name="gene affects chemical association_object form or variant qualifier", curie=BIOLINK.curie('object_form_or_variant_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_object_form_or_variant_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, "ChemicalOrGeneOrGeneProductFormOrVariantEnum"]])

slots.gene_affects_chemical_association_object_part_qualifier = Slot(uri=BIOLINK.object_part_qualifier, name="gene affects chemical association_object part qualifier", curie=BIOLINK.curie('object_part_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_object_part_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalPartQualifierEnum"]])

slots.gene_affects_chemical_association_object_derivative_qualifier = Slot(uri=BIOLINK.object_derivative_qualifier, name="gene affects chemical association_object derivative qualifier", curie=BIOLINK.curie('object_derivative_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_object_derivative_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, "ChemicalEntityDerivativeEnum"]])

slots.gene_affects_chemical_association_object_aspect_qualifier = Slot(uri=BIOLINK.object_aspect_qualifier, name="gene affects chemical association_object aspect qualifier", curie=BIOLINK.curie('object_aspect_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_object_aspect_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"]])

slots.gene_affects_chemical_association_object_context_qualifier = Slot(uri=BIOLINK.object_context_qualifier, name="gene affects chemical association_object context qualifier", curie=BIOLINK.curie('object_context_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_object_context_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, AnatomicalEntityId]])

slots.gene_affects_chemical_association_object_direction_qualifier = Slot(uri=BIOLINK.object_direction_qualifier, name="gene affects chemical association_object direction qualifier", curie=BIOLINK.curie('object_direction_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_object_direction_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, "DirectionQualifierEnum"]])

slots.gene_affects_chemical_association_causal_mechanism_qualifier = Slot(uri=BIOLINK.causal_mechanism_qualifier, name="gene affects chemical association_causal mechanism qualifier", curie=BIOLINK.curie('causal_mechanism_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_causal_mechanism_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, "CausalMechanismQualifierEnum"]])

slots.gene_affects_chemical_association_anatomical_context_qualifier = Slot(uri=BIOLINK.anatomical_context_qualifier, name="gene affects chemical association_anatomical context qualifier", curie=BIOLINK.curie('anatomical_context_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_anatomical_context_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, AnatomicalEntityId]])

slots.gene_affects_chemical_association_species_context_qualifier = Slot(uri=BIOLINK.species_context_qualifier, name="gene affects chemical association_species context qualifier", curie=BIOLINK.curie('species_context_qualifier'),
                   model_uri=BIOLINK.gene_affects_chemical_association_species_context_qualifier, domain=GeneAffectsChemicalAssociation, range=Optional[Union[str, OrganismTaxonId]])

slots.drug_to_gene_association_object = Slot(uri=RDF.object, name="drug to gene association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.drug_to_gene_association_object, domain=DrugToGeneAssociation, range=Union[dict, GeneOrGeneProduct])

slots.material_sample_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="material sample to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.material_sample_to_entity_association_mixin_subject, domain=None, range=Union[str, MaterialSampleId])

slots.material_sample_derivation_association_subject = Slot(uri=RDF.subject, name="material sample derivation association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.material_sample_derivation_association_subject, domain=MaterialSampleDerivationAssociation, range=Union[str, MaterialSampleId])

slots.material_sample_derivation_association_object = Slot(uri=RDF.object, name="material sample derivation association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.material_sample_derivation_association_object, domain=MaterialSampleDerivationAssociation, range=Union[str, NamedThingId])

slots.material_sample_derivation_association_predicate = Slot(uri=RDF.predicate, name="material sample derivation association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.material_sample_derivation_association_predicate, domain=MaterialSampleDerivationAssociation, range=Union[str, PredicateType])

slots.disease_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="disease to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.disease_to_entity_association_mixin_subject, domain=None, range=Union[str, DiseaseId])

slots.entity_to_exposure_event_association_mixin_object = Slot(uri=RDF.object, name="entity to exposure event association mixin_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.entity_to_exposure_event_association_mixin_object, domain=None, range=Union[str, ExposureEventId])

slots.entity_to_outcome_association_mixin_object = Slot(uri=RDF.object, name="entity to outcome association mixin_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.entity_to_outcome_association_mixin_object, domain=None, range=Union[dict, Outcome])

slots.entity_to_phenotypic_feature_association_mixin_object = Slot(uri=RDF.object, name="entity to phenotypic feature association mixin_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.entity_to_phenotypic_feature_association_mixin_object, domain=None, range=Union[str, PhenotypicFeatureId])

slots.phenotypic_feature_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="phenotypic feature to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.phenotypic_feature_to_entity_association_mixin_subject, domain=None, range=Union[str, PhenotypicFeatureId])

slots.information_content_entity_to_named_thing_association_subject = Slot(uri=RDF.subject, name="information content entity to named thing association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.information_content_entity_to_named_thing_association_subject, domain=InformationContentEntityToNamedThingAssociation, range=Union[str, NamedThingId])

slots.information_content_entity_to_named_thing_association_object = Slot(uri=RDF.object, name="information content entity to named thing association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.information_content_entity_to_named_thing_association_object, domain=InformationContentEntityToNamedThingAssociation, range=Union[str, NamedThingId])

slots.information_content_entity_to_named_thing_association_predicate = Slot(uri=RDF.predicate, name="information content entity to named thing association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.information_content_entity_to_named_thing_association_predicate, domain=InformationContentEntityToNamedThingAssociation, range=Union[str, PredicateType])

slots.entity_to_disease_association_mixin_object = Slot(uri=RDF.object, name="entity to disease association mixin_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.entity_to_disease_association_mixin_object, domain=None, range=Union[str, DiseaseId])

slots.disease_or_phenotypic_feature_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="disease or phenotypic feature to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.disease_or_phenotypic_feature_to_entity_association_mixin_subject, domain=None, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.disease_or_phenotypic_feature_to_location_association_object = Slot(uri=RDF.object, name="disease or phenotypic feature to location association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.disease_or_phenotypic_feature_to_location_association_object, domain=DiseaseOrPhenotypicFeatureToLocationAssociation, range=Union[str, AnatomicalEntityId])

slots.disease_or_phenotypic_feature_to_genetic_inheritance_association_predicate = Slot(uri=RDF.predicate, name="disease or phenotypic feature to genetic inheritance association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.disease_or_phenotypic_feature_to_genetic_inheritance_association_predicate, domain=DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation, range=Union[str, PredicateType])

slots.disease_or_phenotypic_feature_to_genetic_inheritance_association_object = Slot(uri=RDF.object, name="disease or phenotypic feature to genetic inheritance association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.disease_or_phenotypic_feature_to_genetic_inheritance_association_object, domain=DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation, range=Union[str, GeneticInheritanceId])

slots.entity_to_disease_or_phenotypic_feature_association_mixin_object = Slot(uri=RDF.object, name="entity to disease or phenotypic feature association mixin_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.entity_to_disease_or_phenotypic_feature_association_mixin_object, domain=None, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.genotype_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="genotype to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.genotype_to_entity_association_mixin_subject, domain=None, range=Union[str, GenotypeId])

slots.genotype_to_phenotypic_feature_association_predicate = Slot(uri=RDF.predicate, name="genotype to phenotypic feature association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.genotype_to_phenotypic_feature_association_predicate, domain=GenotypeToPhenotypicFeatureAssociation, range=Union[str, PredicateType])

slots.genotype_to_phenotypic_feature_association_subject = Slot(uri=RDF.subject, name="genotype to phenotypic feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.genotype_to_phenotypic_feature_association_subject, domain=GenotypeToPhenotypicFeatureAssociation, range=Union[str, GenotypeId])

slots.exposure_event_to_phenotypic_feature_association_subject = Slot(uri=RDF.subject, name="exposure event to phenotypic feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.exposure_event_to_phenotypic_feature_association_subject, domain=ExposureEventToPhenotypicFeatureAssociation, range=Union[str, ExposureEventId])

slots.disease_to_phenotypic_feature_association_subject = Slot(uri=RDF.subject, name="disease to phenotypic feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.disease_to_phenotypic_feature_association_subject, domain=DiseaseToPhenotypicFeatureAssociation, range=Union[str, DiseaseId])

slots.disease_to_phenotypic_feature_association_object = Slot(uri=RDF.object, name="disease to phenotypic feature association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.disease_to_phenotypic_feature_association_object, domain=DiseaseToPhenotypicFeatureAssociation, range=Union[str, PhenotypicFeatureId])

slots.case_to_disease_association_object = Slot(uri=RDF.object, name="case to disease association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.case_to_disease_association_object, domain=CaseToDiseaseAssociation, range=Union[str, DiseaseId])

slots.case_to_variant_association_object = Slot(uri=RDF.object, name="case to variant association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.case_to_variant_association_object, domain=CaseToVariantAssociation, range=Union[str, SequenceVariantId])

slots.case_to_variant_association_has_zygosity = Slot(uri=BIOLINK.has_zygosity, name="case to variant association_has zygosity", curie=BIOLINK.curie('has_zygosity'),
                   model_uri=BIOLINK.case_to_variant_association_has_zygosity, domain=CaseToVariantAssociation, range=Optional[Union[str, ZygosityId]])

slots.case_to_gene_association_object = Slot(uri=RDF.object, name="case to gene association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.case_to_gene_association_object, domain=CaseToGeneAssociation, range=Union[dict, GeneOrGeneProduct])

slots.behavior_to_behavioral_feature_association_subject = Slot(uri=RDF.subject, name="behavior to behavioral feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.behavior_to_behavioral_feature_association_subject, domain=BehaviorToBehavioralFeatureAssociation, range=Union[str, BehaviorId])

slots.behavior_to_behavioral_feature_association_object = Slot(uri=RDF.object, name="behavior to behavioral feature association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.behavior_to_behavioral_feature_association_object, domain=BehaviorToBehavioralFeatureAssociation, range=Union[str, BehavioralFeatureId])

slots.gene_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="gene to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_entity_association_mixin_subject, domain=None, range=Union[dict, GeneOrGeneProduct])

slots.variant_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="variant to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.variant_to_entity_association_mixin_subject, domain=None, range=Union[str, SequenceVariantId])

slots.gene_to_disease_or_phenotypic_feature_association_subject = Slot(uri=RDF.subject, name="gene to disease or phenotypic feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_disease_or_phenotypic_feature_association_subject, domain=GeneToDiseaseOrPhenotypicFeatureAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_to_disease_or_phenotypic_feature_association_subject_aspect_qualifier = Slot(uri=BIOLINK.subject_aspect_qualifier, name="gene to disease or phenotypic feature association_subject aspect qualifier", curie=BIOLINK.curie('subject_aspect_qualifier'),
                   model_uri=BIOLINK.gene_to_disease_or_phenotypic_feature_association_subject_aspect_qualifier, domain=GeneToDiseaseOrPhenotypicFeatureAssociation, range=Optional[Union[str, "GeneOrGeneProductOrChemicalEntityAspectEnum"]])

slots.gene_to_disease_or_phenotypic_feature_association_object = Slot(uri=RDF.object, name="gene to disease or phenotypic feature association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_to_disease_or_phenotypic_feature_association_object, domain=GeneToDiseaseOrPhenotypicFeatureAssociation, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.gene_to_disease_or_phenotypic_feature_association_object_direction_qualifier = Slot(uri=BIOLINK.object_direction_qualifier, name="gene to disease or phenotypic feature association_object direction qualifier", curie=BIOLINK.curie('object_direction_qualifier'),
                   model_uri=BIOLINK.gene_to_disease_or_phenotypic_feature_association_object_direction_qualifier, domain=GeneToDiseaseOrPhenotypicFeatureAssociation, range=Optional[Union[str, "DirectionQualifierEnum"]])

slots.gene_to_disease_or_phenotypic_feature_association_predicate = Slot(uri=RDF.predicate, name="gene to disease or phenotypic feature association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.gene_to_disease_or_phenotypic_feature_association_predicate, domain=GeneToDiseaseOrPhenotypicFeatureAssociation, range=Union[str, PredicateType])

slots.gene_to_phenotypic_feature_association_subject = Slot(uri=RDF.subject, name="gene to phenotypic feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_phenotypic_feature_association_subject, domain=GeneToPhenotypicFeatureAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_to_phenotypic_feature_association_object = Slot(uri=RDF.object, name="gene to phenotypic feature association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_to_phenotypic_feature_association_object, domain=GeneToPhenotypicFeatureAssociation, range=Union[str, PhenotypicFeatureId])

slots.gene_to_disease_association_subject = Slot(uri=RDF.subject, name="gene to disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_disease_association_subject, domain=GeneToDiseaseAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_to_disease_association_object = Slot(uri=RDF.object, name="gene to disease association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_to_disease_association_object, domain=GeneToDiseaseAssociation, range=Union[str, DiseaseId])

slots.causal_gene_to_disease_association_subject = Slot(uri=RDF.subject, name="causal gene to disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.causal_gene_to_disease_association_subject, domain=CausalGeneToDiseaseAssociation, range=Union[dict, GeneOrGeneProduct])

slots.causal_gene_to_disease_association_object = Slot(uri=RDF.object, name="causal gene to disease association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.causal_gene_to_disease_association_object, domain=CausalGeneToDiseaseAssociation, range=Union[str, DiseaseId])

slots.correlated_gene_to_disease_association_subject = Slot(uri=RDF.subject, name="correlated gene to disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.correlated_gene_to_disease_association_subject, domain=CorrelatedGeneToDiseaseAssociation, range=Union[dict, GeneOrGeneProduct])

slots.correlated_gene_to_disease_association_object = Slot(uri=RDF.object, name="correlated gene to disease association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.correlated_gene_to_disease_association_object, domain=CorrelatedGeneToDiseaseAssociation, range=Union[str, DiseaseId])

slots.druggable_gene_to_disease_association_subject = Slot(uri=RDF.subject, name="druggable gene to disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.druggable_gene_to_disease_association_subject, domain=DruggableGeneToDiseaseAssociation, range=Union[dict, GeneOrGeneProduct])

slots.druggable_gene_to_disease_association_predicate = Slot(uri=RDF.predicate, name="druggable gene to disease association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.druggable_gene_to_disease_association_predicate, domain=DruggableGeneToDiseaseAssociation, range=Union[str, PredicateType])

slots.druggable_gene_to_disease_association_has_evidence = Slot(uri=BIOLINK.has_evidence, name="druggable gene to disease association_has evidence", curie=BIOLINK.curie('has_evidence'),
                   model_uri=BIOLINK.druggable_gene_to_disease_association_has_evidence, domain=DruggableGeneToDiseaseAssociation, range=Optional[Union[Union[str, "DruggableGeneCategoryEnum"], list[Union[str, "DruggableGeneCategoryEnum"]]]])

slots.phenotypic_feature_to_disease_association_predicate = Slot(uri=RDF.predicate, name="phenotypic feature to disease association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.phenotypic_feature_to_disease_association_predicate, domain=PhenotypicFeatureToDiseaseAssociation, range=Union[str, PredicateType])

slots.variant_to_gene_association_object = Slot(uri=RDF.object, name="variant to gene association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.variant_to_gene_association_object, domain=VariantToGeneAssociation, range=Union[str, GeneId])

slots.variant_to_gene_association_predicate = Slot(uri=RDF.predicate, name="variant to gene association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.variant_to_gene_association_predicate, domain=VariantToGeneAssociation, range=Union[str, PredicateType])

slots.variant_to_gene_expression_association_predicate = Slot(uri=RDF.predicate, name="variant to gene expression association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.variant_to_gene_expression_association_predicate, domain=VariantToGeneExpressionAssociation, range=Union[str, PredicateType])

slots.variant_to_population_association_subject = Slot(uri=RDF.subject, name="variant to population association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.variant_to_population_association_subject, domain=VariantToPopulationAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_population_association_object = Slot(uri=RDF.object, name="variant to population association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.variant_to_population_association_object, domain=VariantToPopulationAssociation, range=Union[str, PopulationOfIndividualOrganismsId])

slots.variant_to_population_association_has_quotient = Slot(uri=BIOLINK.has_quotient, name="variant to population association_has quotient", curie=BIOLINK.curie('has_quotient'),
                   model_uri=BIOLINK.variant_to_population_association_has_quotient, domain=VariantToPopulationAssociation, range=Optional[float])

slots.variant_to_population_association_has_count = Slot(uri=BIOLINK.has_count, name="variant to population association_has count", curie=BIOLINK.curie('has_count'),
                   model_uri=BIOLINK.variant_to_population_association_has_count, domain=VariantToPopulationAssociation, range=Optional[int])

slots.variant_to_population_association_has_total = Slot(uri=BIOLINK.has_total, name="variant to population association_has total", curie=BIOLINK.curie('has_total'),
                   model_uri=BIOLINK.variant_to_population_association_has_total, domain=VariantToPopulationAssociation, range=Optional[int])

slots.population_to_population_association_subject = Slot(uri=RDF.subject, name="population to population association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.population_to_population_association_subject, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualOrganismsId])

slots.population_to_population_association_object = Slot(uri=RDF.object, name="population to population association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.population_to_population_association_object, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualOrganismsId])

slots.population_to_population_association_predicate = Slot(uri=RDF.predicate, name="population to population association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.population_to_population_association_predicate, domain=PopulationToPopulationAssociation, range=Union[str, PredicateType])

slots.variant_to_phenotypic_feature_association_subject = Slot(uri=RDF.subject, name="variant to phenotypic feature association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.variant_to_phenotypic_feature_association_subject, domain=VariantToPhenotypicFeatureAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_disease_association_subject = Slot(uri=RDF.subject, name="variant to disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.variant_to_disease_association_subject, domain=VariantToDiseaseAssociation, range=Union[str, NamedThingId])

slots.variant_to_disease_association_predicate = Slot(uri=RDF.predicate, name="variant to disease association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.variant_to_disease_association_predicate, domain=VariantToDiseaseAssociation, range=Union[str, PredicateType])

slots.variant_to_disease_association_object = Slot(uri=RDF.object, name="variant to disease association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.variant_to_disease_association_object, domain=VariantToDiseaseAssociation, range=Union[str, NamedThingId])

slots.genotype_to_disease_association_subject = Slot(uri=RDF.subject, name="genotype to disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.genotype_to_disease_association_subject, domain=GenotypeToDiseaseAssociation, range=Union[str, NamedThingId])

slots.genotype_to_disease_association_predicate = Slot(uri=RDF.predicate, name="genotype to disease association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.genotype_to_disease_association_predicate, domain=GenotypeToDiseaseAssociation, range=Union[str, PredicateType])

slots.genotype_to_disease_association_object = Slot(uri=RDF.object, name="genotype to disease association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.genotype_to_disease_association_object, domain=GenotypeToDiseaseAssociation, range=Union[str, NamedThingId])

slots.model_to_disease_association_mixin_subject = Slot(uri=RDF.subject, name="model to disease association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.model_to_disease_association_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.model_to_disease_association_mixin_predicate = Slot(uri=RDF.predicate, name="model to disease association mixin_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.model_to_disease_association_mixin_predicate, domain=None, range=Union[str, PredicateType])

slots.gene_as_a_model_of_disease_association_subject = Slot(uri=RDF.subject, name="gene as a model of disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_as_a_model_of_disease_association_subject, domain=GeneAsAModelOfDiseaseAssociation, range=Union[dict, GeneOrGeneProduct])

slots.variant_as_a_model_of_disease_association_subject = Slot(uri=RDF.subject, name="variant as a model of disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.variant_as_a_model_of_disease_association_subject, domain=VariantAsAModelOfDiseaseAssociation, range=Union[str, SequenceVariantId])

slots.genotype_as_a_model_of_disease_association_subject = Slot(uri=RDF.subject, name="genotype as a model of disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.genotype_as_a_model_of_disease_association_subject, domain=GenotypeAsAModelOfDiseaseAssociation, range=Union[str, GenotypeId])

slots.cell_line_as_a_model_of_disease_association_subject = Slot(uri=RDF.subject, name="cell line as a model of disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.cell_line_as_a_model_of_disease_association_subject, domain=CellLineAsAModelOfDiseaseAssociation, range=Union[str, CellLineId])

slots.organismal_entity_as_a_model_of_disease_association_subject = Slot(uri=RDF.subject, name="organismal entity as a model of disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.organismal_entity_as_a_model_of_disease_association_subject, domain=OrganismalEntityAsAModelOfDiseaseAssociation, range=Union[str, OrganismalEntityId])

slots.organism_to_organism_association_subject = Slot(uri=RDF.subject, name="organism to organism association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.organism_to_organism_association_subject, domain=OrganismToOrganismAssociation, range=Union[str, IndividualOrganismId])

slots.organism_to_organism_association_object = Slot(uri=RDF.object, name="organism to organism association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.organism_to_organism_association_object, domain=OrganismToOrganismAssociation, range=Union[str, IndividualOrganismId])

slots.taxon_to_taxon_association_subject = Slot(uri=RDF.subject, name="taxon to taxon association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.taxon_to_taxon_association_subject, domain=TaxonToTaxonAssociation, range=Union[str, OrganismTaxonId])

slots.taxon_to_taxon_association_object = Slot(uri=RDF.object, name="taxon to taxon association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.taxon_to_taxon_association_object, domain=TaxonToTaxonAssociation, range=Union[str, OrganismTaxonId])

slots.gene_has_variant_that_contributes_to_disease_association_subject = Slot(uri=RDF.subject, name="gene has variant that contributes to disease association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_has_variant_that_contributes_to_disease_association_subject, domain=GeneHasVariantThatContributesToDiseaseAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_has_variant_that_contributes_to_disease_association_object = Slot(uri=RDF.object, name="gene has variant that contributes to disease association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_has_variant_that_contributes_to_disease_association_object, domain=GeneHasVariantThatContributesToDiseaseAssociation, range=Union[str, DiseaseId])

slots.gene_has_variant_that_contributes_to_disease_association_predicate = Slot(uri=RDF.predicate, name="gene has variant that contributes to disease association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.gene_has_variant_that_contributes_to_disease_association_predicate, domain=GeneHasVariantThatContributesToDiseaseAssociation, range=Union[str, PredicateType])

slots.gene_to_expression_site_association_subject = Slot(uri=RDF.subject, name="gene to expression site association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_expression_site_association_subject, domain=GeneToExpressionSiteAssociation, range=Union[dict, GeneOrGeneProduct])

slots.gene_to_expression_site_association_object = Slot(uri=RDF.object, name="gene to expression site association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_to_expression_site_association_object, domain=GeneToExpressionSiteAssociation, range=Union[str, AnatomicalEntityId])

slots.gene_to_expression_site_association_predicate = Slot(uri=RDF.predicate, name="gene to expression site association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.gene_to_expression_site_association_predicate, domain=GeneToExpressionSiteAssociation, range=Union[str, PredicateType])

slots.gene_to_expression_site_association_stage_qualifier = Slot(uri=BIOLINK.stage_qualifier, name="gene to expression site association_stage qualifier", curie=BIOLINK.curie('stage_qualifier'),
                   model_uri=BIOLINK.gene_to_expression_site_association_stage_qualifier, domain=GeneToExpressionSiteAssociation, range=Optional[Union[str, LifeStageId]])

slots.gene_to_expression_site_association_quantifier_qualifier = Slot(uri=BIOLINK.quantifier_qualifier, name="gene to expression site association_quantifier qualifier", curie=BIOLINK.curie('quantifier_qualifier'),
                   model_uri=BIOLINK.gene_to_expression_site_association_quantifier_qualifier, domain=GeneToExpressionSiteAssociation, range=Optional[Union[str, OntologyClassId]])

slots.sequence_variant_modulates_treatment_association_subject = Slot(uri=RDF.subject, name="sequence variant modulates treatment association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.sequence_variant_modulates_treatment_association_subject, domain=SequenceVariantModulatesTreatmentAssociation, range=Union[str, SequenceVariantId])

slots.sequence_variant_modulates_treatment_association_object = Slot(uri=RDF.object, name="sequence variant modulates treatment association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.sequence_variant_modulates_treatment_association_object, domain=SequenceVariantModulatesTreatmentAssociation, range=Union[str, TreatmentId])

slots.functional_association_subject = Slot(uri=RDF.subject, name="functional association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.functional_association_subject, domain=FunctionalAssociation, range=Union[dict, MacromolecularMachineMixin])

slots.functional_association_object = Slot(uri=RDF.object, name="functional association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.functional_association_object, domain=FunctionalAssociation, range=Union[str, OntologyClassId])

slots.macromolecular_machine_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="macromolecular machine to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.macromolecular_machine_to_entity_association_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.macromolecular_machine_to_molecular_activity_association_object = Slot(uri=RDF.object, name="macromolecular machine to molecular activity association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.macromolecular_machine_to_molecular_activity_association_object, domain=MacromolecularMachineToMolecularActivityAssociation, range=Union[str, MolecularActivityId])

slots.macromolecular_machine_to_biological_process_association_object = Slot(uri=RDF.object, name="macromolecular machine to biological process association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.macromolecular_machine_to_biological_process_association_object, domain=MacromolecularMachineToBiologicalProcessAssociation, range=Union[str, BiologicalProcessId])

slots.macromolecular_machine_to_cellular_component_association_object = Slot(uri=RDF.object, name="macromolecular machine to cellular component association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.macromolecular_machine_to_cellular_component_association_object, domain=MacromolecularMachineToCellularComponentAssociation, range=Union[str, CellularComponentId])

slots.molecular_activity_to_chemical_entity_association_subject = Slot(uri=RDF.subject, name="molecular activity to chemical entity association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.molecular_activity_to_chemical_entity_association_subject, domain=MolecularActivityToChemicalEntityAssociation, range=Union[str, MolecularActivityId])

slots.molecular_activity_to_chemical_entity_association_object = Slot(uri=RDF.object, name="molecular activity to chemical entity association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.molecular_activity_to_chemical_entity_association_object, domain=MolecularActivityToChemicalEntityAssociation, range=Union[str, ChemicalEntityId])

slots.molecular_activity_to_molecular_activity_association_subject = Slot(uri=RDF.subject, name="molecular activity to molecular activity association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.molecular_activity_to_molecular_activity_association_subject, domain=MolecularActivityToMolecularActivityAssociation, range=Union[str, MolecularActivityId])

slots.molecular_activity_to_molecular_activity_association_object = Slot(uri=RDF.object, name="molecular activity to molecular activity association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.molecular_activity_to_molecular_activity_association_object, domain=MolecularActivityToMolecularActivityAssociation, range=Union[str, MolecularActivityId])

slots.gene_to_go_term_association_subject = Slot(uri=RDF.subject, name="gene to go term association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_go_term_association_subject, domain=GeneToGoTermAssociation, range=Union[str, GeneId])

slots.gene_to_go_term_association_object = Slot(uri=RDF.object, name="gene to go term association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_to_go_term_association_object, domain=GeneToGoTermAssociation, range=Union[str, OntologyClassId])

slots.genomic_sequence_localization_subject = Slot(uri=RDF.subject, name="genomic sequence localization_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.genomic_sequence_localization_subject, domain=GenomicSequenceLocalization, range=Union[str, NucleicAcidEntityId])

slots.genomic_sequence_localization_object = Slot(uri=RDF.object, name="genomic sequence localization_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.genomic_sequence_localization_object, domain=GenomicSequenceLocalization, range=Union[str, NucleicAcidEntityId])

slots.genomic_sequence_localization_predicate = Slot(uri=RDF.predicate, name="genomic sequence localization_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.genomic_sequence_localization_predicate, domain=GenomicSequenceLocalization, range=Union[str, PredicateType])

slots.sequence_feature_relationship_subject = Slot(uri=RDF.subject, name="sequence feature relationship_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.sequence_feature_relationship_subject, domain=SequenceFeatureRelationship, range=Union[str, NucleicAcidEntityId])

slots.sequence_feature_relationship_object = Slot(uri=RDF.object, name="sequence feature relationship_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.sequence_feature_relationship_object, domain=SequenceFeatureRelationship, range=Union[str, NucleicAcidEntityId])

slots.transcript_to_gene_relationship_subject = Slot(uri=RDF.subject, name="transcript to gene relationship_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.transcript_to_gene_relationship_subject, domain=TranscriptToGeneRelationship, range=Union[str, TranscriptId])

slots.transcript_to_gene_relationship_object = Slot(uri=RDF.object, name="transcript to gene relationship_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.transcript_to_gene_relationship_object, domain=TranscriptToGeneRelationship, range=Union[str, GeneId])

slots.gene_to_gene_product_relationship_subject = Slot(uri=RDF.subject, name="gene to gene product relationship_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.gene_to_gene_product_relationship_subject, domain=GeneToGeneProductRelationship, range=Union[str, GeneId])

slots.gene_to_gene_product_relationship_object = Slot(uri=RDF.object, name="gene to gene product relationship_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.gene_to_gene_product_relationship_object, domain=GeneToGeneProductRelationship, range=Union[dict, GeneProductMixin])

slots.gene_to_gene_product_relationship_predicate = Slot(uri=RDF.predicate, name="gene to gene product relationship_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.gene_to_gene_product_relationship_predicate, domain=GeneToGeneProductRelationship, range=Union[str, PredicateType])

slots.exon_to_transcript_relationship_subject = Slot(uri=RDF.subject, name="exon to transcript relationship_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.exon_to_transcript_relationship_subject, domain=ExonToTranscriptRelationship, range=Union[str, ExonId])

slots.exon_to_transcript_relationship_object = Slot(uri=RDF.object, name="exon to transcript relationship_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.exon_to_transcript_relationship_object, domain=ExonToTranscriptRelationship, range=Union[str, TranscriptId])

slots.chemical_entity_or_gene_or_gene_product_regulates_gene_association_predicate = Slot(uri=RDF.predicate, name="chemical entity or gene or gene product regulates gene association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.chemical_entity_or_gene_or_gene_product_regulates_gene_association_predicate, domain=ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation, range=Union[str, PredicateType])

slots.chemical_entity_or_gene_or_gene_product_regulates_gene_association_subject = Slot(uri=RDF.subject, name="chemical entity or gene or gene product regulates gene association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.chemical_entity_or_gene_or_gene_product_regulates_gene_association_subject, domain=ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation, range=Union[dict, ChemicalEntityOrGeneOrGeneProduct])

slots.chemical_entity_or_gene_or_gene_product_regulates_gene_association_object = Slot(uri=RDF.object, name="chemical entity or gene or gene product regulates gene association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.chemical_entity_or_gene_or_gene_product_regulates_gene_association_object, domain=ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation, range=Union[dict, GeneOrGeneProduct])

slots.chemical_entity_or_gene_or_gene_product_regulates_gene_association_object_direction_qualifier = Slot(uri=BIOLINK.object_direction_qualifier, name="chemical entity or gene or gene product regulates gene association_object direction qualifier", curie=BIOLINK.curie('object_direction_qualifier'),
                   model_uri=BIOLINK.chemical_entity_or_gene_or_gene_product_regulates_gene_association_object_direction_qualifier, domain=ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation, range=Optional[Union[str, "DirectionQualifierEnum"]])

slots.anatomical_entity_to_anatomical_entity_association_subject = Slot(uri=RDF.subject, name="anatomical entity to anatomical entity association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_association_subject, domain=AnatomicalEntityToAnatomicalEntityAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_association_object = Slot(uri=RDF.object, name="anatomical entity to anatomical entity association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_association_object, domain=AnatomicalEntityToAnatomicalEntityAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_subject = Slot(uri=RDF.subject, name="anatomical entity to anatomical entity part of association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_part_of_association_subject, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_object = Slot(uri=RDF.object, name="anatomical entity to anatomical entity part of association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_part_of_association_object, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_predicate = Slot(uri=RDF.predicate, name="anatomical entity to anatomical entity part of association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_part_of_association_predicate, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[str, PredicateType])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_subject = Slot(uri=RDF.subject, name="anatomical entity to anatomical entity ontogenic association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_subject, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_object = Slot(uri=RDF.object, name="anatomical entity to anatomical entity ontogenic association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_object, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_predicate = Slot(uri=RDF.predicate, name="anatomical entity to anatomical entity ontogenic association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_predicate, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[str, PredicateType])

slots.organism_taxon_to_entity_association_subject = Slot(uri=RDF.subject, name="organism taxon to entity association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.organism_taxon_to_entity_association_subject, domain=None, range=Union[str, OrganismTaxonId])

slots.organism_taxon_to_organism_taxon_association_subject = Slot(uri=RDF.subject, name="organism taxon to organism taxon association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.organism_taxon_to_organism_taxon_association_subject, domain=OrganismTaxonToOrganismTaxonAssociation, range=Union[str, OrganismTaxonId])

slots.organism_taxon_to_organism_taxon_association_object = Slot(uri=RDF.object, name="organism taxon to organism taxon association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.organism_taxon_to_organism_taxon_association_object, domain=OrganismTaxonToOrganismTaxonAssociation, range=Union[str, OrganismTaxonId])

slots.organism_taxon_to_organism_taxon_specialization_subject = Slot(uri=RDF.subject, name="organism taxon to organism taxon specialization_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.organism_taxon_to_organism_taxon_specialization_subject, domain=OrganismTaxonToOrganismTaxonSpecialization, range=Union[str, OrganismTaxonId])

slots.organism_taxon_to_organism_taxon_specialization_object = Slot(uri=RDF.object, name="organism taxon to organism taxon specialization_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.organism_taxon_to_organism_taxon_specialization_object, domain=OrganismTaxonToOrganismTaxonSpecialization, range=Union[str, OrganismTaxonId])

slots.organism_taxon_to_organism_taxon_specialization_predicate = Slot(uri=RDF.predicate, name="organism taxon to organism taxon specialization_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.organism_taxon_to_organism_taxon_specialization_predicate, domain=OrganismTaxonToOrganismTaxonSpecialization, range=Union[str, PredicateType])

slots.organism_taxon_to_organism_taxon_interaction_subject = Slot(uri=RDF.subject, name="organism taxon to organism taxon interaction_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.organism_taxon_to_organism_taxon_interaction_subject, domain=OrganismTaxonToOrganismTaxonInteraction, range=Union[str, OrganismTaxonId])

slots.organism_taxon_to_organism_taxon_interaction_object = Slot(uri=RDF.object, name="organism taxon to organism taxon interaction_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.organism_taxon_to_organism_taxon_interaction_object, domain=OrganismTaxonToOrganismTaxonInteraction, range=Union[str, OrganismTaxonId])

slots.organism_taxon_to_organism_taxon_interaction_predicate = Slot(uri=RDF.predicate, name="organism taxon to organism taxon interaction_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.organism_taxon_to_organism_taxon_interaction_predicate, domain=OrganismTaxonToOrganismTaxonInteraction, range=Union[str, PredicateType])

slots.organism_taxon_to_organism_taxon_interaction_associated_environmental_context = Slot(uri=BIOLINK.associated_environmental_context, name="organism taxon to organism taxon interaction_associated environmental context", curie=BIOLINK.curie('associated_environmental_context'),
                   model_uri=BIOLINK.organism_taxon_to_organism_taxon_interaction_associated_environmental_context, domain=OrganismTaxonToOrganismTaxonInteraction, range=Optional[str])

slots.organism_taxon_to_environment_association_subject = Slot(uri=RDF.subject, name="organism taxon to environment association_subject", curie=RDF.curie('subject'),
                   model_uri=BIOLINK.organism_taxon_to_environment_association_subject, domain=OrganismTaxonToEnvironmentAssociation, range=Union[str, OrganismTaxonId])

slots.organism_taxon_to_environment_association_object = Slot(uri=RDF.object, name="organism taxon to environment association_object", curie=RDF.curie('object'),
                   model_uri=BIOLINK.organism_taxon_to_environment_association_object, domain=OrganismTaxonToEnvironmentAssociation, range=Union[str, NamedThingId])

slots.organism_taxon_to_environment_association_predicate = Slot(uri=RDF.predicate, name="organism taxon to environment association_predicate", curie=RDF.curie('predicate'),
                   model_uri=BIOLINK.organism_taxon_to_environment_association_predicate, domain=OrganismTaxonToEnvironmentAssociation, range=Union[str, PredicateType])