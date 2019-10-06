from keras.preprocessing import sequence
from keras.models import Model
from keras.layers import Input, Dense, Embedding, Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb
from sklearn.metrics import accuracy_score

max_features = 6000 #vocabulary 중 가장 많이 쓰인 6000개만 쓰겠다.
max_length = 400 #한 문장의 단어 개수(패딩)

import numpy as np
old = np.load
np.load = lambda *a,**k: old(*a,**k,allow_pickle=True)
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
np.load = old
del(old)

print(x_train[1]) #1 과 2는 특수언어 (vocabulary에 없는 단어 ex- 1: start..)

x_train = sequence.pad_sequences(x_train, maxlen=max_length)
x_test = sequence.pad_sequences(x_test, maxlen=max_length)

xInput = Input(batch_shape=(None, max_length))
xEmbed = Embedding(max_features, 60, input_length = max_length)(xInput) #word embedding 60개 받아야징 
xConv = Conv1D(260, 3, activation='relu')(xEmbed) #padding 옵션을 same으로 주면 얘도 다른애랑 동일해짐
        #필터씌움 filter= 60x3 260개에 바이어스 +260------> 3*60*260+260 하면 w값이 47060이 나온다!
xPool = GlobalMaxPooling1D()(xConv)
xOutput = Dense(1, activation='sigmoid')(xPool)
model = Model(xInput, xOutput)
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(x_train, y_train, batch_size=32, epochs = 1)

model.summary()
#param = weight
#trainable parmeter : w 개수, 

y_hat = model.predict(x_test, batch_size=32)
y_hat_class = np.round(y_hat, 0)
y_hat_class.shape = y_test.shape

print (("Test accuracy:"),(np.round(accuracy_score(y_test,y_hat_class),3)))
