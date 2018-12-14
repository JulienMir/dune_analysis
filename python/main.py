# import home-made modules
from preprocess import preprocess
from termdocumentmatrix import get_termDocumentMatrix
from named_entities import NamedEntities
import numpy as np


def main():
	#files = '.*\.txt'
	# corpus = PlaintextCorpusReader("./", files, encoding='latin-1')

    chapters = preprocess()
   
    tdm = get_termDocumentMatrix(chapters)

    print("Read %d chapters" % len(chapters))

    entities = NamedEntities(chapters)
    ne = entities.get_named_entities()

    print("Name entities : ")
    list_label = list()
    for l in ne:
        for elt in l:
            list_label.append(elt['label'])
    dict_label = np.unique(list_label)
    
    list_text = {}
    for l in dict_label:
        list_text[l] = list()
        
    NE_SEL = ('LOC', 'GPE', 'FAC','EVENT', 'PERSON', 'NORG')
    for i, l in enumerate(ne):
        print('paragraphe: ' + str(i))
        for elt in l:
            if elt['label'] in NE_SEL:
                print("     Entité " + elt['label'] + ": " + elt['text'] + "     count: " + str(elt['count']))
            list_text[elt['label']].append(elt['text'])
    dict_text = np.unique(list_text)




if __name__ == '__main__':
    main()
