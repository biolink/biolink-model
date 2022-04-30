package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */



@Data
@EqualsAndHashCode(callSuper=false)
public class ReactionToParticipantAssociation extends ChemicalToChemicalAssociation {

  private Integer stoichiometry;
  private String reactionDirection;
  private String reactionSide;

}