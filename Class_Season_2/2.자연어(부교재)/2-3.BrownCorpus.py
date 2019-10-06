# Brown Corpus 데이터를 읽어온다
from nltk.corpus import brown

# Brown 코퍼스의 파일 ID를 조회한다.
textId = brown.fileids()
print(textId)

# 카테고리 (장르) 목록을 조회한다
cat = brown.categories()
print(cat)

# 뉴스 텍스트 문서를 조회한다. (품사가 포함됨)
news = brown.raw(categories='news')
print(news[:500])

# 뉴스 텍스트 문서를 단어 단위로 조회한다. (품사 제외)
news = brown.words(categories='news')
print(news)

# 파일 아이디로 문서를 조회한다.
cg22 = brown.words(fileids=['cg22'])
print(cg22)

# 여러 카테고리에 속한 문서를 조회한다.
text = brown.sents(categories=['news', 'editorial', 'reviews'])
print(text)

# 문서에 포함된 단어수의 빈도 (카운트, 분포)를 측정한다.
import nltk
newsText = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in newsText)
fdist

# 원하는 단어의 사용 빈도를 확인한다.
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ':', fdist[m], end=' ')

print()
print(fdist['can'])
print(fdist['could'])

# 장르별 단어의 빈도 분포를 확인한다.
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
    )
print(cfd.conditions())
cfd['adventure']

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor'] 
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)

