package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PathologicalAnatomicalExposure  {

  private String timepoint;

}