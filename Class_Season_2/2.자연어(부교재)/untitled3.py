from keras.preprocessing import sequence
from keras.models import Model
from keras.layers import Input, Dense, Embedding, Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb
from sklearn.metrics import accuracy_score

max_features = 6000
max_length = 400

import numpy as np
old = np.load
np.load = lambda *a,**k: old(*a,**k,allow_pickle=True)
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
np.load = old
del(old)

x_train=sequence.pad_sequences(x_train, maxlen=max_length)
x_test=sequence.pad_sequences(x_test, maxlen=max_length)
print(x_train)
print(y_train[1])