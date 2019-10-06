import tensorflow as tf
from sm_data_part import x_pred, y_pred
from sm_model_part import model_fn1, model_fn2, model_fn3

# 모델-1로 예측
estimator = tf.estimator.Estimator(model_fn = model_fn1, model_dir='./data_out/checkpoint/dnn1')
pred_input_fn = tf.estimator.inputs.numpy_input_fn({'x':x_pred}, shuffle=False)

for y in estimator.predict(pred_input_fn):
    print("predicted 1= ", y['prob'][0])

print("price sequence = ", x_pred)


# 모델-2로 예측
estimator = tf.estimator.Estimator(model_fn = model_fn2, model_dir='./data_out/checkpoint/dnn2')
pred_input_fn = tf.estimator.inputs.numpy_input_fn({'x':x_pred}, shuffle=False)


for y in estimator.predict(pred_input_fn):
    print("predicted = ", y['prob'][0])

print("price sequence = ", x_pred)

# 모델-3로 예측
estimator = tf.estimator.Estimator(model_fn = model_fn3, model_dir='./data_out/checkpoint/dnn3')
pred_input_fn = tf.estimator.inputs.numpy_input_fn({'x':x_pred}, shuffle=False)


for y in estimator.predict(pred_input_fn):
    print("predicted = ", y['prob'][0])

print("price sequence = ", x_pred)
print("actual value = ", y_pred)
