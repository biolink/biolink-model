package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding chemical entities
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstractclass OrganismalEntity extends BiologicalEntity {


}