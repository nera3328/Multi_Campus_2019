	
from keras.models import Model
from keras.layers import Conv1D, Dense, Input, GlobalMaxPooling1D
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from keras import backend as K
from numpy import argmax

text=['dog like cat', 
      'dog dog fish river',
      'cat cute odd eye', 
      'cat dog human',
      'dog bark cut cry',
      'cat run dog run',
      'cat cat cat dog dog dog ',
      'dog eat cat cat dog']
z_test=['dog cat dog cat']

#TF-IDF-수치화
tfvec=TfidfVectorizer()
tf=tfvec.fit(text)

tf_vec=tf.transform(text).toarray()
np.round(tf_vec,3)
tf_vec.shape

tf_vecz=tf.transform(z_test).toarray()
tf_vecz.shape

x_train=tf_vec.reshape([8,14,1])
y_train=np.random.choice([0,1],[8,1])
z_test=tf_vecz.reshape([1,14,1])

#CNN
K.clear_session()

x_input = Input(batch_shape=(None, 14, 1))
conv = Conv1D(20,3, activation='relu')(x_input)
xpool = GlobalMaxPooling1D()(conv)
x_output = (Dense(1, activation='sigmoid'))(xpool)

model=Model(x_input, x_output)
model.summary()
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(x_train, y_train, epochs=50, batch_size=1)

a=model.predict(z_test)
print(a)

np.argmax(a)


dic_text=[]
for i in range(len(text)):
    