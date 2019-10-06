# -*- coding: utf-8 -*-
import nltk
import random
from nltk.corpus import names

def gender_features(word):
    return {'last_letter': word[-1]}

labeled_names=([(name, 'male') for name in names.words('male.txt')] + [(name,'female')for name in names.words('female.txt')])
random.shuffle(labeled_names)
print(labeled_names[:10])

featuresets=[(gender_features(n), gender)
                    for (n, gender) in labeled_names]
train_set, test_set=featuresets[500:],featuresets[:500]
train_set[:5]
test_set[:5]

classifier=nltk.DecisionTreeClassifier.train(train_set)


classifier.classify(gender_features('Neo'))
classifier.classify(gender_features('Sally'))
classifier.classify(gender_features('wick'))
classifier.classify(gender_features('MinJung'))
classifier.classify(gender_features('Kim'))
classifier.classify(gender_features('Park'))
classifier.classify(gender_features('Lee'))
print(nltk.classify.accuracy(classifier, test_set))


from nltk.classify import apply_features


train_set=apply_features(gender_features, labeled_names[500:])
test_set=apply_features(gender_features, labeled_names[:500])
train_set[:5]
test_set[:5]


def gender_features2(name):
    features={}
    features['first_letter']=name[0].lower()
    features['last_letter']=name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuwxyz':
        features['count({})'.format(letter)]=name.lower().count(letter)
        features['has({})'.format(letter)]=(letter in name.lower())
    return features

featuresets=[(gender_features2(n),gender) for (n, gender) in labeled_names]
train_set, test_set=featuresets[500:], featuresets[:500]
print(train_set[0])
print(test_set[1])

classifier=nltk.DecisionTreeClassifier.train(train_set)

classifier.classify(gender_features('Kim'))