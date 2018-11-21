require(spacyr)
require(quanteda)

get_named_entity <- function(corpus) {
  parsed <- spacy_parse(corpus(corpus))
  
  named <- entity_extract(parsed)
  
  return(named)
}