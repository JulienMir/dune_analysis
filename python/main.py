import spacy
import nltk
from nltk.corpus import PlaintextCorpusReader
from spacy import displacy

from preprocess import preprocess
from named_entities import get_named_entities
from topics import get_topics


def main():
    # Modèle de langage utilisé par les différentes foncitons (anglais)
    model = 'en_core_web_sm'
    nlp = spacy.load(model)

    files = '.*\.txt'

    corpus = PlaintextCorpusReader("./", files, encoding='latin-1')
    
    texts = preprocess(nlp, corpus)

    print("Read %d texts" % len(texts))

    ne = get_named_entities(nlp, texts)
    topics = get_topics(nlp, texts)

    print("Name entities : ")
    for i in range(len(ne)):
        print("\t%d entities in paragraph %d" % (len(ne[i]),i))

        if len(ne[i]) > 0:
            print('\t\tMost frequent is %s' % ne[i][0]['text'])

    for i in range(len(topics)):
        print("Topics of paragraph %d" % i)
        print(topics[i])


if __name__ == '__main__':
    main()
