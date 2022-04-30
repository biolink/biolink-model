package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneProductIsoformMixin extends GeneProductMixin {


}