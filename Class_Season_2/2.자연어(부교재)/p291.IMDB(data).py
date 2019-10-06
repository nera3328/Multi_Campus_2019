from keras.datasets import imdb
import numpy as np

old = np.load
np.load = lambda *a,**k: old(*a,**k,allow_pickle=True)
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=6000) #이거 숫자 줄이면 더 많이 * 되겠지?
np.load = old
del(old)

print(x_train[0])
print(y_train[0])

wind = imdb.get_word_index() #imdb 전체 단어 목록을 보여준다 = Key : Value 형태로 보여줌 원래 key값으로 value를 검색하나, 여기선 역방향으로 검색도 가능하다.
wind['kagan']
revind = dict((v, k) for k, v in wind.items())
#                       key value  모든 내용에서
#         value가 key, key가 value가 됨

def decode(sent_list):
    new_words = []
    for i in sent_list:
        new_words.append(revind.get(i-3, '*')) # 0: padding, 1 : start, 2 : out of vocabulary  얘네면 *로 대체
    comb_words = ' '.join(new_words)
    return comb_words

decode(x_train[0])
 # 원래 인코딩 전 raw문서가 나옴. *는 out of voca라 저런식으로 표현됨.