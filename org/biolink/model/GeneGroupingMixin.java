package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  any grouping of multiple genes or gene products
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneGroupingMixin  {

  private List<Gene> hasGeneOrGeneProduct;

}