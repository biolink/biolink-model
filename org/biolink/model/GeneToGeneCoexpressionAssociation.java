package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  Indicates that two genes are co-expressed, generally under the same conditions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneToGeneCoexpressionAssociation extends GeneToGeneAssociation {

  private OntologyClass quantifierQualifier;
  private AnatomicalEntity expressionSite;
  private LifeStage stageQualifier;
  private DiseaseOrPhenotypicFeature phenotypicState;

}