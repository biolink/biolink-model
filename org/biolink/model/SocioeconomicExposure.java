package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SocioeconomicExposure  {

  private String timepoint;

}