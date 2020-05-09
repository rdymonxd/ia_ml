#Starring imnplementation
import pandas as pd 
import matplotlib.pyplot as plt  
import numpy as np  
import seaborn as sns

from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

from sklearn import tree

df = pd.read_csv('/home/rdymonxd/Escritorio/learning_ia/data_preprocessing/algorithms_machinelearning/iris_df.csv')


df.columns = ["X1","X2","X3","X4","Y"]
df.head()
#implementation

from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split
decision = tree.DecisionTreeClassifier(criterion="gini")
X = df.values[:,0:4] 
Y = df.values[:,4]
trainX,testX,trainY,testY = train_test_split(X,Y,test_size = 0.3)
decision.fit(trainX,trainY)
print("Accuracy; \n", decision.score(testX,testY))

#Visulisation
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus as pydot 
dot_data = StringIO()
tree.export_graphviz(decision,out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())
