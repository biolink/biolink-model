package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExposureEventToPhenotypicFeatureAssociation extends Association {

  private BiologicalSex sexQualifier;
  private SeverityValue severityQualifier;
  private Onset onsetQualifier;
  private String frequencyQualifier;

}