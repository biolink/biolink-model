package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DiseaseToPhenotypicFeatureAssociation extends Association {

  private BiologicalSex sexQualifier;
  private SeverityValue severityQualifier;
  private Onset onsetQualifier;
  private String frequencyQualifier;

}