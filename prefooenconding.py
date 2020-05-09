import numpy as np 
from sklearn import preprocessing
#WE IMPORTATED A COUPLE OF PACKAGES. LET'S CREATE SOME SAMPLE DATA AND ADD THE LINE TO THIS FILE:
encoder  = preprocessing.OneHotEncoder()
encoder.fit([
    [0,2,1,12],
    [1,3,5,3],
    [2,3,2,12],
    [1,2,4,3]
])
enconded_vector = encoder.transform([[2,3,5,3]]).toarray()
print("\n Encoded vector = ",enconded_vector)