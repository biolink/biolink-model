package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A chemical entity is a physical entity that pertains to chemistry or biochemistry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ChemicalEntity extends NamedThing {

  private ChemicalEntity tradeName;
  private List<String> availableFrom;
  private String maxToleratedDose;
  private Boolean isToxic;
  private List<ChemicalRole> hasChemicalRole;

}