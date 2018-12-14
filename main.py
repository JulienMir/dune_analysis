import numpy as np

# import home-made modules
from preprocess import preprocess
from termdocumentmatrix import get_termDocumentMatrix
from named_entities import NamedEntities
from entity_matrix import get_entity_matrix
from graph_relations import draw_entities_relation


def main():
	#files = '.*\.txt'
	# corpus = PlaintextCorpusReader("./", files, encoding='latin-1')

    chapters = preprocess()
   
    tdm = get_termDocumentMatrix(chapters)
		
		named_entities = NamedEntities(chapters)
		entities_list = named_entities.get_named_entities()
		
		entity_matrix = get_entity_matrix(entities_list, tdm)
		
		draw_entities_relation(entity_matrix)


if __name__ == '__main__':
    main()
