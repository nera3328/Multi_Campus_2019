from nltk.corpus import CategorizedPlaintextCorpusReader

reader=CategorizedPlaintextCorpusReader(
        r'C:\Users\student\Finance\1장.말뭉치와워드넷\cs\tokens',
        r'.*\.txt',
        cat_pattern=r'(\w+)/*')
print(reader.categories())
print(reader.fileids()[:20]

posFiles=reader.fileids(categories='pos')
negfiles=reader.fileids(categories='neg')

from random import randint

fileP=posfiles[randint(0,len(posfiles)-1)] #임의로 파일을 선택!
fileN=negfiles[randint(0,len(negfiles)-1)] 
print(fileP)
print(fileN)

for w in reader.words(fileP):
    print(w+' ', end='')
    if(w is '.'):
        print()
for w in reader.words(fileN):
    print(w+' ',end='')
    if(w is '.'):
        print()
        
        
import nltk
from nltk.corpus import brown
print(brown.categories())

genres=['fiction','humor','romance']
whs=['what','which','how','why','when','where','who']

for i in range(len(genres)):
    genre=genres[i]
    print()
    print("analysing '"+genre +"' wh")
    genretext=brown.words(categories=genre)
    fdist=nltk.FreqDist(genretext)
    for wh in whs:
        print(wh + ':', fdist[wh], end=' ')
    
import nltk
from nltk.corpus import webtext
from nltk.corpus import stopwords
print(webtext.fileids())

fileid='singles.txt'
wbt=webtext.words(fileid)
print(wbt)
a=stopwords.words('english')
print(a)[:20]
stopw = [w for w in wbt if w.lower() not in a]
fdist=nltk.FreqDist(a)
print(fdist)        


print('Count of the maximum appearing word :', fdist[fdist.max()])
print('Total Number of distinct tokens in the bag : ',fdist.N)
print('Following are the most common 10 words in the bag',fdist.most_common(10))

from nltk. corpus import wordnet as wn

chair='chair'
chairsyn=wn.synsets(chair)
print(chairsyn)

from nltk.corpus import wordnet as wn
print(wn.fileids())
a = wn.synset('woman.n.01')
print(a.hypernyms())
apath=a.hypernym_paths()
print(apath)

for idx, path in enumerate(apath):
    print('\n\nHypernym Path :',idx+1)
    for synset in path:
        print(synset.name(),', ',end=' ')

from nltk.corpus import wordnet as wn
type='n'
synset=wn.all_synsets(type)
synset
lemmas=[]
for synsets in synset:
    for lemma in synset.lemmas():
        lemmas.append(lemma.name())
print(len(lemmas))