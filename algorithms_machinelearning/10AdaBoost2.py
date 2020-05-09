from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
dtree = DecisionTreeClassifier(criterion='gini', max_depth=1)
adabst_fit = AdaBoostClassifier(base_estimator=dtree,n_estimators = 5000, learning_rate = 0.05,random_state=42)
adabst_fit.fit(x_train,y_train)
print("\nAdaBoost - Train Confusion Matrix\n\n", pd.crosstab(y_train,adabst_fit.predict(x_train),rownames= ["Actual"],colnames=["Predicted"]))

