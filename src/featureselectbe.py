import numpy as np
import matplotlib.pyplot as plt
from func import caluMaxNumber, calAverValue

inputFilePath = './data/behaviorwater_20190226-20190307.txt'

datas = np.genfromtxt(inputFilePath,delimiter='|')



datas = np.array(datas)
datas = np.delete(datas,[2,3,4,5,7,8,14,29,30,32,34],axis=1)


np.savetxt('./datapredealed/dataBehaivor.txt',datas,delimiter='|')
