library(tm)
library(lda)
library(topicmodels)
library(spacyr)

source("preprocess.R")
source("topics.R")
source("named.R")

# Load text
raw_text <- readLines("Frank Herbert - Dune.txt", n=100)
corpus <- Corpus(VectorSource(raw_text))

corpus <- preprocess(corpus)

dtm <- DocumentTermMatrix(pcorpus)
dtm <- dtm[,which(table(dtm$j) >= 5)]
tdm <- TermDocumentMatrix(pcorpus)
tdm <- tdm[which(table(tdm$j) >= 5),]
