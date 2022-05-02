package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CaseToPhenotypicFeatureAssociation extends Association {

  private BiologicalSex sexQualifier;
  private SeverityValue severityQualifier;
  private Onset onsetQualifier;
  private String frequencyQualifier;

}