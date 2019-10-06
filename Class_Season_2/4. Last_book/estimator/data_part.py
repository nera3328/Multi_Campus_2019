import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('credit_data.csv')

x_data = np.array(df.iloc[:497, 0:6], dtype=np.float32)
y_data = np.array(df.iloc[:497, 6], dtype=np.float32).reshape(-1, 1)
x_pred = np.array(df.iloc[497:, 0:6], dtype=np.float32)
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.1)

def train_input_fn():
    dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))\
            .repeat()\
            .batch(12)\
            .make_one_shot_iterator()\
            .get_next()
    return {'x': dataset[0]}, dataset[1] #x는 dictionary로, y값은 label로 보내겠다


def test_input_fn():
    dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))\
            .repeat()\
            .batch(x_test.shape[0])\
            .make_one_shot_iterator()\
            .get_next()
    return {'x': dataset[0]}, dataset[1] #x는 dictionary로, y값은 label로 보내겠다