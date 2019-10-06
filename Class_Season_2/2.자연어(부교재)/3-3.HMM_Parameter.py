import nltk

# HMM parameter 추정 (Transition, Emission probability)
tagged_words = []
all_tags = []

for sent in nltk.corpus.brown.tagged_sents(tagset='universal'):
    tagged_words.append( ("START", "START") )
    all_tags.append("START")
    for (word, tag) in sent: #break point 설정 F12
        all_tags.append(tag)
        tagged_words.append( (tag, word) ) 
    tagged_words.append( ("END", "END") )
    all_tags.append("END")

# Transition probability
bigram=nltk.bigrams(all_tags)
cfd_tags= nltk.ConditionalFreqDist(nltk.bigrams(all_tags))
cpd_tags = nltk.ConditionalProbDist(cfd_tags, nltk.MLEProbDist)

print("Count('DET','NOUN') =", cfd_tags['DET']['NOUN'])
print("P('NOUN' | 'DET') =", cpd_tags['DET'].prob('NOUN'))

# Emission probability
cfd_tagwords = nltk.ConditionalFreqDist(tagged_words)
cpd_tagwords = nltk.ConditionalProbDist(cfd_tagwords, nltk.MLEProbDist)

print("Count('DET','the') =", cfd_tagwords['DET']['the'])
print("P('the' | 'DET') =", cpd_tagwords['DET'].prob('the'))