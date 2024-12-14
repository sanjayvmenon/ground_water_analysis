import pandas as pd
df=pd.read_csv("processedexp_task2.csv")
import matplotlib.pyplot as plt
import seaborn as sns

# Parameters to visualize
parameters = ['pH', 'TDS', 'NO3']
# Plot all histograms in a grid
plt.figure(figsize=(12, 6))  # Adjust size for fewer parameters
for i, col in enumerate(parameters, 1):  # Start index at 1 for subplot
    plt.subplot(1, len(parameters), i)  # 1 row, as many columns as parameters
    sns.histplot(df[col], kde=True, bins=20, color='blue', alpha=0.7)
    plt.title(f"{col} Distribution")
    plt.xlabel(col)
    plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 3.2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame
# Select numeric columns for correlation analysis
numeric_columns = ['pH', 'TDS', 'NO3', 'EC', 'Cl', 'SO4', 'TH', 'Ca', 'Mg', 'Na', 'K']  # Replace with your actual numeric columns
df_numeric = df[numeric_columns]  # Filter numeric columns

# 1. Generate the Correlation Matrix
correlation_matrix = df_numeric.corr()

# Display the Correlation Matrix
print("Correlation Matrix:")
print(correlation_matrix)

# 2. Visualize the Correlation Matrix with a Heatmap
plt.figure(figsize=(12, 8))  # Set the figure size
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# 3. Identify Strong Correlations
# Threshold for strong correlation
threshold = 0.7

# Find strong correlations (absolute value > threshold)
strong_corr = correlation_matrix[(correlation_matrix > threshold) | (correlation_matrix < -threshold)]

# Display strong correlations
print("Strong Correlations (absolute value > 0.7):")
print(strong_corr)

# Optional: Pairplot for Visualizing Relationships
sns.pairplot(df_numeric)
plt.suptitle("Pairplot of Numeric Columns", y=1.02)  # Add a title
plt.show()
