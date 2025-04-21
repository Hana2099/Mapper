import pandas as pd
import os

def load_zeek_log(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, sep='\t', comment='#', header=0, low_memory=False)
    return df

# Example usage
if __name__ == "__main__":
    df = load_zeek_log("data/http.log")
    print(df.head())
