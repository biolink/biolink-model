package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An interaction relationship between two taxa. This may be a symbiotic relationship (encompassing mutualism and parasitism), or it may be non-symbiotic. Example: plague transmitted_by flea; cattle domesticated_by Homo sapiens; plague infects Homo sapiens
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrganismTaxonToOrganismTaxonInteraction extends OrganismTaxonToOrganismTaxonAssociation {

  private String associatedEnvironmentalContext;

}