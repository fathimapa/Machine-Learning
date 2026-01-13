print("1. Absolute Maximum Scaling")
import pandas as pd
import numpy as np

df = pd.read_csv(
    "/Users/fathimamanaf/Documents/MAchine Learning/WEEK 2/Day 13/SampleFile.csv"
)

df = df.select_dtypes(include=np.number)
df.head()

max_abs = np.max(np.abs(df), axis=0)

scaled_df = df / max_abs

scaled_df.head()

print("Min-Max Scaling")

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

scaled_df.head()

print(" Normalization (Vector Normalization)")

from sklearn.preprocessing import Normalizer

scaler = Normalizer()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

scaled_df.head()

print("Standardization")
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data,
                         columns=df.columns)
print(scaled_df.head())

print("Robust Scaling")


from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data,
                         columns=df.columns)
print(scaled_df.head())