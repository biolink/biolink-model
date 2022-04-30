package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An association between a variant and a population, where the variant has particular frequency in the population
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VariantToPopulationAssociation extends Association {

  private Integer hasCount;
  private Integer hasTotal;
  private Float hasQuotient;
  private Float hasPercentage;
  private String frequencyQualifier;

}