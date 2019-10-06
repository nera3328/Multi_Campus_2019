from nltk import PorterStemmer, LancasterStemmer, word_tokenize

raw='My name is Maximus Decimus Meridius, Commander of the Armies of the North, General of the Felix Legions, loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next.'
tokens=word_tokenize(raw)
porter=PorterStemmer()
pstems=[porter.stem(t)for t in tokens]
print(pstems)

lancaster=LancasterStemmer()
lStems=[lancaster.stem(t)for t in tokens]
print(lStems)