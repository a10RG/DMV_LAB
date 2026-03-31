import pandas as pd
import numpy as np

# Dataset with missing values
data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [20, None, 22, None, 25],
    'City': ['Kolkata', 'Delhi', None, 'Mumbai', None],
    'Salary': [30000, 40000, None, 50000, None]
}

df = pd.DataFrame(data)

# Display original dataset
print("Original Dataset:")
print(df)

# Handling missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)        # Fill Age with mean
df['Salary'].fillna(df['Salary'].mean(), inplace=True)  # Fill Salary with mean
df['City'].fillna('Unknown', inplace=True)              # Fill City with 'Unknown'

# Display dataset after handling missing values
print("\nDataset After Handling Missing Values:")
print(df)
