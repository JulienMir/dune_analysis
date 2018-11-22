import nltk
import spacy

from nltk.tokenize import RegexpTokenizer
from nltk.collocations import BigramCollocationFinder

def preprocess(corpusReader):
    dune = open('Frank Herbert - Dune.txt')

    lines = dune.read()

    # On regroupe en chapitre
    chapters = lines.split('= = = = = =')

    # On tokenise les chapitre
    tokenizer = RegexpTokenizer(r'[A-z]+')
    for c in chapters:
        c = tokenizer.tokenize(c)

        # On tente de regrouper les bigrammes
        bgm    = nltk.collocations.BigramAssocMeasures()
        finder = nltk.collocations.BigramCollocationFinder.from_words(c)
        scored = finder.score_ngrams( bgm.likelihood_ratio  )

        # Group bigrams by first word in bigram.                                        
        prefix_keys = nltk.collections.defaultdict(list)
        for key, scores in scored:
            prefix_keys[key[0]].append((key[1], scores))

        # Sort keyed bigrams by strongest association.                                  
        for key in prefix_keys:
            prefix_keys[key].sort(key = lambda x: -x[1], reverse = True)
            if prefix_keys[key][0][1] > 20.:
                print('%s -> %s' % (key, prefix_keys[key][0]))

    return chapters