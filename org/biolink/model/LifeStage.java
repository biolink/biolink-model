package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A stage of development or growth of an organism, including post-natal adult stages
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LifeStage extends OrganismalEntity {

  private List<OrganismTaxon> inTaxon;

}