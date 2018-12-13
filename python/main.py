import spacy
import nltk
from nltk.corpus import PlaintextCorpusReader

from preprocess import preprocess
from named_entities import NamedEntities
from topics import get_topics


def main():
		#files = '.*\.txt'
		# corpus = PlaintextCorpusReader("./", files, encoding='latin-1')

		tokens = preprocess()

		print("Read %d chapters" % len(tokens))

		entities = NamedEntities(tokens)
		ne = entities.get_named_entities()

		topics = get_topics(tokens, nb_topics=10, nb_words=15)

		print("Name entities : ")
		for i in range(len(ne)):
				print("%d entities in paragraph %d" % (len(ne[i]),i))

				#if len(ne[i]) > 0:
				#    print('\t\tMost frequent are %s' % ne[i][0]['text'])
				for e in ne[i]:
						print('\t%s' % e)

		for i in range(len(topics)):
				print("Topic n%d accros the book" % i)
				print(topics[i])


if __name__ == '__main__':
    main()
