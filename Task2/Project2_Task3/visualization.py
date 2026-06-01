# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("employees_data.csv")

# Show Dataset
print(df.head())

# Set Style
sns.set(style="whitegrid")

# -----------------------------------
# 1. Department-wise Employee Count
# -----------------------------------
plt.figure(figsize=(8,5))
sns.countplot(x='Department', data=df)

plt.title("Department-wise Employee Count")
plt.xticks(rotation=45)

plt.show()

# -----------------------------------
# 2. Gender Distribution
# -----------------------------------
plt.figure(figsize=(6,6))

df['Gender'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Gender Distribution")
plt.ylabel("")

plt.show()

# -----------------------------------
# 3. Salary Distribution
# -----------------------------------
plt.figure(figsize=(8,5))

sns.histplot(df['Salary'], bins=10, kde=True)

plt.title("Salary Distribution")
plt.xlabel("Salary")

plt.show()

# -----------------------------------
# 4. Experience vs Salary
# -----------------------------------
plt.figure(figsize=(8,5))

sns.scatterplot(
    x='Experience_Years',
    y='Salary',
    data=df
)

plt.title("Experience vs Salary")

plt.show()

# -----------------------------------
# 5. Average Salary by Department
# -----------------------------------
plt.figure(figsize=(8,5))

avg_salary = df.groupby('Department')['Salary'].mean()

avg_salary.plot(kind='bar')

plt.title("Average Salary by Department")
plt.ylabel("Average Salary")

plt.xticks(rotation=45)

plt.show()