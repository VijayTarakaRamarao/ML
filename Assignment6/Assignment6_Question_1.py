# Q1 Six points with the following attributes are given, calculate and find out clustering
# representations and dendrogram using Single,
# complete, and average link proximity function in hierarchical clustering technique.
# Mathematical Part Solution is provided in Document, the below code is just for reference for Q1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from scipy.spatial.distance import squareform, pdist
from matplotlib.pyplot import show


a = np.array([0.4005,0.2148,0.3457,0.2652,0.0789,0.4548])
b = np.array([0.5306,0.3854,0.3156,0.1875,0.4139,0.3022])

point = ['P1','P2','P3','P4','P5','P6']
data = pd.DataFrame({'Point':point, 'x cordinate':a, 'y cordinate':b})
data = data.set_index('Point')
print(data)

dist = pd.DataFrame(squareform(np.round(pdist(data[['x cordinate', 'y cordinate']]),4), 'euclidean'), columns=data.index.values, index=data.index.values)
print(dist)


print("\n")
plt.figure(figsize=(10,4))
plt.title("Dendrogram with Single inkage")
dend = shc.dendrogram(shc.linkage(data[['x cordinate', 'y cordinate']], method='single'), labels=data.index)
show()

plt.figure(figsize=(10,4))
plt.title("Dendrogram with Complete inkage")
dend = shc.dendrogram(shc.linkage(data[['x cordinate', 'y cordinate']], method='complete'), labels=data.index)
show()

plt.figure(figsize=(10,4))
plt.title("Dendrogram with Average inkage")
dend = shc.dendrogram(shc.linkage(data[['x cordinate', 'y cordinate']], method='average'), labels=data.index)
show()
