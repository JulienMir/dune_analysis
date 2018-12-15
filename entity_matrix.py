import numpy as np
from scipy.sparse import csr_matrix
import re

import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

from nltk.corpus import stopwords


def get_entity_matrix(entities_list, vocabulary, vector_space):
	entity_matrix = []

	stop = set(stopwords.words('english'))
	stop.add('shall')
	stop.add('said')
	stop.add('ah')
	stop.add('oh')
	stop.add('ahah')

	# Pour chaque chapitre
	for k in range(len(entities_list)):
		d = dict()

		print("Chapitre ", k)
		entities_list[k] = [' '.join([word for word in entity.split() if word.lower() not in stop]) for entity in entities_list[k]]
		entities_list[k] = [entity for entity in entities_list[k] if len(entity)>2]
		entities_list[k] = list(set(entities_list[k]))
		#entities_list[k] = [re.sub(r'[^\w\s]+', '', entity) for entity in entities_list[k]]
		print(entities_list[k])

		# Pour l'entité j
		for j in range(len(entities_list[k])):
			tmp_res = []

			# On la décompose en unigramme
			entity1 = entities_list[k][j].lower().split()
			#entity1 = [word for word in entity1 if word not in stop]
			# On récupère le vecteur BOW associé à chacun
			# print("Dim de Vs : ", vector_space[k].shape)
			# print("Index of %s : %d" % (entity1[0], vocabulary[k][entity1[0]]))
			
			vectors_e1 = []
			for word in entity1:
				try:
					vectors_e1.append(vector_space[k][vocabulary[k][word],:])
				except:
					pass

			# Pour l'entité i
			for i in range(len(entities_list[k])):
				# On la décompose en unigramme
				entity2 = entities_list[k][i].lower().split()
				#entity2 = [word for word in entity2 if word not in stop]
				# On récupère le vecteur BOW associé à chacun
				
				vectors_e2 = []
				for word in entity2:
					try:
						vectors_e2.append(vector_space[k][vocabulary[k][word],:])
					except:
						pass

				tmp_similarity = []

				# Pour chaque unigramme de i
				for v1 in vectors_e1:
					tmp = []

					# Pour chaque unigramme de j
					for v2 in vectors_e2:
						A = np.array([v1,v2]).reshape(2, v1.shape[1])

						# On calcule la similarité cosinus entre un token de chaque entité
						tmp.append(cosine_similarity(A)[0,1])

					# On moyenne entre chaque token de e2 et le premier de e1
					tmp_similarity.append(np.mean(tmp))

				# On moyenne pour chaque token de e1 pour obtenir le coef i,j
				tmp_res.append(np.mean(tmp_similarity))

			d[entities_list[k][j]] = pd.Series(tmp_res, index=entities_list[k])

		# On passe la matrice en dataframe pour avoir les noms de colonnes
		entity_matrix.append(pd.DataFrame(d))

	return entity_matrix