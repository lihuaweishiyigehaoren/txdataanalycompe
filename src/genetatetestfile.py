import numpy as np 

inputTrainResultPath = './datapredealed/resultTestSelected.txt'
inputTrainBehaivorPath = './datapredealed/behaivorTestSelected.txt'

dataTrainResult = np.genfromtxt(inputTrainResultPath,delimiter='|')
dataTrainBehaivor = np.genfromtxt(inputTrainBehaivorPath,delimiter='|')

dataTrain = np.hstack((dataTrainResult,dataTrainBehaivor))

dataTrain = np.delete(dataTrain,[0,1,9,10,12,14],axis=1)

np.savetxt('./datapredealed/dataTestToPca.txt',dataTrain,delimiter='|')