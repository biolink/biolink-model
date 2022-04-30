package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An association between an mixture behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BehaviorToBehavioralFeatureAssociation extends Association {

  private BiologicalSex sexQualifier;
  private SeverityValue severityQualifier;
  private Onset onsetQualifier;
  private String frequencyQualifier;

}