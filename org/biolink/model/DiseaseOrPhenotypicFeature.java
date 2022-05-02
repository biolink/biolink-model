package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DiseaseOrPhenotypicFeature extends BiologicalEntity {

  private List<OrganismTaxon> inTaxon;

}