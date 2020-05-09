import pandas as pd
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('/home/rdymonxd/Escritorio/learning_ia/data_preprocessing/algorithms_machinelearning/iris_df.csv')
#df = pd.read_csv('')
df.columns = ['X1', 'X2', 'X3', 'X4', 'Y']
df.head()
from sklearn.model_selection import train_test_split

#from sklearn.cross_validation import train_test_split
forest = RandomForestClassifier()
X = df.values[:, 0:4]
Y = df.values[:, 4]
trainX, testX, trainY, testY = train_test_split( X, Y, test_size = 0.3)
forest.fit(trainX, trainY)
print('Accuracy: \n', forest.score(testX, testY))
pred = forest.predict(testX)