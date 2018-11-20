preprocess <- function(corpus) {
  # Preprocessing
  pcorpus <- tm_map(corpus, content_transformer(tolower))
  pcorpus <- tm_map(pcorpus, removePunctuation)
  pcorpus <- tm_map(pcorpus, removeWords, stopwords(kind = "en"))
  
  return(pcorpus)
}