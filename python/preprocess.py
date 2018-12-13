from gensim import corpora

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from collections import defaultdict
import re

def preprocess():
    tokens = []

    dune = open('./Frank Herbert - Dune.txt', encoding = 'latin-1')

    
    lines = dune.read()

    # On sépare en chapitre
    chapters = lines.split('= = = = = =')
    ## Les chapitres en lignes
    # chapters = [chapter.split('\n') for chapter in chapters]

    # On enlève les characteres spéciaux
    chapters = [re.sub(r'[^A-z \n]+', '', chapter) for chapter in chapters]
    chapters = [re.sub(r'[\n]+', ' ', chapter) for chapter in chapters]
    chapters = [re.sub(r' +', ' ', chapter) for chapter in chapters]

    # On enlève les stopwords et on met en minuscule
    #nltk.download('stopwords')
    stop = set(stopwords.words('english'))
    chapters_tokens = [[word for word in chapter.lower().split() if word not in stop]
            for chapter in chapters]

    # Calcul de la fréquence
    frequency = defaultdict(int)
    for tokens in chapters_tokens:
        for word in tokens:
            frequency[word] += 1

    # On retire les apax
    tokens = [[token for token in tokens if frequency[token] > 1]
            for tokens in chapters_tokens]

    return tokens