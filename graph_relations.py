import networkx as nx

import pandas as pd

import matplotlib.pyplot as plt


def draw_entities_relation(entity_matrix, topics):
    for k in range(len(entity_matrix)):
        mat = entity_matrix[k]
        entities_names = mat.columns

        G = nx.Graph()
        
        for j in range(len(entities_names)):
            edges = []

            for i in range(j):
                coef = mat.loc[entities_names[j], entities_names[i]]
                
                if coef > 0.1:
                    edges.append((entities_names[j], entities_names[i], coef))

            G.add_weighted_edges_from(edges)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, font_size=16, with_labels=False)

        # On décale le texte
        for p in pos:
            pos[p][1] += 0.07
        nx.draw_networkx_labels(G, pos)
        plt.title('Chapitre ' + str(k+1), fontweight='bold', fontdict={
            'fontsize': 15,
        })
        plt.show()