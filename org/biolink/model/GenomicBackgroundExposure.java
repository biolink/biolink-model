package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GenomicBackgroundExposure  {

  private String timepoint;
  private List<Gene> hasGeneOrGeneProduct;
  private String hasBiologicalSequence;
  private List<OrganismTaxon> inTaxon;

}