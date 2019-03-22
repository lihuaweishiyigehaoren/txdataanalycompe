import numpy as np 

inputTrainPath = './datapredealed/dataPcaedToLm.txt'
inputLabelTrainPath = './datapredealed/resultSelected.txt'

pca =np.genfromtxt(inputTrainPath,delimiter='|')
label =np.genfromtxt(inputLabelTrainPath,delimiter='|')

label = label[:,9:10]

dataTrain = np.hstack((pca,label))

np.savetxt('./datapredealed/finalDataToLm.txt',dataTrain,delimiter='|')
