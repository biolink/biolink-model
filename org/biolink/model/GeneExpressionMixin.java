package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the expression occurs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneExpressionMixin  {

  private OntologyClass quantifierQualifier;
  private AnatomicalEntity expressionSite;
  private LifeStage stageQualifier;
  private DiseaseOrPhenotypicFeature phenotypicState;

}