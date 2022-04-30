package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */



@Data
@EqualsAndHashCode(callSuper=false)
public class CellLineAsAModelOfDiseaseAssociation extends CellLineToDiseaseOrPhenotypicFeatureAssociation {

  private SeverityValue severityQualifier;
  private Onset onsetQualifier;
  private String frequencyQualifier;

}