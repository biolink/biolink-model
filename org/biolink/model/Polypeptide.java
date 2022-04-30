package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based sequence representations of its precise primary structure; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Polypeptide extends BiologicalEntity {

  private List<OrganismTaxon> inTaxon;

}