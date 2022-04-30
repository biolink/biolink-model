package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An allele that varies in its sequence from what is considered the reference allele at that locus.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SequenceVariant extends BiologicalEntity {

  private List<Gene> hasGene;
  private String hasBiologicalSequence;
  private List<OrganismTaxon> inTaxon;

}