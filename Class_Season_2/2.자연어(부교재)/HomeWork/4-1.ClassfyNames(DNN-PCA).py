# Gender Identification
import random
from nltk.corpus import names
import numpy as np

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from sklearn.metrics import accuracy_score
from sklearn import decomposition

# Names Corpus에서 남자, 여자 이름을 읽어온다. 이름-성별 데이터.
labeled_names = ([(name, 0) for name in names.words('male.txt')] +
                 [(name, 1) for name in names.words('female.txt')]) 
random.shuffle(labeled_names)

# 이름의 마지막 문자 이외에 다른 문자들도 고려하여 Feature를 생성한다.
def gender_features(name):
    features = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    features.append(alphabet.find(name[0].lower()) / 10)
    features.append(alphabet.find(name[-1].lower()) / 10)
    for letter in alphabet:
        features.append(name.lower().count(letter))
    return np.array(features)

# 이름-성별 데이터에서 학습을 위한 Feature를 생성하여, 학습 데이터와 시험 데이터를 생성한다.
featX = np.array([gender_features(n) for (n, gender) in labeled_names])
featY = np.array([gender for (n, gender) in labeled_names])

# PCA로 차원을 축소한다
pca = decomposition.PCA(n_components = 14)
featX = pca.fit_transform(featX)

###################################################################################
## PCA 절차를 manual로 수행하면 아래 절차와 같다.(수동///sklearn없음 해야함)
## feature들의 공분산 행렬을 구한다. Transpose를 취해야 한다.
#mx = featX - np.mean(featX, axis = 0) 
#C = np.cov(featX, rowvar = False)
#
## 공분산 행렬에 대한 고유벡터와 고윳값을 계산한다.
#eigenValue, eigenVector = np.linalg.eigh(C)
#
## eigenValue를 육안으로 확인한다. 가장 큰 순서대로 14개의 비중을 확인해 본다.
## ex : sum(eigenValue[0:14]) / sum(eigenValue) = 90.2%
## 상위 14개 feature 공간으로 projection 한다.
## eigenVectors : The normalized (unit “length”) eigenvectors, such that the 
## column v[:,i] is the eigenvector corresponding to the eigenvalue w[i].
#nFeatures = 14
#idx = np.argsort(eigenValue)[::-1]
#eigenVector = eigenVector[:,idx]
#eigenValue = eigenValue[idx]
#featX = np.dot(mx, eigenVector[:,0:nFeatures])
###################################################################################
n = int(len(featX) * 0.8)
x_train, y_train = featX[:n], featY[:n]
x_test, y_test = featX[n:], featY[n:]

print(x_train[:10])
print(y_train[:10])

batch_size = 256
nb_epochs = 100

# 모델
model = Sequential()
model.add(Dense(100, input_shape= (x_train.shape[1],)))
model.add(Activation('relu'))
model.add(Dropout(0.9))

model.add(Dense(1000))
model.add(Activation('relu'))
model.add(Dropout(0.9))

model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(loss='mse', optimizer='adam')
print (model.summary())

# 학습
model.fit(x_train, y_train, batch_size=batch_size, epochs=nb_epochs, verbose=1)

# 예측
y_pred = model.predict_classes(x_test, batch_size=batch_size).reshape(-1,)

# 평가
acc = accuracy_score(y_test, y_pred)
print("Accuracy = %.4f" % acc)

#######################################################################
# 28개 feature를 2차원 공간상에 투영한 모습을 그려본다.
featX = np.array([gender_features(n) for (n, gender) in labeled_names])
featY = np.array([gender for (n, gender) in labeled_names])

# PCA로 차원을 축소한다
pca = decomposition.PCA(n_components = 2) #2차원으로 줄임
featX = pca.fit_transform(featX)

x = featX[np.where(featY == 0)]
y = featX[np.where(featY == 1)]

import matplotlib.pyplot as plt
plt.figure(figsize=(12, 10))
plt.scatter(x[:, 0], x[:, 1], c='blue', s=10, alpha = 0.5, label = 'mle')
plt.scatter(y[:, 0], y[:, 1], c='red', s=10, alpha = 0.5, label = 'female')
plt.legend()
plt.show()
