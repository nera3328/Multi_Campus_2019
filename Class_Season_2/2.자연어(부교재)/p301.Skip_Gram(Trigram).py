from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import collections
import nltk
from keras.layers import Input, Dense, Dropout
from keras.models import Model
from textUtils import textPreprocessing

#소설을 읽어온다
lines = []
fin = open("alice_in_wonderland.txt", "r")
   #                                   'rb' r=read용, text모드로 한 길로 쭉 open할 때  b=binary모드 읽을때 앞 뒤로 왔다갔다 하면서 읽으라할떄
for line in fin:
    if len(line) <= 1:
        continue
    lines.append(textPreprocessing(line)) #소설 전체로 한 줄씩 읽어옴
fin.close()#          textPreprocessing : preprocessing으로 전처리 (pos/neg)


#vocabulary를 만들어----->Set()-->dict()
counter = collections.Counter()# a=['aa','bb','cc','aa']-->counter(a)하면 ['aa':2, 'bb':1, 'cc' : 1] 이런식으로나와줌
#                                                   counter['aa']=500하면 개수도 바뀜!
for line in lines:
    for word in nltk.word_tokenize(line):
        counter[word.lower()] += 1
#               단어 사용빈도
#counter
#                          _는 더미변수
word2idx = {w:(i+1) for i,(w,_) in enumerate(counter.most_common())} #빈도 순서로 정렬->onehot으로 하는데 굳이 이렇게 할 필요는 없음(컴퓨터에게는 의미 없음)
idx2word = {v:k for k,v in word2idx.items()}
#           뒤집
#Voca완성

#학습 데이터를 만든다
xs = []
ys = []

for line in lines: #한줄씩!
    embedding = [word2idx[w.lower()] for w in nltk.word_tokenize(line)] #word2idx하면 문자->숫자
    triples = list(nltk.trigrams(embedding))#3 단어씩 관계맺기
    #중간 단어를 가지고 학습 data만들어줌-->주변단어(Context-(의미자질(semantic feature)))
    w_lefts = [x[0] for x in triples]
    w_centers = [x[1] for x in triples]
    w_rights = [x[2] for x in triples]
#triples
    xs.extend(w_centers)
    ys.extend(w_lefts)
    xs.extend(w_centers)
    ys.extend(w_rights)
          
print (len(word2idx))
vocab_size = len(word2idx)+1

#onehot으로 바꾸자
ohe = OneHotEncoder(categories = [range(vocab_size)])

X = ohe.fit_transform(np.array(xs).reshape(-1, 1)).todense()
Y = ohe.fit_transform(np.array(ys).reshape(-1, 1)).todense()

Xtrain, Xtest, Ytrain, Ytest, xstr, xsts = train_test_split(X, Y, xs, test_size=0.3, random_state=42)
print(Xtrain.shape, Xtest.shape, Ytrain.shape, Ytest.shape)

#모델 만들기, 학습하기
np.random.seed(42)

BATCH_SIZE = 128
NUM_EPOCHS = 20

input_layer = Input(shape = (Xtrain.shape[1],))
first_layer = Dense(300, activation='relu')(input_layer)
first_dropout = Dropout(0.5)(first_layer)
second_layer = Dense(2, activation='relu')(first_dropout)
third_layer = Dense(300, activation='relu')(second_layer)
third_dropout = Dropout(0.5)(third_layer)
fourth_layer = Dense(Ytrain.shape[1], activation='softmax')(third_dropout)

history = Model(input_layer, fourth_layer)
history.compile(optimizer = "rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
history.fit(Xtrain, Ytrain, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS, verbose=1, validation_split = 0.2)

#word embedding vector 값을 추출한다
encoder = Model(input_layer,fourth_layer)
reduced_X = encoder.predict(Xtest)

#np.argmax(Xtest[0])
#x=encoder.predict(Xtest[1])
#y=encoder.predict(Xtest[1])
#z=encoder.predict(Xtest[2])
#idx2word[np.argmax(Xtest[1])]
#idx2word[np.argmax(Xtest[2])]
#np.sqrt(np.sum((X-y)**2))
#np.sqrt(np.sum((X-Y)**2))

#word embedding  시각화
final_pdframe = pd.DataFrame(reduced_X)
final_pdframe.columns = ["xaxis","yaxis"]
final_pdframe["word_indx"] = xsts
final_pdframe["word"] = final_pdframe["word_indx"].map(idx2word)
final_pdframe.head()

vis_df = final_pdframe.sample(100)

labels = list(vis_df["word"])
xvals = list(vis_df["xaxis"])
yvals = list(vis_df["yaxis"])

#in inches
plt.figure(figsize=(14, 10))  

for i, label in enumerate(labels):
    x = xvals[i]
    y = yvals[i]
    
    plt.scatter(x, y)
    plt.annotate(label,xy=(x, y),xytext=(5, 2),textcoords='offset points', ha='right',va='bottom')

plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.show()

#이해하기 힘든 단어관계====>2차원으로 시각화해서 보기 좋게 만들어서 그럼. 10차원정도는 되어줘야해
