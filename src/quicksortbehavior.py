import numpy as np
inputFile = './datapredealed/dataBehaivor.txt'

datas = np.genfromtxt(inputFile,delimiter='|')

datas = np.genfromtxt(inputFile,delimiter='|',dtype = [('A', float), ('B', float), ('C', float),('A2', float), ('B2', float), ('C2', float),
('D', float), ('E', float), ('F', float),('G', float), ('H', float), ('I', float), ('J', float),('K', float), ('L', float), ('M', float),
('D1', float), ('E1', float), ('F1', float),('G1', float), ('H1', float), ('I1', float), ('J1', float),('K1', float), ('L1', float), ('M1', float)])

datas = np.sort(datas,order='A')

np.savetxt('./datapredealed/behaivorSorted.txt',datas,delimiter='|')
