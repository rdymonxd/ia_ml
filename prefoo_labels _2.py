from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
input_classes = ['suzuki','ford','suzuki','toyota','ford','bmw']

label_encoder.fit(input_classes)#indexa los datos convirtiendolos en numeros
labels = ['toyota','ford','suzuki']#creamos una nueva variable labels que es un lista
encoded_labels = label_encoder.transform(labels)#codifica la lista indexando los elementos correspondientes de labels 



print("\nClass mapping:")
for i, item in enumerate(label_encoder.classes_):
    print(item,'-->',i)

print("\nLabels = ", labels)
print("Encoded labels = ", list(encoded_labels))#imprimi los 
