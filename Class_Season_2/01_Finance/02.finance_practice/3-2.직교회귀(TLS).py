# TensorFlow를 이용하여 직선회귀를 연습한다.
# 직선회귀 방법 : Total Least Square (직교 회귀 : Orthogonal Distance)
# ------------------------------------------------------------------
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# 샘플 데이터 1,000개를 생성한다
# y = ax + b + e
def createData(a, b, n):
   resultX = []
   resultY = []
   for i in range(n):
       x = np.random.normal(0.0, 0.5)
       y = a * x + b + np.random.normal(0.0, 0.05)
       resultX.append(x)
       resultY.append(y)
       
   return resultX, resultY

# inputY = 0.1 * inputX + 0.3 + 잔차
inputX, inputY = createData(0.1, 0.3, 1000)

# predY = W * inputX + b
tf.reset_default_graph()
r = tf.random_uniform([1], -1.0, 1.0)
W = tf.Variable(r, name = "W")
b = tf.Variable(tf.zeros([1]), name = "Bias")
x = tf.placeholder(tf.float32, name = "X")
y = tf.placeholder(tf.float32, name = "Y")

# 점 (x, y)와 회귀직선 사이의 수직 거리
bunja = tf.abs(tf.subtract(tf.add(tf.multiply(W, x), b), y))  # 분자
bunmo = tf.sqrt(tf.add(tf.square(W), tf.constant(1.0)))       # 분모

# Loss function을 정의한다. (MSE : Mean Square Error)
loss = tf.reduce_mean(tf.square(tf.divide(bunja, bunmo)))

# Loss function만 바꾸어주면 tls든 ols든 별로 다르지 X, 계산 결과도 소수점차이


# 학습할 optimizer를 정의한다
optimizer = tf.train.AdamOptimizer(0.05)
train = optimizer.minimize(loss)

# 세션을 오픈하고 그래프를 실행한다.
sess = tf.Session()
sess.run(tf.global_variables_initializer())

trLoss = []
for i in range(100):
    _, resultLoss = sess.run([train, loss], feed_dict={x: inputX, y: inputY})
    trLoss.append(resultLoss)
    
    if i % 10 == 0:
        print("%d) %f" % (i, resultLoss))

sW = sess.run(W)
sb = sess.run(b)
sess.close()

# 결과를 확인한다
print("\n*회귀직선의 방정식 (TLS) : y = %.4f * x +  %.4f" % (sW, sb))
y = sW * inputX + sb

fig = plt.figure(figsize=(10, 4))
p1 = fig.add_subplot(1,2,1)
p2 = fig.add_subplot(1,2,2)

p1.plot(inputX, inputY, 'ro', markersize=1.5)
p1.plot(inputX, y)

p2.plot(trLoss, color='red', linewidth=1)
p2.set_title("Loss function")
p2.set_xlabel("epoch")
p2.set_ylabel("loss")
plt.show()

