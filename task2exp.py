import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("processed_task1_data.csv")
# 2.1 checking null values
# print(df.info())
# print(df.isnull().sum())
numeric_columns = ['LATITUDE', 'LONGITUDE', 'pH', 'EC','CO3', 'HCO3', 'Cl', 'SO4','NO3','PO4', 'TH', 'Ca', 'Mg', 'Na', 'K', 'F', 'SiO2', 'TDS', 'U(ppb)']
for col in numeric_columns:
    df[col]=df[col].fillna(df[col].mean())
categorical_columns = ['Well ID', 'S.No', 'STATE', 'DISTRICT', 'BLOCK', 'LOCATION']
for col in categorical_columns:
    df[col]=df[col].fillna(df[col].mode()[0])
# print(df.isnull().sum())

# 2.2 outlier detection
for col in numeric_columns:
    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    iqr=q3-q1
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_limit) | (df[col] > upper_limit)]
    outlier_num = outliers[col].count()
    print(f"Column: {col}")
    print(f"Q1: {q1}")
    print(f"Q3: {q3}")
    print(f"IQR: {iqr}")
    print(f"Lower limit: {lower_limit}")
    print(f"Upper limit: {upper_limit}")
    print(f"Number of outliers in {col}: {outlier_num}")
    print(outliers[col].sum)
    print("-" * 30)



df = df[(df[col] >= lower_limit) & (df[col] <= upper_limit)]

# Printing the DataFrame after outlier removal
print("DataFrame after removing outliers:")
print(df)


# 2.3

from sklearn.preprocessing import MinMaxScaler

# Create a MinMaxScaler object
scaler = MinMaxScaler()

# Select numeric columns to normalize
  # Replace with your numeric columns

# Fit and transform the data
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

print("Data normalized.")
print(df)


df.to_csv("processedexp_task2.csv",index=False)
















