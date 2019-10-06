# CNN 예시 : 1D convolution을 이용하여 직선 (y=x) 시계열을 예측해 본다.
# 
# [Convolution --> Relu --> Max pooling] -> [Fulliy connected N/W]
# Convolution layer 1개와 단층 신경망으로 구성함.
#
# 2018.11.28, 아마추어퀀트 (조성현)
# -------------------------------------------------------------------
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Batch data를 생성한다.
def createTrainData(xData, step):
    m = np.arange(len(xData) - step)
#    np.random.shuffle(m)
    
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

# 시계열 데이터 (y=x 직선 10001개)
data = np.arange(1001)

nStep = 10
nFilterDim = 3     # 3 x 1 filter
nFilter = 10       # filter 10개
nKsize = 3         # 1 x 3 ksize

# Create batch data
xBatch, yBatch = createTrainData(data, nStep)
nY = yBatch.shape[0]
nBatch = nY

tf.reset_default_graph()
X = tf.placeholder(tf.float32, [None, 1, nStep, 1])
Y = tf.placeholder(tf.float32, [None, 1])

# 1. Convolution layer (1개)
# --------------------------
Wc = tf.Variable(tf.random_normal([1,nFilterDim,1,nFilter], stddev=0.01))
Bc = tf.Variable(tf.random_normal([nFilter]))
Cl = tf.nn.conv2d(X, Wc, strides=[1,1,1,1], padding='SAME')
Cl = tf.nn.relu(tf.add(Cl, Bc))
Pl = tf.nn.max_pool(Cl, ksize=[1,1,nKsize,1], strides=[1,1,1,1], padding='SAME')
Pl = tf.reshape(Pl, [-1, nStep * nFilter])

# 2. Fully connected layer (단층 신경망)
# --------------------------------------
Wo = tf.Variable(tf.random_normal([nStep * nFilter, 1], stddev=0.01))
Bo = tf.Variable(tf.random_normal([1]))
predY = tf.add(tf.matmul(Pl, Wo), Bo)

# Loss function 정의
loss = tf.reduce_mean(tf.square(tf.subtract(predY, Y)))
optimizer = tf.train.AdamOptimizer(learning_rate=0.0005).minimize(loss)

# Train
# -----
sess = tf.Session()
sess.run(tf.global_variables_initializer())

lossHist = []
for i in range(0, 2000):
    rLoss, _ = sess.run([loss, optimizer], feed_dict={X: xBatch, Y: yBatch})
    lossHist.append(rLoss)
    
    if (i % 10) == 0:
        print("%d] loss = %.4f" % (i, rLoss))

# 향후 10 기간 데이터를 예측한다. 향후 1 기간을 예측하고, 예측값을 다시 입력하여 2 기간을 예측한다.
# 이런 방식으로 10 기간까지 예측한다.
nFuture = 10
if len(data) > 50:
    lastData = np.copy(data[-50:])  # 원 데이터의 마지막 50개만 그려본다
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
plt.figure(figsize=(8, 3))
plt.plot(ax1, lastData, 'b-o', markersize=2, color='blue', label='Time series', linewidth=1)
plt.plot(ax2, estimate, 'b-o', markersize=2, color='red', label='Estimate')
plt.axvline(x=ax1[-1],  linestyle='dashed', linewidth=1)
plt.legend()
plt.show()
