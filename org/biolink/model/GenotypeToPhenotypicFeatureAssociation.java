package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GenotypeToPhenotypicFeatureAssociation extends Association {

  private BiologicalSex sexQualifier;
  private SeverityValue severityQualifier;
  private Onset onsetQualifier;
  private String frequencyQualifier;

}