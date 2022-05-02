package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class QuantityValue extends Annotation {

  private String hasUnit;
  private Float hasNumericValue;

}