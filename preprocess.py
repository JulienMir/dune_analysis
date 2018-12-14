import re


def preprocess():
    dune = open('./Frank Herbert - Dune.txt', encoding = 'latin-1')
    
    lines = dune.read()

    # On sépare en chapitre
    chapters = lines.split('= = = = = =')
    
    # Les chapitres en lignes
    chapters = [c.split('\n') for c in chapters]

    # On enlève les characteres spéciaux
    chapters = [[re.sub(r'[^A-z \n]+', '', line) for line in c] for c in chapters]
    chapters = [[re.sub(r'[\n]+', ' ', line) for line in c] for c in chapters]
    chapters = [[re.sub(r' +', ' ', line)  for line in c] for c in chapters]

    # On enlève les chapitres trop petits
    chapters = [[line for line in c if len(line) > 20] for c in chapters]
    chapters = [[line for line in c] for c in chapters if len(c) != 0]
    
    return chapters