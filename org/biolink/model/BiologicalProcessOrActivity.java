package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BiologicalProcessOrActivity extends BiologicalEntity {

  private List<BiologicalProcessOrActivity> hasInput;
  private List<BiologicalProcessOrActivity> hasOutput;
  private List<PhysicalEntity> enabledBy;

}