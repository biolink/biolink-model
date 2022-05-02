package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PairwiseGeneToGeneInteraction extends GeneToGeneAssociation {


}