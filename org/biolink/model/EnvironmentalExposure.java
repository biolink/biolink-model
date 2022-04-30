package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution) and water-born contaminants.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EnvironmentalExposure  {

  private String timepoint;

}