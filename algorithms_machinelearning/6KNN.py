import numpy as np 
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
iris.keys()#dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])
iris['data']#datos
iris['target_names']#parametros y caracteristicas
iris['target']# indexacion de los parametros
iris['DESCR']# descripcion de DATA SET IRIS PLANTS DATASET
iris['feature_names']#nombres de la unidad de cada de las datos
print(iris['filename'])#Direccion de donde de encuentra los archivos .csv

#separamos nuestros datos en set de entrenamiento y set de testing
X_train,X_test,y_train,y_test = train_test_split(iris['data'],iris['target'])#regresa 4 valores

from sklearn.neighbors import KNeighborsClassifier#importamos a kNN
knn = KNeighborsClassifier(n_neighbors=20)# k = 20
knn.fit(X_train,y_train)
knn.score(X_test,y_test)
print(knn.predict([[1.2,3.4,5.6,1.1]]))









