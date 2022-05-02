package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NucleicAcidEntity extends MolecularEntity {

  private String hasBiologicalSequence;
  private List<OrganismTaxon> inTaxon;

}