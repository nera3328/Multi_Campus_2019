# CNN 예시 : 2D convolution을 이용하여 Stock price 시계열을 예측해 본다.
# 
# Image data: 10-기간, 8개 feature data를 학습한다.
#          t1  t2  t3  t4  t5  t6  t7  t8  t9  t10  y
# Open      .   .   .   .   .   .   .   .   .   .   .
# High      .   .   .   .   .   .   .   .   .   .   .
# Low       .   .   .   .   .   .   .   .   .   .   .
# Close     .   .   여기에 Convolution filter    .   .
# ShortMA   .   .   (4 X 4)를 적용한다. .   .    .   .
# LongMA    .   .   .   .   .   .   .   .   .   .   .
# MACD      .   .   .   .   .   .   .   .   .   .   .
# RSI       .   .   .   .   .   .   .   .   .   .   .
#
# [Convolution --> Relu --> Max pooling] --> [Convolution --> Relu --> Max pooling] -> [Fulliy connected N/W]
# Convolution layer 2개와 2층 신경망으로 구성함.
#
# 2018.11.28, 아마추어퀀트 (조성현)
# ------------------------------------------------------------------------------------------------------------
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from MyUtil import TaFeatureSet

MASHORT = 5         # 종가의 단기 이동평균
MALONG = 20         # 종가의 장기 이동평균
nStep = 20
nFilRow1, nFilCol1 = (4, 6)        # 4 x 6 filter
nFilRow2, nFilCol2 = (4, 6)        # 4 x 6 filter
nFilter1 = 10                      # filter 10개
nFilter2 = 10                      # filter 10개
nKsizeRow1, nKsizeCol1 = (4, 6)    # 4 x 6 ksize
nKsizeRow2, nKsizeCol2 = (4, 6)    # 4 x 6 ksize
nHidden = 100                      # Fully connected layer의 hidden neuron 개수

saveDir = './Saver/6-7.save'   # 학습 결과를 저정할 폴더
saveFile = saveDir + '/save'   # 학습 결과를 저장할 파일

# Batch data를 생성한다.
# MNIST 이미지와 같은 형태의 데이터 차원으로 변환한다.
def createTrainData(xData, step=nStep):
    height = xData.shape[1]
    width = step
    channel = 1
    m = np.arange(xData.shape[0] + 1)
    xData = xData.T
    
    x, y = [], []
    for i in m[0:(-step-5)]:
        a = xData[:, i:(i+step)]
        x.append(a)
    xBatch = np.reshape(np.array(x), (len(m[0:(-step-5)]), height, width, channel))
    
    # 5일후 이동평균을 예측한다
    for i in m[0:(-step-5)]:
        a = xData[4, i + step + 5 - 1]
        y.append(a)
    yBatch = np.reshape(np.array(y), (len(m[0:(-step-5)]), 1))
    
    return xBatch, yBatch

# Normalize OHLC price
def normalizeOHLC(ohlc):
    m = np.mean(ohlc.mean())
    scale = np.mean(ohlc.std())
    
    rdf = pd.DataFrame((ohlc['Open'] - m) / scale)
    rdf['High'] = (ohlc['High'] - m) / scale
    rdf['Low'] = (ohlc['Low'] - m) / scale
    rdf['Close'] = (ohlc['Close'] - m) / scale
    return rdf

# Chart OHLC price
def plotOHLC(ohlc, n=300):
    d = ohlc.tail(n)
    plt.figure(figsize=(8, 5))
    plt.plot(d['Open'])
    plt.plot(d['High'])
    plt.plot(d['Low'])
    plt.plot(d['Close'])
    plt.title("OHLC chart")
    plt.show()
    
# 주가 데이터
df = pd.read_csv('./stockData/005930.csv', index_col=0, parse_dates=True)
df = df.sort_index()
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
df = df.drop('Volume', 1)

# Normalize OHLC
ndf = normalizeOHLC(df)

ndf['maShort'] = pd.DataFrame(df['Close']).rolling(window=MASHORT).mean()
ndf['maLong'] = pd.DataFrame(df['Close']).rolling(window=MALONG).mean()
ndf['macd'] = TaFeatureSet.MACD(df)
ndf['rsi'] = TaFeatureSet.RSI(df)
ndf = ndf.dropna()

# Normalize other features
ndf['maShort'] = (ndf['maShort'] - ndf['maShort'].mean()) / ndf['maShort'].std()
ndf['maLong'] = (ndf['maLong'] - ndf['maLong'].mean()) / ndf['maLong'].std()
ndf['macd'] = (ndf['macd'] - ndf['macd'].mean()) / ndf['macd'].std()
ndf['rsi'] = (ndf['rsi'] - ndf['rsi'].mean()) / ndf['rsi'].std()

# Normalize가 잘 되었는지 chart로 확인해 본다
plotOHLC(df)
plotOHLC(ndf)

# Create batch data
data = np.array(ndf)
xBatch, yBatch = createTrainData(data, nStep)
nHeight = xBatch.shape[1]
nY = yBatch.shape[0]
nBatch = nY

tf.reset_default_graph()
X = tf.placeholder(tf.float32, [None, nHeight, nStep, 1])
Y = tf.placeholder(tf.float32, [None, 1])

# 1. First convolution layer
# --------------------------
Wc1 = tf.Variable(tf.random_normal([nFilRow1, nFilCol1, 1, nFilter1], stddev=0.01))
Bc1 = tf.Variable(tf.random_normal([nFilter1]))
Cl1 = tf.nn.conv2d(X, Wc1, strides=[1,1,1,1], padding='SAME')
Cl1 = tf.nn.relu(tf.add(Cl1, Bc1))
Pl1 = tf.nn.max_pool(Cl1, ksize=[1, nKsizeRow1, nKsizeCol1, 1], strides=[1,1,1,1], padding='SAME')

# 2. Second convolution layer
# ---------------------------
Wc2 = tf.Variable(tf.random_normal([nFilRow2, nFilCol2, nFilter1, nFilter2], stddev=0.01))
Bc2 = tf.Variable(tf.random_normal([nFilter2]))
Cl2 = tf.nn.conv2d(Pl1, Wc2, strides=[1,1,1,1], padding='SAME')
Cl2 = tf.nn.relu(tf.add(Cl2, Bc2))
Pl2 = tf.nn.max_pool(Cl2, ksize=[1, nKsizeRow2, nKsizeCol2, 1], strides=[1,1,1,1], padding='SAME')
Pl2 = tf.reshape(Pl2, [-1, nHeight * nStep * nFilter2])

# 3. Fully connected layer (Hidden layer 1개, nHidden개의 neuron)
# ---------------------------------------------------------------
Wh = tf.Variable(tf.random_normal([nHeight * nStep * nFilter2, nHidden], stddev=0.01))
Bh = tf.Variable(tf.random_normal([nHidden]))
Oh = tf.nn.relu(tf.add(tf.matmul(Pl2, Wh), Bh))

Wo = tf.Variable(tf.random_normal([nHidden, 1], stddev=0.01))
Bo = tf.Variable(tf.random_normal([1]))
predY = tf.add(tf.matmul(Oh, Wo), Bo)

loss = tf.reduce_mean(tf.square(tf.subtract(predY, Y)))
optimizer = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(loss)

# 저장
saver = tf.train.Saver()

# Train
# -----
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 기존 학습 결과를 적용한 후 추가로 학습한다
if tf.train.checkpoint_exists(saveDir):
    saver.restore(sess, saveFile)
    
lossHist = []
nBatchCnt = 10       # Mini-batch를 위해 input 데이터를 n개 블록으로 나눈다.
nBatchSize = int(xBatch.shape[0] / nBatchCnt)  # 블록 당 Size
m = np.arange(xBatch.shape[0])
for i in range(0, 10):
    # xBatch, yBatch를 shuffing 한다. 순차적 이미지의 상관성 제거.
    np.random.shuffle(m)
    xShuffle = xBatch[m]
    yShuffle = yBatch[m]
    
    # Mini-batch training
    for n in range(nBatchCnt):
        # input 데이터를 Mini-batch 크기에 맞게 자른다
        nFrom = n * nBatchSize
        nTo = n * nBatchSize + nBatchSize
        
        # 마지막 루프이면 nTo는 input 데이터의 끝까지.
        if n == nBatchCnt - 1:
            nTo = xBatch.shape[0]
               
        # 학습 데이터를 준비한다
        bx = xShuffle[nFrom : nTo]
        by = yShuffle[nFrom : nTo]
        rLoss, _ = sess.run([loss, optimizer], feed_dict={X: bx, Y: by})
    lossHist.append(rLoss)
    print("%d] loss = %.4f" % (i, rLoss))

# 학습 결과를 저장해 둔다
saver.save(sess, saveFile)

# 향후 1 기간 데이터를 예측한다.
if len(data) > 200:
    lastData = np.copy(data[-200:])  # 원 데이터의 마지막 100개만 이용한다
else:
    lastData = np.copy(data[:])
    
# 마지막 nStep 만큼 입력데이로 다음 값을 예측한다
dx = np.copy(lastData[-nStep:,]).T
px = np.reshape(dx, (-1, nHeight, nStep, 1))

# 다음 값을 예측한다.
yHat = sess.run(predY, feed_dict={X: px})[0][0]
    
# Loss history를 그린다
plt.figure(figsize=(8, 3))
plt.plot(lossHist, color='red')
plt.title("Loss History")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 원 시계열과 예측된 시계열을 그린다
ax1 = np.arange(1, len(lastData) + 1)
ax2 = np.arange(len(lastData), len(lastData) + 5 + 1)
plt.figure(figsize=(10, 5))
plt.plot(ax1, lastData[:, 3], 'b-o', markersize=4, color='blue', label='Time series', linewidth=1)
plt.plot(ax1, lastData[:, 4], color='red', label='Time series', linewidth=1)
plt.plot((200, 205), (lastData[-1:, 3], yHat), 'b-o', markersize=8, color='red', label='Estimate')
plt.axvline(x=ax1[-1],  linestyle='dashed', linewidth=1)
plt.legend()
plt.show()
