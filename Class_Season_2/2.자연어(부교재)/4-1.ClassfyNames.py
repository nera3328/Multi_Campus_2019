# Gender Identification
import nltk
import random
from nltk.corpus import names

# 주어진 단어의 마지막 문자를 리턴한다.
def gender_features(word):
    return {'last_letter': word[-1]}

# Names Corpus에서 남자, 여자 이름을 읽어온다. 이름-성별 데이터.
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')]) 
random.shuffle(labeled_names)
print(labeled_names[:10])

# 이름-성별 데이터에서 학습을 위한 Feature를 생성하여, 학습 데이터와
# 시험 데이터를 생성한다. Feature는 이름의 마지막 문자로 한다.
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
train_set[:5]
test_set[:5]

# Decision Tree 알고리즘으로 학습 데이터를 학습한다.
classifier = nltk.DecisionTreeClassifier.train(train_set)

# 학습 결과를 확인한다.
classifier.classify(gender_features('Neo'))
classifier.classify(gender_features('Samanda'))

# 시험 데이터로 성능을 평가한다.
print(nltk.classify.accuracy(classifier, test_set))

# 학습용 데이터와 시험용 데이터는 아래와 같이 생성해도 좋다.
from nltk.classify import apply_features
train_set = apply_features(gender_features, labeled_names[500:])
test_set = apply_features(gender_features, labeled_names[:500])
train_set[:5]
test_set[:5]

# 이름의 마지막 문자 이외에 다른 문자들도 고려하여 Feature를 생성한다.
def gender_features2(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

# 이름-성별 데이터에서 학습을 위한 Feature를 생성하여, 학습 데이터와
# 시험 데이터를 생성한다. Feature는 이름의 전체를 고려한다. 
featuresets = [(gender_features2(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
print(train_set[0])
print(test_set[0])

# Decision Tree 알고리즘으로 학습 데이터를 학습한다.
classifier = nltk.DecisionTreeClassifier.train(train_set)

# 학습 결과를 확인한다.
classifier.classify(gender_features('Neo'))
classifier.classify(gender_features('Samanda'))

# 시험 데이터로 성능을 평가한다.
print(nltk.classify.accuracy(classifier, test_set))
