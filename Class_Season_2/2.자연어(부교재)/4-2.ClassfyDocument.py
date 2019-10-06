# Movie Review Classification
import nltk
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords


# movie_reviews 데이터를 읽어온다
movie_reviews.categories()
movie_reviews.fileids('neg')[:3]
movie_reviews.fileids('pos')[:3]

documents = [(list(movie_reviews.words(fileid)), category) 
            for category in movie_reviews.categories() 
            for fileid in movie_reviews.fileids(category)]
print(documents[0][0][:20]) #첫번재 열 중 첫 번째 열 에서 뒤에서 20개 뽑아
print(documents[0][1]) # 첫 번째 열의 카테고리


# 영어의 Stop words를 확인한다.
stopWords = stopwords.words('english')

# movie_reviews에서 Stop words를 제거한다.
netText = []
for x, y in documents:
    m = [w for w in x if w.lower() not in stopWords and len(w) > 2]
    netText.append((m, y))
   
len(netText)
print(netText[0][0][:20])
print(netText[0][1])


# 학습을 위한 Feature를 생성한다.
# netText에 사용된 단어의 빈도를 측정한다. review 텍스트 word를 한데 모은다.
netTextWords = [x for (x, y) in netText]
netTextWords = [x for w in netTextWords for x in w]
all_words = nltk.FreqDist(netTextWords)
all_words

# review 텍스트에 가장 많이 쓰인 단어 1000개를 뽑는다.
topWord = [x for (x, y) in all_words.most_common(1000)]
print(topWord[:20])

# Feature를 생성한다. 1000개 단어중 사용된 것에는 True, 사용되지 않은
# 것에는 False를 표시한다.
def document_features(document, tw):
    document_words = set(document)
    features = {}
    for word in tw: 
        features['contains({})'.format(word)] = (word in document_words)
    return features

# 한개 리뷰의 Feaure를 확인해 본다.
features = document_features(movie_reviews.words('pos/cv957_8737.txt'), topWord)
features

# 학습을 위한 Feature Set을 생성한다.
featuresets = [(document_features(d, topWord), c) for (d,c) in documents]
featuresets[0]

train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))

##############################################
# stop word 제거 연습
stopword = ['is', 'i', 'am', 'the']
text = []
text.append(("I am a student and I am 15 year's old.".split(), 'neg'))
text.append(("Yesterday is wednsday and today is thursday.".split(), 'pos'))
netText = []
for x, y in text:
    rm = [w for w in x if w.lower() not in stopword and len(w) > 1]
    netText.append((rm, y))
    
# list of list 합치기
aa = [['a', 'b'], ['c', 'd']]
[j for i in aa for j in i]

