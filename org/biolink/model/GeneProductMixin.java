package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneProductMixin extends GeneOrGeneProduct {

  private List<String> synonym;
  private List<String> xref;

}