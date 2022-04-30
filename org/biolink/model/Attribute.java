package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Attribute extends Annotation {

  private String name;
  private OntologyClass hasAttributeType;
  private List<QuantityValue> hasQuantitativeValue;
  private NamedThing hasQualitativeValue;
  private String iri;
  private String source;

}