# Convolution, Pooling, Upsampling 과정의 Shape 설정과 세부 동작을 확인해 본다.
#
# 2018.12.10, 아마추어퀀트 (조성현)
# ---------------------------------------------------------------------------
import tensorflow as tf
import numpy as np

nBatch, nHeight, nWidth, nChannel = (1, 5, 5, 1)                    # Image data shape
nFheight, nFwidth, nFchannel, nFcount = (3, 3, nChannel, 1)         # Convolution Filter shape
nPheight, nPwidth, nPchannel, nPcount = (3, 3, nChannel, nFcount)   # Pooling shape
nUheight, nUwidth, nUchannel, nUcount = (3, 3, nChannel, nFcount)   # Upsampling shape

X = np.arange(0.1, 2.6, 0.1).reshape(nBatch, nHeight, nWidth, nChannel)
F = np.random.rand(9).reshape(nFheight, nFwidth, nFchannel, nFcount)
U = np.array(np.repeat(1,9), np.float32).reshape(nUheight, nUwidth, nUchannel, nUcount)

print("\nInput image :")
print(X.reshape(nHeight, nWidth))

print("\nConvolution filter :")
print(F.reshape(nFheight, nFwidth))

print("\nUpsampling filter :")
print(U.reshape(nUheight, nUwidth))

tf.reset_default_graph()
tX = tf.constant(X, tf.float32)
tF = tf.constant(F, tf.float32)
Cl = tf.nn.conv2d(tX, tF, strides=[1,1,1,1], padding='VALID') # Convolution layer
Pl = tf.nn.max_pool(Cl, ksize=[1, nPheight, nPwidth, 1], strides=[1,1,1,1], padding='SAME')
Ul = tf.nn.conv2d_transpose(Pl, U, output_shape=(1, nHeight, nWidth, 1), strides=[1, 1, 1, 1], padding='VALID')

sess = tf.Session()
print("\nConvolution :")
print(sess.run(Cl).reshape(nHeight-2, nWidth-2))    # padding = VALID가 적용되었음

print("\nPooling :")
print(sess.run(Pl).reshape(nFheight, nFwidth))      # padding = SAME이 적용되었음

print("\nUpSampling :")
print(sess.run(Ul).reshape(nHeight, nWidth))
