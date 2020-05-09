import pandas
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

data = 'iris_df.csv'
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(data,names = names)
#dataset.plot(kind = 'box',subplots = True, layout=(2,2),sharex = False, sharey=False)
#dataset.hist()#imprime los histogramas de las variables de entrada
scatter_matrix(dataset)#diagrama de dispersion de todos los pares de atributos
plt.show()


