package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DrugToGeneInteractionExposure extends DrugExposure {

  private List<Gene> hasGeneOrGeneProduct;

}