import tensorflow as tf
from data_part import train_input_fn, test_input_fn, x_pred
from model_part import model_fn, model_fn2, model_fn3, model_fn4


#모델 1로 예측
estimator= tf.estimator.Estimator(model_fn = model_fn, model_dir='/DATA_OUT/checkpoint/dnn')# 별도의 파일임으로 train_part에서 정의되었어도 선언 필요
pred_input_fn = tf.estimator.inputs.numpy_input_fn({'x' : x_pred}, shuffle=False)

for y in estimator.predict(pred_input_fn):
    print('prob = ', y['prob'][0])
    print('class = ', y['class'][0])
    
    

#모델 2로 예측
estimator2= tf.estimator.Estimator(model_fn = model_fn2, model_dir='/DATA_OUT/checkpoint/dnn')# 별도의 파일임으로 train_part에서 정의되었어도 선언 필요
pred_input_fn = tf.estimator.inputs.numpy_input_fn({'x' : x_pred}, shuffle=False)

for y in estimator2.predict(pred_input_fn):
    print('prob = ', y['prob'][0])
    print('class = ', y['class'][0])
    
    
#모델 3로 예측
estimator3= tf.estimator.Estimator(model_fn = model_fn3, model_dir='/DATA_OUT/checkpoint/dnn')# 별도의 파일임으로 train_part에서 정의되었어도 선언 필요
pred_input_fn = tf.estimator.inputs.numpy_input_fn({'x' : x_pred}, shuffle=False)

for y in estimator3.predict(pred_input_fn):
    print('prob = ', y['prob'][0])
    print('class = ', y['class'][0])
    
    
    
#모델 4로 예측
estimator4= tf.estimator.Estimator(model_fn = model_fn4, model_dir='/DATA_OUT/checkpoint/dnn')# 별도의 파일임으로 train_part에서 정의되었어도 선언 필요
pred_input_fn = tf.estimator.inputs.numpy_input_fn({'x' : x_pred}, shuffle=False)

for y in estimator4.predict(pred_input_fn):
    print('prob = ', y['prob'][0])
    print('class = ', y['class'][0])