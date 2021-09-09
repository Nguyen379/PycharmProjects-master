from sklearn.model_selection import train_test_split
from sklearn.datasets import load_files
from transformers import TFAutoModel, AutoTokenizer
from vncorenlp import VnCoreNLP
import tensorflow as tf
from tensorflow.keras.losses import SparseCategoricalCrossentropy
# Tao file
reviews = load_files(r"E:\PycharmProjects\Data Mining - Training\Data_Mining_Training_V6_Week2"
                     r"\combined_for_cross_validation", encoding="utf16")
files, categories = reviews.data, reviews.target

# Segment File cho Phobert
rdrsegmenter = VnCoreNLP(r"E:\PycharmProjects\venv\Lib\site-packages\vncorenlp\VnCoreNLP-1.1.1.jar",
                         annotators="wseg", max_heap_size='-Xmx500m')

new_files = []
for file in files:
    new_sentence = []
    new_file = rdrsegmenter.tokenize(file)
    for sentence in new_file:
        new_sentence.extend(sentence)
    new_files.append(new_sentence)

train_files, val_files, train_labels, val_labels = train_test_split(new_files, categories)

tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base", use_fast=False)

train_encodings = tokenizer(train_files, padding=True, truncation=True, return_tensors="tf")
val_encodings = tokenizer(val_files, padding=True, truncation=True, return_tensors="tf")

train_dataset = tf.data.Dataset.from_tensor_slices((
    dict(train_encodings),
    train_labels
))
val_dataset = tf.data.Dataset.from_tensor_slices((
    dict(val_encodings),
    val_labels
))

phobert = TFAutoModel.from_pretrained("vinai/phobert-base", num_labels=27)
phobert.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=5e-5),
    loss=SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy'],
)
phobert.fit(train_dataset.shuffle(100).batch(16),
            epochs=5,
            batch_size=16,
            validation_data=val_dataset.shuffle(100).batch(16))

phobert.save_pretrained("phobert_1st_test")
