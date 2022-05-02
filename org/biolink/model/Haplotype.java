package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A set of zero or more Alleles on a single instance of a Sequence[VMC]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Haplotype extends BiologicalEntity {

  private String hasBiologicalSequence;
  private List<OrganismTaxon> inTaxon;

}