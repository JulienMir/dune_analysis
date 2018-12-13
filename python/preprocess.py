import nltk
import spacy
import pickle

from nltk.tokenize import RegexpTokenizer
from nltk.collocations import BigramCollocationFinder
from nltk.corpus import stopwords

def preprocess(corpusReader):
    tokens = []

    # On vérifie si les tokens existent déja dans un fichier
    try:
        with open('preprocessed_tokens.res', 'r') as f:
            for line in f:
                line.strip()
                tokens.append(line.split())

            f.close()
    except:
        #Le fichier n'existe pas donc on créer les tokens

        dune = open('Frank Herbert - Dune.txt')

        lines = dune.read()

        # On définit le charactère de chapitre
        lines = lines.replace('= = = = = =', '======')

        # On tokenise
        tokenizer = RegexpTokenizer(r'[A-z=]+')
        tokens = tokenizer.tokenize(lines)

        # On enlève les stopwords
        stopWords = set(stopwords.words('english'))
        wordsFiltered = []
        for w in tokens:
            if w not in stopWords:
                wordsFiltered.append(w)

        tokens = wordsFiltered

        # On enlève les apax
        print('Count before apax : %d' % len(tokens))
        uniqueTokens = set(tokens)

        for ut in uniqueTokens:
            if tokens.count(ut) < 3:
                while True:
                    try:
                        tokens.remove(ut)
                    except:
                        break

        print('Count after apax : %d' % len(tokens))

        # On fusionne les 'iter+1' mots qui apparaissent tout le temps ensemble
        for iter in range(1):
            print('Unmerged : %d' % len(tokens))
            bigrams = []
            for i in range(len(tokens)-1):
                bigrams.append((tokens[i], tokens[i+1]))

            print('Got %d bigrams' % len(bigrams))

            uniqueTokens = set(tokens)
            tokensOccurences = dict()
            uniqueBigrams = set(bigrams)
            bigramOccurences = dict()

            for ut in uniqueTokens:
                tokensOccurences.update({ut: tokens.count(ut)})

            for ub in uniqueBigrams:
                bigramOccurences.update({ub: bigrams.count(ub)})

            print('%d unique tokens and  %d unique bigrams' % (len(uniqueTokens), len(uniqueBigrams)))

            mergedTokens = []
            i = 0
            while i < len(tokens)-1:
                bgo = bigramOccurences[(tokens[i], tokens[i+1])]
                t1o = tokensOccurences[tokens[i]]
                t2o = tokensOccurences[tokens[i+1]]

                if bgo == t1o and t1o == t2o:
                    print('Merging %s and %s' % (tokens[i], tokens[i+1]))
                    mergedTokens.append('_'.join((tokens[i], tokens[i+1])))
                    i += 1
                else:
                    mergedTokens.append(tokens[i])

                i += 1

            tokens = mergedTokens

            print('Merged = %d' % len(mergedTokens))

        # On sépare en chapitre et retokenise
        chapters = (' '.join(tokens)).split('======')
        word_tokenizer = RegexpTokenizer('\s+', gaps=True)
        tokens = [word_tokenizer.tokenize(c) for c in chapters]

        # On ecrit un fichier contenant les tokens
        with open('preprocessed_tokens.res', 'w') as f:
            for chapter in tokens:
                f.write(' '.join(chapter))
                f.write('\n')

            f.close()
            #pickle.dump(tokens, f)

    return tokens