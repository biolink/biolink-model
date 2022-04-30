package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A conserved part of protein sequence and (tertiary) structure that can evolve, function, and exist independently of the rest of the protein chain. Protein domains maintain their structure and function independently of the proteins in which they are found. e.g. an SH3 domain.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProteinDomain extends BiologicalEntity {

  private List<Gene> hasGeneOrGeneProduct;

}