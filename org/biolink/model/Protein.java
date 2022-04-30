package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Protein extends Polypeptide {

  private List<String> synonym;
  private List<String> xref;

}