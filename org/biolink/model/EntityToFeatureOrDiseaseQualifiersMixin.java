package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  Qualifiers for entity to disease or phenotype associations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EntityToFeatureOrDiseaseQualifiersMixin extends FrequencyQualifierMixin {

  private SeverityValue severityQualifier;
  private Onset onsetQualifier;

}