package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */



@Data
@EqualsAndHashCode(callSuper=false)
public class Article extends Publication {

  private String publishedIn;
  private String isoAbbreviation;
  private String volume;
  private String issue;

}