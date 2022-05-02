package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AnatomicalEntityToAnatomicalEntityPartOfAssociation extends AnatomicalEntityToAnatomicalEntityAssociation {


}