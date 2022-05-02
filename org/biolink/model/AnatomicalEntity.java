package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A subcellular location, cell type or gross anatomical part
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AnatomicalEntity extends OrganismalEntity {

  private List<OrganismTaxon> inTaxon;

}