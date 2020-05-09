import pandas as pd
from sklearn import decomposition
df = pd.read_csv('/home/rdymonxd/Escritorio/learning_ia/data_preprocessing/algorithms_machinelearning/iris_df.csv')
#df = pd.read_csv('iris_df.csv')
df.columns = ['X1', 'X2', 'X3', 'X4', 'Y']
df.head()
from sklearn import decomposition
from sklearn.model_selection import train_test_split
pca = decomposition.PCA()
fa = decomposition.FactorAnalysis()
X = df.values[:, 0:4]
Y = df.values[:, 4]
train, test = train_test_split(X,test_size = 0.3)
train_reduced = pca.fit_transform(train)
test_reduced = pca.transform(test)
print(pca.n_components_)