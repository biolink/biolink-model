package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  a piece of information that typically describes some topic of discourse or is used as support.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstractclass InformationContentEntity extends NamedThing {

  private String license;
  private String rights;
  private String format;
  private String creationDate;

}