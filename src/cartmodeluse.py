
import numpy as np 
from random import shuffle

inputTrainPath = './datapredealed/finalDataToLm.txt'

data =np.genfromtxt(inputTrainPath,delimiter='|')

shuffle(data)

p = 0.8
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

from sklearn.tree import DecisionTreeClassifier

treefile = './tmp/tree.pkl'
tree = DecisionTreeClassifier()
tree.fit(train[:,:3],train[:,3])

from sklearn.externals import joblib
joblib.dump(tree,treefile)

from cm_plot import * 
cm_plot(train[:,3],tree.predict(train[:,:3])).show()