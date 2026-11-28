import pandas as pd

FILES = {
    "d2": "data/raw/PUBG_Player_Statistics.csv",
    "d3": "data/raw/train_V2.csv",
}

for name, path in FILES.items():
    df = pd.read_csv(path, nrows=1000)
    print("=" * 20, name, path)
    print("columns:", df.columns.tolist())
    print("dtypes:")
    print(df.dtypes)
    print("sample:")
    print(df.head(3))