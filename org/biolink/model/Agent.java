package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  person, group, organization or project that provides a piece of information (i.e. a knowledge association)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Agent extends AdministrativeEntity {

  private List<String> affiliation;
  private String address;

}