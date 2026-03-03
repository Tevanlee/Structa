import pandas as pd

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w\s]", "", regex=True)
        .str.replace(r"\s+", "_", regex=True)
    )
    return df

def clean_email_column(df: pd.DataFrame) -> pd.DataFrame:
    if "email" in df.columns:
        df["email"] = df["email"].str.strip().str.lower()
    return df

def normalize_tabular(df: pd.DataFrame) -> pd.DataFrame:
    normalize_columns(df)
    clean_email_column(df)
    return df