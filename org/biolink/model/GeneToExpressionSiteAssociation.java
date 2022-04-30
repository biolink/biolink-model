package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An association between a gene and a gene expression site, possibly qualified by stage/timing info.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneToExpressionSiteAssociation extends Association {

  private LifeStage stageQualifier;
  private OntologyClass quantifierQualifier;

}