import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("C:\\Users\\LENOVO\\Downloads\\finance_dataset_30x30.xlsx")
print("\nMissing Values:\n")
print(df.isnull().sum())
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col] = df[col].fillna(df[col].mean())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())
Q1 = df['Revenue'].quantile(0.25)
Q3 = df['Revenue'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['Revenue'] < lower) | (df['Revenue'] > upper)]
print("\nRevenue Outliers:\n")
print(outliers)
top_profit = df.sort_values(by='NetProfit', ascending=False).head(10)
#bar chart
plt.bar(top_profit['ID'], top_profit['NetProfit'])
plt.title("Top Companies by Net Profit")
plt.xlabel("Company ID")
plt.ylabel("Net Profit")
plt.show()
#histogram
df['Revenue'].plot(kind='hist', bins=10)
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()
#line chart
df_sorted = df.sort_values(by='ID')
plt.plot(df_sorted['ID'], df_sorted['StockPrice'])
plt.title("Stock Price Trend")
plt.xlabel("Company ID")
plt.ylabel("Stock Price")
plt.show()
#scatter plot
plt.scatter(df['Revenue'], df['NetProfit'])
plt.title("Revenue vs Net Profit")
plt.xlabel("Revenue")
plt.ylabel("Net Profit")
plt.show()
#pie chart
top_marketcap = df.sort_values(by='MarketCap', ascending=False).head(5)
plt.pie(top_marketcap['MarketCap'], labels=top_marketcap['ID'], autopct='%1.1f%%')
plt.title("Top 5 Companies by Market Capitalization")
plt.show()
