import pandas as pd
df = pd.read_csv("data/raw/dataset_Cheat_Detection.csv", sep=";", decimal=",")
print(df.shape)
print(df.columns.tolist())
print(df["es_trampa_max"].value_counts())

print(df.isna().sum())
print("duplicates:", df.duplicated().sum())
sub = ["isAimbot_max","isVidaInfinita_max","isMunicionInfinita_max","isSuperVelocidad_max"]
any_sub = (df[sub].sum(axis=1) > 0).astype(int)
print(pd.crosstab(df["es_trampa_max"], any_sub))

print(df.describe().T[["min", "max"]])
print(df["timestamp"].dtype)
print(df["timestamp"].head())

ts = pd.to_datetime(df["timestamp"])
print(ts.min(), ts.max())
print("unique timestamps:", ts.nunique())
print("unique days:", ts.dt.date.nunique())