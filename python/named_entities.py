import spacy
import nltk

"""
Renvoie une liste contenant chaque unique entitées dans chaque documents
"""
def get_named_entities(nlp, corpus):
    res = []

    for p in corpus:
        para = ''
        # On concatène chaque ligne du paragraphe
        for l in p:
            para += ' '.join(l)

        # On trouve les entitées nommées
        doc = nlp(para)
        
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

    return res