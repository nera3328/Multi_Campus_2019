# RNN 예시 : Noisy Sine 그래프를 예측해 본다.
# RNN은 many-to-many 방식으로 구성하여 과거 시계열 데이터의 패턴을 분석하여 미래 시계열을 예측한다.
#
# 2018.11.16, 아마추어퀀트 (조성현)
# --------------------------------------------------------------------------------------------
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1차원 배열의 시계열 데이터로 학습용 배치 파일을 만든다. 입력값 = 1개, 출력값 = 1개
# return : xBatch - RNN 입력
#          yBatch - RNN 출력
#
# step = 3 인 경우의 예시
# xData = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# 
# xBatch, yBatch는 3차원 텐서로 만든다. (-1, step=3, 1)
# xBatch = [[1]] [[2]] [[3]] [[4]] [[5]] [[6]] [[7]] --> 3 행 1 열 짜리가 7개 만들어진다.
#          [[2]] [[3]] [[4]] [[5]] [[6]] [[7]] [[8]]
#          [[3]] [[4]] [[5]] [[6]] [[7]] [[8]] [[9]]
#
# yBatch = [[2]] [[3]] [[4]] [[5]] [[6]] [[7]] [[8]] --> 3 행 1 열 짜리가 7개 만들어진다.
#          [[3]] [[4]] [[5]] [[6]] [[7]] [[8]] [[9]]
#          [[4]] [[5]] [[6]] [[7]] [[8]] [[9]] [[10]]
#
# 실제는 위의 데이터가 dim-0 방향으로 shffling하여 리턴한다. (학습 효율을 위해)
# ex : xBatch[0] = [[3],[4],[5]],   yBatch[0] = [[4],[5],[6]]
#      3-step 짜리 RNN에 3,4,5가 입력되면 4,5,6이 출력되도록 학습한다.
def createTrainData(xData, step):
    m = np.arange(len(xData) - step)
    np.random.shuffle(m)
    
    x, y = [], []
    for i in m:
        a = xData[i:(i+step)]
        x.append(a)
    xBatch = np.reshape(np.array(x), (len(m), step, 1))
    
    for i in m+1:
        a = xData[i:(i+step)]
        y.append(a)
    yBatch = np.reshape(np.array(y), (len(m), step, 1))
    
    return xBatch, yBatch

# 시계열 데이터 (noisy sin)
#data = np.arange(1001)     # 직선
#data = np.sin(2 * np.pi * 0.03 * np.arange(1001))   # sine 곡선
data = np.arange(1001)*0.01 + np.sin(2 * np.pi * 0.03 * np.arange(1001)) + np.random.random(1001) # trend & noisy sine
nInput = 1
nOutput = 1
nStep = 20
nNeuron = 50

# 학습 데이터를 생성한다.
xBatch, yBatch = createTrainData(data, nStep)

# RNN 그래프를 생성한다 (Wx, Wh). xBatch를 RNN에 입력한다.
tf.reset_default_graph()
x = tf.placeholder(tf.float32, [None, nStep, nInput])  
rnn = tf.keras.layers.SimpleRNNCell(nNeuron, activation=tf.nn.relu)
#rnn = tf.keras.layers.LSTMCell(nNeuron)
output, state = tf.nn.dynamic_rnn(rnn, x, dtype=tf.float32)

# RNN의 출력값을 입력으로 받아 1개의 y가 출력되도록 하는 feed-forward network를 생성한다. (Wy)
y = tf.placeholder(tf.float32, [None, nStep, nOutput])
fc1 = tf.contrib.layers.fully_connected(inputs=output, num_outputs=nNeuron)
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
for i in range(500):
    sess.run(minLoss, feed_dict={x: xBatch, y: yBatch})
    
    if i % 10 == 0:
        ploss = sess.run(loss, feed_dict={x: xBatch, y: yBatch})
        lossHist.append(ploss)
        print(i, "\tLoss:", ploss)

# 향후 20 기간 데이터를 예측한다. 향후 1 기간을 예측하고, 예측값을 다시 입력하여 2 기간을 예측한다.
# 이런 방식으로 20 기간까지 예측한다.
nFuture = 20
if len(data) > 100:
    lastData = np.copy(data[-100:])  # 원 데이터의 마지막 50개만 그려본다
else:
    lastData = np.copy(data)
dx = np.copy(lastData)
estimate = [dx[-1]]
for i in range(nFuture):
    # 마지막 nStep 만큼 입력데이로 다음 값을 예측한다
    px = dx[-nStep:]
    px = np.reshape(px, (1, nStep, 1))
    
    # 다음 값을 예측한다.
    yHat = sess.run(predY, feed_dict={x: px})[0][-1][0]
    
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
plt.plot(ax1, lastData, 'b-o', color='blue', markersize=3, label='Time series', linewidth=1)
plt.plot(ax2, estimate, 'b-o', color='red', markersize=3, label='Estimate')
plt.axvline(x=ax1[-1],  linestyle='dashed', linewidth=1)
plt.legend()
plt.show()


