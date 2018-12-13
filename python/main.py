# import libraries
import spacy
import nltk
from nltk.corpus import PlaintextCorpusReader

# import home-made modules
from preprocess import preprocess
from named_entities import NamedEntities
from topics import get_topics
import numpy as np


def main():
	#files = '.*\.txt'
	# corpus = PlaintextCorpusReader("./", files, encoding='latin-1')

    texts = preprocess()

    print("Read %d chapters" % len(texts))

    entities = NamedEntities(texts)
    ne = entities.get_named_entities()

    topics = get_topics(texts)

    print("Name entities : ")
    list_label = list()
    for l in ne:
        for elt in l:
            list_label.append(elt['label'])
    dict_label = np.unique(list_label)
    
    list_text = {}
    for l in dict_label:
        list_text[l] = list()
        
    NE_SEL = ('LOC', 'PERSON')
    for i, l in enumerate(ne):
        print('paragraphe: ' + str(i))
        for elt in l:
            if elt['label'] in NE_SEL:
                print("     Entité " + elt['label'] + ": " + elt['text'] + "     count: " + str(elt['count']))
            list_text[elt['label']].append(elt['text'])
    dict_text = np.unique(list_text)

    for i in range(len(topics)):
        print("Topic n%d accros the book" % i)
        print(topics[i])






if __name__ == '__main__':
    main()
