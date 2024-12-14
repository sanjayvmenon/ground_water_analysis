import pandas as pd
df=pd.read_csv("processedexp_task2.csv")
# print(df.shape)
# print(df.isnull().sum())
# Creating a new feature for Water Hardness Score
df['Water Hardness Score'] = 2.5 * df['Ca'] + 4.1 * df['Mg']
# print(df.shape)


# Function to classify water quality
def classify_water_quality(row):
    # Normalized thresholds for TDS, pH, and Water Hardness Score
    tds_safe = 0.3
    tds_moderate = 0.6

    ph_safe_low = 0.464
    ph_safe_high = 0.607
    ph_moderate_low = 0.393
    ph_moderate_high = 0.679

    hardness_safe = 0.2
    hardness_moderate = 0.4

    if (
        row['TDS'] <= tds_safe
        and ph_safe_low <= row['pH'] <= ph_safe_high
        and row['Water Hardness Score'] <= hardness_safe
    ):
        return 'Safe'
    elif (
        (tds_safe < row['TDS'] <= tds_moderate)
        or (ph_moderate_low <= row['pH'] < ph_safe_low)
        or (ph_safe_high < row['pH'] <= ph_moderate_high)
        or (hardness_safe < row['Water Hardness Score'] <= hardness_moderate)
    ):
        return 'Moderate'
    else:
        return 'Unsafe'

# Creating the new feature
df['Water Quality'] = df.apply(classify_water_quality, axis=1)

# Displaying the new feature
print("Water Quality Classification:")
print(df[['TDS', 'pH', 'Water Hardness Score', 'Water Quality']].head())




# Apply one-hot encoding to the 'STATE' column
df = pd.get_dummies(df, columns=['STATE'], prefix=['STATE'])

# Check the new column names generated after encoding
print("New columns after one-hot encoding:")
print(df.columns)

# View the first few rows of the DataFrame
print(df.head())







df.to_csv("processed_task4.csv")