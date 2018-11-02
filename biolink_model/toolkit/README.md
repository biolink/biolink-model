# Biolink Model Toolkit

This package has a number of useful methods for validating edge labels and categories.

#### Edge label and category validation:
```python
>>> from biolink_model import toolkit as tk
>>> tk.is_edgelabel('related_to')
True
>>> tk.is_edgelabel('related to')
False
>>> tk.is_category('named thing')
True
>>> tk.is_category('causes')
False
```

#### Ontology mapping:
```python
>>> tk.get_all_by_mapping('SEMMEDDB:AFFECTS')
['decreases_abundance_of', 'decreases_transport_of', 'affects_metabolic_processing_of', 'affects_response_to', 'increases_metabolic_processing_of', 'affects_stability_of', 'affects', 'decreases_stability_of', 'increases_activity_of', 'decreases_degradation_of', 'increases_folding_of', 'decreases_response_to', 'decreases_activity_of', 'increases_expression_of', 'increases_uptake_of', 'increases_synthesis_of', 'affects_uptake_of', 'affects_secretion_of', 'decreases_localization_of', 'decreases_folding_of', 'decreases_metabolic_processing_of', 'decreases_splicing_of', 'increases_localization_of', 'increases_response_to', 'increases_secretion_of', 'decreases_molecular_modification_of', 'affects_splicing_of', 'affects_mutation_rate_of', 'increases_degradation_of', 'decreases_uptake_of', 'affects_abundance_of', 'affects_folding_of', 'increases_abundance_of', 'increases_stability_of', 'affects_molecular_modification_of', 'affects_transport_of', 'increases_molecular_modification_of', 'affects_expression_of', 'decreases_expression_of', 'affects_synthesis_of', 'affects_degradation_of', 'decreases_secretion_of', 'increases_transport_of', 'affects_activity_of', 'increases_mutation_rate_of', 'increases_splicing_of', 'affects_localization_of', 'decreases_synthesis_of', 'decreases_mutation_rate_of']
>>> tk.get_by_mapping('SEMMEDDB:AFFECTS')
'affects'
```
