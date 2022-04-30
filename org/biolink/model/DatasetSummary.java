package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  an item that holds summary level information about a dataset.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DatasetSummary extends InformationContentEntity {

  private String sourceWebPage;
  private String sourceLogo;

}