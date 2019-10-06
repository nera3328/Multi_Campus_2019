# 소설의 등장인물의 이름을 발췌한다
import nltk

# 사람 이름 코퍼스
names = nltk.corpus.names.fileids()
print(names)

maleName = nltk.corpus.names.words(names[0])
femName = nltk.corpus.names.words(names[1])

# 소설 text
text = nltk.corpus.gutenberg.words('austen-emma.txt')

# text에서 남자, 여자 이름을 발췌한다
maleText = set(w for w in text if w in maleName)
femText = set(w for w in text if w in femName)

# 등장인물의 인물을 확인한다. 이 소설에는 남자가 많이 등장하는가?
print("Male : ", maleText)
print()
print("Female : ", femText)
