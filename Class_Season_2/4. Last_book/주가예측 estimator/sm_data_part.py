import pandas as pd
import numpy as np
import tensorflow as tf

df=pd.read_csv('005930.csv' )
df=df.sort_index()
df=df.dropna()

df.iloc[0]
price =  np.array(df.iloc[:, 5], dtype=np.float32)
price = list((price-price.mean())/price.std())

xdata=[]
ydata=[]

ntime=20
nstep=3

#3차원으로 넣어주기--lSTM
for i in range(0, len(price)-ntime, nstep):
    xdata.append(price[i : i+ntime])
    ydata.append(price[i + ntime])

#학습용
xtrain = np.array(xdata)[:-1, :].reshape(-1, ntime, 1)
ytrain = np.array(ydata)[:-1].reshape(-1, 1)

#예측용
x_pred = np.array(xdata)[-1:, :].reshape(-1, ntime, 1)
y_pred = np.array(ydata)[-1:].reshape(-1, 1)  # 예측 결과 확인용 (참고용임)

#np.round(price,5)

def train_input_fn():
    dataset = tf.data.Dataset.from_tensor_slices((xtrain, ytrain))\
            .repeat()\
            .batch(12)\
            .make_one_shot_iterator()\
            .get_next()
    return {'x': dataset[0]}, dataset[1] #x는 dictionary로, y값은 label로 보내겠다


def test_input_fn():
    dataset = tf.data.Dataset.from_tensor_slices((xtest, ytest))\
            .repeat()\
            .batch(xtest.shape[0])\
            .make_one_shot_iterator()\
            .get_next()
    return {'x': dataset[0]}, dataset[1] #x는 dictionary로, y값은 label로 보내겠다