package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  mixin class for any association whose object (target node) is a disease
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EntityToDiseaseAssociationMixin extends EntityToFeatureOrDiseaseQualifiersMixin {


}