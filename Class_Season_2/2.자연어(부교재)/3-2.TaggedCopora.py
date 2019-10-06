# Tagged Corpora
import nltk

# Penn Treebank
penn = nltk.corpus.treebank.tagged_words()
print(penn[:20])

# Brown corpus
brown1 = nltk.corpus.brown.tagged_words() 
print(brown1[:20])

brown2 = nltk.corpus.brown.tagged_words(tagset='universal')
print(brown2[:20])

# NPS Chat
chat = nltk.corpus.nps_chat.tagged_words()
print(chat[:20])

# CONLL Corpus (2000)
conll = nltk.corpus.conll2000.tagged_words()
print(conll[:20])
