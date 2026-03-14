import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

# Show first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# -------------------------------
# Graph 1: Sales Distribution
# -------------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["Total Amount"], bins=20, color="blue")
plt.title("Sales Distribution")
plt.xlabel("Total Amount")
plt.ylabel("Frequency")
plt.show()

# -------------------------------
# Graph 2: Product Category Count
# -------------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="Product Category", data=df)
plt.title("Product Category Distribution")
plt.xlabel("Product Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# Graph 3: Age vs Purchase Amount
# -------------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(x="Age", y="Total Amount", data=df)
plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Total Amount")
plt.show()

print("\nEDA Analysis Completed Successfully!")