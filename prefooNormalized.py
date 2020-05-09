import numpy as np 
from sklearn import preprocessing
#WE IMPORTATED A COUPLE OF PACKAGES. LET'S CREATE SOME SAMPLE DATA AND ADD THE LINE TO THIS FILE:
input_data = np.array([[3,-1.5,3,-6.4],[0,3,-1.3,4.1],[1,2.3,-2.9,-4.3]])
data_normalized = preprocessing.normalize(input_data, norm = 'l1')
print("\n L1 normalized data = ", data_normalized)