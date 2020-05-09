import pandas as pd 
from sklearn import svm

df = pd.read_csv('/home/rdymonxd/Escritorio/learning_ia/data_preprocessing/algorithms_machinelearning/iris_df.csv')
df.column = ['X4','X3','X1','X2','Y']
df = df.drop(['X4','X3'],1)
df.head()
from sklearn.cross_validation import train_test_split
support = svm.SVC()
X = df.values[:,0:2]
Y = df.values[:,2]
trainX,testX,trainY,testY = train_test_split(X,Y,test_size=0.3)
sns.set_context('notebook',font_scale=1.1)
sns.set_style('ticks')
sns.lmplot('X1','X2',scatter=True,fit_reg=False,data=df,hue='Y')
plt.ylabel('X2')
plt.xlabel('X1')

