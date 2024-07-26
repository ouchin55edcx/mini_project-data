# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Part 1: Reading and Analyzing Data
print("# --- Reading data from CSV file --- #")

df = pd.read_csv('dataset-sell4all.csv', on_bad_lines='skip')  


print("# --- Displaying 5 rows --- #")
print(df.head())

print("# --- Displaying a technical summary  --- #")
print(df.info())

print("# --- Converting columns to  data types --- #")
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Dépenses des clients'] = pd.to_numeric(df['Dépenses des clients'], errors='coerce')

print("# --- Re-displaying the technical summary after conversion --- #")
print(df.info())

print("# --- Calculating the mean and median  --- #")
mean_age = df['Age'].mean()
median_age = df['Age'].median()
mean_spending = df['Dépenses des clients'].mean()
median_spending = df['Dépenses des clients'].median()

print(f'Mean Age: {mean_age}, Median Age: {median_age}')
print(f'Mean Spending: {mean_spending}, Median Spending: {median_spending}')

# Part 2: Data Visualization and Cleaning
print("# --- Creating a bar chart  --- #")
df.groupby('Pays')['Dépenses des clients'].sum().plot(kind='bar')
plt.title('Customer Spending by Country')
plt.xlabel('Country')
plt.ylabel('Customer Spending')
plt.show()

print("# --- Cleaning data: Removing rows with less than €10 spending --- #")
df = df[df['Dépenses des clients'] >= 10]

print("# --- Cleaning data: Removing duplicate rows --- #")
df = df.drop_duplicates()

print("# --- Writing cleaned data to a new CSV file --- #")
df_cleaned = df[['Pays', 'Age', 'Genre', 'Dépenses des clients']]
df_cleaned.to_csv('cleaned_dataset.csv', index=False)
print("Cleaned data written to 'cleaned_dataset.csv'")
