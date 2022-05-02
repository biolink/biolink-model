package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A chemical mixture is a chemical entity composed of two or more molecular entities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ChemicalMixture extends ChemicalEntity {

  private ChemicalMixture isSupplement;
  private String highestFDAApprovalStatus;
  private String drugRegulatoryStatusWorldWide;
  private List<String> routesOfDelivery;

}