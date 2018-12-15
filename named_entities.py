import spacy
import nltk

import pandas as pd

import matplotlib.pyplot as plt


class NamedEntities:
    def __init__(self, chapters):
        # Modèle de langage utilisé par les différentes foncitons (anglais)
        # Requiert "python -m spacy download xx_ent_wiki_sm"
        self.model = 'en_core_web_sm'
        # Requiert "python -m spacy download xx_ent_wiki_sm"
        # self.model = 'xx_ent_wiki_sm'
        self.nlp = spacy.load(self.model)

        self.chapters = chapters
        self.docs = [self.nlp(' '.join(chapter)) for chapter in self.chapters]
        self.entities_list = []

    """
    Renvoie une liste par chapitre contenant les entités et leur nombre d'occurences.
    """
    def get_named_entities(self):
        for doc in self.docs:
            entities = []
            for ent in doc.ents:
                if (ent.label_ == "GPE" or 
                    ent.label_ == "LOC" or 
                    ent.label_ == "PERSON" or 
                    ent.label_ == "ORG"):

                    entities.append(ent.text)

            # Liste d'entités uniques
            self.entities_list.append(list(set(entities)))

        return self.entities_list