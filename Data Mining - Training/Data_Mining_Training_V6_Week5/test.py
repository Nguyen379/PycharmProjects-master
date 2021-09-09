from transformers import TFAutoModel, AutoTokenizer
import tensorflow as tf
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base", use_fast=False)
loaded_model = TFAutoModel.from_pretrained("phobert_1st_test")

np.set_printoptions(formatter={'float_kind':'{:f}'.format})
test_sent = "Tôi là sinh_viên trường đại_học Công_nghệ ."
predict_input = tokenizer.encode(test_sent, truncation=True, padding=True, return_tensors="tf")
tf_output = loaded_model.predict(predict_input)[0]
tf_prediction = tf.nn.softmax(tf_output, axis=1).numpy()[0]
print(tf_prediction)
