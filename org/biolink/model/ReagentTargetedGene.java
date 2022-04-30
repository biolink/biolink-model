package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReagentTargetedGene extends BiologicalEntity {

  private String hasBiologicalSequence;
  private List<OrganismTaxon> inTaxon;

}