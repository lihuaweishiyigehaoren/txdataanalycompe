import numpy as np 
from random import shuffle

inputTrainPath = './datapredealed/finalDataToLm.txt'

data =np.genfromtxt(inputTrainPath,delimiter='|')

shuffle(data)

p = 0.8
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

import numpy
from keras.models import Sequential
from keras.layers.core import Dense, Activation

netfile = './tmp/net.model'

net = Sequential()
net.add(Dense(10, input_dim = 3,)) 
net.add(Activation('relu')) 
net.add(Dense(10))
net.add(Activation('relu'))
net.add(Dense(1))
net.add(Activation('sigmoid'))
# net.compile(optimizer='adam',loss='binary_crossentropy')
net.compile(optimizer='adam',loss = 'binary_crossentropy')

net.fit(train[:,:3], train[:,3], epochs=10, batch_size=1) 
net.save_weights(netfile)

predict_result = net.predict_classes(train[:,:3]).reshape(len(train))


from cm_plot import * 
cm_plot(train[:,3], predict_result).show()
