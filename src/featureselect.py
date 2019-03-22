import numpy as np
import matplotlib.pyplot as plt
from func import caluMaxNumber, calAverValue

inputFilePath = './data/behaviorwater_20190226-20190307.txt'
inputBeFilePath = './data/resultwater_20190226-20190307.txt'
inputTestFilePath = './data/transnames.txt'

datas = np.genfromtxt(inputFilePath,delimiter='|',dtype=['i8','int','int','object','object',
'int','int','int','int','int','int','int','int','int','int',
'int','int','int','int','int','int','int','int','int','int',
'int','int','int','int','int','int','int','int','float','object','int','int'])

dataResults = np.genfromtxt(inputBeFilePath,delimiter='|')

dataTests = np.loadtxt(inputTestFilePath,delimiter='|');

# 英雄id特征-提取众数不明显，且散度计算比较复杂
# heroidoverratio = []
# for datatest in dataTests:
#     count = 0
#     heroid = []
#     for dataresult in dataResults:
#         if dataresult[0] == datatest[0] and dataresult[1] == datatest[1]:
#             count += 1
#             heroid.append(dataresult[5])

    # print(caluMaxNumber(heroid)/len(heroid))


# 评分均值计算
# avers = []
# for datatest in dataTests:
#     grades = []
#     for dataresult in datas:# 改成行为
#         if dataresult[0] == datatest[0] and dataresult[1] == datatest[1]:
#             grades.append(dataresult[8])

#     avers.append(calAverValue(grades))

# plt.bar(range(0,10),avers)

# plt.show()
dataResults = np.array(dataResults)
dataResults = np.delete(dataResults,[2,3,4,5,12,13],axis=1)

np.savetxt('./datapredealed/dataResult.txt',dataResults,delimiter='|')
