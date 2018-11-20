library(tm)
library(lda)
library(topicmodels)
library(spacyr)

# Load text
raw_text <- readLines("Frank Herbert - Dune.txt", n=100)
corpus <- Corpus(VectorSource(raw_text))

# Preprocessing
pcorpus <- tm_map(corpus, content_transformer(tolower))
pcorpus <- tm_map(pcorpus, removePunctuation)
pcorpus <- tm_map(pcorpus, removeWords, stopwords(kind = "en"))


dtm <- DocumentTermMatrix(pcorpus)
dtm <- dtm[,which(table(dtm$j) >= 5)]
tdm <- TermDocumentMatrix(pcorpus)
tdm <- tdm[which(table(tdm$j) >= 5),]

# LDA
ap_lda <- LDA(tdm, k = 10, control = list(seed = 1234))
inspect(ap_lda)
