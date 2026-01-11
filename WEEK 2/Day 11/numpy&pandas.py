print("Step 1: Import Libraries and Load Dataset")
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

df = pd.read_csv(
    "/Users/fathimamanaf/Documents/MAchine Learning/WEEK 2/Day 11/titanic.csv"
)
df.info()
df.head()

print("Step 2: Check for Duplicate Rows")
df.duplicated()

print("Step 3: Identify Column Data Types")
cat_col = [col for col in df.columns if df[col].dtype == 'object']
num_col = [col for col in df.columns if df[col].dtype != 'object']

print('Categorical columns:', cat_col)
print('Numerical columns:', num_col)

print("Step 4: Count Unique Values in the Categorical Columns")
df[cat_col].nunique()

print("Step 5: Calculate Missing Values as Percentage")
round((df.isnull().sum() / df.shape[0]) * 100, 2)

print("Step 6: Drop Irrelevant or Data-Heavy Missing Columns")
df1 = df.drop(columns=['Name', 'Ticket', 'Cabin'])
df1.dropna(subset=['Embarked'], inplace=True)
df1['Age'].fillna(df1['Age'].mean(), inplace=True)


print("Step 7: Detect Outliers with Box Plot")
plt.boxplot(df1['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Box Plot')
plt.show()

print("Step 8: Calculate Outlier Boundaries and Remove Them")
mean = df1['Age'].mean()
std = df1['Age'].std()

lower_bound = mean - 2 * std
upper_bound = mean + 2 * std

df2 = df1[(df1['Age'] >= lower_bound) & (df1['Age'] <= upper_bound)]

print("Step 9: Impute Missing Data Again if Any")
df3 = df2.fillna(df2['Age'].mean())
df3.isnull().sum()

print("Step 10: Recalculate Outlier Bounds and Remove Outliers from the Updated Data")
mean = df3['Age'].mean()
std = df3['Age'].std()

lower_bound = mean - 2 * std
upper_bound = mean + 2 * std

print('Lower Bound :', lower_bound)
print('Upper Bound :', upper_bound)

df4 = df3[(df3['Age'] >= lower_bound) & (df3['Age'] <= upper_bound)]

print("Step 11: Data validation and verification")
X = df3[['Pclass','Sex','Age', 'SibSp','Parch','Fare','Embarked']]
Y = df3['Survived']

print("Step 12: Data formatting")
scaler = MinMaxScaler(feature_range=(0, 1))

num_col_ = [col for col in X.columns if X[col].dtype != 'object']
x1 = X
x1[num_col_] = scaler.fit_transform(x1[num_col_])
x1.head()