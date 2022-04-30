package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneToGeneHomologyAssociation extends GeneToGeneAssociation {


}