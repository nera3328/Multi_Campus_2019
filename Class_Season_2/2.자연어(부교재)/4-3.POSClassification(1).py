# Part-of-Speech Tagging : 접미사를 feature로 단어의 품사 추정
import nltk
from nltk.corpus import brown

# word의 마지막 1 ~ 3 문자로 접미사 FreqDist를 생성한다.
suffix_fdist = nltk.FreqDist()
for word in brown.words():
    word = word.lower()
    if len(word) >= 3:
        suffix_fdist[word[-1:]] += 1
        suffix_fdist[word[-2:]] += 1
        suffix_fdist[word[-3:]] += 1
suffix_fdist

# 가장 많이 사용되는 접미사 100개를 선택한다.
common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]
print(common_suffixes)

# 주어진 word가 common_suffixes로 끝나면 True, 아니면 False를 부여한다.
def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith({})'.format(suffix)] = word.lower().endswith(suffix)
    return features

# 접미사를 feature로 하는 word vector를 생성한다.
tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n), g) for (n,g) in tagged_words]
featuresets[0]

# Feature word vector로 학습 데이터와 시험 데이터를 생성한다.
test_size = 500
train_set, test_set = featuresets[test_size:], featuresets[:test_size]

# Naive Bayes 알고리즘으로 학습 데이터를 학습한다.
classifier = nltk.NaiveBayesClassifier.train(train_set)

# 시험 데이터로 성능을 평가한다.
nltk.classify.accuracy(classifier, test_set)
# 0.512

# 학습 결과를 이용하여 특정 단어의 품사를 추정한다.
classifier.classify(pos_features('cats'))
classifier.classify(pos_features('completely'))
classifier.classify(pos_features('different'))
