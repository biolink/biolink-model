package org.biolink.model;

import java.util.List;
import lombok.*;



/* version: 2.2.16 */


/**
  Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Publication extends InformationContentEntity {

  private List<String> authors;
  private List<String> pages;
  private String summary;
  private List<String> keywords;
  private List<String> meshTerms;
  private List<String> xref;

}