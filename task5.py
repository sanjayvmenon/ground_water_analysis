import pandas as pd
df=pd.read_csv("processed_task4.csv")

from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report


key_features = ['TDS', 'pH', 'Water Hardness Score']
X = df[key_features]
y = df['Water Quality']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)
 

#decision tree

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)

print("Decision Tree Performance:")
print(classification_report(y_test, y_pred_dt))
accuracy=accuracy_score(y_pred_dt,y_test)
print(f"accuracy:{accuracy}")
dump(dt_model, 'decision_tree_model.joblib')





# df.to_csv("Processed_task5.csv")