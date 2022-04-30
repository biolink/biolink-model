package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A union of gene locus, gene product, and macromolecular complex mixin. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MacromolecularMachineMixin  {

  private String name;

}