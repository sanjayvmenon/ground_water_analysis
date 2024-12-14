import pandas as pd
df=pd.read_csv("GroundWaterQuality.csv")

# 1.1 analyzing data
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)

# 1.2 converting the data type
columns_to_check = ['pH', 'CO3', 'SO4', 'NO3', 'PO4', 'SiO2', 'U(ppb)', 'F']
for col in columns_to_check:
    print(f"Unique values in {col}: {df[col].unique()}")

for col in columns_to_check:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 1.3 removing unnecessary columns
df=df.drop(columns=['Year'])
print(df.info())
df.to_csv('processed_task1_data.csv', index=False)









