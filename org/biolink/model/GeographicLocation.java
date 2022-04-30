package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  a location that can be described in lat/long coordinates
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeographicLocation extends PlanetaryEntity {

  private Float latitude;
  private Float longitude;

}