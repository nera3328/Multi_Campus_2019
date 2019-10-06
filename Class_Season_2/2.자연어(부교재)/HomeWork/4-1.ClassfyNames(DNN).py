# Gender Identification
import random
from nltk.corpus import names
import numpy as np

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from sklearn.metrics import accuracy_score

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

n = int(len(featX) * 0.8)
x_train, y_train = featX[:n], featY[:n]
x_test, y_test = featX[n:], featY[n:]

print(x_train[:10])
print(y_train[:10])

batch_size = 256
nb_epochs = 100

# 모델
model = Sequential()
model.add(Dense(500, input_shape= (x_train.shape[1],))) #히든 레이어 노드 수  500개 dense는입력과 출력을 연결해줌
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(500))
model.add(Activation('relu'))
model.add(Dropout(0.1))

model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam')
print (model.summary())

# 학습
model.fit(x_train, y_train, batch_size=batch_size, epochs=nb_epochs, verbose=1) #verbose 주면 중간 중간 결과를 보여준다.

# 예측
y_pred = model.predict_classes(x_test, batch_size=batch_size).reshape(-1,)

# 평가
acc = accuracy_score(y_test, y_pred)
print("Accuracy = %.4f" % acc)
