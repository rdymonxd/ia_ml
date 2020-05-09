from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
input_classes = ['suzuki','ford','suzuki','toyota','ford','bmw']

label_encoder.fit(input_classes)#indexa los datos convirtiendolos en numeros
labels = ['toyota','ford','suzuki']#creamos una nueva variable labels que es un lista
encoded_labels = label_encoder.transform(labels)#codifica la lista indexando los elementos correspondientes de labels 

encoded_labels_nro = [3,2,0,2,1]
decoded_labels = label_encoder.inverse_transform(encoded_labels_nro)


print("\nClass mapping:")
for i, item in enumerate(label_encoder.classes_):#mapa de indexado
    print(item,'-->',i)

print("\nLabels = ", labels)
print("Encoded labels nro = ", list(encoded_labels))#imprimi los indices correspondientes codificados

print("\nEncoded labels = ", encoded_labels_nro)
print("Decoded labels = ", list(decoded_labels))#imprimie los indices correspondientes decodificados
