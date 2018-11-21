import nltk
import spacy

from nltk.corpus import PlaintextCorpusReader

def preprocess(nlp, corpusReader):
    text  = nltk.Text(corpusReader.paras())

    return text