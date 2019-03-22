import numpy as np 
from sklearn.decomposition import PCA

inputFilePath = './datapredealed/dataTrainToPca.txt'

X =np.genfromtxt(inputFilePath,delimiter='|')
X[np.isnan(X)]=0

pca = PCA(n_components=3)
y = pca.fit_transform(X)

np.savetxt('./datapredealed/dataPcaedToLm.txt',y,delimiter='|')