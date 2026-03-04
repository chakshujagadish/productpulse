import pandas as pd
from datetime import timezone
from src.config import DATA_RAW, DATA_PROCESSED, RAW_FILES, PROCESSED_EVENTS

def load_raw():
    dfs = []
    for f in RAW_FILES:
        path = DATA_RAW / f
        df = pd.read_csv(path)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def clean_events(df: pd.DataFrame) -> pd.DataFrame:
    # Parse time
    df["event_time"] = pd.to_datetime(df["event_time"], utc=True, errors="coerce")
    df = df.dropna(subset=["event_time", "user_id", "event_type"])

    # Basic typing / cleaning
    df["user_id"] = df["user_id"].astype("int64")
    df["event_type"] = df["event_type"].astype("string")

    # Some rows may have missing price for views; keep them
    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Derive helpful columns
    df["event_date"] = df["event_time"].dt.date
    df["event_week"] = df["event_time"].dt.to_period("W").astype(str)

    # Standardize session 
    if "user_session" in df.columns:
        df["session_id"] = df["user_session"].astype("string")
    else:
        df["session_id"] = pd.NA

    keep_cols = [c for c in [
        "event_time", "event_date", "event_week",
        "event_type", "product_id", "category_id",
        "category_code", "brand", "price",
        "user_id", "session_id"
    ] if c in df.columns]

    return df[keep_cols].copy()

def run():
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    raw = load_raw()
    clean = clean_events(raw)
    clean.to_parquet(PROCESSED_EVENTS, index=False)
    print(f"Saved: {PROCESSED_EVENTS} | rows={len(clean):,}")

if __name__ == "__main__":
    run()