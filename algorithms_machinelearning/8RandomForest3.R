install.packages("randomForest")
library(caret)
library(randomForest)

banknote <- read.csv("BankNote_Authentication.csv")
banknote$class <- factor(banknote$class)

