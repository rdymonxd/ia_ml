import numpy as np 
from sklearn import preprocessing
#WE IMPORTATED A COUPLE OF PACKAGES. LET'S CREATE SOME SAMPLE DATA AND ADD THE LINE TO THIS FILE:
input_data = np.array([[3,-1.5,3,-6.4],[0,3,-1.3,4.1],[1,2.3,-2.9,-4.3]])
data_standardized = preprocessing.scale(input_data)
print("\nMEAN = ",data_standardized.mean(axis = 0))
print("Std deviation = " , data_standardized.std(axis = 0))
