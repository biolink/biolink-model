package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A typed association between two entities, supported by evidence
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Association extends Entity {

  private NamedThing subject;
  private String predicate;
  private NamedThing object;
  private String relation;
  private Boolean negated;
  private List<OntologyClass> qualifiers;
  private List<Publication> publications;
  private List<EvidenceType> hasEvidence;
  private List<InformationResource> knowledgeSource;
  private List<InformationResource> originalKnowledgeSource;
  private List<InformationResource> primaryKnowledgeSource;
  private List<InformationResource> aggregatorKnowledgeSource;

}