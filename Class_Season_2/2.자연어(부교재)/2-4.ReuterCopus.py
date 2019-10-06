# Reuter Corpus 데이터를 읽어온다
from nltk.corpus import reuters 

# 로이터 코퍼스의 파일 ID를 조회한다.
textId = reuters.fileids()
print(textId[:10])
print(textId[5000:5010])

# 카테고리 목록을 조회한다
cat = reuters.categories()
print(cat)

# 원시 문서를 읽는다
text = reuters.raw('training/9865')
print(text)

# 문서의 주제어를 조회한다.
topic = reuters.categories('training/9865')
print(topic)

topic = reuters.categories(['training/9865', 'training/9880'])
print(topic)

# 해당 주제어를 갖는 문서를 찾는다
textTopic = reuters.fileids('cpu')
print(textTopic)

textTopic = reuters.fileids(['cpu', 'naphtha'])
print(textTopic)

# 유사한 주제어를 갖는 문서의 내용을 조회한다.
text = reuters.words('training/5388')
print(text[:40])

text = reuters.words('training/5460')
print(text[:60])
