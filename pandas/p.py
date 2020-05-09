import pandas
data = 'pima_indians.csv'
names = ['Pregnacies','Glucose','BloodPressure','SkinThickness','Insulin','Outcome']
dataset = pandas.read_csv(data,names = names)
#print(dataset.shape)#IMPRIMI EL NRO DE FILAS Y COLUMNAS
#print(dataset.head(20))# IMPRIMI LOS 20 PRIMEROS VALORES
#print(dataset.describe())# IMPRIMIE UN RESUMEN ESTADISTICo
print(dataset.groupby('Outcome').size())# ver el nro de elementos que "select * from name_table group by (name_campo)"