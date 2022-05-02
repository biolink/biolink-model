package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A clinical measurement is a special kind of attribute which results from a laboratory observation from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ClinicalMeasurement extends ClinicalAttribute {


}