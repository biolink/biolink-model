package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */



@Data
@EqualsAndHashCode(callSuper=false)
public class RNAProduct extends Transcript {

  private List<String> synonym;
  private List<String> xref;

}