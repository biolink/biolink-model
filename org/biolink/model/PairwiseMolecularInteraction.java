package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An interaction at the molecular level between two physical entities
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PairwiseMolecularInteraction extends PairwiseGeneToGeneInteraction {

  private OntologyClass interactingMoleculesCategory;

}