import numpy as np
from matplotlib.dates import strpdate2num, num2date
from datetime import datetime

inputBehaviorFilePath = './dataselect/testreadbehavior.txt'
inputResultFilePath = './dataselect/testreadresult.txt'
# inputBehaviorFilePath = './dataselect/behaviorwater_20190226-20190307.txt'
# inputResultFilePath = './dataselect/resultwater_20190226-20190307.txt'

# testFilePath = './dataselect/testnames.txt'
# transNamesFilePath = './dataselect/transnames.txt'

# ,converters={0: str2date}
str2date = lambda x: datetime.strptime(x.decode("utf-8"), '%Y-%m-%d %H:%M:%S')
dataBehavior = np.genfromtxt(inputBehaviorFilePath,delimiter='|',dtype=['i8','int','int','object','object',
'int','int','int','int','int','int','int','int','int','int',
'int','int','int','int','int','int','int','int','int','int',
'int','int','int','int','int','int','int','int','float','object',
'int','int'])
# dataResult = np.genfromtxt(inputResultFilePath,delimiter='|',dtype=['i8','int','i8','int','object',
# 'int','int','int','int','int','int','int','int','int','int'])
# dataTrans = np.loadtxt(transNamesFilePath,delimiter='|')
# dataTest = np.loadtxt(testFilePath,delimiter='|')

print(dataBehavior)