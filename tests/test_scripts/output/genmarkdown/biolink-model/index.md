# Biolink Model schema


A high level datamodel of biological entities (genes, diseases, phenotypes, pathways, individuals, substances, etc) and their associations.

### Classes

 * administrative entity
    * provider - person, group, organization or project that provides a piece of information
 * attribute - A property or characteristic of an entity
    * zygosity
    * clinical modifier - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    * severity value - describes the severity of a phenotypic feature or disease
    * biological sex
       * genotypic sex - An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
       * phenotypic sex - An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    * frequency value - describes the frequency of occurrence of an event or condition
    * onset - The age group in which manifestations appear
 * named thing - a databased entity or concept/class
    * planetary entity - Any entity or process that exists at the level of the whole planet
       * environmental feature
       * geographic location - a location that can be described in lat/long coordinates
          * geographic location at time - a location that can be described in lat/long coordinates, for a particular time
       * environmental process
    * clinical entity - Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
       * clinical trial
       * clinical intervention
    * information content entity - a piece of information that typically describes some piece of biology or is used as support.
       * confidence level - Level of confidence in a statement
       * publication - Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
       * association - A typed association between two entities, supported by evidence
          * genotype to thing association
          * genotype to gene association - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
          * genomic sequence localization - A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
          * biosample to thing association - An association between a biosample and something
          * gene to phenotypic feature association
          * thing to disease or phenotypic feature association
          * chemical to gene association - An interaction between a chemical entity and a gene or gene product
          * molecular interaction - An interaction at the molecular level between two physical entities
          * chemical to thing association - An interaction between a chemical entity and another entity
          * variant to phenotypic feature association
          * sequence variant modulates treatment association - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
          * chemical to disease or phenotypic feature association - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
          * gene to disease association
             * gene as a model of disease association
             * gene has variant that contributes to disease association
          * variant to population association - An association between a variant and a population, where the variant has particular frequency in the population
          * gene to expression site association - An association between a gene and an expression site, possibly qualified by stage/timing info.
          * environment to phenotypic feature association - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
          * cell line to thing association - An relationship between a cell line and another entity
          * genotype to variant association - Any association between a genotype and a sequence variant.
          * cell line to disease or phenotypic feature association - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
          * case to thing association - An abstract association for use where the case is the subject
          * gene regulatory relationship - A regulatory relationship between two genes
          * genotype to genotype part association - Any association between one genotype and a genotypic entity that is a sub-component of it
          * entity to phenotypic feature association
          * gene to gene association - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
             * pairwise gene or protein interaction association - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
             * gene to gene homology association - A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
          * functional association - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
             * macromolecular machine to molecular activity association - A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution
             * macromolecular machine to cellular component association - A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component
             * macromolecular machine to biological process association - A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
             * gene to go term association
          * anatomical entity to anatomical entity association
             * anatomical entity to anatomical entity ontogenic association - A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
             * anatomical entity to anatomical entity part of association - A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
          * genotype to phenotypic feature association - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
          * biosample to disease or phenotypic feature association - An association between a biosample and a disease or phenotype
  definitional: true
          * variant to disease association
          * gene to thing association
          * disease to phenotypic feature association - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
          * sequence feature relationship - For example, a particular exon is part of a particular transcript or gene
             * gene to gene product relationship - A gene is transcribed and potentially translated to a gene product
             * exon to transcript relationship - A transcript is formed from multiple exons
             * transcript to gene relationship - A gene is a collection of transcripts
          * disease to thing association
          * population to population association - An association between a two populations
          * variant to thing association
          * disease or phenotypic feature association to thing association
             * disease or phenotypic feature association to location association - An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
          * chemical to pathway association - An interaction between a chemical entity and a biological process or pathway
          * case to phenotypic feature association - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
       * evidence type - Class of evidence that supports an association
    * device - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    * biological entity
       * environment - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
          * drug exposure - A drug exposure is an intake of a particular chemical substance
          * treatment - A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
       * molecular entity - A gene, gene product, small molecule or macromolecule (including protein complex)
          * genomic entity - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
             * transcript - An RNA synthesized on a DNA or RNA template by an RNA polymerase
             * sequence variant - An allele that varies in its sequence from what is considered the reference allele at that locus.
             * macromolecular machine - A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
                * gene or gene product - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
                   * gene
                   * gene product - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
                      * gene product isoform - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
                      * protein - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
                         * protein isoform - Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
                      * RNA product
                         * noncoding RNA product
                            * microRNA
                         * RNA product isoform - Represents a protein that is a specific isoform of the canonical or reference RNA
                * macromolecular complex
             * exon - A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
             * genotype - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
             * haplotype - A set of zero or more Alleles on a single instance of a Sequence[VMC]
             * coding sequence
             * genome - A genome is the sum of genetic material within a cell or virion.
          * chemical substance - May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
             * metabolite - Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
             * drug - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
          * gene family - any grouping of multiple genes or gene products related by common descent
       * disease or phenotypic feature - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
          * disease
          * phenotypic feature
       * organismal entity - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
          * anatomical entity - A subcellular location, cell type or gross anatomical part
             * cell
             * gross anatomical structure
             * cellular component - A location in or around a cell
          * life stage - A stage of development or growth of an organism, including post-natal adult stages
          * population of individual organisms
          * individual organism
             * case - An individual organism that has a patient role in some clinical context.
          * biosample
             * cell line
       * biological process or activity - Either an individual molecular activity, or a collection of causally connected molecular activities
          * biological process - One or more causally connected executions of molecular functions
             * physiological process
             * pathway
          * molecular activity - An execution of a molecular function carried out by a gene product or macromolecular complex.
 * occurrent - A processual entity
    * activity and behavior - Activity or behavior of any independent integral living, organization or mechanical actor in the world
    * phenomenon - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    * procedure - A series of actions conducted in a certain order or manner
 * ontology class - a concept or class in an ontology, vocabulary or thesaurus
    * organism taxon
    * gene ontology class - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * relationship type - An OWL property used as an edge label
### Mixins

 * entity to disease association - mixin class for any association whose object (target node) is a disease
 * frequency quantifier
 * gene grouping - any grouping of multiple genes or gene products
 * gene ontology class - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * model to disease mixin - This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
 * molecular interaction - An interaction at the molecular level between two physical entities
 * pathognomonicity quantifier - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * relationship quantifier
    * frequency quantifier
    * senstivity quantifier
    * specificity quantifier
       * pathognomonicity quantifier - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * senstivity quantifier
 * specificity quantifier
    * pathognomonicity quantifier - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * thing with taxon - A mixin that can be used on any entity with a taxon
 * variant to thing association
### Slots

 * association slot - any slot that relates an association to another entity
    * has confidence level - connects an association to a qualitative term denoting the level of confidence
    * qualifiers - connects an association to qualifiers that modify or qualify the meaning of that association
    * subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * variant to thing association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to gene association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * functional association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * variant to population association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * case to thing association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * genotype to gene association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * variant to phenotypic feature association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * genotype to phenotypic feature association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene regulatory relationship subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to disease association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * disease or phenotypic feature association to thing association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * cell line to thing association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * genotype to genotype part association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * cell line to disease or phenotypic feature association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * population to population association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene has variant that contributes to disease association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * variant to disease association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to go term association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * anatomical entity to anatomical entity association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * chemical to thing association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * environment to phenotypic feature association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to expression site association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * genotype to thing association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * genomic sequence localization subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * anatomical entity to anatomical entity ontogenic association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * transcript to gene relationship subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to thing association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * biosample to thing association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * sequence variant modulates treatment association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * sequence feature relationship subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * genotype to variant association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * molecular interaction subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene as a model of disease association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to gene product relationship subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to phenotypic feature association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * exon to transcript relationship subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * anatomical entity to anatomical entity part of association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * disease to thing association subject - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * negated - if set to true, then the association is negated i.e. is not true
    * provided by - connects an association to the agent (person, organization or group) that provided it
    * edge label - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * association type - connects an association to the type of association (e.g. gene to phenotype)
    * has evidence - connects an association to an instance of supporting evidence
    * sex qualifier - a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * onset qualifier - a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * sequence variant qualifier - a qualifier used in an association where the variant
    * severity qualifier - a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * publications - connects an association to publications supporting the association
    * frequency qualifier - a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * molecular interaction object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * disease or phenotypic feature association to location association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to gene association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * genomic sequence localization object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * transcript to gene relationship object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * chemical to disease or phenotypic feature association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * functional association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * population to population association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * macromolecular machine to molecular activity association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * sequence variant modulates treatment association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to expression site association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * anatomical entity to anatomical entity part of association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * genotype to genotype part association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * anatomical entity to anatomical entity association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * variant to population association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene regulatory relationship object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * chemical to gene association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * macromolecular machine to cellular component association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to gene product relationship object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * macromolecular machine to biological process association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * gene to go term association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * entity to phenotypic feature association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * variant to disease association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * sequence feature relationship object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * anatomical entity to anatomical entity ontogenic association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * exon to transcript relationship object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * thing to disease or phenotypic feature association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * chemical to pathway association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * genotype to variant association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * genotype to gene association object - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * stage qualifier - stage at which expression takes place
    * clinical modifier qualifier - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    * quantifier qualifier - A measurable quantity for the object of the association
    * relation - the relationship type by which a subject is connected to an object in an association
       * variant to disease association relation - the relationship type by which a subject is connected to an object in an association
       * genotype to phenotypic feature association relation - the relationship type by which a subject is connected to an object in an association
       * population to population association relation - the relationship type by which a subject is connected to an object in an association
       * genotype to gene association relation - the relationship type by which a subject is connected to an object in an association
       * genotype to genotype part association relation - the relationship type by which a subject is connected to an object in an association
       * anatomical entity to anatomical entity ontogenic association relation - the relationship type by which a subject is connected to an object in an association
       * genotype to variant association relation - the relationship type by which a subject is connected to an object in an association
       * gene to gene homology association relation - the relationship type by which a subject is connected to an object in an association
       * gene to expression site association relation - the relationship type by which a subject is connected to an object in an association
       * gene regulatory relationship relation - the relationship type by which a subject is connected to an object in an association
       * pairwise gene or protein interaction association relation - the relationship type by which a subject is connected to an object in an association
       * molecular interaction relation - the relationship type by which a subject is connected to an object in an association
       * anatomical entity to anatomical entity part of association relation - the relationship type by which a subject is connected to an object in an association
       * gene to gene product relationship relation - the relationship type by which a subject is connected to an object in an association
 * drug exposure drug
 * entity to disease association object - disease
 * gene to expression site association quantifier qualifier - can be used to indicate magnitude, or also ranking
 * gene to expression site association stage qualifier - stage at which the gene is expressed in the site
 * model to disease mixin relation - The relationship to the disease
 * model to disease mixin subject - The entity that serves as the model of the disease. This may be an organism, a strain of organism, a genotype or variant that exhibits similar features, or a gene that when mutated exhibits features of the disease
 * molecular interaction interacting molecules category
 * node property - A grouping for any property that holds between a node and a value
    * has gene - connects and entity to a single gene
    * longitude - longitude
    * iri - An IRI for the node. This is determined by the id using expansion rules.
    * interbase coordinate - TODO
       * start interbase coordinate - TODO
       * end interbase coordinate - TODO
    * name - A human-readable name for a thing
       * macromolecular machine name - A human-readable name for a thing
    * has chemical formula - description of chemical compound based on element symbols
    * latitude - latitude
    * creation date - date on which thing was created. This can be applied to nodes or edges
    * description - a human-readable description of a thing
       * entity to phenotypic feature association description - a human-readable description of a thing
    * filler - The value in a property-value tuple
    * has biological sequence - connects a genomic feature to its sequence
       * sequence variant has biological sequence - connects a genomic feature to its sequence
    * full name - a long-form human readable name for a thing
    * systematic synonym - more commonly used for gene symbols in yeast
    * update date - date on which thing was updated. This can be applied to nodes or edges
    * aggregate statistic - A grouping for any property that holds between a node and a value
       * has total - total number of things in a particular reference set
       * has percentage - equivalent to has quotient multiplied by 100
       * has count - number of things with a particular property
       * has quotient - A grouping for any property that holds between a node and a value
    * has zygosity - A grouping for any property that holds between a node and a value
    * timepoint - a point in time
    * genome build - TODO
    * category - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * phase - TODO
    * id - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
       * sequence variant id - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
 * related to - A grouping for any relationship type that holds between any two things
    * has molecular consequence - connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
    * gene associated with condition - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
    * expressed in - holds between a gene or gene product and an anatomical entity in which it is expressed
    * interacts with - holds between any two entities that directly or indirectly interact with each other
       * genetically interacts with - holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
       * physically interacts with - holds between two entities that make physical contact as part of some interaction
          * molecularly interacts with - holds between two entities that make physical contact as part of some interaction
    * contributes to - holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
       * causes - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or  generation of the other
    * model of - holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exibiting similar features of the studied entity.
    * has gene product - holds between a gene and a transcribed and/or translated product generated from it
    * derives into - holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * location of - holds between material entity or site and a material entity that is located within it (but not considered a part of it)
    * occurs in - holds between a process and a material entity or site within which the process occurs
    * same as - holds between two entities that are considered equivalent to each other
    * overlaps - holds between entties that overlap in their extents (materials or processes)
       * part of - holds between parts and wholes (material entities or processes)
       * has part - holds between wholes and their parts (material entities or processes)
    * homologous to - holds between two biological entities that have common evolutionary origin
       * xenologous to - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
       * paralogous to - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
       * orthologous to - a homology relationship between entities (typically genes) that diverged after a speciation event.
    * produces - holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
    * affects - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
       * disrupts - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
       * regulates - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
          * negatively regulates - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
          * regulates, process to process - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
             * positively regulates, process to process - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
             * negatively regulates, process to process - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
          * positively regulates - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
          * regulates, entity to entity - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
             * negatively regulates, entity to entity - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
             * positively regulates, entity to entity - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
       * treats - holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
    * subclass of - holds between two classes where the domain class is a specialization of the range class
    * participates in - holds between a continuant and a process, where the continuant is somehow involved in the process
       * actively involved in - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
          * capable of - holds between a continuant and process or function, where the continuant alone has the ability to carry out the process or function.
    * expresses - holds between an anatomical entity and gene or gene product that is expressed there
    * coexists with - holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
       * co-localizes with - holds between two entities that are observed to be located in the same place.
       * in complex with - holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
       * in cell population with - holds between two genes or gene products that are expressed in the same cell type or population
       * in pathway with - holds between two genes or gene products that are part of in the same biological pathway
    * treated by - holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition
    * has participant - holds between a process and a continuant, where the continuant is somehow involved in the process
       * has input - holds between a process and a continuant, where the continuant is an input into the process
    * has phenotype - holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature).
    * precedes - holds between two processes, where one completes before the other begins
    * manifestation of - used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
    * derives from - holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * correlated with - holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
       * biomarker for - holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
       * has biomarker - holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * in taxon - connects a thing to a class representing a taxon
    * affects risk for - holds between two entities where exposure to one entity alters the chance of developing the other
       * predisposes - holds between two entities where exposure to one entity increases the chance of developing the other
       * prevents - holds between an entity whose application or use reduces the likelihood of a potential outcome.  Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
    * located in - holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
 * sequence variant has gene - Each allele can be associated with any number of genes
 * treatment has exposure parts
 * treatment treats
 * variant to population association has count - number in object population that carry a particular allele, aka allele count
 * variant to population association has quotient - frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency
 * variant to population association has total - number all populations that carry a particular allele, aka allele number
### Types

#### Built in

 * **boolean**
 * **date**
 * **double**
 * **float**
 * **integer**
 * **string**
 * **time**
#### Defined

 * biological sequence (**string**)
 * chemical formula type (**string**)
 * chemical formula value (**string**)
 * evidence instance (**string**)
 * frequency value (**string**)
 * identifier type (**string**) - A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form
 * iri type (**string**) - An IRI
 * label type (**string**) - A string that provides a human-readable name for a thing
 * narrative text (**string**) - A string that provides a human-readable description of something
 * perecentage frequency value (**double**)
 * phenotype (**string**)
 * quotient (**double**)
 * symbol type (**string**)
 * time type (**time**)
 * unit (**string**)
