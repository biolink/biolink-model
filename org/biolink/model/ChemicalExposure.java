package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A chemical exposure is an intake of a particular chemical entity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ChemicalExposure  {

  private List<QuantityValue> hasQuantitativeValue;
  private String timepoint;

}