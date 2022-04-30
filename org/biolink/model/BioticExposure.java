package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BioticExposure  {

  private String timepoint;

}