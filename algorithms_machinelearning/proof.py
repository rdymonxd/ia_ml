import csv
import codecs


filename = '/home/rdymonxd/Escritorio/learning_ia/data_preprocessing/algorithms_machinelearning/BankNote_Authentication.csv'

file = open(filename,"rb")
read = csv.reader(codecs.iterdecode(file,'utf-8'))
dataset = list(read)

#f = float(dataset)

#lines = reader(file)
print(dataset[0])





