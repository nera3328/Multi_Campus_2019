# Stemmer 
import nltk

raw = """
    DENNIS: Listen, strange women lying in ponds distributing swords
    is no basis for a system of government.  Supreme executive power derives from
    a mandate from the masses, not from some farcical aquatic ceremony.
    """
tokens = nltk.word_tokenize(raw)
print(tokens)

# Porter stemmer
porter = nltk.PorterStemmer()
stem = [porter.stem(t) for t in tokens]
print(stem)

# Lancaster stemmer
lancaster = nltk.LancasterStemmer()
stem = [lancaster.stem(t) for t in tokens]
print(stem)
