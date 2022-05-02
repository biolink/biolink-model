package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  an item that holds distribution level information about a dataset.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DatasetDistribution extends InformationContentEntity {

  private String distributionDownloadUrl;

}