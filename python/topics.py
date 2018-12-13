from gensim.models import LdaModel
from gensim import corpora

def get_topics(tokens):
    dictionary = corpora.Dictionary(tokens)

    corpus_chapters = [dictionary.doc2bow(token) for token in tokens]

    nb_topics = 10
    lda = LdaModel(corpus_chapters, num_topics=nb_topics)

    res = []
    for i in range(nb_topics):
        words = []
        # On regarde les 10 mots les plus associés au topic
        for x in lda.show_topic(i, topn=10):
            words.append(dictionary[int(x[0])])
            
        print(words)
        res.append(words)

    return res