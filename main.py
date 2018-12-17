# import home-made modules
from preprocess import preprocess
from termdocumentmatrix import get_termDocumentMatrix
from named_entities import NamedEntities
from entity_matrix import get_entity_matrix
from topics import get_topics
from graph_relations import draw_entities_relation


def main():
	#files = '.*\.txt'
	# corpus = PlaintextCorpusReader("./", files, encoding='latin-1')

    print('Starting preprocess...')
    chapters = preprocess()

    print('Creating TermDocumentMatrix...')
    vocabulary, vector_space = get_termDocumentMatrix(chapters)
		
    print('Finding named entities...')
    named_entities = NamedEntities(chapters)
    entities_list = named_entities.get_named_entities()

    print('Computing entities relationships...')
    entity_matrix = get_entity_matrix(entities_list, vocabulary, vector_space)
    
    print('Topic extraction...')
    topics = get_topics(chapters)

    print('Entities graph...')
    draw_entities_relation(entity_matrix, topics)


if __name__ == '__main__':
    main()
