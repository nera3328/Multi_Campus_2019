import tensorflow as tf
from data_part import train_input_fn, test_input_fn
from model_part import model_fn, model_fn2, model_fn3, model_fn4,


#모델 1을 사용
estimator= tf.estimator.Estimator(model_fn=model_fn, model_dir='/DATA_OUT/checkpoint/dnn')#model_fn으로 만든 함수 넣기

estimator.train(train_input_fn, steps=100) #data를 함수로 묶어 넣어줌

estimator.evaluate(test_input_fn, steps=1)

#모델 2를 사용
estimator2= tf.estimator.Estimator(model_fn=model_fn2, model_dir='/DATA_OUT/checkpoint/dnn2')#model_fn으로 만든 함수 넣기

estimator2.train(train_input_fn, steps=100) #data를 함수로 묶어 넣어줌

estimator2.evaluate(test_input_fn, steps=1)

#모델 3를 사용
estimator3= tf.estimator.Estimator(model_fn=model_fn3, model_dir='/DATA_OUT/checkpoint/dnn2')#model_fn으로 만든 함수 넣기

estimator3.train(train_input_fn, steps=100) #data를 함수로 묶어 넣어줌

estimator3.evaluate(test_input_fn, steps=1)



#모델 4를 사용
estimator4= tf.estimator.Estimator(model_fn=model_fn4, model_dir='/DATA_OUT/checkpoint/dnn2')#model_fn으로 만든 함수 넣기

estimator4.train(train_input_fn, steps=100) #data를 함수로 묶어 넣어줌

estimator4.evaluate(test_input_fn, steps=1)