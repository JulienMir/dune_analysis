#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 18:07:02 2018

@author: pierre
"""

import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

def get_termDocumentMatrix(chapters):

    # On enlève les stopwords et on met en minuscule
    # décommenter la ligne suivante si les stopwords n'ont pas été téléchargés
    #nltk.download('stopwords')
    stop = set(stopwords.words('english'))

    vectorizer = TfidfVectorizer(ngram_range=(1, 1),
                                     max_df=0.8,
                                     min_df=1,
                                     stop_words=stop)

    vector_space = list()
    vocabulary = list()
    for c in chapters:
        vector_space.append(vectorizer.fit_transform(c))
        vocab = vectorizer.get_feature_names()
        vocabulary.append(dict([(s, i) for i, s in enumerate(vocab)]))

    return {'vocabulary'  : vocabulary,
            'vector_space': vector_space }