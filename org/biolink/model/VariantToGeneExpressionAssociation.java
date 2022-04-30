package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An association between a variant and expression of a gene (i.e. e-QTL)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VariantToGeneExpressionAssociation extends VariantToGeneAssociation {

  private OntologyClass quantifierQualifier;
  private AnatomicalEntity expressionSite;
  private LifeStage stageQualifier;
  private DiseaseOrPhenotypicFeature phenotypicState;

}