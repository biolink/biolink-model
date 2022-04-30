package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IndividualOrganism extends OrganismalEntity {

  private List<OrganismTaxon> inTaxon;

}