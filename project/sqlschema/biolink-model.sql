

CREATE TABLE accessible_dna_region (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_biological_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE activity (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE agent (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	address TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE anatomical_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE article (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	authors TEXT, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	published_in TEXT NOT NULL, 
	iso_abbreviation TEXT, 
	volume TEXT, 
	issue TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE bacterium (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE behavior (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE behavioral_feature (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE biological_process (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE biological_process_or_activity (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE book (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	authors TEXT, 
	summary TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE book_chapter (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	authors TEXT, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	published_in TEXT NOT NULL, 
	volume TEXT, 
	chapter TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "case" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cell (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cell_line (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cellular_component (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cellular_organism (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE chemical_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	object_direction_qualifier VARCHAR(13), 
	predicate TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE chi_squared_analysis_result (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE clinical_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE clinical_finding (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE clinical_intervention (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE clinical_trial (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE coding_sequence (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_biological_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cohort (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE common_data_element (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE concept_count_analysis_result (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE confidence_level (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE dataset (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE dataset_distribution (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	distribution_download_url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE dataset_summary (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	source_web_page TEXT, 
	source_logo TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE diagnostic_aid (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE disease (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE disease_or_phenotypic_feature (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE drug_label (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	authors TEXT, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE environmental_feature (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE environmental_process (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE event (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE evidence_type (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE exon (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE functional_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE fungus (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE gene (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	symbol TEXT, 
	has_biological_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE gene_family (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_gene_or_gene_product TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE gene_to_gene_homology_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE genetic_inheritance (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE genome (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_biological_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE geographic_location (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	latitude FLOAT, 
	longitude FLOAT, 
	PRIMARY KEY (id)
);

CREATE TABLE geographic_location_at_time (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	latitude FLOAT, 
	longitude FLOAT, 
	timepoint TIME, 
	PRIMARY KEY (id)
);

CREATE TABLE gross_anatomical_structure (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE haplotype (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_biological_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE hospitalization (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE human (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE individual_organism (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE invertebrate (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE journal_article (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	authors TEXT, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	published_in TEXT NOT NULL, 
	iso_abbreviation TEXT, 
	volume TEXT, 
	issue TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE life_stage (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE log_odds_analysis_result (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE macromolecular_complex (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE mammal (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE material_sample (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "microRNA" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE molecular_activity (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE named_thing (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "noncoding_RNA_product" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE nucleic_acid_sequence_motif (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE nucleosome_modification (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_biological_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE observed_expected_frequency_analysis_result (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE patent (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	authors TEXT, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE pathological_anatomical_structure (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE pathological_process (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE pathway (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE phenomenon (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE phenotypic_feature (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE physical_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE physiological_process (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE planetary_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE plant (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE polypeptide (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE population_of_individual_organisms (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE posttranslational_modification (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE preprint_publication (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	authors TEXT, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE protein (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE protein_domain (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_gene_or_gene_product TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE protein_family (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_gene_or_gene_product TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE protein_isoform (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE publication (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	authors TEXT, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE quantity_value (
	has_unit TEXT, 
	has_numeric_value FLOAT, 
	PRIMARY KEY (has_unit, has_numeric_value)
);

CREATE TABLE reagent_targeted_gene (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_biological_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE regulatory_region (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_biological_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE relationship_type (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE relative_frequency_analysis_result (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE retrieval_source (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	resource_id TEXT NOT NULL, 
	resource_role VARCHAR(27) NOT NULL, 
	upstream_resource_ids TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "RNA_product" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "RNA_product_isoform" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE sequence_variant (
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_gene TEXT, 
	has_biological_sequence TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE serial (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	authors TEXT, 
	summary TEXT, 
	name TEXT, 
	iso_abbreviation TEXT, 
	volume TEXT, 
	issue TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "siRNA" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE snv (
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_gene TEXT, 
	has_biological_sequence TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE study (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE study_population (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE study_variable (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE taxonomic_rank (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE text_mining_result (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE transcript (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE transcription_factor_binding_site (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_biological_sequence TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE treatment (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id)
);

CREATE TABLE vertebrate (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE virus (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE web_page (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	authors TEXT, 
	summary TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(object) REFERENCES anatomical_entity (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(object) REFERENCES anatomical_entity (id)
);

CREATE TABLE association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE attribute (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE behavioral_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE biological_sex (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE biotic_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(subject) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES chemical_entity (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE chemical_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	has_quantitative_value TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE chemical_gene_interaction_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_form_or_variant_qualifier VARCHAR(29), 
	subject_part_qualifier VARCHAR(11), 
	subject_derivative_qualifier VARCHAR(10), 
	subject_context_qualifier TEXT, 
	object_form_or_variant_qualifier VARCHAR(29), 
	object_part_qualifier VARCHAR(11), 
	object_context_qualifier TEXT, 
	anatomical_context_qualifier TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject_context_qualifier) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(object_context_qualifier) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(anatomical_context_qualifier) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(subject) REFERENCES chemical_entity (id)
);

CREATE TABLE chemical_mixture (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	is_supplement TEXT, 
	"highest_FDA_approval_status" TEXT, 
	drug_regulatory_status_world_wide TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES chemical_mixture (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	"FDA_adverse_event_level" VARCHAR(30), 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	"FDA_adverse_event_level" VARCHAR(30), 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE chemical_role (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE chemical_to_chemical_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES chemical_entity (id)
);

CREATE TABLE chemical_to_chemical_derivation_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES chemical_entity (id), 
	FOREIGN KEY(object) REFERENCES chemical_entity (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE chemical_to_pathway_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES chemical_entity (id), 
	FOREIGN KEY(object) REFERENCES pathway (id)
);

CREATE TABLE clinical_attribute (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	clinical_finding_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id), 
	FOREIGN KEY(clinical_finding_id) REFERENCES clinical_finding (id)
);

CREATE TABLE clinical_course (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE clinical_measurement (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	has_attribute_type TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE clinical_modifier (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE complex_chemical_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE contributor_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES agent (id)
);

CREATE TABLE dataset_version (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	has_dataset TEXT, 
	ingest_date TEXT, 
	has_distribution TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_dataset) REFERENCES dataset (id), 
	FOREIGN KEY(has_distribution) REFERENCES dataset_distribution (id)
);

CREATE TABLE device (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	treatment_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(treatment_id) REFERENCES treatment (id)
);

CREATE TABLE disease_or_phenotypic_feature_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES genetic_inheritance (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES anatomical_entity (id)
);

CREATE TABLE disease_to_exposure_event_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE drug_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	has_quantitative_value TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE drug_to_gene_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id)
);

CREATE TABLE drug_to_gene_interaction_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	has_quantitative_value TEXT, 
	timepoint TIME, 
	has_gene_or_gene_product TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE entity_to_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	"FDA_approval_status" VARCHAR(31), 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE entity_to_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	"FDA_approval_status" VARCHAR(31), 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE environmental_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE environmental_food_contaminant (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id)
);

CREATE TABLE exon_to_transcript_relationship (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES exon (id), 
	FOREIGN KEY(object) REFERENCES transcript (id)
);

CREATE TABLE exposure_event_to_outcome_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	population_context_qualifier TEXT, 
	temporal_context_qualifier TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(population_context_qualifier) REFERENCES population_of_individual_organisms (id)
);

CREATE TABLE food_additive (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id)
);

CREATE TABLE gene_to_expression_site_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	stage_qualifier TEXT, 
	quantifier_qualifier TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(stage_qualifier) REFERENCES life_stage (id), 
	FOREIGN KEY(object) REFERENCES anatomical_entity (id)
);

CREATE TABLE gene_to_gene_coexpression_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	quantifier_qualifier TEXT, 
	expression_site TEXT, 
	stage_qualifier TEXT, 
	phenotypic_state TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(expression_site) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(stage_qualifier) REFERENCES life_stage (id), 
	FOREIGN KEY(phenotypic_state) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE gene_to_gene_family_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES gene (id), 
	FOREIGN KEY(object) REFERENCES gene_family (id)
);

CREATE TABLE gene_to_gene_product_relationship (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES gene (id)
);

CREATE TABLE gene_to_go_term_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES gene (id)
);

CREATE TABLE gene_to_pathway_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES pathway (id)
);

CREATE TABLE genomic_background_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	has_gene_or_gene_product TEXT, 
	has_biological_sequence TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE genotypic_sex (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE geographic_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE information_content_entity_to_named_thing_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES biological_process (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES cellular_component (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES molecular_activity (id)
);

CREATE TABLE material_sample_derivation_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES material_sample (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES molecular_activity (id), 
	FOREIGN KEY(object) REFERENCES chemical_entity (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES molecular_activity (id), 
	FOREIGN KEY(object) REFERENCES molecular_activity (id)
);

CREATE TABLE molecular_activity_to_pathway_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES molecular_activity (id), 
	FOREIGN KEY(object) REFERENCES pathway (id)
);

CREATE TABLE molecular_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	is_metabolite BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	predicate TEXT NOT NULL, 
	subject_aspect_qualifier TEXT, 
	subject_context_qualifier TEXT, 
	object_aspect_qualifier TEXT, 
	object_context_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE nucleic_acid_entity (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	is_metabolite BOOLEAN, 
	has_biological_sequence TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id)
);

CREATE TABLE onset (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE organism_attribute (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE organism_taxon (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	has_taxonomic_rank TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_taxonomic_rank) REFERENCES taxonomic_rank (id)
);

CREATE TABLE organism_to_organism_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES individual_organism (id), 
	FOREIGN KEY(object) REFERENCES individual_organism (id)
);

CREATE TABLE pathological_anatomical_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE pathological_process_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE phenotypic_quality (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE phenotypic_sex (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE population_to_population_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES population_of_individual_organisms (id), 
	FOREIGN KEY(object) REFERENCES population_of_individual_organisms (id)
);

CREATE TABLE procedure (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	treatment_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(treatment_id) REFERENCES treatment (id)
);

CREATE TABLE sequence_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id)
);

CREATE TABLE severity_value (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE small_molecule (
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	is_metabolite BOOLEAN, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id)
);

CREATE TABLE socioeconomic_exposure (
	id TEXT NOT NULL, 
	description TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	timepoint TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE transcript_to_gene_relationship (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES transcript (id), 
	FOREIGN KEY(object) REFERENCES gene (id)
);

CREATE TABLE variant_to_gene_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES gene (id)
);

CREATE TABLE variant_to_gene_expression_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	quantifier_qualifier TEXT, 
	expression_site TEXT, 
	stage_qualifier TEXT, 
	phenotypic_state TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES gene (id), 
	FOREIGN KEY(expression_site) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(stage_qualifier) REFERENCES life_stage (id), 
	FOREIGN KEY(phenotypic_state) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE variant_to_population_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	has_quotient FLOAT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_percentage FLOAT, 
	frequency_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES sequence_variant (id), 
	FOREIGN KEY(object) REFERENCES population_of_individual_organisms (id)
);

CREATE TABLE zygosity (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id)
);

CREATE TABLE accessible_dna_region_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES accessible_dna_region (id)
);

CREATE TABLE accessible_dna_region_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES accessible_dna_region (id)
);

CREATE TABLE accessible_dna_region_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES accessible_dna_region (id)
);

CREATE TABLE accessible_dna_region_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES accessible_dna_region (id)
);

CREATE TABLE accessible_dna_region_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES accessible_dna_region (id)
);

CREATE TABLE activity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES activity (id)
);

CREATE TABLE activity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES activity (id)
);

CREATE TABLE activity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES activity (id)
);

CREATE TABLE activity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES activity (id)
);

CREATE TABLE activity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES activity (id)
);

CREATE TABLE agent_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE agent_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE agent_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE agent_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE agent_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE agent_affiliation (
	backref_id TEXT, 
	affiliation TEXT, 
	PRIMARY KEY (backref_id, affiliation), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE anatomical_entity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity (id)
);

CREATE TABLE anatomical_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity (id)
);

CREATE TABLE anatomical_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity (id)
);

CREATE TABLE anatomical_entity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity (id)
);

CREATE TABLE anatomical_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity (id)
);

CREATE TABLE article_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_mesh_terms (
	backref_id TEXT, 
	mesh_terms TEXT, 
	PRIMARY KEY (backref_id, mesh_terms), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE article_publication_type (
	backref_id TEXT, 
	publication_type TEXT NOT NULL, 
	PRIMARY KEY (backref_id, publication_type), 
	FOREIGN KEY(backref_id) REFERENCES article (id)
);

CREATE TABLE bacterium_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES bacterium (id)
);

CREATE TABLE bacterium_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES bacterium (id)
);

CREATE TABLE bacterium_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES bacterium (id)
);

CREATE TABLE bacterium_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES bacterium (id)
);

CREATE TABLE bacterium_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES bacterium (id)
);

CREATE TABLE behavior_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES behavior (id)
);

CREATE TABLE behavior_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES behavior (id)
);

CREATE TABLE behavior_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES behavior (id)
);

CREATE TABLE behavior_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES behavior (id)
);

CREATE TABLE behavior_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES behavior (id)
);

CREATE TABLE behavioral_feature_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_feature (id)
);

CREATE TABLE behavioral_feature_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_feature (id)
);

CREATE TABLE behavioral_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_feature (id)
);

CREATE TABLE behavioral_feature_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_feature (id)
);

CREATE TABLE behavioral_feature_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_feature (id)
);

CREATE TABLE biological_process_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES biological_process (id)
);

CREATE TABLE biological_process_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES biological_process (id)
);

CREATE TABLE biological_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES biological_process (id)
);

CREATE TABLE biological_process_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES biological_process (id)
);

CREATE TABLE biological_process_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES biological_process (id)
);

CREATE TABLE biological_process_or_activity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES biological_process_or_activity (id)
);

CREATE TABLE biological_process_or_activity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES biological_process_or_activity (id)
);

CREATE TABLE biological_process_or_activity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES biological_process_or_activity (id)
);

CREATE TABLE biological_process_or_activity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES biological_process_or_activity (id)
);

CREATE TABLE biological_process_or_activity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES biological_process_or_activity (id)
);

CREATE TABLE book_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_mesh_terms (
	backref_id TEXT, 
	mesh_terms TEXT, 
	PRIMARY KEY (backref_id, mesh_terms), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_publication_type (
	backref_id TEXT, 
	publication_type TEXT NOT NULL, 
	PRIMARY KEY (backref_id, publication_type), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_chapter_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_mesh_terms (
	backref_id TEXT, 
	mesh_terms TEXT, 
	PRIMARY KEY (backref_id, mesh_terms), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_publication_type (
	backref_id TEXT, 
	publication_type TEXT NOT NULL, 
	PRIMARY KEY (backref_id, publication_type), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE case_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES "case" (id)
);

CREATE TABLE case_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "case" (id)
);

CREATE TABLE case_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "case" (id)
);

CREATE TABLE case_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES "case" (id)
);

CREATE TABLE case_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "case" (id)
);

CREATE TABLE cell_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES cell (id)
);

CREATE TABLE cell_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES cell (id)
);

CREATE TABLE cell_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES cell (id)
);

CREATE TABLE cell_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES cell (id)
);

CREATE TABLE cell_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES cell (id)
);

CREATE TABLE cell_line_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES cell_line (id)
);

CREATE TABLE cell_line_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES cell_line (id)
);

CREATE TABLE cell_line_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES cell_line (id)
);

CREATE TABLE cell_line_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES cell_line (id)
);

CREATE TABLE cell_line_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES cell_line (id)
);

CREATE TABLE cellular_component_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES cellular_component (id)
);

CREATE TABLE cellular_component_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES cellular_component (id)
);

CREATE TABLE cellular_component_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES cellular_component (id)
);

CREATE TABLE cellular_component_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES cellular_component (id)
);

CREATE TABLE cellular_component_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES cellular_component (id)
);

CREATE TABLE cellular_organism_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES cellular_organism (id)
);

CREATE TABLE cellular_organism_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES cellular_organism (id)
);

CREATE TABLE cellular_organism_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES cellular_organism (id)
);

CREATE TABLE cellular_organism_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES cellular_organism (id)
);

CREATE TABLE cellular_organism_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES cellular_organism (id)
);

CREATE TABLE chemical_entity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity (id)
);

CREATE TABLE chemical_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity (id)
);

CREATE TABLE chemical_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity (id)
);

CREATE TABLE chemical_entity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity (id)
);

CREATE TABLE chemical_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity (id)
);

CREATE TABLE chemical_entity_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_or_gene_or_gene_product_regulates_gene_association (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_or_gene_or_gene_product_regulates_gene_association (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_or_gene_or_gene_product_regulates_gene_association (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_or_gene_or_gene_product_regulates_gene_association (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_or_gene_or_gene_product_regulates_gene_association (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_or_gene_or_gene_product_regulates_gene_association (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_or_gene_or_gene_product_regulates_gene_association (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_or_gene_or_gene_product_regulates_gene_association (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_or_gene_or_gene_product_regulates_gene_association (id)
);

CREATE TABLE chemical_entity_or_gene_or_gene_product_regulates_gene_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_or_gene_or_gene_product_regulates_gene_association (id)
);

CREATE TABLE chi_squared_analysis_result_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chi_squared_analysis_result (id)
);

CREATE TABLE chi_squared_analysis_result_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES chi_squared_analysis_result (id)
);

CREATE TABLE chi_squared_analysis_result_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES chi_squared_analysis_result (id)
);

CREATE TABLE chi_squared_analysis_result_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES chi_squared_analysis_result (id)
);

CREATE TABLE chi_squared_analysis_result_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chi_squared_analysis_result (id)
);

CREATE TABLE clinical_entity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES clinical_entity (id)
);

CREATE TABLE clinical_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES clinical_entity (id)
);

CREATE TABLE clinical_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES clinical_entity (id)
);

CREATE TABLE clinical_entity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES clinical_entity (id)
);

CREATE TABLE clinical_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES clinical_entity (id)
);

CREATE TABLE clinical_finding_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES clinical_finding (id)
);

CREATE TABLE clinical_finding_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES clinical_finding (id)
);

CREATE TABLE clinical_finding_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES clinical_finding (id)
);

CREATE TABLE clinical_finding_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES clinical_finding (id)
);

CREATE TABLE clinical_finding_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES clinical_finding (id)
);

CREATE TABLE clinical_intervention_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES clinical_intervention (id)
);

CREATE TABLE clinical_intervention_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES clinical_intervention (id)
);

CREATE TABLE clinical_intervention_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES clinical_intervention (id)
);

CREATE TABLE clinical_intervention_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES clinical_intervention (id)
);

CREATE TABLE clinical_intervention_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES clinical_intervention (id)
);

CREATE TABLE clinical_trial_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES clinical_trial (id)
);

CREATE TABLE clinical_trial_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES clinical_trial (id)
);

CREATE TABLE clinical_trial_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES clinical_trial (id)
);

CREATE TABLE clinical_trial_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES clinical_trial (id)
);

CREATE TABLE clinical_trial_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES clinical_trial (id)
);

CREATE TABLE coding_sequence_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES coding_sequence (id)
);

CREATE TABLE coding_sequence_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES coding_sequence (id)
);

CREATE TABLE coding_sequence_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES coding_sequence (id)
);

CREATE TABLE coding_sequence_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES coding_sequence (id)
);

CREATE TABLE coding_sequence_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES coding_sequence (id)
);

CREATE TABLE cohort_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES cohort (id)
);

CREATE TABLE cohort_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES cohort (id)
);

CREATE TABLE cohort_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES cohort (id)
);

CREATE TABLE cohort_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES cohort (id)
);

CREATE TABLE cohort_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES cohort (id)
);

CREATE TABLE common_data_element_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES common_data_element (id)
);

CREATE TABLE common_data_element_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES common_data_element (id)
);

CREATE TABLE common_data_element_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES common_data_element (id)
);

CREATE TABLE common_data_element_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES common_data_element (id)
);

CREATE TABLE common_data_element_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES common_data_element (id)
);

CREATE TABLE concept_count_analysis_result_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES concept_count_analysis_result (id)
);

CREATE TABLE concept_count_analysis_result_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES concept_count_analysis_result (id)
);

CREATE TABLE concept_count_analysis_result_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES concept_count_analysis_result (id)
);

CREATE TABLE concept_count_analysis_result_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES concept_count_analysis_result (id)
);

CREATE TABLE concept_count_analysis_result_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES concept_count_analysis_result (id)
);

CREATE TABLE confidence_level_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES confidence_level (id)
);

CREATE TABLE confidence_level_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES confidence_level (id)
);

CREATE TABLE confidence_level_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES confidence_level (id)
);

CREATE TABLE confidence_level_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES confidence_level (id)
);

CREATE TABLE confidence_level_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES confidence_level (id)
);

CREATE TABLE dataset_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE dataset_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE dataset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE dataset_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE dataset_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE dataset_distribution_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES dataset_distribution (id)
);

CREATE TABLE dataset_distribution_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES dataset_distribution (id)
);

CREATE TABLE dataset_distribution_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset_distribution (id)
);

CREATE TABLE dataset_distribution_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES dataset_distribution (id)
);

CREATE TABLE dataset_distribution_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES dataset_distribution (id)
);

CREATE TABLE dataset_summary_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES dataset_summary (id)
);

CREATE TABLE dataset_summary_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES dataset_summary (id)
);

CREATE TABLE dataset_summary_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset_summary (id)
);

CREATE TABLE dataset_summary_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES dataset_summary (id)
);

CREATE TABLE dataset_summary_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES dataset_summary (id)
);

CREATE TABLE diagnostic_aid_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES diagnostic_aid (id)
);

CREATE TABLE diagnostic_aid_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES diagnostic_aid (id)
);

CREATE TABLE diagnostic_aid_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES diagnostic_aid (id)
);

CREATE TABLE diagnostic_aid_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES diagnostic_aid (id)
);

CREATE TABLE diagnostic_aid_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES diagnostic_aid (id)
);

CREATE TABLE disease_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES disease (id)
);

CREATE TABLE disease_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES disease (id)
);

CREATE TABLE disease_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES disease (id)
);

CREATE TABLE disease_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES disease (id)
);

CREATE TABLE disease_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES disease (id)
);

CREATE TABLE disease_or_phenotypic_feature_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE disease_or_phenotypic_feature_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE disease_or_phenotypic_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE disease_or_phenotypic_feature_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE disease_or_phenotypic_feature_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE drug_label_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES drug_label (id)
);

CREATE TABLE drug_label_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES drug_label (id)
);

CREATE TABLE drug_label_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES drug_label (id)
);

CREATE TABLE drug_label_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES drug_label (id)
);

CREATE TABLE drug_label_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES drug_label (id)
);

CREATE TABLE drug_label_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES drug_label (id)
);

CREATE TABLE drug_label_mesh_terms (
	backref_id TEXT, 
	mesh_terms TEXT, 
	PRIMARY KEY (backref_id, mesh_terms), 
	FOREIGN KEY(backref_id) REFERENCES drug_label (id)
);

CREATE TABLE drug_label_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES drug_label (id)
);

CREATE TABLE drug_label_publication_type (
	backref_id TEXT, 
	publication_type TEXT NOT NULL, 
	PRIMARY KEY (backref_id, publication_type), 
	FOREIGN KEY(backref_id) REFERENCES drug_label (id)
);

CREATE TABLE environmental_feature_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES environmental_feature (id)
);

CREATE TABLE environmental_feature_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES environmental_feature (id)
);

CREATE TABLE environmental_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES environmental_feature (id)
);

CREATE TABLE environmental_feature_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES environmental_feature (id)
);

CREATE TABLE environmental_feature_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES environmental_feature (id)
);

CREATE TABLE environmental_process_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES environmental_process (id)
);

CREATE TABLE environmental_process_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES environmental_process (id)
);

CREATE TABLE environmental_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES environmental_process (id)
);

CREATE TABLE environmental_process_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES environmental_process (id)
);

CREATE TABLE environmental_process_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES environmental_process (id)
);

CREATE TABLE event_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES event (id)
);

CREATE TABLE event_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES event (id)
);

CREATE TABLE event_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES event (id)
);

CREATE TABLE event_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES event (id)
);

CREATE TABLE event_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES event (id)
);

CREATE TABLE evidence_type_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES evidence_type (id)
);

CREATE TABLE evidence_type_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES evidence_type (id)
);

CREATE TABLE evidence_type_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES evidence_type (id)
);

CREATE TABLE evidence_type_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES evidence_type (id)
);

CREATE TABLE evidence_type_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES evidence_type (id)
);

CREATE TABLE exon_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES exon (id)
);

CREATE TABLE exon_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES exon (id)
);

CREATE TABLE exon_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES exon (id)
);

CREATE TABLE exon_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES exon (id)
);

CREATE TABLE exon_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES exon (id)
);

CREATE TABLE functional_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE functional_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE functional_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE functional_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE functional_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE functional_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE functional_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE functional_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE functional_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE functional_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES functional_association (id)
);

CREATE TABLE fungus_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES fungus (id)
);

CREATE TABLE fungus_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES fungus (id)
);

CREATE TABLE fungus_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES fungus (id)
);

CREATE TABLE fungus_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES fungus (id)
);

CREATE TABLE fungus_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES fungus (id)
);

CREATE TABLE gene_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene (id)
);

CREATE TABLE gene_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES gene (id)
);

CREATE TABLE gene_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES gene (id)
);

CREATE TABLE gene_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene (id)
);

CREATE TABLE gene_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES gene (id)
);

CREATE TABLE gene_family_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_family (id)
);

CREATE TABLE gene_family_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES gene_family (id)
);

CREATE TABLE gene_family_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES gene_family (id)
);

CREATE TABLE gene_family_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES gene_family (id)
);

CREATE TABLE gene_family_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_family (id)
);

CREATE TABLE gene_to_gene_homology_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_homology_association (id)
);

CREATE TABLE gene_to_gene_homology_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_homology_association (id)
);

CREATE TABLE gene_to_gene_homology_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_homology_association (id)
);

CREATE TABLE gene_to_gene_homology_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_homology_association (id)
);

CREATE TABLE gene_to_gene_homology_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_homology_association (id)
);

CREATE TABLE gene_to_gene_homology_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_homology_association (id)
);

CREATE TABLE gene_to_gene_homology_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_homology_association (id)
);

CREATE TABLE gene_to_gene_homology_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_homology_association (id)
);

CREATE TABLE gene_to_gene_homology_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_homology_association (id)
);

CREATE TABLE gene_to_gene_homology_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_homology_association (id)
);

CREATE TABLE genetic_inheritance_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genetic_inheritance (id)
);

CREATE TABLE genetic_inheritance_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES genetic_inheritance (id)
);

CREATE TABLE genetic_inheritance_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES genetic_inheritance (id)
);

CREATE TABLE genetic_inheritance_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES genetic_inheritance (id)
);

CREATE TABLE genetic_inheritance_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genetic_inheritance (id)
);

CREATE TABLE genome_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genome (id)
);

CREATE TABLE genome_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES genome (id)
);

CREATE TABLE genome_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES genome (id)
);

CREATE TABLE genome_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES genome (id)
);

CREATE TABLE genome_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genome (id)
);

CREATE TABLE geographic_location_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location (id)
);

CREATE TABLE geographic_location_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location (id)
);

CREATE TABLE geographic_location_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location (id)
);

CREATE TABLE geographic_location_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location (id)
);

CREATE TABLE geographic_location_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location (id)
);

CREATE TABLE geographic_location_at_time_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location_at_time (id)
);

CREATE TABLE geographic_location_at_time_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location_at_time (id)
);

CREATE TABLE geographic_location_at_time_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location_at_time (id)
);

CREATE TABLE geographic_location_at_time_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location_at_time (id)
);

CREATE TABLE geographic_location_at_time_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES geographic_location_at_time (id)
);

CREATE TABLE gross_anatomical_structure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gross_anatomical_structure (id)
);

CREATE TABLE gross_anatomical_structure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES gross_anatomical_structure (id)
);

CREATE TABLE gross_anatomical_structure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES gross_anatomical_structure (id)
);

CREATE TABLE gross_anatomical_structure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES gross_anatomical_structure (id)
);

CREATE TABLE gross_anatomical_structure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gross_anatomical_structure (id)
);

CREATE TABLE haplotype_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES haplotype (id)
);

CREATE TABLE haplotype_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES haplotype (id)
);

CREATE TABLE haplotype_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES haplotype (id)
);

CREATE TABLE haplotype_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES haplotype (id)
);

CREATE TABLE haplotype_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES haplotype (id)
);

CREATE TABLE hospitalization_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES hospitalization (id)
);

CREATE TABLE hospitalization_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES hospitalization (id)
);

CREATE TABLE hospitalization_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES hospitalization (id)
);

CREATE TABLE hospitalization_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES hospitalization (id)
);

CREATE TABLE hospitalization_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES hospitalization (id)
);

CREATE TABLE human_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES human (id)
);

CREATE TABLE human_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES human (id)
);

CREATE TABLE human_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES human (id)
);

CREATE TABLE human_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES human (id)
);

CREATE TABLE human_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES human (id)
);

CREATE TABLE individual_organism_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES individual_organism (id)
);

CREATE TABLE individual_organism_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES individual_organism (id)
);

CREATE TABLE individual_organism_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES individual_organism (id)
);

CREATE TABLE individual_organism_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES individual_organism (id)
);

CREATE TABLE individual_organism_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES individual_organism (id)
);

CREATE TABLE invertebrate_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES invertebrate (id)
);

CREATE TABLE invertebrate_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES invertebrate (id)
);

CREATE TABLE invertebrate_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES invertebrate (id)
);

CREATE TABLE invertebrate_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES invertebrate (id)
);

CREATE TABLE invertebrate_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES invertebrate (id)
);

CREATE TABLE journal_article_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES journal_article (id)
);

CREATE TABLE journal_article_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES journal_article (id)
);

CREATE TABLE journal_article_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES journal_article (id)
);

CREATE TABLE journal_article_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES journal_article (id)
);

CREATE TABLE journal_article_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES journal_article (id)
);

CREATE TABLE journal_article_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES journal_article (id)
);

CREATE TABLE journal_article_mesh_terms (
	backref_id TEXT, 
	mesh_terms TEXT, 
	PRIMARY KEY (backref_id, mesh_terms), 
	FOREIGN KEY(backref_id) REFERENCES journal_article (id)
);

CREATE TABLE journal_article_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES journal_article (id)
);

CREATE TABLE journal_article_publication_type (
	backref_id TEXT, 
	publication_type TEXT NOT NULL, 
	PRIMARY KEY (backref_id, publication_type), 
	FOREIGN KEY(backref_id) REFERENCES journal_article (id)
);

CREATE TABLE life_stage_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES life_stage (id)
);

CREATE TABLE life_stage_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES life_stage (id)
);

CREATE TABLE life_stage_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES life_stage (id)
);

CREATE TABLE life_stage_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES life_stage (id)
);

CREATE TABLE life_stage_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES life_stage (id)
);

CREATE TABLE log_odds_analysis_result_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES log_odds_analysis_result (id)
);

CREATE TABLE log_odds_analysis_result_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES log_odds_analysis_result (id)
);

CREATE TABLE log_odds_analysis_result_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES log_odds_analysis_result (id)
);

CREATE TABLE log_odds_analysis_result_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES log_odds_analysis_result (id)
);

CREATE TABLE log_odds_analysis_result_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES log_odds_analysis_result (id)
);

CREATE TABLE macromolecular_complex_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_complex (id)
);

CREATE TABLE macromolecular_complex_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_complex (id)
);

CREATE TABLE macromolecular_complex_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_complex (id)
);

CREATE TABLE macromolecular_complex_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_complex (id)
);

CREATE TABLE macromolecular_complex_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_complex (id)
);

CREATE TABLE mammal_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES mammal (id)
);

CREATE TABLE mammal_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES mammal (id)
);

CREATE TABLE mammal_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES mammal (id)
);

CREATE TABLE mammal_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES mammal (id)
);

CREATE TABLE mammal_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES mammal (id)
);

CREATE TABLE material_sample_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES material_sample (id)
);

CREATE TABLE material_sample_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES material_sample (id)
);

CREATE TABLE material_sample_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES material_sample (id)
);

CREATE TABLE material_sample_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES material_sample (id)
);

CREATE TABLE material_sample_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES material_sample (id)
);

CREATE TABLE "microRNA_type" (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES "microRNA" (id)
);

CREATE TABLE "microRNA_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "microRNA" (id)
);

CREATE TABLE "microRNA_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "microRNA" (id)
);

CREATE TABLE "microRNA_synonym" (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES "microRNA" (id)
);

CREATE TABLE "microRNA_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "microRNA" (id)
);

CREATE TABLE molecular_activity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity (id)
);

CREATE TABLE molecular_activity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity (id)
);

CREATE TABLE molecular_activity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity (id)
);

CREATE TABLE molecular_activity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity (id)
);

CREATE TABLE molecular_activity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity (id)
);

CREATE TABLE molecular_activity_enabled_by (
	backref_id TEXT, 
	enabled_by TEXT, 
	PRIMARY KEY (backref_id, enabled_by), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity (id)
);

CREATE TABLE named_thing_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES named_thing (id)
);

CREATE TABLE named_thing_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES named_thing (id)
);

CREATE TABLE named_thing_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES named_thing (id)
);

CREATE TABLE named_thing_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES named_thing (id)
);

CREATE TABLE named_thing_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES named_thing (id)
);

CREATE TABLE "noncoding_RNA_product_type" (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES "noncoding_RNA_product" (id)
);

CREATE TABLE "noncoding_RNA_product_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "noncoding_RNA_product" (id)
);

CREATE TABLE "noncoding_RNA_product_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "noncoding_RNA_product" (id)
);

CREATE TABLE "noncoding_RNA_product_synonym" (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES "noncoding_RNA_product" (id)
);

CREATE TABLE "noncoding_RNA_product_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "noncoding_RNA_product" (id)
);

CREATE TABLE nucleic_acid_sequence_motif_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_sequence_motif (id)
);

CREATE TABLE nucleic_acid_sequence_motif_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_sequence_motif (id)
);

CREATE TABLE nucleic_acid_sequence_motif_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_sequence_motif (id)
);

CREATE TABLE nucleic_acid_sequence_motif_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_sequence_motif (id)
);

CREATE TABLE nucleic_acid_sequence_motif_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_sequence_motif (id)
);

CREATE TABLE nucleosome_modification_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES nucleosome_modification (id)
);

CREATE TABLE nucleosome_modification_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES nucleosome_modification (id)
);

CREATE TABLE nucleosome_modification_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES nucleosome_modification (id)
);

CREATE TABLE nucleosome_modification_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES nucleosome_modification (id)
);

CREATE TABLE nucleosome_modification_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES nucleosome_modification (id)
);

CREATE TABLE observed_expected_frequency_analysis_result_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES observed_expected_frequency_analysis_result (id)
);

CREATE TABLE observed_expected_frequency_analysis_result_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES observed_expected_frequency_analysis_result (id)
);

CREATE TABLE observed_expected_frequency_analysis_result_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES observed_expected_frequency_analysis_result (id)
);

CREATE TABLE observed_expected_frequency_analysis_result_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES observed_expected_frequency_analysis_result (id)
);

CREATE TABLE observed_expected_frequency_analysis_result_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES observed_expected_frequency_analysis_result (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_gene_to_gene_interaction (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_gene_to_gene_interaction (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_gene_to_gene_interaction (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_gene_to_gene_interaction (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_gene_to_gene_interaction (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_gene_to_gene_interaction (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_gene_to_gene_interaction (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_gene_to_gene_interaction (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_gene_to_gene_interaction (id)
);

CREATE TABLE pairwise_gene_to_gene_interaction_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_gene_to_gene_interaction (id)
);

CREATE TABLE patent_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES patent (id)
);

CREATE TABLE patent_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES patent (id)
);

CREATE TABLE patent_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES patent (id)
);

CREATE TABLE patent_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES patent (id)
);

CREATE TABLE patent_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES patent (id)
);

CREATE TABLE patent_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES patent (id)
);

CREATE TABLE patent_mesh_terms (
	backref_id TEXT, 
	mesh_terms TEXT, 
	PRIMARY KEY (backref_id, mesh_terms), 
	FOREIGN KEY(backref_id) REFERENCES patent (id)
);

CREATE TABLE patent_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES patent (id)
);

CREATE TABLE patent_publication_type (
	backref_id TEXT, 
	publication_type TEXT NOT NULL, 
	PRIMARY KEY (backref_id, publication_type), 
	FOREIGN KEY(backref_id) REFERENCES patent (id)
);

CREATE TABLE pathological_anatomical_structure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES pathological_anatomical_structure (id)
);

CREATE TABLE pathological_anatomical_structure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES pathological_anatomical_structure (id)
);

CREATE TABLE pathological_anatomical_structure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES pathological_anatomical_structure (id)
);

CREATE TABLE pathological_anatomical_structure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES pathological_anatomical_structure (id)
);

CREATE TABLE pathological_anatomical_structure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES pathological_anatomical_structure (id)
);

CREATE TABLE pathological_process_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES pathological_process (id)
);

CREATE TABLE pathological_process_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES pathological_process (id)
);

CREATE TABLE pathological_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES pathological_process (id)
);

CREATE TABLE pathological_process_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES pathological_process (id)
);

CREATE TABLE pathological_process_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES pathological_process (id)
);

CREATE TABLE pathway_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES pathway (id)
);

CREATE TABLE pathway_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES pathway (id)
);

CREATE TABLE pathway_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES pathway (id)
);

CREATE TABLE pathway_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES pathway (id)
);

CREATE TABLE pathway_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES pathway (id)
);

CREATE TABLE phenomenon_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES phenomenon (id)
);

CREATE TABLE phenomenon_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES phenomenon (id)
);

CREATE TABLE phenomenon_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES phenomenon (id)
);

CREATE TABLE phenomenon_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES phenomenon (id)
);

CREATE TABLE phenomenon_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES phenomenon (id)
);

CREATE TABLE phenotypic_feature_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_feature (id)
);

CREATE TABLE phenotypic_feature_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_feature (id)
);

CREATE TABLE phenotypic_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_feature (id)
);

CREATE TABLE phenotypic_feature_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_feature (id)
);

CREATE TABLE phenotypic_feature_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_feature (id)
);

CREATE TABLE physical_entity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES physical_entity (id)
);

CREATE TABLE physical_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES physical_entity (id)
);

CREATE TABLE physical_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES physical_entity (id)
);

CREATE TABLE physical_entity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES physical_entity (id)
);

CREATE TABLE physical_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES physical_entity (id)
);

CREATE TABLE physiological_process_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES physiological_process (id)
);

CREATE TABLE physiological_process_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES physiological_process (id)
);

CREATE TABLE physiological_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES physiological_process (id)
);

CREATE TABLE physiological_process_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES physiological_process (id)
);

CREATE TABLE physiological_process_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES physiological_process (id)
);

CREATE TABLE planetary_entity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES planetary_entity (id)
);

CREATE TABLE planetary_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES planetary_entity (id)
);

CREATE TABLE planetary_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES planetary_entity (id)
);

CREATE TABLE planetary_entity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES planetary_entity (id)
);

CREATE TABLE planetary_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES planetary_entity (id)
);

CREATE TABLE plant_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES plant (id)
);

CREATE TABLE plant_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES plant (id)
);

CREATE TABLE plant_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES plant (id)
);

CREATE TABLE plant_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES plant (id)
);

CREATE TABLE plant_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES plant (id)
);

CREATE TABLE polypeptide_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES polypeptide (id)
);

CREATE TABLE polypeptide_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES polypeptide (id)
);

CREATE TABLE polypeptide_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES polypeptide (id)
);

CREATE TABLE polypeptide_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES polypeptide (id)
);

CREATE TABLE polypeptide_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES polypeptide (id)
);

CREATE TABLE population_of_individual_organisms_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES population_of_individual_organisms (id)
);

CREATE TABLE population_of_individual_organisms_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES population_of_individual_organisms (id)
);

CREATE TABLE population_of_individual_organisms_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES population_of_individual_organisms (id)
);

CREATE TABLE population_of_individual_organisms_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES population_of_individual_organisms (id)
);

CREATE TABLE population_of_individual_organisms_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES population_of_individual_organisms (id)
);

CREATE TABLE posttranslational_modification_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES posttranslational_modification (id)
);

CREATE TABLE posttranslational_modification_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES posttranslational_modification (id)
);

CREATE TABLE posttranslational_modification_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES posttranslational_modification (id)
);

CREATE TABLE posttranslational_modification_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES posttranslational_modification (id)
);

CREATE TABLE posttranslational_modification_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES posttranslational_modification (id)
);

CREATE TABLE preprint_publication_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES preprint_publication (id)
);

CREATE TABLE preprint_publication_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES preprint_publication (id)
);

CREATE TABLE preprint_publication_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES preprint_publication (id)
);

CREATE TABLE preprint_publication_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES preprint_publication (id)
);

CREATE TABLE preprint_publication_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES preprint_publication (id)
);

CREATE TABLE preprint_publication_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES preprint_publication (id)
);

CREATE TABLE preprint_publication_mesh_terms (
	backref_id TEXT, 
	mesh_terms TEXT, 
	PRIMARY KEY (backref_id, mesh_terms), 
	FOREIGN KEY(backref_id) REFERENCES preprint_publication (id)
);

CREATE TABLE preprint_publication_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES preprint_publication (id)
);

CREATE TABLE preprint_publication_publication_type (
	backref_id TEXT, 
	publication_type TEXT NOT NULL, 
	PRIMARY KEY (backref_id, publication_type), 
	FOREIGN KEY(backref_id) REFERENCES preprint_publication (id)
);

CREATE TABLE protein_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES protein (id)
);

CREATE TABLE protein_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES protein (id)
);

CREATE TABLE protein_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES protein (id)
);

CREATE TABLE protein_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES protein (id)
);

CREATE TABLE protein_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES protein (id)
);

CREATE TABLE protein_domain_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES protein_domain (id)
);

CREATE TABLE protein_domain_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES protein_domain (id)
);

CREATE TABLE protein_domain_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES protein_domain (id)
);

CREATE TABLE protein_domain_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES protein_domain (id)
);

CREATE TABLE protein_domain_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES protein_domain (id)
);

CREATE TABLE protein_family_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES protein_family (id)
);

CREATE TABLE protein_family_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES protein_family (id)
);

CREATE TABLE protein_family_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES protein_family (id)
);

CREATE TABLE protein_family_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES protein_family (id)
);

CREATE TABLE protein_family_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES protein_family (id)
);

CREATE TABLE protein_isoform_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES protein_isoform (id)
);

CREATE TABLE protein_isoform_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES protein_isoform (id)
);

CREATE TABLE protein_isoform_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES protein_isoform (id)
);

CREATE TABLE protein_isoform_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES protein_isoform (id)
);

CREATE TABLE protein_isoform_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES protein_isoform (id)
);

CREATE TABLE publication_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_mesh_terms (
	backref_id TEXT, 
	mesh_terms TEXT, 
	PRIMARY KEY (backref_id, mesh_terms), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE publication_publication_type (
	backref_id TEXT, 
	publication_type TEXT NOT NULL, 
	PRIMARY KEY (backref_id, publication_type), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE reagent_targeted_gene_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES reagent_targeted_gene (id)
);

CREATE TABLE reagent_targeted_gene_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES reagent_targeted_gene (id)
);

CREATE TABLE reagent_targeted_gene_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES reagent_targeted_gene (id)
);

CREATE TABLE reagent_targeted_gene_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES reagent_targeted_gene (id)
);

CREATE TABLE reagent_targeted_gene_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES reagent_targeted_gene (id)
);

CREATE TABLE regulatory_region_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES regulatory_region (id)
);

CREATE TABLE regulatory_region_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES regulatory_region (id)
);

CREATE TABLE regulatory_region_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES regulatory_region (id)
);

CREATE TABLE regulatory_region_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES regulatory_region (id)
);

CREATE TABLE regulatory_region_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES regulatory_region (id)
);

CREATE TABLE relative_frequency_analysis_result_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES relative_frequency_analysis_result (id)
);

CREATE TABLE relative_frequency_analysis_result_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES relative_frequency_analysis_result (id)
);

CREATE TABLE relative_frequency_analysis_result_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES relative_frequency_analysis_result (id)
);

CREATE TABLE relative_frequency_analysis_result_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES relative_frequency_analysis_result (id)
);

CREATE TABLE relative_frequency_analysis_result_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES relative_frequency_analysis_result (id)
);

CREATE TABLE retrieval_source_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES retrieval_source (id)
);

CREATE TABLE retrieval_source_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES retrieval_source (id)
);

CREATE TABLE retrieval_source_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES retrieval_source (id)
);

CREATE TABLE retrieval_source_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES retrieval_source (id)
);

CREATE TABLE retrieval_source_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES retrieval_source (id)
);

CREATE TABLE "RNA_product_type" (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES "RNA_product" (id)
);

CREATE TABLE "RNA_product_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "RNA_product" (id)
);

CREATE TABLE "RNA_product_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "RNA_product" (id)
);

CREATE TABLE "RNA_product_synonym" (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES "RNA_product" (id)
);

CREATE TABLE "RNA_product_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "RNA_product" (id)
);

CREATE TABLE "RNA_product_isoform_type" (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES "RNA_product_isoform" (id)
);

CREATE TABLE "RNA_product_isoform_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "RNA_product_isoform" (id)
);

CREATE TABLE "RNA_product_isoform_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "RNA_product_isoform" (id)
);

CREATE TABLE "RNA_product_isoform_synonym" (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES "RNA_product_isoform" (id)
);

CREATE TABLE "RNA_product_isoform_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "RNA_product_isoform" (id)
);

CREATE TABLE sequence_variant_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES sequence_variant (id)
);

CREATE TABLE sequence_variant_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES sequence_variant (id)
);

CREATE TABLE sequence_variant_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES sequence_variant (id)
);

CREATE TABLE sequence_variant_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES sequence_variant (id)
);

CREATE TABLE sequence_variant_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES sequence_variant (id)
);

CREATE TABLE serial_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_mesh_terms (
	backref_id TEXT, 
	mesh_terms TEXT, 
	PRIMARY KEY (backref_id, mesh_terms), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_publication_type (
	backref_id TEXT, 
	publication_type TEXT NOT NULL, 
	PRIMARY KEY (backref_id, publication_type), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE serial_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES serial (id)
);

CREATE TABLE "siRNA_type" (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES "siRNA" (id)
);

CREATE TABLE "siRNA_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "siRNA" (id)
);

CREATE TABLE "siRNA_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "siRNA" (id)
);

CREATE TABLE "siRNA_synonym" (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES "siRNA" (id)
);

CREATE TABLE "siRNA_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "siRNA" (id)
);

CREATE TABLE snv_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES snv (id)
);

CREATE TABLE snv_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES snv (id)
);

CREATE TABLE snv_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES snv (id)
);

CREATE TABLE snv_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES snv (id)
);

CREATE TABLE snv_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES snv (id)
);

CREATE TABLE study_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE study_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE study_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE study_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE study_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE study_population_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES study_population (id)
);

CREATE TABLE study_population_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES study_population (id)
);

CREATE TABLE study_population_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES study_population (id)
);

CREATE TABLE study_population_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES study_population (id)
);

CREATE TABLE study_population_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES study_population (id)
);

CREATE TABLE study_variable_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES study_variable (id)
);

CREATE TABLE study_variable_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES study_variable (id)
);

CREATE TABLE study_variable_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES study_variable (id)
);

CREATE TABLE study_variable_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES study_variable (id)
);

CREATE TABLE study_variable_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES study_variable (id)
);

CREATE TABLE text_mining_result_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES text_mining_result (id)
);

CREATE TABLE text_mining_result_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES text_mining_result (id)
);

CREATE TABLE text_mining_result_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES text_mining_result (id)
);

CREATE TABLE text_mining_result_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES text_mining_result (id)
);

CREATE TABLE text_mining_result_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES text_mining_result (id)
);

CREATE TABLE transcript_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES transcript (id)
);

CREATE TABLE transcript_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES transcript (id)
);

CREATE TABLE transcript_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES transcript (id)
);

CREATE TABLE transcript_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES transcript (id)
);

CREATE TABLE transcript_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES transcript (id)
);

CREATE TABLE transcription_factor_binding_site_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES transcription_factor_binding_site (id)
);

CREATE TABLE transcription_factor_binding_site_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES transcription_factor_binding_site (id)
);

CREATE TABLE transcription_factor_binding_site_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES transcription_factor_binding_site (id)
);

CREATE TABLE transcription_factor_binding_site_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES transcription_factor_binding_site (id)
);

CREATE TABLE transcription_factor_binding_site_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES transcription_factor_binding_site (id)
);

CREATE TABLE treatment_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES treatment (id)
);

CREATE TABLE treatment_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES treatment (id)
);

CREATE TABLE treatment_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES treatment (id)
);

CREATE TABLE treatment_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES treatment (id)
);

CREATE TABLE treatment_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES treatment (id)
);

CREATE TABLE vertebrate_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES vertebrate (id)
);

CREATE TABLE vertebrate_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES vertebrate (id)
);

CREATE TABLE vertebrate_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES vertebrate (id)
);

CREATE TABLE vertebrate_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES vertebrate (id)
);

CREATE TABLE vertebrate_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES vertebrate (id)
);

CREATE TABLE virus_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES virus (id)
);

CREATE TABLE virus_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES virus (id)
);

CREATE TABLE virus_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES virus (id)
);

CREATE TABLE virus_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES virus (id)
);

CREATE TABLE virus_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES virus (id)
);

CREATE TABLE web_page_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES web_page (id)
);

CREATE TABLE web_page_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES web_page (id)
);

CREATE TABLE web_page_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES web_page (id)
);

CREATE TABLE web_page_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES web_page (id)
);

CREATE TABLE web_page_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES web_page (id)
);

CREATE TABLE web_page_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES web_page (id)
);

CREATE TABLE web_page_mesh_terms (
	backref_id TEXT, 
	mesh_terms TEXT, 
	PRIMARY KEY (backref_id, mesh_terms), 
	FOREIGN KEY(backref_id) REFERENCES web_page (id)
);

CREATE TABLE web_page_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES web_page (id)
);

CREATE TABLE web_page_publication_type (
	backref_id TEXT, 
	publication_type TEXT NOT NULL, 
	PRIMARY KEY (backref_id, publication_type), 
	FOREIGN KEY(backref_id) REFERENCES web_page (id)
);

CREATE TABLE behavior_to_behavioral_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES behavior (id), 
	FOREIGN KEY(object) REFERENCES behavioral_feature (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE case_to_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE causal_gene_to_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_aspect_qualifier VARCHAR(22), 
	object_direction_qualifier VARCHAR(13), 
	predicate TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id), 
	FOREIGN KEY(object) REFERENCES disease (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(subject) REFERENCES cell_line (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id)
);

CREATE TABLE chemical_affects_gene_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_form_or_variant_qualifier VARCHAR(29), 
	subject_part_qualifier VARCHAR(11), 
	subject_derivative_qualifier VARCHAR(10), 
	subject_aspect_qualifier VARCHAR(22), 
	subject_context_qualifier TEXT, 
	subject_direction_qualifier VARCHAR(13), 
	object_form_or_variant_qualifier VARCHAR(29), 
	object_part_qualifier VARCHAR(11), 
	object_aspect_qualifier VARCHAR(22), 
	object_context_qualifier TEXT, 
	causal_mechanism_qualifier VARCHAR(30), 
	anatomical_context_qualifier TEXT, 
	qualified_predicate TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	object_direction_qualifier VARCHAR(13), 
	species_context_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject_context_qualifier) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(object_context_qualifier) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(anatomical_context_qualifier) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(subject) REFERENCES chemical_entity (id), 
	FOREIGN KEY(species_context_qualifier) REFERENCES organism_taxon (id)
);

CREATE TABLE complex_molecular_mixture (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	is_supplement TEXT, 
	"highest_FDA_approval_status" TEXT, 
	drug_regulatory_status_world_wide TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES chemical_mixture (id)
);

CREATE TABLE correlated_gene_to_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_aspect_qualifier VARCHAR(22), 
	object_direction_qualifier VARCHAR(13), 
	predicate TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id), 
	FOREIGN KEY(object) REFERENCES disease (id)
);

CREATE TABLE disease_to_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES disease (id), 
	FOREIGN KEY(object) REFERENCES phenotypic_feature (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE drug (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	is_supplement TEXT, 
	"highest_FDA_approval_status" TEXT, 
	drug_regulatory_status_world_wide TEXT, 
	treatment_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES chemical_mixture (id), 
	FOREIGN KEY(treatment_id) REFERENCES treatment (id)
);

CREATE TABLE druggable_gene_to_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_aspect_qualifier VARCHAR(22), 
	object_direction_qualifier VARCHAR(13), 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	object TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id), 
	FOREIGN KEY(object) REFERENCES disease (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE food (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	is_supplement TEXT, 
	"highest_FDA_approval_status" TEXT, 
	drug_regulatory_status_world_wide TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES chemical_mixture (id)
);

CREATE TABLE gene_affects_chemical_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_form_or_variant_qualifier VARCHAR(29), 
	subject_part_qualifier VARCHAR(11), 
	subject_derivative_qualifier TEXT, 
	subject_aspect_qualifier VARCHAR(22), 
	subject_context_qualifier TEXT, 
	subject_direction_qualifier VARCHAR(13), 
	object_form_or_variant_qualifier VARCHAR(29), 
	object_part_qualifier VARCHAR(11), 
	object_aspect_qualifier VARCHAR(22), 
	object_context_qualifier TEXT, 
	causal_mechanism_qualifier VARCHAR(30), 
	anatomical_context_qualifier TEXT, 
	qualified_predicate TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	object_derivative_qualifier VARCHAR(10), 
	object_direction_qualifier VARCHAR(13), 
	species_context_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject_context_qualifier) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(object_context_qualifier) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(anatomical_context_qualifier) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(object) REFERENCES chemical_entity (id), 
	FOREIGN KEY(species_context_qualifier) REFERENCES organism_taxon (id)
);

CREATE TABLE gene_as_a_model_of_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_aspect_qualifier VARCHAR(22), 
	object_direction_qualifier VARCHAR(13), 
	predicate TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	object TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id), 
	FOREIGN KEY(object) REFERENCES disease (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_aspect_qualifier VARCHAR(22), 
	object_direction_qualifier VARCHAR(13), 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	subject_form_or_variant_qualifier TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id), 
	FOREIGN KEY(object) REFERENCES disease (id)
);

CREATE TABLE gene_to_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_aspect_qualifier VARCHAR(22), 
	object_direction_qualifier VARCHAR(13), 
	predicate TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id), 
	FOREIGN KEY(object) REFERENCES disease (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_aspect_qualifier VARCHAR(22), 
	object_direction_qualifier VARCHAR(13), 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES disease_or_phenotypic_feature (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE gene_to_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject_aspect_qualifier VARCHAR(22), 
	object_direction_qualifier VARCHAR(13), 
	predicate TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id), 
	FOREIGN KEY(object) REFERENCES phenotypic_feature (id)
);

CREATE TABLE genomic_sequence_localization (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	start_interbase_coordinate INTEGER, 
	end_interbase_coordinate INTEGER, 
	genome_build VARCHAR(1), 
	strand VARCHAR(1), 
	phase VARCHAR(1), 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES nucleic_acid_entity (id), 
	FOREIGN KEY(object) REFERENCES nucleic_acid_entity (id)
);

CREATE TABLE genotype (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	in_taxon TEXT, 
	in_taxon_label TEXT, 
	has_zygosity TEXT, 
	has_biological_sequence TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_zygosity) REFERENCES zygosity (id)
);

CREATE TABLE genotype_to_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id)
);

CREATE TABLE molecular_mixture (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	is_supplement TEXT, 
	"highest_FDA_approval_status" TEXT, 
	drug_regulatory_status_world_wide TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES chemical_mixture (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	associated_environmental_context TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES organism_taxon (id), 
	FOREIGN KEY(object) REFERENCES organism_taxon (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES organism_taxon (id), 
	FOREIGN KEY(object) REFERENCES organism_taxon (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id)
);

CREATE TABLE pairwise_molecular_interaction (
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	interacting_molecules_category TEXT, 
	subject TEXT NOT NULL, 
	id TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES molecular_entity (id), 
	FOREIGN KEY(object) REFERENCES molecular_entity (id)
);

CREATE TABLE predicate_mapping (
	mapped_predicate TEXT, 
	subject_aspect_qualifier TEXT, 
	subject_direction_qualifier VARCHAR(13), 
	subject_form_or_variant_qualifier TEXT, 
	subject_part_qualifier TEXT, 
	subject_derivative_qualifier TEXT, 
	subject_context_qualifier TEXT, 
	predicate TEXT NOT NULL, 
	qualified_predicate TEXT, 
	object_aspect_qualifier TEXT, 
	object_direction_qualifier VARCHAR(13), 
	object_form_or_variant_qualifier TEXT, 
	object_part_qualifier TEXT, 
	object_derivative_qualifier TEXT, 
	object_context_qualifier TEXT, 
	causal_mechanism_qualifier VARCHAR(30), 
	anatomical_context_qualifier TEXT, 
	species_context_qualifier TEXT, 
	exact_match TEXT, 
	narrow_match TEXT, 
	broad_match TEXT, 
	PRIMARY KEY (mapped_predicate, subject_aspect_qualifier, subject_direction_qualifier, subject_form_or_variant_qualifier, subject_part_qualifier, subject_derivative_qualifier, subject_context_qualifier, predicate, qualified_predicate, object_aspect_qualifier, object_direction_qualifier, object_form_or_variant_qualifier, object_part_qualifier, object_derivative_qualifier, object_context_qualifier, causal_mechanism_qualifier, anatomical_context_qualifier, species_context_qualifier, exact_match, narrow_match, broad_match), 
	FOREIGN KEY(species_context_qualifier) REFERENCES organism_taxon (id)
);

CREATE TABLE processed_material (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	trade_name TEXT, 
	max_tolerated_dose TEXT, 
	is_toxic BOOLEAN, 
	has_chemical_role TEXT, 
	is_supplement TEXT, 
	"highest_FDA_approval_status" TEXT, 
	drug_regulatory_status_world_wide TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trade_name) REFERENCES chemical_entity (id), 
	FOREIGN KEY(is_supplement) REFERENCES chemical_mixture (id)
);

CREATE TABLE reaction_to_catalyst_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	stoichiometry INTEGER, 
	reaction_direction VARCHAR(13), 
	reaction_side VARCHAR(5), 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES molecular_entity (id)
);

CREATE TABLE reaction_to_participant_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	object TEXT NOT NULL, 
	stoichiometry INTEGER, 
	reaction_direction VARCHAR(13), 
	reaction_side VARCHAR(5), 
	subject TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES chemical_entity (id), 
	FOREIGN KEY(subject) REFERENCES molecular_entity (id)
);

CREATE TABLE sequence_feature_relationship (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES nucleic_acid_entity (id), 
	FOREIGN KEY(object) REFERENCES nucleic_acid_entity (id)
);

CREATE TABLE socioeconomic_attribute (
	id TEXT NOT NULL, 
	description TEXT, 
	has_attribute TEXT, 
	full_name TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	socioeconomic_exposure_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES named_thing (id), 
	FOREIGN KEY(socioeconomic_exposure_id) REFERENCES socioeconomic_exposure (id)
);

CREATE TABLE taxon_to_taxon_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES organism_taxon (id), 
	FOREIGN KEY(object) REFERENCES organism_taxon (id)
);

CREATE TABLE variant_as_a_model_of_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	subject TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(subject) REFERENCES sequence_variant (id)
);

CREATE TABLE variant_to_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES named_thing (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id)
);

CREATE TABLE variant_to_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	subject TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(subject) REFERENCES sequence_variant (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_ontogenic_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_ontogenic_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_ontogenic_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_ontogenic_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_ontogenic_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_ontogenic_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_ontogenic_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_ontogenic_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_ontogenic_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_ontogenic_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_ontogenic_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_part_of_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_part_of_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_part_of_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_part_of_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_part_of_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_part_of_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_part_of_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_part_of_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_part_of_association (id)
);

CREATE TABLE anatomical_entity_to_anatomical_entity_part_of_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity_to_anatomical_entity_part_of_association (id)
);

CREATE TABLE association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES association (id)
);

CREATE TABLE attribute_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES attribute (id)
);

CREATE TABLE attribute_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES attribute (id)
);

CREATE TABLE attribute_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES attribute (id)
);

CREATE TABLE attribute_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES attribute (id)
);

CREATE TABLE attribute_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES attribute (id)
);

CREATE TABLE behavioral_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_exposure (id)
);

CREATE TABLE behavioral_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_exposure (id)
);

CREATE TABLE behavioral_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_exposure (id)
);

CREATE TABLE behavioral_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_exposure (id)
);

CREATE TABLE behavioral_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES behavioral_exposure (id)
);

CREATE TABLE biological_sex_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES biological_sex (id)
);

CREATE TABLE biological_sex_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES biological_sex (id)
);

CREATE TABLE biological_sex_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES biological_sex (id)
);

CREATE TABLE biological_sex_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES biological_sex (id)
);

CREATE TABLE biological_sex_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES biological_sex (id)
);

CREATE TABLE biotic_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES biotic_exposure (id)
);

CREATE TABLE biotic_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES biotic_exposure (id)
);

CREATE TABLE biotic_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES biotic_exposure (id)
);

CREATE TABLE biotic_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES biotic_exposure (id)
);

CREATE TABLE biotic_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES biotic_exposure (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE cell_line_to_disease_or_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_assesses_named_thing_association (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_assesses_named_thing_association (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_assesses_named_thing_association (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_assesses_named_thing_association (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_assesses_named_thing_association (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_assesses_named_thing_association (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_assesses_named_thing_association (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_assesses_named_thing_association (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_assesses_named_thing_association (id)
);

CREATE TABLE chemical_entity_assesses_named_thing_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_entity_assesses_named_thing_association (id)
);

CREATE TABLE chemical_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_exposure (id)
);

CREATE TABLE chemical_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES chemical_exposure (id)
);

CREATE TABLE chemical_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES chemical_exposure (id)
);

CREATE TABLE chemical_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES chemical_exposure (id)
);

CREATE TABLE chemical_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_exposure (id)
);

CREATE TABLE chemical_gene_interaction_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES chemical_gene_interaction_association (id)
);

CREATE TABLE chemical_gene_interaction_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES chemical_gene_interaction_association (id)
);

CREATE TABLE chemical_gene_interaction_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_gene_interaction_association (id)
);

CREATE TABLE chemical_gene_interaction_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_gene_interaction_association (id)
);

CREATE TABLE chemical_gene_interaction_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_gene_interaction_association (id)
);

CREATE TABLE chemical_gene_interaction_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_gene_interaction_association (id)
);

CREATE TABLE chemical_gene_interaction_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_gene_interaction_association (id)
);

CREATE TABLE chemical_gene_interaction_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_gene_interaction_association (id)
);

CREATE TABLE chemical_gene_interaction_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_gene_interaction_association (id)
);

CREATE TABLE chemical_gene_interaction_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_gene_interaction_association (id)
);

CREATE TABLE chemical_mixture_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_mixture (id)
);

CREATE TABLE chemical_mixture_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES chemical_mixture (id)
);

CREATE TABLE chemical_mixture_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES chemical_mixture (id)
);

CREATE TABLE chemical_mixture_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES chemical_mixture (id)
);

CREATE TABLE chemical_mixture_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_mixture (id)
);

CREATE TABLE chemical_mixture_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES chemical_mixture (id)
);

CREATE TABLE chemical_mixture_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(27), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES chemical_mixture (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_side_effect_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_role_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_role (id)
);

CREATE TABLE chemical_role_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES chemical_role (id)
);

CREATE TABLE chemical_role_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES chemical_role (id)
);

CREATE TABLE chemical_role_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES chemical_role (id)
);

CREATE TABLE chemical_role_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_role (id)
);

CREATE TABLE chemical_to_chemical_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_association (id)
);

CREATE TABLE chemical_to_chemical_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_association (id)
);

CREATE TABLE chemical_to_chemical_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_association (id)
);

CREATE TABLE chemical_to_chemical_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_association (id)
);

CREATE TABLE chemical_to_chemical_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_association (id)
);

CREATE TABLE chemical_to_chemical_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_association (id)
);

CREATE TABLE chemical_to_chemical_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_association (id)
);

CREATE TABLE chemical_to_chemical_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_association (id)
);

CREATE TABLE chemical_to_chemical_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_association (id)
);

CREATE TABLE chemical_to_chemical_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_chemical_derivation_association_catalyst_qualifier (
	backref_id TEXT, 
	catalyst_qualifier TEXT, 
	PRIMARY KEY (backref_id, catalyst_qualifier), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_chemical_derivation_association (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_to_disease_or_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE chemical_to_pathway_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_pathway_association (id)
);

CREATE TABLE chemical_to_pathway_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_pathway_association (id)
);

CREATE TABLE chemical_to_pathway_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_pathway_association (id)
);

CREATE TABLE chemical_to_pathway_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_pathway_association (id)
);

CREATE TABLE chemical_to_pathway_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_pathway_association (id)
);

CREATE TABLE chemical_to_pathway_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_pathway_association (id)
);

CREATE TABLE chemical_to_pathway_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_pathway_association (id)
);

CREATE TABLE chemical_to_pathway_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_pathway_association (id)
);

CREATE TABLE chemical_to_pathway_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_pathway_association (id)
);

CREATE TABLE chemical_to_pathway_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_to_pathway_association (id)
);

CREATE TABLE clinical_attribute_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES clinical_attribute (id)
);

CREATE TABLE clinical_attribute_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES clinical_attribute (id)
);

CREATE TABLE clinical_attribute_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES clinical_attribute (id)
);

CREATE TABLE clinical_attribute_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES clinical_attribute (id)
);

CREATE TABLE clinical_attribute_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES clinical_attribute (id)
);

CREATE TABLE clinical_course_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES clinical_course (id)
);

CREATE TABLE clinical_course_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES clinical_course (id)
);

CREATE TABLE clinical_course_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES clinical_course (id)
);

CREATE TABLE clinical_course_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES clinical_course (id)
);

CREATE TABLE clinical_course_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES clinical_course (id)
);

CREATE TABLE clinical_measurement_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES clinical_measurement (id)
);

CREATE TABLE clinical_measurement_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES clinical_measurement (id)
);

CREATE TABLE clinical_measurement_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES clinical_measurement (id)
);

CREATE TABLE clinical_measurement_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES clinical_measurement (id)
);

CREATE TABLE clinical_measurement_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES clinical_measurement (id)
);

CREATE TABLE clinical_modifier_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES clinical_modifier (id)
);

CREATE TABLE clinical_modifier_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES clinical_modifier (id)
);

CREATE TABLE clinical_modifier_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES clinical_modifier (id)
);

CREATE TABLE clinical_modifier_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES clinical_modifier (id)
);

CREATE TABLE clinical_modifier_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES clinical_modifier (id)
);

CREATE TABLE complex_chemical_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES complex_chemical_exposure (id)
);

CREATE TABLE complex_chemical_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES complex_chemical_exposure (id)
);

CREATE TABLE complex_chemical_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES complex_chemical_exposure (id)
);

CREATE TABLE complex_chemical_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES complex_chemical_exposure (id)
);

CREATE TABLE complex_chemical_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES complex_chemical_exposure (id)
);

CREATE TABLE contributor_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE contributor_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE contributor_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE contributor_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE contributor_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE contributor_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE contributor_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE contributor_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE contributor_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE contributor_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES contributor_association (id)
);

CREATE TABLE dataset_version_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES dataset_version (id)
);

CREATE TABLE dataset_version_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES dataset_version (id)
);

CREATE TABLE dataset_version_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset_version (id)
);

CREATE TABLE dataset_version_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES dataset_version (id)
);

CREATE TABLE dataset_version_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES dataset_version (id)
);

CREATE TABLE device_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES device (id)
);

CREATE TABLE device_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES device (id)
);

CREATE TABLE device_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES device (id)
);

CREATE TABLE device_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES device (id)
);

CREATE TABLE device_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES device (id)
);

CREATE TABLE disease_or_phenotypic_feature_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_exposure (id)
);

CREATE TABLE disease_or_phenotypic_feature_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_exposure (id)
);

CREATE TABLE disease_or_phenotypic_feature_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_exposure (id)
);

CREATE TABLE disease_or_phenotypic_feature_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_exposure (id)
);

CREATE TABLE disease_or_phenotypic_feature_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_exposure (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_genetic_inheritance_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_genetic_inheritance_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_genetic_inheritance_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_genetic_inheritance_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_genetic_inheritance_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_genetic_inheritance_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_genetic_inheritance_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_genetic_inheritance_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_genetic_inheritance_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_genetic_inheritance_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_genetic_inheritance_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_location_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_location_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_location_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_location_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_location_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_location_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_location_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_location_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_location_association (id)
);

CREATE TABLE disease_or_phenotypic_feature_to_location_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature_to_location_association (id)
);

CREATE TABLE disease_to_exposure_event_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_exposure_event_association (id)
);

CREATE TABLE disease_to_exposure_event_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_exposure_event_association (id)
);

CREATE TABLE disease_to_exposure_event_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_exposure_event_association (id)
);

CREATE TABLE disease_to_exposure_event_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_exposure_event_association (id)
);

CREATE TABLE disease_to_exposure_event_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_exposure_event_association (id)
);

CREATE TABLE disease_to_exposure_event_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_exposure_event_association (id)
);

CREATE TABLE disease_to_exposure_event_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_exposure_event_association (id)
);

CREATE TABLE disease_to_exposure_event_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_exposure_event_association (id)
);

CREATE TABLE disease_to_exposure_event_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_exposure_event_association (id)
);

CREATE TABLE disease_to_exposure_event_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_exposure_event_association (id)
);

CREATE TABLE drug_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES drug_exposure (id)
);

CREATE TABLE drug_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES drug_exposure (id)
);

CREATE TABLE drug_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES drug_exposure (id)
);

CREATE TABLE drug_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES drug_exposure (id)
);

CREATE TABLE drug_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES drug_exposure (id)
);

CREATE TABLE drug_to_gene_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_association (id)
);

CREATE TABLE drug_to_gene_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_association (id)
);

CREATE TABLE drug_to_gene_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_association (id)
);

CREATE TABLE drug_to_gene_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_association (id)
);

CREATE TABLE drug_to_gene_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_association (id)
);

CREATE TABLE drug_to_gene_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_association (id)
);

CREATE TABLE drug_to_gene_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_association (id)
);

CREATE TABLE drug_to_gene_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_association (id)
);

CREATE TABLE drug_to_gene_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_association (id)
);

CREATE TABLE drug_to_gene_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_association (id)
);

CREATE TABLE drug_to_gene_interaction_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_interaction_exposure (id)
);

CREATE TABLE drug_to_gene_interaction_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_interaction_exposure (id)
);

CREATE TABLE drug_to_gene_interaction_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_interaction_exposure (id)
);

CREATE TABLE drug_to_gene_interaction_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_interaction_exposure (id)
);

CREATE TABLE drug_to_gene_interaction_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES drug_to_gene_interaction_exposure (id)
);

CREATE TABLE entity_to_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_disease_association (id)
);

CREATE TABLE entity_to_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_disease_association (id)
);

CREATE TABLE entity_to_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_disease_association (id)
);

CREATE TABLE entity_to_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_disease_association (id)
);

CREATE TABLE entity_to_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_disease_association (id)
);

CREATE TABLE entity_to_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_disease_association (id)
);

CREATE TABLE entity_to_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_disease_association (id)
);

CREATE TABLE entity_to_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_disease_association (id)
);

CREATE TABLE entity_to_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_disease_association (id)
);

CREATE TABLE entity_to_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_disease_association (id)
);

CREATE TABLE entity_to_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_phenotypic_feature_association (id)
);

CREATE TABLE entity_to_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_phenotypic_feature_association (id)
);

CREATE TABLE entity_to_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_phenotypic_feature_association (id)
);

CREATE TABLE entity_to_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_phenotypic_feature_association (id)
);

CREATE TABLE entity_to_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_phenotypic_feature_association (id)
);

CREATE TABLE entity_to_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_phenotypic_feature_association (id)
);

CREATE TABLE entity_to_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_phenotypic_feature_association (id)
);

CREATE TABLE entity_to_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_phenotypic_feature_association (id)
);

CREATE TABLE entity_to_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_phenotypic_feature_association (id)
);

CREATE TABLE entity_to_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES entity_to_phenotypic_feature_association (id)
);

CREATE TABLE environmental_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES environmental_exposure (id)
);

CREATE TABLE environmental_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES environmental_exposure (id)
);

CREATE TABLE environmental_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES environmental_exposure (id)
);

CREATE TABLE environmental_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES environmental_exposure (id)
);

CREATE TABLE environmental_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES environmental_exposure (id)
);

CREATE TABLE environmental_food_contaminant_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES environmental_food_contaminant (id)
);

CREATE TABLE environmental_food_contaminant_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES environmental_food_contaminant (id)
);

CREATE TABLE environmental_food_contaminant_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES environmental_food_contaminant (id)
);

CREATE TABLE environmental_food_contaminant_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES environmental_food_contaminant (id)
);

CREATE TABLE environmental_food_contaminant_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES environmental_food_contaminant (id)
);

CREATE TABLE environmental_food_contaminant_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES environmental_food_contaminant (id)
);

CREATE TABLE exon_to_transcript_relationship_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES exon_to_transcript_relationship (id)
);

CREATE TABLE exon_to_transcript_relationship_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES exon_to_transcript_relationship (id)
);

CREATE TABLE exon_to_transcript_relationship_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES exon_to_transcript_relationship (id)
);

CREATE TABLE exon_to_transcript_relationship_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES exon_to_transcript_relationship (id)
);

CREATE TABLE exon_to_transcript_relationship_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES exon_to_transcript_relationship (id)
);

CREATE TABLE exon_to_transcript_relationship_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES exon_to_transcript_relationship (id)
);

CREATE TABLE exon_to_transcript_relationship_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES exon_to_transcript_relationship (id)
);

CREATE TABLE exon_to_transcript_relationship_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES exon_to_transcript_relationship (id)
);

CREATE TABLE exon_to_transcript_relationship_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES exon_to_transcript_relationship (id)
);

CREATE TABLE exon_to_transcript_relationship_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES exon_to_transcript_relationship (id)
);

CREATE TABLE exposure_event_to_outcome_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE exposure_event_to_outcome_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE exposure_event_to_outcome_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE exposure_event_to_outcome_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE exposure_event_to_outcome_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE exposure_event_to_outcome_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE exposure_event_to_outcome_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE exposure_event_to_outcome_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE exposure_event_to_outcome_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE exposure_event_to_outcome_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_outcome_association (id)
);

CREATE TABLE food_additive_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES food_additive (id)
);

CREATE TABLE food_additive_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES food_additive (id)
);

CREATE TABLE food_additive_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES food_additive (id)
);

CREATE TABLE food_additive_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES food_additive (id)
);

CREATE TABLE food_additive_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES food_additive (id)
);

CREATE TABLE food_additive_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES food_additive (id)
);

CREATE TABLE gene_to_expression_site_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_expression_site_association (id)
);

CREATE TABLE gene_to_expression_site_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_expression_site_association (id)
);

CREATE TABLE gene_to_expression_site_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_expression_site_association (id)
);

CREATE TABLE gene_to_expression_site_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_expression_site_association (id)
);

CREATE TABLE gene_to_expression_site_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_expression_site_association (id)
);

CREATE TABLE gene_to_expression_site_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_expression_site_association (id)
);

CREATE TABLE gene_to_expression_site_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_expression_site_association (id)
);

CREATE TABLE gene_to_expression_site_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_expression_site_association (id)
);

CREATE TABLE gene_to_expression_site_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_expression_site_association (id)
);

CREATE TABLE gene_to_expression_site_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_expression_site_association (id)
);

CREATE TABLE gene_to_gene_coexpression_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_coexpression_association (id)
);

CREATE TABLE gene_to_gene_coexpression_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_coexpression_association (id)
);

CREATE TABLE gene_to_gene_coexpression_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_coexpression_association (id)
);

CREATE TABLE gene_to_gene_coexpression_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_coexpression_association (id)
);

CREATE TABLE gene_to_gene_coexpression_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_coexpression_association (id)
);

CREATE TABLE gene_to_gene_coexpression_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_coexpression_association (id)
);

CREATE TABLE gene_to_gene_coexpression_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_coexpression_association (id)
);

CREATE TABLE gene_to_gene_coexpression_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_coexpression_association (id)
);

CREATE TABLE gene_to_gene_coexpression_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_coexpression_association (id)
);

CREATE TABLE gene_to_gene_coexpression_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_coexpression_association (id)
);

CREATE TABLE gene_to_gene_family_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_family_association (id)
);

CREATE TABLE gene_to_gene_family_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_family_association (id)
);

CREATE TABLE gene_to_gene_family_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_family_association (id)
);

CREATE TABLE gene_to_gene_family_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_family_association (id)
);

CREATE TABLE gene_to_gene_family_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_family_association (id)
);

CREATE TABLE gene_to_gene_family_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_family_association (id)
);

CREATE TABLE gene_to_gene_family_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_family_association (id)
);

CREATE TABLE gene_to_gene_family_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_family_association (id)
);

CREATE TABLE gene_to_gene_family_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_family_association (id)
);

CREATE TABLE gene_to_gene_family_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_family_association (id)
);

CREATE TABLE gene_to_gene_product_relationship_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_product_relationship (id)
);

CREATE TABLE gene_to_gene_product_relationship_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_product_relationship (id)
);

CREATE TABLE gene_to_gene_product_relationship_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_product_relationship (id)
);

CREATE TABLE gene_to_gene_product_relationship_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_product_relationship (id)
);

CREATE TABLE gene_to_gene_product_relationship_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_product_relationship (id)
);

CREATE TABLE gene_to_gene_product_relationship_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_product_relationship (id)
);

CREATE TABLE gene_to_gene_product_relationship_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_product_relationship (id)
);

CREATE TABLE gene_to_gene_product_relationship_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_product_relationship (id)
);

CREATE TABLE gene_to_gene_product_relationship_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_product_relationship (id)
);

CREATE TABLE gene_to_gene_product_relationship_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_gene_product_relationship (id)
);

CREATE TABLE gene_to_go_term_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_go_term_association (id)
);

CREATE TABLE gene_to_go_term_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_go_term_association (id)
);

CREATE TABLE gene_to_go_term_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_go_term_association (id)
);

CREATE TABLE gene_to_go_term_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_go_term_association (id)
);

CREATE TABLE gene_to_go_term_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_go_term_association (id)
);

CREATE TABLE gene_to_go_term_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_go_term_association (id)
);

CREATE TABLE gene_to_go_term_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_go_term_association (id)
);

CREATE TABLE gene_to_go_term_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_go_term_association (id)
);

CREATE TABLE gene_to_go_term_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_go_term_association (id)
);

CREATE TABLE gene_to_go_term_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_go_term_association (id)
);

CREATE TABLE gene_to_pathway_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_pathway_association (id)
);

CREATE TABLE gene_to_pathway_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_pathway_association (id)
);

CREATE TABLE gene_to_pathway_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_pathway_association (id)
);

CREATE TABLE gene_to_pathway_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_pathway_association (id)
);

CREATE TABLE gene_to_pathway_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_pathway_association (id)
);

CREATE TABLE gene_to_pathway_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_pathway_association (id)
);

CREATE TABLE gene_to_pathway_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_pathway_association (id)
);

CREATE TABLE gene_to_pathway_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_pathway_association (id)
);

CREATE TABLE gene_to_pathway_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_pathway_association (id)
);

CREATE TABLE gene_to_pathway_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_pathway_association (id)
);

CREATE TABLE genomic_background_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genomic_background_exposure (id)
);

CREATE TABLE genomic_background_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES genomic_background_exposure (id)
);

CREATE TABLE genomic_background_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES genomic_background_exposure (id)
);

CREATE TABLE genomic_background_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES genomic_background_exposure (id)
);

CREATE TABLE genomic_background_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genomic_background_exposure (id)
);

CREATE TABLE genotypic_sex_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genotypic_sex (id)
);

CREATE TABLE genotypic_sex_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES genotypic_sex (id)
);

CREATE TABLE genotypic_sex_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES genotypic_sex (id)
);

CREATE TABLE genotypic_sex_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES genotypic_sex (id)
);

CREATE TABLE genotypic_sex_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genotypic_sex (id)
);

CREATE TABLE geographic_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES geographic_exposure (id)
);

CREATE TABLE geographic_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES geographic_exposure (id)
);

CREATE TABLE geographic_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES geographic_exposure (id)
);

CREATE TABLE geographic_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES geographic_exposure (id)
);

CREATE TABLE geographic_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES geographic_exposure (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE information_content_entity_to_named_thing_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity_to_named_thing_association (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_biological_process_association (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_biological_process_association (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_biological_process_association (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_biological_process_association (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_biological_process_association (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_biological_process_association (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_biological_process_association (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_biological_process_association (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_biological_process_association (id)
);

CREATE TABLE macromolecular_machine_to_biological_process_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_biological_process_association (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_cellular_component_association (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_cellular_component_association (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_cellular_component_association (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_cellular_component_association (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_cellular_component_association (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_cellular_component_association (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_cellular_component_association (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_cellular_component_association (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_cellular_component_association (id)
);

CREATE TABLE macromolecular_machine_to_cellular_component_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_cellular_component_association (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_molecular_activity_association (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_molecular_activity_association (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_molecular_activity_association (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_molecular_activity_association (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_molecular_activity_association (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_molecular_activity_association (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_molecular_activity_association (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_molecular_activity_association (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_molecular_activity_association (id)
);

CREATE TABLE macromolecular_machine_to_molecular_activity_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES macromolecular_machine_to_molecular_activity_association (id)
);

CREATE TABLE material_sample_derivation_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_derivation_association (id)
);

CREATE TABLE material_sample_derivation_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_derivation_association (id)
);

CREATE TABLE material_sample_derivation_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_derivation_association (id)
);

CREATE TABLE material_sample_derivation_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_derivation_association (id)
);

CREATE TABLE material_sample_derivation_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_derivation_association (id)
);

CREATE TABLE material_sample_derivation_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_derivation_association (id)
);

CREATE TABLE material_sample_derivation_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_derivation_association (id)
);

CREATE TABLE material_sample_derivation_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_derivation_association (id)
);

CREATE TABLE material_sample_derivation_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_derivation_association (id)
);

CREATE TABLE material_sample_derivation_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_derivation_association (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE material_sample_to_disease_or_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES material_sample_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_chemical_entity_association (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_chemical_entity_association (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_chemical_entity_association (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_chemical_entity_association (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_chemical_entity_association (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_chemical_entity_association (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_chemical_entity_association (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_chemical_entity_association (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_chemical_entity_association (id)
);

CREATE TABLE molecular_activity_to_chemical_entity_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_chemical_entity_association (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_molecular_activity_association (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_molecular_activity_association (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_molecular_activity_association (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_molecular_activity_association (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_molecular_activity_association (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_molecular_activity_association (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_molecular_activity_association (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_molecular_activity_association (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_molecular_activity_association (id)
);

CREATE TABLE molecular_activity_to_molecular_activity_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_molecular_activity_association (id)
);

CREATE TABLE molecular_activity_to_pathway_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_pathway_association (id)
);

CREATE TABLE molecular_activity_to_pathway_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_pathway_association (id)
);

CREATE TABLE molecular_activity_to_pathway_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_pathway_association (id)
);

CREATE TABLE molecular_activity_to_pathway_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_pathway_association (id)
);

CREATE TABLE molecular_activity_to_pathway_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_pathway_association (id)
);

CREATE TABLE molecular_activity_to_pathway_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_pathway_association (id)
);

CREATE TABLE molecular_activity_to_pathway_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_pathway_association (id)
);

CREATE TABLE molecular_activity_to_pathway_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_pathway_association (id)
);

CREATE TABLE molecular_activity_to_pathway_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_pathway_association (id)
);

CREATE TABLE molecular_activity_to_pathway_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES molecular_activity_to_pathway_association (id)
);

CREATE TABLE molecular_entity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES molecular_entity (id)
);

CREATE TABLE molecular_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES molecular_entity (id)
);

CREATE TABLE molecular_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES molecular_entity (id)
);

CREATE TABLE molecular_entity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES molecular_entity (id)
);

CREATE TABLE molecular_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES molecular_entity (id)
);

CREATE TABLE molecular_entity_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES molecular_entity (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES named_thing_associated_with_likelihood_of_named_thing_association (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES named_thing_associated_with_likelihood_of_named_thing_association (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES named_thing_associated_with_likelihood_of_named_thing_association (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES named_thing_associated_with_likelihood_of_named_thing_association (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES named_thing_associated_with_likelihood_of_named_thing_association (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES named_thing_associated_with_likelihood_of_named_thing_association (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES named_thing_associated_with_likelihood_of_named_thing_association (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES named_thing_associated_with_likelihood_of_named_thing_association (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES named_thing_associated_with_likelihood_of_named_thing_association (id)
);

CREATE TABLE named_thing_associated_with_likelihood_of_named_thing_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES named_thing_associated_with_likelihood_of_named_thing_association (id)
);

CREATE TABLE nucleic_acid_entity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_entity (id)
);

CREATE TABLE nucleic_acid_entity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_entity (id)
);

CREATE TABLE nucleic_acid_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_entity (id)
);

CREATE TABLE nucleic_acid_entity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_entity (id)
);

CREATE TABLE nucleic_acid_entity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_entity (id)
);

CREATE TABLE nucleic_acid_entity_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES nucleic_acid_entity (id)
);

CREATE TABLE onset_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES onset (id)
);

CREATE TABLE onset_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES onset (id)
);

CREATE TABLE onset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES onset (id)
);

CREATE TABLE onset_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES onset (id)
);

CREATE TABLE onset_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES onset (id)
);

CREATE TABLE organism_attribute_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES organism_attribute (id)
);

CREATE TABLE organism_attribute_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES organism_attribute (id)
);

CREATE TABLE organism_attribute_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES organism_attribute (id)
);

CREATE TABLE organism_attribute_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES organism_attribute (id)
);

CREATE TABLE organism_attribute_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES organism_attribute (id)
);

CREATE TABLE organism_taxon_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon (id)
);

CREATE TABLE organism_taxon_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon (id)
);

CREATE TABLE organism_taxon_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon (id)
);

CREATE TABLE organism_taxon_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon (id)
);

CREATE TABLE organism_taxon_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon (id)
);

CREATE TABLE organism_to_organism_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES organism_to_organism_association (id)
);

CREATE TABLE organism_to_organism_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES organism_to_organism_association (id)
);

CREATE TABLE organism_to_organism_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_to_organism_association (id)
);

CREATE TABLE organism_to_organism_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_to_organism_association (id)
);

CREATE TABLE organism_to_organism_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_to_organism_association (id)
);

CREATE TABLE organism_to_organism_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_to_organism_association (id)
);

CREATE TABLE organism_to_organism_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_to_organism_association (id)
);

CREATE TABLE organism_to_organism_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_to_organism_association (id)
);

CREATE TABLE organism_to_organism_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES organism_to_organism_association (id)
);

CREATE TABLE organism_to_organism_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES organism_to_organism_association (id)
);

CREATE TABLE pathological_anatomical_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES pathological_anatomical_exposure (id)
);

CREATE TABLE pathological_anatomical_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES pathological_anatomical_exposure (id)
);

CREATE TABLE pathological_anatomical_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES pathological_anatomical_exposure (id)
);

CREATE TABLE pathological_anatomical_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES pathological_anatomical_exposure (id)
);

CREATE TABLE pathological_anatomical_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES pathological_anatomical_exposure (id)
);

CREATE TABLE pathological_process_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES pathological_process_exposure (id)
);

CREATE TABLE pathological_process_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES pathological_process_exposure (id)
);

CREATE TABLE pathological_process_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES pathological_process_exposure (id)
);

CREATE TABLE pathological_process_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES pathological_process_exposure (id)
);

CREATE TABLE pathological_process_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES pathological_process_exposure (id)
);

CREATE TABLE phenotypic_quality_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_quality (id)
);

CREATE TABLE phenotypic_quality_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_quality (id)
);

CREATE TABLE phenotypic_quality_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_quality (id)
);

CREATE TABLE phenotypic_quality_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_quality (id)
);

CREATE TABLE phenotypic_quality_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_quality (id)
);

CREATE TABLE phenotypic_sex_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_sex (id)
);

CREATE TABLE phenotypic_sex_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_sex (id)
);

CREATE TABLE phenotypic_sex_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_sex (id)
);

CREATE TABLE phenotypic_sex_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_sex (id)
);

CREATE TABLE phenotypic_sex_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_sex (id)
);

CREATE TABLE population_to_population_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE population_to_population_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE population_to_population_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE population_to_population_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE population_to_population_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE population_to_population_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE population_to_population_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE population_to_population_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE population_to_population_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE population_to_population_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES population_to_population_association (id)
);

CREATE TABLE procedure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES procedure (id)
);

CREATE TABLE procedure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES procedure (id)
);

CREATE TABLE procedure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES procedure (id)
);

CREATE TABLE procedure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES procedure (id)
);

CREATE TABLE procedure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES procedure (id)
);

CREATE TABLE sequence_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES sequence_association (id)
);

CREATE TABLE sequence_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES sequence_association (id)
);

CREATE TABLE sequence_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_association (id)
);

CREATE TABLE sequence_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_association (id)
);

CREATE TABLE sequence_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_association (id)
);

CREATE TABLE sequence_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_association (id)
);

CREATE TABLE sequence_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_association (id)
);

CREATE TABLE sequence_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_association (id)
);

CREATE TABLE sequence_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES sequence_association (id)
);

CREATE TABLE sequence_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES sequence_association (id)
);

CREATE TABLE severity_value_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES severity_value (id)
);

CREATE TABLE severity_value_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES severity_value (id)
);

CREATE TABLE severity_value_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES severity_value (id)
);

CREATE TABLE severity_value_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES severity_value (id)
);

CREATE TABLE severity_value_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES severity_value (id)
);

CREATE TABLE small_molecule_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES small_molecule (id)
);

CREATE TABLE small_molecule_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES small_molecule (id)
);

CREATE TABLE small_molecule_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES small_molecule (id)
);

CREATE TABLE small_molecule_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES small_molecule (id)
);

CREATE TABLE small_molecule_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES small_molecule (id)
);

CREATE TABLE small_molecule_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES small_molecule (id)
);

CREATE TABLE socioeconomic_exposure_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_exposure (id)
);

CREATE TABLE socioeconomic_exposure_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_exposure (id)
);

CREATE TABLE socioeconomic_exposure_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_exposure (id)
);

CREATE TABLE socioeconomic_exposure_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_exposure (id)
);

CREATE TABLE socioeconomic_exposure_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_exposure (id)
);

CREATE TABLE transcript_to_gene_relationship_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES transcript_to_gene_relationship (id)
);

CREATE TABLE transcript_to_gene_relationship_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES transcript_to_gene_relationship (id)
);

CREATE TABLE transcript_to_gene_relationship_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES transcript_to_gene_relationship (id)
);

CREATE TABLE transcript_to_gene_relationship_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES transcript_to_gene_relationship (id)
);

CREATE TABLE transcript_to_gene_relationship_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES transcript_to_gene_relationship (id)
);

CREATE TABLE transcript_to_gene_relationship_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES transcript_to_gene_relationship (id)
);

CREATE TABLE transcript_to_gene_relationship_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES transcript_to_gene_relationship (id)
);

CREATE TABLE transcript_to_gene_relationship_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES transcript_to_gene_relationship (id)
);

CREATE TABLE transcript_to_gene_relationship_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES transcript_to_gene_relationship (id)
);

CREATE TABLE transcript_to_gene_relationship_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES transcript_to_gene_relationship (id)
);

CREATE TABLE variant_to_gene_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_association (id)
);

CREATE TABLE variant_to_gene_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_association (id)
);

CREATE TABLE variant_to_gene_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_association (id)
);

CREATE TABLE variant_to_gene_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_association (id)
);

CREATE TABLE variant_to_gene_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_association (id)
);

CREATE TABLE variant_to_gene_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_association (id)
);

CREATE TABLE variant_to_gene_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_association (id)
);

CREATE TABLE variant_to_gene_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_association (id)
);

CREATE TABLE variant_to_gene_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_association (id)
);

CREATE TABLE variant_to_gene_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_association (id)
);

CREATE TABLE variant_to_gene_expression_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_expression_association (id)
);

CREATE TABLE variant_to_gene_expression_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_expression_association (id)
);

CREATE TABLE variant_to_gene_expression_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_expression_association (id)
);

CREATE TABLE variant_to_gene_expression_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_expression_association (id)
);

CREATE TABLE variant_to_gene_expression_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_expression_association (id)
);

CREATE TABLE variant_to_gene_expression_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_expression_association (id)
);

CREATE TABLE variant_to_gene_expression_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_expression_association (id)
);

CREATE TABLE variant_to_gene_expression_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_expression_association (id)
);

CREATE TABLE variant_to_gene_expression_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_expression_association (id)
);

CREATE TABLE variant_to_gene_expression_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_gene_expression_association (id)
);

CREATE TABLE variant_to_population_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_population_association (id)
);

CREATE TABLE variant_to_population_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_population_association (id)
);

CREATE TABLE variant_to_population_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_population_association (id)
);

CREATE TABLE variant_to_population_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_population_association (id)
);

CREATE TABLE variant_to_population_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_population_association (id)
);

CREATE TABLE variant_to_population_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_population_association (id)
);

CREATE TABLE variant_to_population_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_population_association (id)
);

CREATE TABLE variant_to_population_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_population_association (id)
);

CREATE TABLE variant_to_population_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_population_association (id)
);

CREATE TABLE variant_to_population_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_population_association (id)
);

CREATE TABLE zygosity_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES zygosity (id)
);

CREATE TABLE zygosity_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES zygosity (id)
);

CREATE TABLE zygosity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES zygosity (id)
);

CREATE TABLE zygosity_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES zygosity (id)
);

CREATE TABLE zygosity_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES zygosity (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	subject TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(subject) REFERENCES genotype (id)
);

CREATE TABLE genotype_to_gene_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	predicate TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES genotype (id), 
	FOREIGN KEY(object) REFERENCES gene (id)
);

CREATE TABLE genotype_to_genotype_part_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	predicate TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES genotype (id), 
	FOREIGN KEY(object) REFERENCES genotype (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	predicate TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	frequency_qualifier TEXT, 
	severity_qualifier TEXT, 
	onset_qualifier TEXT, 
	sex_qualifier TEXT, 
	has_count INTEGER, 
	has_total INTEGER, 
	has_quotient FLOAT, 
	has_percentage FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES named_thing (id), 
	FOREIGN KEY(subject) REFERENCES genotype (id), 
	FOREIGN KEY(severity_qualifier) REFERENCES severity_value (id), 
	FOREIGN KEY(onset_qualifier) REFERENCES onset (id), 
	FOREIGN KEY(sex_qualifier) REFERENCES biological_sex (id)
);

CREATE TABLE genotype_to_variant_association (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	negated BOOLEAN, 
	publications TEXT, 
	has_evidence TEXT, 
	knowledge_source TEXT, 
	primary_knowledge_source TEXT, 
	timepoint TIME, 
	original_subject TEXT, 
	original_predicate TEXT, 
	original_object TEXT, 
	subject_category TEXT, 
	object_category TEXT, 
	subject_namespace TEXT, 
	object_namespace TEXT, 
	retrieval_source_ids TEXT, 
	predicate TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES genotype (id), 
	FOREIGN KEY(object) REFERENCES sequence_variant (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE behavior_to_behavioral_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES behavior_to_behavioral_feature_association (id)
);

CREATE TABLE case_to_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES case_to_phenotypic_feature_association (id)
);

CREATE TABLE case_to_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES case_to_phenotypic_feature_association (id)
);

CREATE TABLE case_to_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES case_to_phenotypic_feature_association (id)
);

CREATE TABLE case_to_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES case_to_phenotypic_feature_association (id)
);

CREATE TABLE case_to_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES case_to_phenotypic_feature_association (id)
);

CREATE TABLE case_to_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES case_to_phenotypic_feature_association (id)
);

CREATE TABLE case_to_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES case_to_phenotypic_feature_association (id)
);

CREATE TABLE case_to_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES case_to_phenotypic_feature_association (id)
);

CREATE TABLE case_to_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES case_to_phenotypic_feature_association (id)
);

CREATE TABLE case_to_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES case_to_phenotypic_feature_association (id)
);

CREATE TABLE causal_gene_to_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES causal_gene_to_disease_association (id)
);

CREATE TABLE causal_gene_to_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES causal_gene_to_disease_association (id)
);

CREATE TABLE causal_gene_to_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES causal_gene_to_disease_association (id)
);

CREATE TABLE causal_gene_to_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES causal_gene_to_disease_association (id)
);

CREATE TABLE causal_gene_to_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES causal_gene_to_disease_association (id)
);

CREATE TABLE causal_gene_to_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES causal_gene_to_disease_association (id)
);

CREATE TABLE causal_gene_to_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES causal_gene_to_disease_association (id)
);

CREATE TABLE causal_gene_to_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES causal_gene_to_disease_association (id)
);

CREATE TABLE causal_gene_to_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES causal_gene_to_disease_association (id)
);

CREATE TABLE causal_gene_to_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES causal_gene_to_disease_association (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_as_a_model_of_disease_association (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_as_a_model_of_disease_association (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_as_a_model_of_disease_association (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_as_a_model_of_disease_association (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_as_a_model_of_disease_association (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_as_a_model_of_disease_association (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_as_a_model_of_disease_association (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_as_a_model_of_disease_association (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_as_a_model_of_disease_association (id)
);

CREATE TABLE cell_line_as_a_model_of_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES cell_line_as_a_model_of_disease_association (id)
);

CREATE TABLE chemical_affects_gene_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES chemical_affects_gene_association (id)
);

CREATE TABLE chemical_affects_gene_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES chemical_affects_gene_association (id)
);

CREATE TABLE chemical_affects_gene_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_affects_gene_association (id)
);

CREATE TABLE chemical_affects_gene_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_affects_gene_association (id)
);

CREATE TABLE chemical_affects_gene_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_affects_gene_association (id)
);

CREATE TABLE chemical_affects_gene_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_affects_gene_association (id)
);

CREATE TABLE chemical_affects_gene_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_affects_gene_association (id)
);

CREATE TABLE chemical_affects_gene_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES chemical_affects_gene_association (id)
);

CREATE TABLE chemical_affects_gene_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES chemical_affects_gene_association (id)
);

CREATE TABLE chemical_affects_gene_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES chemical_affects_gene_association (id)
);

CREATE TABLE complex_molecular_mixture_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES complex_molecular_mixture (id)
);

CREATE TABLE complex_molecular_mixture_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES complex_molecular_mixture (id)
);

CREATE TABLE complex_molecular_mixture_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES complex_molecular_mixture (id)
);

CREATE TABLE complex_molecular_mixture_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES complex_molecular_mixture (id)
);

CREATE TABLE complex_molecular_mixture_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES complex_molecular_mixture (id)
);

CREATE TABLE complex_molecular_mixture_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES complex_molecular_mixture (id)
);

CREATE TABLE complex_molecular_mixture_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(27), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES complex_molecular_mixture (id)
);

CREATE TABLE correlated_gene_to_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES correlated_gene_to_disease_association (id)
);

CREATE TABLE correlated_gene_to_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES correlated_gene_to_disease_association (id)
);

CREATE TABLE correlated_gene_to_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES correlated_gene_to_disease_association (id)
);

CREATE TABLE correlated_gene_to_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES correlated_gene_to_disease_association (id)
);

CREATE TABLE correlated_gene_to_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES correlated_gene_to_disease_association (id)
);

CREATE TABLE correlated_gene_to_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES correlated_gene_to_disease_association (id)
);

CREATE TABLE correlated_gene_to_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES correlated_gene_to_disease_association (id)
);

CREATE TABLE correlated_gene_to_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES correlated_gene_to_disease_association (id)
);

CREATE TABLE correlated_gene_to_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES correlated_gene_to_disease_association (id)
);

CREATE TABLE correlated_gene_to_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES correlated_gene_to_disease_association (id)
);

CREATE TABLE disease_to_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_phenotypic_feature_association (id)
);

CREATE TABLE disease_to_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_phenotypic_feature_association (id)
);

CREATE TABLE disease_to_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_phenotypic_feature_association (id)
);

CREATE TABLE disease_to_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_phenotypic_feature_association (id)
);

CREATE TABLE disease_to_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_phenotypic_feature_association (id)
);

CREATE TABLE disease_to_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_phenotypic_feature_association (id)
);

CREATE TABLE disease_to_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_phenotypic_feature_association (id)
);

CREATE TABLE disease_to_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_phenotypic_feature_association (id)
);

CREATE TABLE disease_to_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_phenotypic_feature_association (id)
);

CREATE TABLE disease_to_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES disease_to_phenotypic_feature_association (id)
);

CREATE TABLE drug_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES drug (id)
);

CREATE TABLE drug_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES drug (id)
);

CREATE TABLE drug_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES drug (id)
);

CREATE TABLE drug_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES drug (id)
);

CREATE TABLE drug_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES drug (id)
);

CREATE TABLE drug_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES drug (id)
);

CREATE TABLE drug_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(27), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES drug (id)
);

CREATE TABLE druggable_gene_to_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE druggable_gene_to_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE druggable_gene_to_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE druggable_gene_to_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE druggable_gene_to_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE druggable_gene_to_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE druggable_gene_to_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE druggable_gene_to_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE druggable_gene_to_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE druggable_gene_to_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE druggable_gene_to_disease_association_has_evidence (
	backref_id TEXT, 
	has_evidence VARCHAR(5), 
	PRIMARY KEY (backref_id, has_evidence), 
	FOREIGN KEY(backref_id) REFERENCES druggable_gene_to_disease_association (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_phenotypic_feature_association (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_phenotypic_feature_association (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_phenotypic_feature_association (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_phenotypic_feature_association (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_phenotypic_feature_association (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_phenotypic_feature_association (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_phenotypic_feature_association (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_phenotypic_feature_association (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_phenotypic_feature_association (id)
);

CREATE TABLE exposure_event_to_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES exposure_event_to_phenotypic_feature_association (id)
);

CREATE TABLE food_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES food (id)
);

CREATE TABLE food_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES food (id)
);

CREATE TABLE food_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES food (id)
);

CREATE TABLE food_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES food (id)
);

CREATE TABLE food_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES food (id)
);

CREATE TABLE food_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES food (id)
);

CREATE TABLE food_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(27), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES food (id)
);

CREATE TABLE gene_affects_chemical_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_affects_chemical_association (id)
);

CREATE TABLE gene_affects_chemical_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_affects_chemical_association (id)
);

CREATE TABLE gene_affects_chemical_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_affects_chemical_association (id)
);

CREATE TABLE gene_affects_chemical_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_affects_chemical_association (id)
);

CREATE TABLE gene_affects_chemical_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_affects_chemical_association (id)
);

CREATE TABLE gene_affects_chemical_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_affects_chemical_association (id)
);

CREATE TABLE gene_affects_chemical_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_affects_chemical_association (id)
);

CREATE TABLE gene_affects_chemical_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_affects_chemical_association (id)
);

CREATE TABLE gene_affects_chemical_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_affects_chemical_association (id)
);

CREATE TABLE gene_affects_chemical_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_affects_chemical_association (id)
);

CREATE TABLE gene_as_a_model_of_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_as_a_model_of_disease_association (id)
);

CREATE TABLE gene_as_a_model_of_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_as_a_model_of_disease_association (id)
);

CREATE TABLE gene_as_a_model_of_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_as_a_model_of_disease_association (id)
);

CREATE TABLE gene_as_a_model_of_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_as_a_model_of_disease_association (id)
);

CREATE TABLE gene_as_a_model_of_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_as_a_model_of_disease_association (id)
);

CREATE TABLE gene_as_a_model_of_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_as_a_model_of_disease_association (id)
);

CREATE TABLE gene_as_a_model_of_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_as_a_model_of_disease_association (id)
);

CREATE TABLE gene_as_a_model_of_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_as_a_model_of_disease_association (id)
);

CREATE TABLE gene_as_a_model_of_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_as_a_model_of_disease_association (id)
);

CREATE TABLE gene_as_a_model_of_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_as_a_model_of_disease_association (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_has_variant_that_contributes_to_disease_association (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_has_variant_that_contributes_to_disease_association (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_has_variant_that_contributes_to_disease_association (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_has_variant_that_contributes_to_disease_association (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_has_variant_that_contributes_to_disease_association (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_has_variant_that_contributes_to_disease_association (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_has_variant_that_contributes_to_disease_association (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_has_variant_that_contributes_to_disease_association (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_has_variant_that_contributes_to_disease_association (id)
);

CREATE TABLE gene_has_variant_that_contributes_to_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_has_variant_that_contributes_to_disease_association (id)
);

CREATE TABLE gene_to_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_association (id)
);

CREATE TABLE gene_to_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_association (id)
);

CREATE TABLE gene_to_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_association (id)
);

CREATE TABLE gene_to_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_association (id)
);

CREATE TABLE gene_to_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_association (id)
);

CREATE TABLE gene_to_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_association (id)
);

CREATE TABLE gene_to_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_association (id)
);

CREATE TABLE gene_to_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_association (id)
);

CREATE TABLE gene_to_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_association (id)
);

CREATE TABLE gene_to_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_association (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_disease_or_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_disease_or_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_phenotypic_feature_association (id)
);

CREATE TABLE gene_to_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES gene_to_phenotypic_feature_association (id)
);

CREATE TABLE genomic_sequence_localization_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES genomic_sequence_localization (id)
);

CREATE TABLE genomic_sequence_localization_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES genomic_sequence_localization (id)
);

CREATE TABLE genomic_sequence_localization_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES genomic_sequence_localization (id)
);

CREATE TABLE genomic_sequence_localization_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES genomic_sequence_localization (id)
);

CREATE TABLE genomic_sequence_localization_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genomic_sequence_localization (id)
);

CREATE TABLE genomic_sequence_localization_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genomic_sequence_localization (id)
);

CREATE TABLE genomic_sequence_localization_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genomic_sequence_localization (id)
);

CREATE TABLE genomic_sequence_localization_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genomic_sequence_localization (id)
);

CREATE TABLE genomic_sequence_localization_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genomic_sequence_localization (id)
);

CREATE TABLE genomic_sequence_localization_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genomic_sequence_localization (id)
);

CREATE TABLE genotype_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genotype (id)
);

CREATE TABLE genotype_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES genotype (id)
);

CREATE TABLE genotype_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES genotype (id)
);

CREATE TABLE genotype_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES genotype (id)
);

CREATE TABLE genotype_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genotype (id)
);

CREATE TABLE genotype_to_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_disease_association (id)
);

CREATE TABLE genotype_to_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_disease_association (id)
);

CREATE TABLE genotype_to_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_disease_association (id)
);

CREATE TABLE genotype_to_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_disease_association (id)
);

CREATE TABLE genotype_to_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_disease_association (id)
);

CREATE TABLE genotype_to_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_disease_association (id)
);

CREATE TABLE genotype_to_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_disease_association (id)
);

CREATE TABLE genotype_to_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_disease_association (id)
);

CREATE TABLE genotype_to_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_disease_association (id)
);

CREATE TABLE genotype_to_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_disease_association (id)
);

CREATE TABLE molecular_mixture_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES molecular_mixture (id)
);

CREATE TABLE molecular_mixture_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES molecular_mixture (id)
);

CREATE TABLE molecular_mixture_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES molecular_mixture (id)
);

CREATE TABLE molecular_mixture_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES molecular_mixture (id)
);

CREATE TABLE molecular_mixture_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES molecular_mixture (id)
);

CREATE TABLE molecular_mixture_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES molecular_mixture (id)
);

CREATE TABLE molecular_mixture_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(27), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES molecular_mixture (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_interaction (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_interaction (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_interaction (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_interaction (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_interaction (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_interaction (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_interaction (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_interaction (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_interaction (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_interaction_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_interaction (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_specialization (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_specialization (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_specialization (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_specialization (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_specialization (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_specialization (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_specialization (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_specialization (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_specialization (id)
);

CREATE TABLE organism_taxon_to_organism_taxon_specialization_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES organism_taxon_to_organism_taxon_specialization (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES organismal_entity_as_a_model_of_disease_association (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES organismal_entity_as_a_model_of_disease_association (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES organismal_entity_as_a_model_of_disease_association (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES organismal_entity_as_a_model_of_disease_association (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES organismal_entity_as_a_model_of_disease_association (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES organismal_entity_as_a_model_of_disease_association (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES organismal_entity_as_a_model_of_disease_association (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES organismal_entity_as_a_model_of_disease_association (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES organismal_entity_as_a_model_of_disease_association (id)
);

CREATE TABLE organismal_entity_as_a_model_of_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES organismal_entity_as_a_model_of_disease_association (id)
);

CREATE TABLE pairwise_molecular_interaction_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_molecular_interaction (id)
);

CREATE TABLE pairwise_molecular_interaction_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_molecular_interaction (id)
);

CREATE TABLE pairwise_molecular_interaction_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_molecular_interaction (id)
);

CREATE TABLE pairwise_molecular_interaction_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_molecular_interaction (id)
);

CREATE TABLE pairwise_molecular_interaction_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_molecular_interaction (id)
);

CREATE TABLE pairwise_molecular_interaction_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_molecular_interaction (id)
);

CREATE TABLE pairwise_molecular_interaction_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_molecular_interaction (id)
);

CREATE TABLE pairwise_molecular_interaction_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_molecular_interaction (id)
);

CREATE TABLE pairwise_molecular_interaction_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_molecular_interaction (id)
);

CREATE TABLE pairwise_molecular_interaction_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES pairwise_molecular_interaction (id)
);

CREATE TABLE processed_material_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE processed_material_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE processed_material_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE processed_material_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE processed_material_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE processed_material_available_from (
	backref_id TEXT, 
	available_from VARCHAR(16), 
	PRIMARY KEY (backref_id, available_from), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE processed_material_routes_of_delivery (
	backref_id TEXT, 
	routes_of_delivery VARCHAR(27), 
	PRIMARY KEY (backref_id, routes_of_delivery), 
	FOREIGN KEY(backref_id) REFERENCES processed_material (id)
);

CREATE TABLE reaction_to_catalyst_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_catalyst_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_catalyst_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_catalyst_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_catalyst_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_catalyst_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_catalyst_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_catalyst_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_catalyst_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_catalyst_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_catalyst_association (id)
);

CREATE TABLE reaction_to_participant_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE reaction_to_participant_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE reaction_to_participant_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE reaction_to_participant_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE reaction_to_participant_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE reaction_to_participant_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE reaction_to_participant_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE reaction_to_participant_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE reaction_to_participant_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE reaction_to_participant_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES reaction_to_participant_association (id)
);

CREATE TABLE sequence_feature_relationship_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES sequence_feature_relationship (id)
);

CREATE TABLE sequence_feature_relationship_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES sequence_feature_relationship (id)
);

CREATE TABLE sequence_feature_relationship_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_feature_relationship (id)
);

CREATE TABLE sequence_feature_relationship_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_feature_relationship (id)
);

CREATE TABLE sequence_feature_relationship_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_feature_relationship (id)
);

CREATE TABLE sequence_feature_relationship_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_feature_relationship (id)
);

CREATE TABLE sequence_feature_relationship_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_feature_relationship (id)
);

CREATE TABLE sequence_feature_relationship_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES sequence_feature_relationship (id)
);

CREATE TABLE sequence_feature_relationship_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES sequence_feature_relationship (id)
);

CREATE TABLE sequence_feature_relationship_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES sequence_feature_relationship (id)
);

CREATE TABLE socioeconomic_attribute_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_attribute (id)
);

CREATE TABLE socioeconomic_attribute_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_attribute (id)
);

CREATE TABLE socioeconomic_attribute_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_attribute (id)
);

CREATE TABLE socioeconomic_attribute_synonym (
	backref_id TEXT, 
	synonym TEXT, 
	PRIMARY KEY (backref_id, synonym), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_attribute (id)
);

CREATE TABLE socioeconomic_attribute_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES socioeconomic_attribute (id)
);

CREATE TABLE taxon_to_taxon_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE taxon_to_taxon_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE taxon_to_taxon_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE taxon_to_taxon_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE taxon_to_taxon_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE taxon_to_taxon_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE taxon_to_taxon_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE taxon_to_taxon_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE taxon_to_taxon_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE taxon_to_taxon_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES taxon_to_taxon_association (id)
);

CREATE TABLE variant_as_a_model_of_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES variant_as_a_model_of_disease_association (id)
);

CREATE TABLE variant_as_a_model_of_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES variant_as_a_model_of_disease_association (id)
);

CREATE TABLE variant_as_a_model_of_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_as_a_model_of_disease_association (id)
);

CREATE TABLE variant_as_a_model_of_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_as_a_model_of_disease_association (id)
);

CREATE TABLE variant_as_a_model_of_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_as_a_model_of_disease_association (id)
);

CREATE TABLE variant_as_a_model_of_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_as_a_model_of_disease_association (id)
);

CREATE TABLE variant_as_a_model_of_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_as_a_model_of_disease_association (id)
);

CREATE TABLE variant_as_a_model_of_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_as_a_model_of_disease_association (id)
);

CREATE TABLE variant_as_a_model_of_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES variant_as_a_model_of_disease_association (id)
);

CREATE TABLE variant_as_a_model_of_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES variant_as_a_model_of_disease_association (id)
);

CREATE TABLE variant_to_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_disease_association (id)
);

CREATE TABLE variant_to_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_disease_association (id)
);

CREATE TABLE variant_to_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_disease_association (id)
);

CREATE TABLE variant_to_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_disease_association (id)
);

CREATE TABLE variant_to_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_disease_association (id)
);

CREATE TABLE variant_to_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_disease_association (id)
);

CREATE TABLE variant_to_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_disease_association (id)
);

CREATE TABLE variant_to_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_disease_association (id)
);

CREATE TABLE variant_to_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_disease_association (id)
);

CREATE TABLE variant_to_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_disease_association (id)
);

CREATE TABLE variant_to_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_phenotypic_feature_association (id)
);

CREATE TABLE variant_to_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_phenotypic_feature_association (id)
);

CREATE TABLE variant_to_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_phenotypic_feature_association (id)
);

CREATE TABLE variant_to_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_phenotypic_feature_association (id)
);

CREATE TABLE variant_to_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_phenotypic_feature_association (id)
);

CREATE TABLE variant_to_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_phenotypic_feature_association (id)
);

CREATE TABLE variant_to_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_phenotypic_feature_association (id)
);

CREATE TABLE variant_to_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_phenotypic_feature_association (id)
);

CREATE TABLE variant_to_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_phenotypic_feature_association (id)
);

CREATE TABLE variant_to_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES variant_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES genotype_as_a_model_of_disease_association (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES genotype_as_a_model_of_disease_association (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_as_a_model_of_disease_association (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_as_a_model_of_disease_association (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_as_a_model_of_disease_association (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_as_a_model_of_disease_association (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_as_a_model_of_disease_association (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_as_a_model_of_disease_association (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genotype_as_a_model_of_disease_association (id)
);

CREATE TABLE genotype_as_a_model_of_disease_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genotype_as_a_model_of_disease_association (id)
);

CREATE TABLE genotype_to_gene_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_gene_association (id)
);

CREATE TABLE genotype_to_gene_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_gene_association (id)
);

CREATE TABLE genotype_to_gene_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_gene_association (id)
);

CREATE TABLE genotype_to_gene_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_gene_association (id)
);

CREATE TABLE genotype_to_gene_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_gene_association (id)
);

CREATE TABLE genotype_to_gene_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_gene_association (id)
);

CREATE TABLE genotype_to_gene_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_gene_association (id)
);

CREATE TABLE genotype_to_gene_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_gene_association (id)
);

CREATE TABLE genotype_to_gene_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_gene_association (id)
);

CREATE TABLE genotype_to_gene_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_gene_association (id)
);

CREATE TABLE genotype_to_genotype_part_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_genotype_part_association (id)
);

CREATE TABLE genotype_to_genotype_part_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_genotype_part_association (id)
);

CREATE TABLE genotype_to_genotype_part_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_genotype_part_association (id)
);

CREATE TABLE genotype_to_genotype_part_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_genotype_part_association (id)
);

CREATE TABLE genotype_to_genotype_part_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_genotype_part_association (id)
);

CREATE TABLE genotype_to_genotype_part_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_genotype_part_association (id)
);

CREATE TABLE genotype_to_genotype_part_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_genotype_part_association (id)
);

CREATE TABLE genotype_to_genotype_part_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_genotype_part_association (id)
);

CREATE TABLE genotype_to_genotype_part_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_genotype_part_association (id)
);

CREATE TABLE genotype_to_genotype_part_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_genotype_part_association (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_to_phenotypic_feature_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_phenotypic_feature_association (id)
);

CREATE TABLE genotype_to_variant_association_qualifiers (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_variant_association (id)
);

CREATE TABLE genotype_to_variant_association_aggregator_knowledge_source (
	backref_id TEXT, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY (backref_id, aggregator_knowledge_source), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_variant_association (id)
);

CREATE TABLE genotype_to_variant_association_subject_closure (
	backref_id TEXT, 
	subject_closure TEXT, 
	PRIMARY KEY (backref_id, subject_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_variant_association (id)
);

CREATE TABLE genotype_to_variant_association_object_closure (
	backref_id TEXT, 
	object_closure TEXT, 
	PRIMARY KEY (backref_id, object_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_variant_association (id)
);

CREATE TABLE genotype_to_variant_association_subject_category_closure (
	backref_id TEXT, 
	subject_category_closure TEXT, 
	PRIMARY KEY (backref_id, subject_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_variant_association (id)
);

CREATE TABLE genotype_to_variant_association_object_category_closure (
	backref_id TEXT, 
	object_category_closure TEXT, 
	PRIMARY KEY (backref_id, object_category_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_variant_association (id)
);

CREATE TABLE genotype_to_variant_association_subject_label_closure (
	backref_id TEXT, 
	subject_label_closure TEXT, 
	PRIMARY KEY (backref_id, subject_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_variant_association (id)
);

CREATE TABLE genotype_to_variant_association_object_label_closure (
	backref_id TEXT, 
	object_label_closure TEXT, 
	PRIMARY KEY (backref_id, object_label_closure), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_variant_association (id)
);

CREATE TABLE genotype_to_variant_association_type (
	backref_id TEXT, 
	type TEXT, 
	PRIMARY KEY (backref_id, type), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_variant_association (id)
);

CREATE TABLE genotype_to_variant_association_category (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES genotype_to_variant_association (id)
);
