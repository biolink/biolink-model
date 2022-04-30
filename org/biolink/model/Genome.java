package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A genome is the sum of genetic material within a cell or virion.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Genome extends BiologicalEntity {

  private String hasBiologicalSequence;
  private List<OrganismTaxon> inTaxon;

}