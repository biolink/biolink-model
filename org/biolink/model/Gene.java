package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Gene extends BiologicalEntity {

  private String symbol;
  private List<String> synonym;
  private List<String> xref;
  private String hasBiologicalSequence;
  private List<OrganismTaxon> inTaxon;

}