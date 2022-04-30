package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction IF R has-input C1 AND R has-output C2 AND R enabled-by P AND R type Reaction THENC1 derives-into C2 <<catalyst qualifier P>>
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ChemicalToChemicalDerivationAssociation extends ChemicalToChemicalAssociation {

  private List<MacromolecularMachineMixin> catalystQualifier;

}