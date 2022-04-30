package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  an item that holds version level information about a dataset.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DatasetVersion extends InformationContentEntity {

  private Dataset hasDataset;
  private String ingestDate;
  private DatasetDistribution hasDistribution;

}