import tensorflow as tf
from sm_data_part import train_input_fn
from sm_model_part import model_fn1, model_fn2, model_fn3
from keras.losses import mean_squared_error


#모델 1을 사용
estimator1= tf.estimator.Estimator(model_fn=model_fn1, model_dir='/DATA_OUT/checkpoint/dnn1')#model_fn으로 만든 함수 넣기

estimator1.train(train_input_fn, steps=100) #data를 함수로 묶어 넣어줌

#모델 2을 사용
estimator2= tf.estimator.Estimator(model_fn=model_fn2, model_dir='/DATA_OUT/checkpoint/dnn2')#model_fn으로 만든 함수 넣기

estimator2.train(train_input_fn, steps=100) #data를 함수로 묶어 넣어줌


#모델 3을 사용
estimator2= tf.estimator.Estimator(model_fn=model_fn3, model_dir='/DATA_OUT/checkpoint/dnn3')#model_fn으로 만든 함수 넣기

estimator2.train(train_input_fn, steps=100) #data를 함수로 묶어 넣어줌