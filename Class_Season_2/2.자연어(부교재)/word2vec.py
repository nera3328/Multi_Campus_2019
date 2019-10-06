
import gensim
import numpy as np

path = './GoogleNews-vectors-negative300.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(path, binary=True)


#단어 간 유사도
m=model['mother']
f=model['father']
d=model['daughter']
s=model['son']

#유클리드 거리(유사도)
np.sqrt(np.sum((m-f)**2))
np.sqrt(np.sum((d-s)**2))
np.sqrt(np.sum((m-d)**2))
np.sqrt(np.sum((s-f)**2))

#cos거리
cos=np.dot(m,f)/(np.linalg.norm(m)*np.linalg.norm(y))
cos

#링코프스키(Minkovski)
np.sum((m-f)**3)**(1/3)**3
