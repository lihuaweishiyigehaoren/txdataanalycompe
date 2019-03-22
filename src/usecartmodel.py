from sklearn.externals import joblib
import numpy as np
clf = joblib.load('./tmp/tree.pkl')

inputTestPath = './datapredealed/dataTestPcaedToLm.txt'
dataResults = np.genfromtxt(inputTestPath,delimiter='|')

thisvalue = clf.predict(dataResults)

np.savetxt('./datapredealed/finalresult.txt',thisvalue,delimiter='|')
