package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstractclass SequenceVariantModulatesTreatmentAssociation extends Association {


}