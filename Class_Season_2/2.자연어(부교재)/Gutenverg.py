import nltk
from nltk.corpus import gutenberg
print(gutenberg.fileids())

words=gutenberg.words('bible-kjv.txt')
words_filtered=[e for e in words if len(e) >= 3]
stopwords=nltk.corpus.stopwords.words('english')
word=[w for w in words_filtered if w.lower() not in stopwords]

fdistPlain=nltk.FreqDist(words)
fdist=nltk.FreqDist(word)

print('most common word', fdist.most_common(10))
print('min common word', )