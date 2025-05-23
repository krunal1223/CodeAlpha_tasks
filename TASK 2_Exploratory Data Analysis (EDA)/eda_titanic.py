# Step 1: Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the dataset
df = pd.read_csv("titanic.csv")

# Step 3: View first few rows
print("First 5 rows:")
print(df.head())

# Step 4: Basic Info
print("\nDataset Info:")
print(df.info())

# Step 5: Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Step 6: Summary Statistics
print("\nStatistics:")
print(df.describe())

# Step 7: Visualizations
# 1. Count of Survived passengers
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

# 2. Survival count by gender
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title("Survival by Gender")
plt.show()

# 3. Age distribution
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title("Age Distribution")
plt.show()
