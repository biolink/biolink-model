package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  Root Biolink Model class for all things and informational relationships, real or imagined.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstractclass Entity  {

  private String id;
  private String iri;
  private List<String> category;
  private String type;
  private String name;
  private String description;
  private String source;
  private List<Attribute> hasAttribute;

}