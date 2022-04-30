package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExposureEvent  {

  private String timepoint;

}