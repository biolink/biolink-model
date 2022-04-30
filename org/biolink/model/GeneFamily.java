package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  any grouping of multiple genes or gene products related by common descent
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneFamily extends BiologicalEntity {

  private List<Gene> hasGeneOrGeneProduct;

}