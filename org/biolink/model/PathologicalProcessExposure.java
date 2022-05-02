package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A pathological process, when viewed as an exposure, representing a precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PathologicalProcessExposure  {

  private String timepoint;

}