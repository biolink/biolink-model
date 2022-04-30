package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  A relationship between a sequence feature and a nucleic acid entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GenomicSequenceLocalization extends SequenceAssociation {

  private Integer startInterbaseCoordinate;
  private Integer endInterbaseCoordinate;
  private String genomeBuild;
  private String strand;
  private String phase;

}