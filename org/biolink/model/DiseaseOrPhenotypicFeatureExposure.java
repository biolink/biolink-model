package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin pigmentation predisposing an individual to skin cancer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DiseaseOrPhenotypicFeatureExposure  {

  private String timepoint;

}