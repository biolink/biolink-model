package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Genotype extends BiologicalEntity {

  private Zygosity hasZygosity;
  private String hasBiologicalSequence;
  private List<OrganismTaxon> inTaxon;

}