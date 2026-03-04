import duckdb
from pathlib import Path

DB_PATH = Path("data/processed/productpulse.duckdb")

def run_sql_file(con, path: str):
    with open(path, "r") as f:
        con.execute(f.read())

def run():
    con = duckdb.connect(str(DB_PATH))

    run_sql_file(con, "sql/01_create_tables.sql")
    run_sql_file(con, "sql/02_metrics.sql")

    # create user feature table
    run_sql_file(con, "sql/04_user_features.sql")

    # export reports
    con.execute("COPY funnel_daily TO 'reports/funnel_daily.csv' (HEADER, DELIMITER ',');")
    con.execute("COPY retention_weekly TO 'reports/retention_weekly.csv' (HEADER, DELIMITER ',');")
    con.execute("COPY user_features TO 'reports/user_features.csv' (HEADER, DELIMITER ',');")

    print("Saved reports:")
    print("reports/funnel_daily.csv")
    print("reports/retention_weekly.csv")
    print("reports/user_features.csv")

    con.close()

if __name__ == "__main__":
    run()
