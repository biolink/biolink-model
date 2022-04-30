package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ChemicalEntityOrGeneOrGeneProduct  {


}