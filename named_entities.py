import spacy
import nltk

import pandas as pd

import matplotlib.pyplot as plt


class NamedEntities:
    def __init__(self, chapters):
        # Modèle de langage utilisé par les différentes fonctions (anglais)
        # Requiert "python -m spacy download xx_ent_wiki_sm"
        self.model = 'en_core_web_sm'
        # Requiert "python -m spacy download xx_ent_wiki_sm"
        # self.model = 'xx_ent_wiki_sm'
        self.nlp = spacy.load(self.model)

        self.chapters = chapters
        self.docs = [self.nlp(" ".join(c)) for c in self.chapters]
        self.entities_list = None

    """
    Renvoie une liste par chapitre contenant les entités et leur nombre d'occurences.
    """
    def get_named_entities(self):
        if self.entities_list is None:

            res = []

            for doc in self.docs:                
                # On les met dans un tableau et on compte les occurences
                entities = []
                for ent in doc.ents:
                    if (ent.label_ == "GPE" or 
                        ent.label_ == "LOC" or 
                        ent.label_ == "PERSON" or 
                        ent.label_ == "ORG"):

                        entities.append(ent.text)

                res.append(set(entities))

            self.entities_list = res

        return self.entities_list


    def matrix_entities(self):
        data = {
			'Al' : pd.Series([0., 1., 2., 0.],
			index=['Al', 'Betty', 'Carol', 'Dom']),
			'Betty' : pd.Series([10., 0., 30., 60.], 
			index=['Al', 'Betty', 'Carol', 'Dom']),
			'Carol' : pd.Series([2., 30., 0., 0.], 
			index=['Al', 'Betty', 'Carol', 'Dom']),
			'Dom' : pd.Series([0., 60., 0., 0.], 
			index=['Al', 'Betty', 'Carol', 'Dom']),
		}