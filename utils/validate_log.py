import pandas as pd

REQUIRED_COLUMNS = ["ts", "method", "host", "uri"]

def validate_log_file(filepath: str):
    print(f"📂 Checking log file: {filepath}")

    try:
        df = pd.read_csv(filepath, sep="\t", comment="#", low_memory=False)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    print(f"✅ Loaded {len(df)} rows with {len(df.columns)} columns")
    
    # Check for required columns
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        print(f"❌ Missing required columns: {missing}")
        return

    # Check for nulls
    null_report = df[REQUIRED_COLUMNS].isnull().sum()
    if null_report.any():
        print("⚠️  Null values found:")
        print(null_report[null_report > 0])
    else:
        print("✅ No null values in required columns")

    # Show a preview
    print("\n🔍 Sample data:")
    print(df[REQUIRED_COLUMNS].head(3))

    print("\n🚦 Log validation complete.\n")
    return df
