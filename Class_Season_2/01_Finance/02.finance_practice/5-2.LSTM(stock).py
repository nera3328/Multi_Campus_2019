# LSTM(GRU) 예시 : KODEX200 주가 (2010 ~ 현재)를 예측해 본다.
# KODEX200의 종가와, 10일, 40일 이동평균을 이용하여 향후 10일 동안의 종가를 예측해 본다.
# 과거 20일 (step = 20) 종가, 이동평균 패턴을 학습하여 예측한다.
# 일일 주가에 대해 예측이 가능할까 ??
#
# 2018.11.22, 아마추어퀀트 (조성현)
# --------------------------------------------------------------------------
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from MyUtil import YahooData

nInput = 3
nOutput = 3
nStep = 20
nNeuron = 50

# 2차원 배열의 시계열 데이터로 학습용 배치 파일을 만든다.
# return : xBatch - RNN 입력
#          yBatch - RNN 출력
#
# step = 2, n = 3 이라면,
# xData = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], ...]
# xBatch = [[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]], ...]
# yBatch = [[[4,5,6], [7,8,9]], [[10,11,12], [13,14,15]], ...]
def createTrainData(xData, step, n=nInput):
    m = np.arange(len(xData) - step)
    np.random.shuffle(m)
    
    x, y = [], []
    for i in m:
        a = xData[i:(i+step)]
        x.append(a)
    xBatch = np.reshape(np.array(x), (len(m), step, n))
    
    for i in m+1:
        a = xData[i:(i+step)]
        y.append(a)
    yBatch = np.reshape(np.array(y), (len(m), step, n))
    
    return xBatch, yBatch

# 주가 데이터
df = pd.read_csv('./stockData/005930.csv', index_col=0, parse_dates=True)
df = df.sort_index()
df = pd.DataFrame(df['close'])
df['ma_10'] = pd.DataFrame(df['close']).rolling(window=10).mean()
df['ma_40'] = pd.DataFrame(df['close']).rolling(window=40).mean()
df = df.dropna()
df = (df - df.mean()) / df.std()

# 학습 데이터를 생성한다.
data = np.array(df)
xBatch, yBatch = createTrainData(data, nStep)

# RNN 그래프를 생성한다 (Wx, Wh). xBatch를 RNN에 입력한다.
tf.reset_default_graph()
x = tf.placeholder(tf.float32, [None, nStep, nInput])  
rnn = tf.nn.rnn_cell.LSTMCell(nNeuron)
#rnn = tf.nn.rnn_cell.GRUCell(nNeuron)
output, state = tf.nn.dynamic_rnn(rnn, x, dtype=tf.float32)

# RNN의 출력값을 입력으로 받아 3개의 y가 출력되도록 하는 feed-forward network를 생성한다. (Wy)
y = tf.placeholder(tf.float32, [None, nStep, nOutput])
inFC = tf.reshape(output, [-1, nNeuron])          
fc1 = tf.contrib.layers.fully_connected(inputs=inFC, num_outputs=nNeuron)
predY = tf.contrib.layers.fully_connected(inputs=fc1, num_outputs=nOutput, activation_fn=None)    
predY = tf.reshape(predY, [-1, nStep, nOutput])

# Mean square error (MSE)로 Loss를 정의한다. xBatch가 입력되면 yBatch가 출력되도록 함.
loss = tf.reduce_sum(tf.square(predY - y))    
optimizer = tf.train.AdamOptimizer(learning_rate=0.001)         
minLoss = optimizer.minimize(loss)

# 그래프를 실행한다. 학습한다. (Wx, Wh, Wy를 업데이트함)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
lossHist = []
for i in range(300):
    sess.run(minLoss, feed_dict={x: xBatch, y: yBatch})
    
    if i % 5 == 0:
        ploss = sess.run(loss, feed_dict={x: xBatch, y: yBatch})
        lossHist.append(ploss)
        print(i, "\tLoss:", ploss)

# 향후 10 기간 데이터를 예측한다. 향후 1 기간을 예측하고, 예측값을 다시 입력하여 2 기간을 예측한다.
# 이런 방식으로 10 기간까지 예측한다.
nFuture = 10
if len(data) > 100:
    lastData = np.copy(data[-100:])  # 원 데이터의 마지막 100개만 그려본다
else:
    lastData = np.copy(data)
dx = np.copy(lastData)
estimate = [dx[-1]]
for i in range(nFuture):
    # 마지막 nStep 만큼 입력데이로 다음 값을 예측한다
    px = dx[-nStep:,]
    px = np.reshape(px, (1, nStep, nInput))
    
    # 다음 값을 예측한다.
    yHat = sess.run(predY, feed_dict={x: px})[0][-1]
    
    # 예측값을 저장해 둔다
    estimate.append(yHat)
    
    # 이전 예측값을 포함하여 또 다음 값을 예측하기위해 예측한 값을 저장해 둔다
    dx = np.vstack([dx, yHat])

# Loss history를 그린다
plt.figure(figsize=(8, 3))
plt.plot(lossHist, color='red')
plt.title("Loss History")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 주가 차트와 이동평균을 그린다.
plt.figure(figsize=(8, 3))
plt.plot(df['close'], color='red')
plt.plot(df['ma_10'], color='blue')
plt.plot(df['ma_40'], color='green')
plt.title("Samsung stock price")
plt.show()

# 원 시계열과 예측된 시계열을 그린다
CLOSE = 0       # 종가를 예측한다
estimate = np.array(estimate)
ax1 = np.arange(1, len(lastData[:, CLOSE]) + 1)
ax2 = np.arange(len(lastData), len(lastData) + len(estimate))
plt.figure(figsize=(8, 3))
plt.plot(ax1, lastData[:, CLOSE], 'b-o', color='blue', markersize=4, label='Stock price', linewidth=1)
plt.plot(ax2, estimate[:, CLOSE], 'b-o', color='red', markersize=4, label='Estimate')
plt.axvline(x=ax1[-1],  linestyle='dashed', linewidth=1)
plt.legend()
plt.title("Samsung prediction")
plt.show()

