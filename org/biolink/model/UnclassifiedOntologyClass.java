package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  this is used for nodes that are taken from an ontology but are not typed using an existing biolink class
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UnclassifiedOntologyClass extends OntologyClass {


}