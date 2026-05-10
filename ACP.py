# Import pandas
import pandas as pd
import numpy as np

# Create dictionary
employees = {
    "Id": [1, 2, 3, 4],
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", np.nan, np.nan, np.nan],
    "Salary": [100, 200, np.nan, np.nan]
}

# Create DataFrame
df = pd.DataFrame(employees)

# Print original DataFrame
print("Original DataFrame:\n")
print(df)

# Print initial 2 values
print("\nFirst 2 rows:\n")
print(df.head(2))

# Print last 2 values
print("\nLast 2 rows:\n")
print(df.tail(2))

# Total number of null values
print("\nTotal null values:")
print(df.isnull().sum().sum())

# Detailed information of DataFrame
print("\nDataFrame Information:\n")
print(df.info())

# Drop rows with null values
new_df_rows = df.dropna()

print("\nDataFrame after dropping rows with null values:\n")
print(new_df_rows)

# Drop columns with null values
new_df_cols = df.dropna(axis=1)

print("\nDataFrame after dropping columns with null values:\n")
print(new_df_cols)

# Fill null values in Salary column with 300
df["Salary"] = df["Salary"].fillna(300)

print("\nDataFrame after filling Salary null values with 300:\n")
print(df)

# Fill null values in Role column with 'CEO'
df["Role"] = df["Role"].fillna("CEO")

print("\nDataFrame after filling Role null values with 'CEO':\n")
print(df)