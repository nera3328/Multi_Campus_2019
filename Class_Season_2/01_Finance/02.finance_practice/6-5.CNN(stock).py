# CNN 예시 : 1D convolution을 이용하여 Stock price 시계열을 예측해 본다.
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

# Batch data를 생성한다.
def createTrainData(xData, step):
    m = np.arange(len(xData) - step)
    np.random.shuffle(m)
    
    x, y = [], []
    for i in m:
        a = xData[i:(i+step)]
        x.append(a)
    xBatch = np.reshape(np.array(x), (len(m), 1, step, 1))
    
    for i in m+1:
        a = xData[i:(i+step)][-1]
        y.append(a)
    yBatch = np.reshape(np.array(y), (len(m), 1))
    
    return xBatch, yBatch

# 주가 데이터
df = pd.read_csv('./stockData/105560.csv', index_col=0, parse_dates=True)
df = df.sort_index()
data = np.array(df['close'])
data = (data - data.mean()) / data.std() # Normalization

nStep = 20
nFilterDim1 = 4     # 4 x 1 filter
nFilterDim2 = 4     # 4 x 1 filter
nFilter1 = 10       # filter 10개
nFilter2 = 10       # filter 10개
nKsize1 = 4         # 1 x 4 ksize
nKsize2 = 4         # 1 x 4 ksize
nHidden = 100       # Fully connected layer의 hidden neuron 개수

# Create batch data
xBatch, yBatch = createTrainData(data, nStep)
nY = yBatch.shape[0]
nBatch = nY

tf.reset_default_graph()
X = tf.placeholder(tf.float32, [None, 1, nStep, 1])
Y = tf.placeholder(tf.float32, [None, 1])

# 1. First convolution layer
# --------------------------
Wc1 = tf.Variable(tf.random_normal([1,nFilterDim1,1,nFilter1], stddev=0.01))
Bc1 = tf.Variable(tf.random_normal([nFilter1]))
Cl1 = tf.nn.conv2d(X, Wc1, strides=[1,1,1,1], padding='SAME')
Cl1 = tf.nn.relu(tf.add(Cl1, Bc1))
Pl1 = tf.nn.max_pool(Cl1, ksize=[1,1,nKsize1,1], strides=[1,1,1,1], padding='SAME')

# 2. Second convolution layer
# ---------------------------
Wc2 = tf.Variable(tf.random_normal([1,nFilterDim2,nFilter1,nFilter2], stddev=0.01))
Bc2 = tf.Variable(tf.random_normal([nFilter2]))
Cl2 = tf.nn.conv2d(Pl1, Wc2, strides=[1,1,1,1], padding='SAME')
Cl2 = tf.nn.relu(tf.add(Cl2, Bc2))
Pl2 = tf.nn.max_pool(Cl2, ksize=[1,1,nKsize2,1], strides=[1,1,1,1], padding='SAME')
Pl2 = tf.reshape(Pl2, [-1, nStep * nFilter2])

# 3. Fully connected layer (Hidden layer 1개, nHidden개의 neuron)
# ---------------------------------------------------------------
Wh = tf.Variable(tf.random_normal([nStep * nFilter2, nHidden], stddev=0.01))
Bh = tf.Variable(tf.random_normal([nHidden]))
Oh = tf.nn.relu(tf.add(tf.matmul(Pl2, Wh), Bh))

Wo = tf.Variable(tf.random_normal([nHidden, 1], stddev=0.01))
Bo = tf.Variable(tf.random_normal([1]))
predY = tf.add(tf.matmul(Oh, Wo), Bo)

loss = tf.reduce_mean(tf.square(tf.subtract(predY, Y)))
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

# Train
# -----
sess = tf.Session()
sess.run(tf.global_variables_initializer())

lossHist = []
for i in range(0, 1000):
    rLoss, _ = sess.run([loss, optimizer], feed_dict={X: xBatch, Y: yBatch})
    lossHist.append(rLoss)
    
    if (i % 10) == 0:
        print("%d] loss = %.4f" % (i, rLoss))

# 향후 10 기간 데이터를 예측한다. 향후 1 기간을 예측하고, 예측값을 다시 입력하여 2 기간을 예측한다.
# 이런 방식으로 10 기간까지 예측한다.
nFuture = 10
if len(data) > 200:
    lastData = np.copy(data[-200:])  # 원 데이터의 마지막 100개만 그려본다
else:
    lastData = np.copy(data)
dx = np.copy(lastData)
estimate = [dx[-1]]
for i in range(nFuture):
    # 마지막 nStep 만큼 입력데이로 다음 값을 예측한다
    px = dx[-nStep:]
    px = np.reshape(px, (-1, 1, nStep, 1))
    
    # 다음 값을 예측한다.
    yHat = sess.run(predY, feed_dict={X: px})[0]
    
    # 예측값을 저장해 둔다
    estimate.append(yHat)
    
    # 이전 예측값을 포함하여 또 다음 값을 예측하기위해 예측한 값을 저장해 둔다
    dx = np.insert(dx, len(dx), yHat)

# Loss history를 그린다
plt.figure(figsize=(8, 3))
plt.plot(lossHist, color='red')
plt.title("Loss History")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 원 시계열과 예측된 시계열을 그린다
ax1 = np.arange(1, len(lastData) + 1)
ax2 = np.arange(len(lastData), len(lastData) + len(estimate))
plt.figure(figsize=(8, 5))
plt.plot(ax1, lastData, 'b-o', markersize=4, color='blue', label='Time series', linewidth=1)
plt.plot(ax2, estimate, 'b-o', markersize=4, color='red', label='Estimate')
plt.axvline(x=ax1[-1],  linestyle='dashed', linewidth=1)
plt.legend()
plt.show()
