import numpy as np 

# inputResultPath = './datapredealed/dataResult.txt'

inputResultPath = './datapredealed/dataResult.txt'
dataTest = './data/traintest.txt'

dataResults = np.genfromtxt(inputResultPath,delimiter='|')

dataTests = np.loadtxt(dataTest,delimiter='|')

result = []
# result = np.array(result)
for datatest in dataTests:
    item = []
    count = 0
    # item = np.array(item)
    for dataresult in dataResults:
        if dataresult[0] == datatest[0]:
            item.append(dataresult)
            count = count+1
            if count > 3:
                break

    if item != []:
        item = np.mean(item,axis=0)
        item = item.tolist()
        item.append(datatest[2])
        result.append(item)

result = np.array(result)

np.savetxt('./datapredealed/result.txt',result,delimiter='|')

