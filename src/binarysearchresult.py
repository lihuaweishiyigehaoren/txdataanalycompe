import numpy as np 
from func import binary_chop

inputFile = './datapredealed/resultSorted.txt'

dataTest = './data/transnames.txt'

dataResults = np.genfromtxt(inputFile,delimiter='|')
dataTests = np.loadtxt(dataTest,delimiter='|')

result = []
lookrange = dataResults[:,0]

for datatest in dataTests:

    item = []
    dataSec = binary_chop(lookrange,datatest[0])
    if dataSec != []:
        for index in range(dataSec[0],dataSec[1]+1):
            item.append(dataResults[index])

    if item != []:
        item = np.mean(item,axis=0)
        item = item.tolist()
        item.append(datatest[2])
        result.append(item)

result = np.array(result)

np.savetxt('./datapredealed/resultSelected.txt',result,delimiter='|')
