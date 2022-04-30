package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PopulationOfIndividualOrganisms extends OrganismalEntity {

  private List<OrganismTaxon> inTaxon;

}