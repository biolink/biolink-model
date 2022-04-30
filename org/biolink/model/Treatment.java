package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices and/or procedures
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Treatment extends NamedThing {

  private List<Drug> hasDrug;
  private List<Device> hasDevice;
  private List<Procedure> hasProcedure;
  private String timepoint;

}