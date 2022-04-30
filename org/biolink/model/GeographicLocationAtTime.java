package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  a location that can be described in lat/long coordinates, for a particular time
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeographicLocationAtTime extends GeographicLocation {

  private String timepoint;

}