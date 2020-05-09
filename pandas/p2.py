import pandas
import matplotlib.pyplot as plt
data = 'iris_df.csv'
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(data,names = names)
dataset.plot(kind = 'box',subplots = True, layout=(2,2),sharex = False, sharey=False)
dataset.hist()#imprime los histogramas de las variables de entrada
plt.show()
