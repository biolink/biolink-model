package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  a databased entity or concept/class
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NamedThing extends Entity {

  private List<String> providedBy;

}