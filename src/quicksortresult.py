import numpy as np
inputFile = './datapredealed/dataResult.txt'

datas = np.genfromtxt(inputFile,delimiter='|',dtype = [('A', float), ('B', float), ('C', float),
('D', float), ('E', float), ('F', float),('G', float), ('H', float), ('I', float)])

datas = np.sort(datas,order='A')

np.savetxt('./datapredealed/resultSorted.txt',datas,delimiter='|')
