from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer

raw='My name is Maximus Decimus Meridius, Commander of the Armies of the North, General of the Felix Legions, loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next.'
tokens=word_tokenize(raw)

porter=PorterStemmer()
stems=[porter.stem(t) for t in tokens]
print(stems)

lemmatizer=WordNetLemmatizer()
lemmas=[lemmatizer.lemmatize(t)for t in tokens]
print(lemmas)
