package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GenotypeToGeneAssociation extends Association {


}