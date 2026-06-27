import pandas as pd
import os
from datetime import datetime

DATA_PATH = "../data/"
REPORTS_PATH = "../reports/"

def load_data():
    print("Loading data...")
    df = pd.read_csv(DATA_PATH + "cleaned_data.csv")
    print("Loaded", len(df), "rows")
    return df

def clean_data(df):
    print("Cleaning data...")
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    print("Data cleaned!")
    return df

def calculate_kpis(df):
    print("Calculating KPIs...")
    kpis = {
        "total_records": len(df),
        "report_date": datetime.now().strftime("%Y-%m-%d")
    }
    print("KPIs done:", kpis)
    return kpis

def export_results(kpis):
    print("Saving results...")
    os.makedirs(REPORTS_PATH, exist_ok=True)
    pd.DataFrame([kpis]).to_csv(
        REPORTS_PATH + "kpi_report.csv", index=False
    )
    print("Saved successfully!")

def run_pipeline():
    print("Pipeline Started!")
    df = load_data()
    df = clean_data(df)
    kpis = calculate_kpis(df)
    export_results(kpis)
    print("Pipeline Completed!")

if __name__ == "__main__":
    run_pipeline()