package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OntologyClass  {


}