import pandas as pd

# Load dataset
df = pd.read_csv("employees_data.csv")

# First 5 rows
print(df.head())

# Shape
print("\nDataset Shape:")
print(df.shape)

# Columns
print("\nColumns:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Dataset info
print("\nDataset Info:")
print(df.info())

# Statistics
print("\nStatistical Summary:")
print(df.describe())