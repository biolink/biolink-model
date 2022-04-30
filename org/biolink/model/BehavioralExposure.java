package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A behavioral exposure is a factor relating to behavior impacting an individual.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BehavioralExposure  {

  private String timepoint;

}