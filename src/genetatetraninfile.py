import numpy as np 

inputTrainResultPath = './datapredealed/resultSelected.txt'
inputTrainBehaivorPath = './datapredealed/behaivorSelected.txt'

dataTrainResult = np.genfromtxt(inputTrainResultPath,delimiter='|')
dataTrainBehaivor = np.genfromtxt(inputTrainBehaivorPath,delimiter='|')

dataTrain = np.hstack((dataTrainResult,dataTrainBehaivor))

print(dataTrain.shape)
dataTrain = np.delete(dataTrain,[0,1,9,10,11,13,15,36],axis=1)

np.savetxt('./datapredealed/dataTrainToPca.txt',dataTrain,delimiter='|')
