# from sklearn.externals import joblib
# clf = joblib.load('./tmp/net.model')

# print(clf.predict([[1,1.3,0.5]]))
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import numpy as np
def create_model():
    net = Sequential()
    net.add(Dense(10, input_dim = 3,)) 
    net.add(Activation('relu')) 
    net.add(Dense(10))
    net.add(Activation('relu'))
    net.add(Dense(1))
    net.add(Activation('sigmoid'))

    return net

# def train():
#    model = create_model()
#    sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
#    model.compile(loss='binary_crossentropy', optimizer=sgd)

#    checkpointer = ModelCheckpoint(filepath="/tmp/weights.hdf5", verbose=1, save_best_only=True)
#    model.fit(X_train, y_train, nb_epoch=20, batch_size=16, show_accuracy=True, validation_split=0.2, verbose=2, callbacks=[checkpointer])

def load_trained_model(value):
   model = create_model()
   model.load_weights('./tmp/net.model')
   actualValue = model.predict_classes(value)
   return actualValue

# clf = joblib.load('./tmp/net.model')

# print(clf.predict([[1,1.3,0.5]]))

inputTestPath = './datapredealed/dataTestPcaedToLm.txt'
dataResults = np.genfromtxt(inputTestPath,delimiter='|')
thisvalue = load_trained_model(dataResults)
#print(thisvalue)

np.savetxt('./datapredealed/finalresult.txt',thisvalue,delimiter='|')
