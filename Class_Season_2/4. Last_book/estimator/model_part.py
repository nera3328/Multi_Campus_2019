import tensorflow as tf
from keras.layers import Dense
from keras.losses import binary_crossentropy
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def model_fn(features, labels, mode): #얘는 기본적으로 이러한 변수를 넣어줘야 한다.!
                                #mode = train : 학습, Eval: 평가, Predict : 예측
#    TRAIN = mode == tf.estimator.ModeKeys.TRAIN---책!
    nInput = 6      # input layer의 neuron 개수
    nHidden = 12    # hidden layer의 neuron 개수
    nOutput = 1     # output layer의 neuron 개수

# hidden layer의 Weight (Wh)와 Bias (Bh)
    H1 = Dense(nHidden, activation='relu')(features['x']) #features에서 바로 넣어준다!
    predY = Dense(nOutput, activation='sigmoid')(H1)

# 학습
    if mode == tf.estimator.ModeKeys.TRAIN:
        loss = tf.reduce_mean(binary_crossentropy(labels, predY))
        optimizer = tf.train.AdamOptimizer(0.01)
        global_step= tf.train.get_global_step()
        train = optimizer.minimize(loss, global_step)
    
        return tf.estimator.EstimatorSpec(mode=mode, train_op=train, loss=loss)
# 평가
    elif mode == tf.estimator.ModeKeys.EVAL:
        loss= tf.reduce_mean(binary_crossentropy(labels, predY))
        accuracy = tf.metrics.accuracy(labels, tf.round(predY))
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops={'acc': accuracy})

#예측
    elif mode == tf.estimator.ModeKeys.PREDICT:
        yClass = tf.round(predY)
        return tf.estimator.EstimatorSpec(
        mode = mode,
        predictions = {'prob' : predY , 'class' : yClass})
        
        
#좀더 히든 더 쌓아준 복사본
def model_fn2(features, labels, mode): #얘는 기본적으로 이러한 변수를 넣어줘야 한다.!
                                #mode = train : 학습, Eval: 평가, Predict : 예측
#    TRAIN = mode == tf.estimator.ModeKeys.TRAIN---책!
    nInput = 6      # input layer의 neuron 개수
    nHidden = 12    # hidden layer의 neuron 개수
    nOutput = 1     # output layer의 neuron 개수

# hidden layer의 Weight (Wh)와 Bias (Bh)
    H1 = Dense(nHidden, activation='relu')(features['x']) #features에서 바로 넣어준다!
    H2 = Dense(nHidden, activation='relu')(H1)
    H3 = Dense(nHidden, activation='relu')(H2)
    predY = Dense(nOutput, activation='sigmoid')(H3)

# 학습
    if mode == tf.estimator.ModeKeys.TRAIN:
        loss = tf.reduce_mean(binary_crossentropy(labels, predY))
        optimizer = tf.train.AdamOptimizer(0.01)
        global_step= tf.train.get_global_step()
        train = optimizer.minimize(loss, global_step)
    
        return tf.estimator.EstimatorSpec(mode=mode, train_op=train, loss=loss)
# 평가
    elif mode == tf.estimator.ModeKeys.EVAL:
        loss= tf.reduce_mean(binary_crossentropy(labels, predY))
        accuracy = tf.metrics.accuracy(labels, tf.round(predY))
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops={'acc': accuracy})

#예측
    elif mode == tf.estimator.ModeKeys.PREDICT:
        yClass = tf.round(predY)
        return tf.estimator.EstimatorSpec(
        mode = mode,
        predictions = {'prob' : predY , 'class' : yClass})
        
        
def model_fn3(features, labels, mode): #얘는 기본적으로 이러한 변수를 넣어줘야 한다.!
                                #mode = train : 학습, Eval: 평가, Predict : 예측
#    TRAIN = mode == tf.estimator.ModeKeys.TRAIN---책!
    nInput = 6      # input layer의 neuron 개수
    nHidden = 12    # hidden layer의 neuron 개수
    nOutput = 1     # output layer의 neuron 개수

# hidden layer의 Weight (Wh)와 Bias (Bh)
    H1 = Dense(nHidden, activation='relu')(features['x']) #features에서 바로 넣어준다!
    H2 = Dense(nHidden, activation='relu')(H1)
    H3 = Dense(nHidden, activation='relu')(H2)
    H4 = Dense(nHidden, activation='relu')(H3)
    predY = Dense(nOutput, activation='sigmoid')(H4)

# 학습
    if mode == tf.estimator.ModeKeys.TRAIN:
        loss = tf.reduce_mean(binary_crossentropy(labels, predY))
        optimizer = tf.train.AdamOptimizer(0.01)
        global_step= tf.train.get_global_step()
        train = optimizer.minimize(loss, global_step)
    
        return tf.estimator.EstimatorSpec(mode=mode, train_op=train, loss=loss)
# 평가
    elif mode == tf.estimator.ModeKeys.EVAL:
        loss= tf.reduce_mean(binary_crossentropy(labels, predY))
        accuracy = tf.metrics.accuracy(labels, tf.round(predY))
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops={'acc': accuracy})

#예측
    elif mode == tf.estimator.ModeKeys.PREDICT:
        yClass = tf.round(predY)
        return tf.estimator.EstimatorSpec(
        mode = mode,
        predictions = {'prob' : predY , 'class' : yClass})
        
        
        
def model_fn4(features, labels, mode): #얘는 기본적으로 이러한 변수를 넣어줘야 한다.!
                                #mode = train : 학습, Eval: 평가, Predict : 예측
#    TRAIN = mode == tf.estimator.ModeKeys.TRAIN---책!
    nInput = 6      # input layer의 neuron 개수
    nHidden = 12    # hidden layer의 neuron 개수
    nOutput = 1     # output layer의 neuron 개수

# hidden layer의 Weight (Wh)와 Bias (Bh)
    H1 = Dense(nHidden, activation='relu')(features['x']) #features에서 바로 넣어준다!
    H2 = Dense(nHidden, activation='relu')(H1)
    H3 = Dense(nHidden, activation='relu')(H2)
    H4 = Dense(nHidden, activation='relu')(H3)
    predY = Dense(nOutput, activation='sigmoid')(H4)

# 학습
    if mode == tf.estimator.ModeKeys.TRAIN:
        loss = tf.reduce_mean(binary_crossentropy(labels, predY))
        optimizer = tf.train.AdamOptimizer(0.01)
        global_step= tf.train.get_global_step()
        train = optimizer.minimize(loss, global_step)
    
        return tf.estimator.EstimatorSpec(mode=mode, train_op=train, loss=loss)
# 평가
    elif mode == tf.estimator.ModeKeys.EVAL:
        loss= tf.reduce_mean(binary_crossentropy(labels, predY))
        accuracy = tf.metrics.accuracy(labels, tf.round(predY))
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops={'acc': accuracy})

#예측
    elif mode == tf.estimator.ModeKeys.PREDICT:
        yClass = tf.round(predY)
        return tf.estimator.EstimatorSpec(
        mode = mode,
        predictions = {'prob' : predY , 'class' : yClass})