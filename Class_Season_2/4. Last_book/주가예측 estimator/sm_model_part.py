import tensorflow as tf
from keras.layers import Dense,LSTM, Bidirectional, Conv1D
from keras.losses import binary_crossentropy, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def model_fn1(features, labels, mode):

    nhidden = 60
    noutput = 1
    
    # hidden layer의 Weight (Wh)와 Bias (Bh)
    H1 = LSTM(nhidden, activation='relu')(features['x']) #features에서 바로 넣어준다!
    predY = Dense(noutput, activation='sigmoid')(H1)

# 학습
    if mode == tf.estimator.ModeKeys.TRAIN:
        loss = tf.reduce_mean(mean_squared_error(labels, predY))
        optimizer = tf.train.AdamOptimizer(0.01)
        global_step= tf.train.get_global_step()
        train = optimizer.minimize(loss, global_step)
    
        return tf.estimator.EstimatorSpec(mode=mode, train_op=train, loss=loss)

#예측
    elif mode == tf.estimator.ModeKeys.PREDICT:
        yClass = tf.round(predY)
        return tf.estimator.EstimatorSpec(
        mode = mode,
        predictions = {'prob' : predY , 'class' : yClass})
        
        

def model_fn2(features, labels, mode):

    nhidden = 60
    noutput = 1
    
    # hidden layer의 Weight (Wh)와 Bias (Bh)
    H1 = Bidirectional(LSTM(nhidden, activation='relu'))(features['x']) #features에서 바로 넣어준다!
    predY = Dense(noutput, activation='sigmoid')(H1)

# 학습
    if mode == tf.estimator.ModeKeys.TRAIN:
        loss = tf.reduce_mean(mean_squared_error(labels, predY))
        optimizer = tf.train.AdamOptimizer(0.01)
        global_step= tf.train.get_global_step()
        train = optimizer.minimize(loss, global_step)
    
        return tf.estimator.EstimatorSpec(mode=mode, train_op=train, loss=loss)

#예측
    elif mode == tf.estimator.ModeKeys.PREDICT:
        yClass = tf.round(predY)
        return tf.estimator.EstimatorSpec(
        mode = mode,
        predictions = {'prob' : predY , 'class' : yClass})
        
        
def model_fn3(features, labels, mode):

    nhidden = 60
    noutput = 1
    
    # hidden layer의 Weight (Wh)와 Bias (Bh)
    H1 = Conv1D(12, 3, strides=1, activation='relu')(features['x']) #features에서 바로 넣어준다!
    predY = Dense(noutput, activation='sigmoid')(H1)

# 학습
    if mode == tf.estimator.ModeKeys.TRAIN:
        loss = tf.reduce_mean(mean_squared_error(labels, predY))
        optimizer = tf.train.AdamOptimizer(0.01)
        global_step= tf.train.get_global_step()
        train = optimizer.minimize(loss, global_step)
    
        return tf.estimator.EstimatorSpec(mode=mode, train_op=train, loss=loss)

#예측
    elif mode == tf.estimator.ModeKeys.PREDICT:
        yClass = tf.round(predY)
        return tf.estimator.EstimatorSpec(
        mode = mode,
        predictions = {'prob' : predY , 'class' : yClass})