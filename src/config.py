from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

RAW_FILES = [
    "2019-Oct.csv",
    "2019-Nov.csv",
]

PROCESSED_EVENTS = DATA_PROCESSED / "events_clean.parquet"