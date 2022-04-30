package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  An association between an exposure event and an outcome.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExposureEventToOutcomeAssociation extends Association {

  private PopulationOfIndividualOrganisms hasPopulationContext;
  private String hasTemporalContext;

}