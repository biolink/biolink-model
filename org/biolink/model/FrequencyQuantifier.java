package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */



@Data
@EqualsAndHashCode(callSuper=false)
public class FrequencyQuantifier extends RelationshipQuantifier {

  private Integer hasCount;
  private Integer hasTotal;
  private Float hasQuotient;
  private Float hasPercentage;

}