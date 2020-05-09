import seaborn as sns
import pandas as pd 
from sklearn.cluster import KMeans
df = pd.read_csv('/home/rdymonxd/Escritorio/learning_ia/data_preprocessing/algorithms_machinelearning/iris_df.csv')


df.columns = ['X1', 'X2', 'X3', 'X4', 'Y']
df = df.drop(['X4', 'X3'], 1)
df.head()
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split
kmeans = KMeans(n_clusters = 3)
X = df.values[:, 0:2]
kmeans.fit(X)
df['Pred'] = kmeans.predict(X)
df.head()
sns.set_context('notebook', font_scale = 1.1)
sns.set_style('ticks')
sns.lmplot('X1','X2', scatter = True, fit_reg = False, data = df, hue = 'Pred')

