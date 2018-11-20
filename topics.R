detect_topic <- function(tdm) {
  # LDA
  ap_lda <- LDA(tdm, k = 10, control = list(seed = 1234))
  inspect(ap_lda)
}