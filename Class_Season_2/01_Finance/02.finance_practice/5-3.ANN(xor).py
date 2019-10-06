# XOR 예시
import tensorflow as tf

inputX = [[0, 0], [0, 1], [1, 0], [1, 1]]   # input 데이터
outputY = [[1], [0], [1], [0]]              # desired output 데이터

nInput = 2      # input layer의 neuron 개수
nHidden = 4     # hidden layer의 neuron 개수
nOutput = 1     # output layer의 neuron 개수

# 그래프를 생성한다
tf.reset_default_graph()
x = tf.placeholder(tf.float32, shape=[None, nInput], name='x')
y = tf.placeholder(tf.float32, shape=[None, nOutput], name='y')

# hidden layer의 Weight (Wh)와 Bias (Bh)
Wh = tf.Variable(tf.truncated_normal([nInput, nHidden]), dtype=tf.float32, name='Wh')
Bh = tf.Variable(tf.zeros(nHidden), dtype=tf.float32, name='Bh')

# output layer의 Weight (Wo)와 Bias (Bo)
Wo = tf.Variable(tf.truncated_normal([nHidden, nOutput]), dtype=tf.float32, name='Wo')
Bo = tf.Variable(tf.zeros(nOutput), dtype=tf.float32, name='Bo')

# Hidden layer의 출력값. activation function은 sigmoid
H1 = tf.sigmoid(tf.matmul(x, Wh) + Bh, name='H1')

# Output layer의 출력값. activation function은 sigmoid
predY = tf.sigmoid(tf.matmul(H1, Wo) + Bo, name='predY')

# Cost function 정의. cross-entropy 사용
clipY = tf.clip_by_value(predY, 0.000001, 0.99999)  # log(0)를 방지한다
cost = -tf.reduce_mean(y * tf.log(clipY) + (1-y) * tf.log(1-clipY))

# 학습
optimizer = tf.train.AdamOptimizer(0.05)
train = optimizer.minimize(cost)

# 그래프를 실행한다
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 인공신경망에 inputX, outputY를 1000번 집어 넣어서 학습 시킨다.
for i in range(1000):
    sess.run(train, feed_dict={x: inputX, y: outputY})

# 학습이 완료되면, Wh, Bh, Wo, Bo 이 모두 업데이트 되었으면, inputX를 넣어서 출력값을 확인한다.
# 출력값은 inputY의 추정값이다.
yHat = sess.run(predY, feed_dict={x: inputX})

print("\ny-추정치 = \n", yHat)

# Weight, Bias의 최종값을 확인해 본다
rWh, rBh, rWo, rBo = sess.run([Wh, Bh, Wo, Bo])

print("\nWh = \n", rWh)
print("\nBh = \n", rBh)
print("\nWo = \n", rWo)
print("\nBo = \n", rBo)
sess.close()
