package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A molecular entity is a chemical entity composed of individual or covalently bonded atoms.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MolecularEntity extends ChemicalEntity {

  private Boolean isMetabolite;

}