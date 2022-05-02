package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ThingWithTaxon  {

  private List<OrganismTaxon> inTaxon;

}