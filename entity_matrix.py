import numpy as np
import pandas as pd
from nltk.corpus import stopwords
import itertools as it

def get_entity_matrix(entities_list, tdm):
    
    stop = set(stopwords.words('english'))
    entities_list = ['the dune', 'arrakis', 'MuadDib', 'Atreides', 'Paul', 'Lady Jessica']
    entities_list = [entity.lower() for entity in entities_list]
    entities_list = [(entity.split()) for entity in entities_list if entity.split() != entity]
    entities_list = [[ngram for ngram in entity if ngram not in stop] for entity in entities_list]

    vector_space = tdm['vector_space']
    vocabulary = tdm['vocabulary']
    
    entities_list_joint = list(it.chain.from_iterable(entities_list))
    entity_matrix = pd.DataFrame(columns = entities_list_joint, index = entities_list_joint)
    for ent_i in entities_list_joint:
        id_mot_i = vocabulary[0][ent_i]
        for ent_j in entities_list_joint:
            id_mot_j = vocabulary[0][ent_j]
            entity_matrix[ent_i][ent_j] = float(cos_similarity(vector_space[0][:, id_mot_i].todense(), v2 = vector_space[0][:, id_mot_j].todense()))
    
    return entity_matrix
    
    

def cos_similarity(v1, v2):
    return ( v1.T * v2 ) / ( np.sqrt(sum(np.square(v1))) * np.sqrt(sum(np.square(v2))) )