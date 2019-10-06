# Part-of-Speech Tagging
# 접미사와 이전 단어, 그리고 이전 단어의 품사를 feature로 단어의 품사 추정
import nltk
from nltk.corpus import brown

def pos_features(sentence, i, history):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-tag"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
        features["prev-tag"] = history[i-1]
    return features

tagged_sents = brown.tagged_sents(categories='news')

# 접미사와 이전 단어를 feature로 하는 featureset을 생성한다.
featuresets = []
for tagged_sent in tagged_sents:
    untagged_sent = nltk.tag.untag(tagged_sent)
    history = []
    for i, (word, tag) in enumerate(tagged_sent):
        featuresets.append( (pos_features(untagged_sent, i, history), tag) )
        history.append(tag)
featuresets[0]
featuresets[1]

# Feature word vector로 학습 데이터와 시험 데이터를 생성한다.
test_size = 500
train_set, test_set = featuresets[test_size:], featuresets[:test_size]

# Naive Bayes 알고리즘으로 학습 데이터를 학습한다.
classifier = nltk.NaiveBayesClassifier.train(train_set)

# 시험 데이터로 성능을 평가한다.
nltk.classify.accuracy(classifier, test_set)
# 0.852

