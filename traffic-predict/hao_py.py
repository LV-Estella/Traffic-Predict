# -*- coding: utf-8 -*-
"""hao.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11-a9yuORf3-aDQCyhDgRYNiajnV5SFYo
"""

import pandas as pd

#Clone git data file
# !git clone https://github.com/PCHao1/traffic-predict.git
# !git fetch

#Using Path library to define base-path
from pathlib import Path
data_dir = Path('c:/tmp/Traffic/demo_traffic_jam_prediction')

#import csv data file as a DataFrame panda type
with open(data_dir/'rawData.csv','rb') as f:
  df = pd.read_csv(f,  
            header=0, 
            names=[ 'ev','lb'])

#print 10 first rows
print(df.head(10))

#Print 10 last rows
print(df.tail(10))

#import csv dict file as a DataFrame panda type
with open(data_dir/'dict.csv','rb') as f:
  event_dict = pd.read_csv(f, 
            header=0, 
            names=[ 'stt','event'])

#Print event_dict
print(event_dict)

import numpy as np
from tensorflow.keras.utils import to_categorical

from keras.preprocessing.sequence import pad_sequences
# fixed size of all vector of vector's list



#[Function]Transfer raw list(string type) to new formatted list(list type)
def format_event_list(event_list):
  list_idxs = [0]*len(event_dict)
  for x in range(0,len(event_dict)):
    if str(event_list).find(event_dict.event[x])!=-1:
      list_idxs[x]=1
  return list_idxs

format_data = df.ev.apply(format_event_list).tolist()
# Apply format_event_list to all single data row to a list
format_data[0]

data = pad_sequences(format_data, maxlen=len(event_dict))
labels = np.array(df.lb)
# Transfer data, label to numpy array

#Random shuffle data
np.random.seed(13)
#Create new shuffle array index
indices = np.arange(data.shape[0])
np.random.shuffle(indices)

#apply above random index to our data
data = data[indices]
labels = labels[indices]

#Slice dataset to 2 component
training_samples = int(len(indices) * .8)
validation_samples = len(indices) - training_samples
X_train = data[:training_samples]
y_train = labels[:training_samples]
X_valid = data[training_samples: training_samples + validation_samples]
y_valid = labels[training_samples: training_samples + validation_samples]

print(X_train)

num_events = len(event_dict)
embedding_dim = 20
# Create num_events*20 matrix
embedding_matrix = np.random.rand(num_events, embedding_dim)

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
clf = MultinomialNB()
# training 
clf.fit(X_train, y_train)
test= clf.predict(X_valid)
# test
print(accuracy_score(y_valid, test))
# from keras.models import Sequential
# from keras.layers import Embedding, Flatten, Dense, LSTM

# units = 32

# model = Sequential()
# model.add(Embedding(num_events, embedding_dim))
# model.add(LSTM(units))
# model.add(Dense(1, activation='sigmoid'))
# # hàm dense 1 chỉ có 1 output là 0 hoặc 1 
# # thuật toán LSTM dựa trên cái 1 2 3 để suy ra có tắc đường hay k
# # 1 mô hình RNN lớp 1 là embed lớp 2 là LSTM lớp 3 là hàm dense với hàm kích hoạt là sigmoid

# model.layers[0].set_weights([embedding_matrix])
# # Khởi tạo trọng số
# model.layers[0].trainable = False
# # Không train

# #Setup the model
# model.compile(optimizer='rmsprop',
#               loss='binary_crossentropy',
#               metrics=['acc'])
# #Tranning
# history = model.fit(X_train, y_train,
#                     epochs=10,
#                     batch_size=1024,
#                     validation_data=(X_valid, y_valid))
# #Save model
# model.save(data_dir /"model1.h5")

# #Draw chart
# import matplotlib.pyplot as plt

# acc = history.history['acc']
# val_acc = history.history['val_acc']
# loss = history.history['loss']
# val_loss = history.history['val_loss']

# epochs = range(1, len(acc) + 1)

# plt.plot(epochs, acc, 'bo', label='Training acc')
# plt.plot(epochs, val_acc, 'b', label='Validation acc')
# plt.title('Training and validation accuracy')
# plt.legend()

# plt.figure()

# plt.plot(epochs, loss, 'bo', label='Training loss')
# plt.plot(epochs, val_loss, 'b', label='Validation loss')
# plt.title('Training and validation loss')
# plt.legend()

# plt.show()

# from keras.models import Sequential
# from keras.layers import Embedding, Flatten, Dense, LSTM

# units = 32
# #Over fitting model

# model = Sequential()
# model.add(Embedding(num_events, embedding_dim))
# model.add(LSTM(units))
# model.add(Dense(1, activation='sigmoid'))

# model.layers[0].set_weights([embedding_matrix])
# model.layers[0].trainable = True

# model.compile(optimizer='rmsprop',
#               loss='binary_crossentropy',
#               metrics=['acc'])
# history = model.fit(data, labels,
#                     epochs=10,
#                     batch_size=1024,
#                     validation_data=(X_valid, y_valid))
# model.save(data_dir/"model2.h5")

# import matplotlib.pyplot as plt

# acc = history.history['acc']
# val_acc = history.history['val_acc']
# loss = history.history['loss']
# val_loss = history.history['val_loss']

# epochs = range(1, len(acc) + 1)

# plt.plot(epochs, acc, 'bo', label='Training acc')
# plt.plot(epochs, val_acc, 'b', label='Validation acc')
# plt.title('Training and validation accuracy')
# plt.legend()

# plt.figure()

# plt.plot(epochs, loss, 'bo', label='Training loss')
# plt.plot(epochs, val_loss, 'b', label='Validation loss')
# plt.title('Training and validation loss')
# plt.legend()

# plt.show()

# from keras.models import Sequential
# from keras.layers import Embedding, Flatten, Dense, LSTM

# units = 32

# model = Sequential()
# model.add(Embedding(num_events, embedding_dim))
# model.add(LSTM(units, dropout=0.2, recurrent_dropout=0.2))
# # dropout solve over fitting 
# model.add(Dense(1, activation='sigmoid'))

# model.layers[0].set_weights([embedding_matrix])
# model.layers[0].trainable = True

# model.compile(optimizer='rmsprop',
#               loss='binary_crossentropy',
#               metrics=['acc'])
# history = model.fit(data, labels,
#                     epochs=10,
#                     batch_size=1024,
#                     validation_data=(X_valid, y_valid))
# model.save(data_dir/"model3.h5")

# import matplotlib.pyplot as plt

# acc = history.history['acc']
# val_acc = history.history['val_acc']
# loss = history.history['loss']
# val_loss = history.history['val_loss']

# epochs = range(1, len(acc) + 1)

# plt.plot(epochs, acc, 'bo', label='Training acc')
# plt.plot(epochs, val_acc, 'b', label='Validation acc')
# plt.title('Training and validation accuracy')
# plt.legend()

# plt.figure()

# plt.plot(epochs, loss, 'bo', label='Training loss')
# plt.plot(epochs, val_loss, 'b', label='Validation loss')
# plt.title('Training and validation loss')
# plt.legend()

# plt.show()

