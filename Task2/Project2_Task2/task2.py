import pandas as pd

# Load dataset
df = pd.read_csv("employees_data.csv")

print("ORIGINAL DATASET")
print(df.head())

# -----------------------------------
# CHECK MISSING VALUES
# -----------------------------------
print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# -----------------------------------
# HANDLE NUMERIC MISSING VALUES
# -----------------------------------
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# -----------------------------------
# HANDLE TEXT MISSING VALUES
# -----------------------------------
text_columns = df.select_dtypes(include=['object', 'string']).columns

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# -----------------------------------
# REMOVE DUPLICATES
# -----------------------------------
duplicates = df.duplicated().sum()

print("\nNUMBER OF DUPLICATES:", duplicates)

df = df.drop_duplicates()

# -----------------------------------
# FORMAT COLUMN NAMES
# -----------------------------------
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# -----------------------------------
# FINAL CLEANED DATASET
# -----------------------------------
print("\nCLEANED DATASET")
print(df.head())

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_employee_data.csv", index=False)

print("\nDATA CLEANING COMPLETED SUCCESSFULLY")

