print("Step 1: Import Libraries and Load Dataset")

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    "/Users/fathimamanaf/Documents/MAchine Learning/WEEK 2/Day 12/diabetes.csv"
)
print(df.head())

print("Step 2: Inspect Data Structure and Check Missing Values")

df.info()
print(df.isnull().sum())

print("Step 3: Statistical Summary and Visualizing Outliers")
df.describe()

fig, axs = plt.subplots(len(df.columns), 1, figsize=(7, 18), dpi=95)
for i, col in enumerate(df.columns):
    axs[i].boxplot(df[col], vert=False)
    axs[i].set_ylabel(col)
plt.tight_layout()
plt.show()

print("Step 4: Remove Outliers Using the Interquartile Range (IQR) Method")
q1, q3 = np.percentile(df['Insulin'], [25, 75])
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
clean_df = df[(df['Insulin'] >= lower) & (df['Insulin'] <= upper)]

print("Step 5: Correlation Analysis")
corr = df.corr()
plt.figure(dpi=130)
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.show()

print(corr['Outcome'].sort_values(ascending=False))

print("Step 6: Visualize Target Variable Distribution")
plt.pie(df['Outcome'].value_counts(), labels=[
        'Diabetes', 'Not Diabetes'], autopct='%.f%%', shadow=True)
plt.title('Outcome Proportionality')
plt.show()

print("Step 7: Separate Features and Target Variable")
X = df.drop(columns=['Outcome'])
y = df['Outcome']

print("Step 8: Feature Scaling: Normalization and Standardization")
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
print(X_normalized[:5])

scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)
print(X_standardized[:5])