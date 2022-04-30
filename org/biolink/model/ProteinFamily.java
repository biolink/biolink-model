package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */



@Data
@EqualsAndHashCode(callSuper=false)
public class ProteinFamily extends BiologicalEntity {

  private List<Gene> hasGeneOrGeneProduct;

}