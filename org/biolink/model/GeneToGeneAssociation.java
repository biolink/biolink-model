package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstractclass GeneToGeneAssociation extends Association {


}