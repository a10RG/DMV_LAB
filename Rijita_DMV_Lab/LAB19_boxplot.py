import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\LENOVO\Documents\OneDrive Folder\OneDrive\Desktop\Rijita_DMV_Lab\finance_dataset_cleaned_30x30.csv")

# Select numeric columns
numeric_cols = df.select_dtypes(include=['int64','float64'])

# Select top 5 columns with highest variance
top_columns = list(numeric_cols.var().sort_values(ascending=False).head(5).index)

print("Selected Columns:", top_columns)

# Draw boxplot
plt.figure(figsize=(8,5))
df[top_columns].boxplot()

plt.title("Boxplot for Selected Finance Features")
plt.xticks(rotation=30)
plt.tight_layout()

plt.show()