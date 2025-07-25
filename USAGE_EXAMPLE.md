# Usage Example: Gene to Disease Statistical Association

## For EBI Gene2Phenotype "limited" confidence associations

The new `gene to disease statistical association` provides a proper biolink model class for representing gene-disease associations with limited confidence that are statistical/correlational rather than causal in nature.

### Before (using generic predicate)
```yaml
- subject: HGNC:1100
  predicate: biolink:related_to  # Too generic
  object: MONDO:0005148
  association_type: gene to disease association  # Doesn't fit well
```

### After (using the new statistical association class)
```yaml
- subject: HGNC:1100
  predicate: biolink:associated_with_likelihood_of  # Appropriate for statistical evidence
  object: MONDO:0005148
  association_type: gene to disease statistical association  # Designed for this use case
```

### More specific examples
```yaml
# For protective associations (decreased likelihood)
- subject: HGNC:2197  # COL1A1
  predicate: biolink:associated_with_decreased_likelihood_of
  object: MONDO:0007947  # Ehlers-Danlos syndrome
  association_type: gene to disease statistical association

# For risk associations (increased likelihood)
- subject: HGNC:1100
  predicate: biolink:associated_with_increased_likelihood_of
  object: MONDO:0005148  # Type 1 diabetes
  association_type: gene to disease statistical association
```

### Mapping EBI Gene2Phenotype confidence levels

| Confidence Level | Recommended Predicate | Association Type |
|------------------|----------------------|------------------|
| limited | `associated_with_likelihood_of` or children | `gene to disease statistical association` |
| moderate/strong/definitive | `causes` or `contributes_to` | `causal gene to disease association` |
| refuted/disputed | (exclude from mapping) | N/A |

This approach follows the guidance in the biolink model comment: "if the relationship of the statement using this predicate is statistical in nature, please use `associated with likelihood` or one of its children."