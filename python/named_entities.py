import spacy
import nltk
from spacy import displacy

class NamedEntities:
    def __init__(self, corpus):
        # Modèle de langage utilisé par les différentes foncitons (anglais)
        # Requiert "python -m spacy download xx_ent_wiki_sm"
        # model = 'en_core_web_sm'
        # Requiert "python -m spacy download xx_ent_wiki_sm"
        self.model = 'xx_ent_wiki_sm'
        self.nlp = spacy.load(self.model)

        self.corpus = corpus
        self.entities_list = None


    """
    Renvoie une liste ordonnée selon le nombre d'occurences de chaque unique entitées dans chaque document
    """
    def get_named_entities(self):
        if self.entities_list is None:

            res = []

            for p in self.corpus:
                para = ''
                # On concatène chaque ligne du paragraphe
                for l in p:
                    para += ' '.join(l)

                # On trouve les entitées nommées
                doc = self.nlp(para)
                
                # On les met dans un tableau et on compte les occurences
                unique = []
                for ent in doc.ents:
                    d = dict(text = ent.text, label = ent.label_, count = 1)
                    found  = False

                    for e in unique:
                        if e['text'] == d['text'] and e['label'] == d['label']:
                            e['count'] += 1
                            found = True
                    
                    if found == False:
                        unique.append(d)

                
                res.append(sorted(unique, reverse = True, key = lambda x: x['count']))

            # Permet une visualisation des entitées nommées dans une page web
            # displacy.serve(doc, style='ent')

            self.entities_list = res

        return self.entities_list