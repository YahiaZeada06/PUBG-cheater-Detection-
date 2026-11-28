import pandas as pd

RAW_D1 = "data/raw/dataset_Cheat_Detection.csv"
OUT = "data/interim/d1_labeled.csv"

LABELS = [
    "es_trampa_max", "isAimbot_max", "isVidaInfinita_max",
    "isMunicionInfinita_max", "isSuperVelocidad_max",
]


def main():
    df = pd.read_csv(RAW_D1, sep=";", decimal=",")

   
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

    
    df[LABELS] = df[LABELS].astype(int)

    
    df["source_id"] = "D1"

    
    features = [c for c in df.columns if c not in LABELS + ["timestamp", "source_id"]]
    assert df[features].apply(lambda s: s.between(0, 1).all()).all()

    df.to_csv(OUT, index=False)
    print("wrote", OUT, df.shape)
    print(df["source_id"].value_counts())
    print(df[LABELS].sum())


if __name__ == "__main__":
    main()