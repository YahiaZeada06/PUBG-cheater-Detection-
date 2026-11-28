import pandas as pd

df = pd.read_csv("data/raw/dataset_Cheat_Detection.csv", sep=";", decimal=",")
LABELS = ["es_trampa_max", "isAimbot_max", "isVidaInfinita_max",
          "isMunicionInfinita_max", "isSuperVelocidad_max"]

def test_shape():
    assert df.shape == (3584, 18)

def test_no_missing_values():
    assert df.isna().sum().sum() == 0

def test_no_duplicate_rows():
    assert df.duplicated().sum() == 0

def test_labels_are_binary():
    for col in LABELS:
        assert set(df[col].unique()) <= {0, 1}

def test_general_label_consistent():
    sub = ["isAimbot_max", "isVidaInfinita_max",
           "isMunicionInfinita_max", "isSuperVelocidad_max"]
    any_sub = (df[sub].sum(axis=1) > 0).astype(int)
    assert (df["es_trampa_max"] == any_sub).all()

def test_features_are_normalized():
    features = [c for c in df.columns if c != "timestamp"]
    for col in features:
        assert df[col].between(0, 1).all()