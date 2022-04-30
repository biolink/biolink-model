package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  association between a named thing and a information content entity where the specific context of the relationship between that named thing and the publication is unknown. For example, model organisms databases often capture the knowledge that a gene is found in a journal article, but not specifically the context in which that gene was documented in the article. In these cases, this association with the accompanying predicate 'mentions' could be used. Conversely, for more specific associations (like 'gene to disease association', the publication should be captured as an edge property).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InformationContentEntityToNamedThingAssociation extends Association {


}