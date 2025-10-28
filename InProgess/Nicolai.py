# src/data_preprocessing.py prototype til at fjerne duplikates og missing values

#Import the Panda framework to work with coloms and rows and in generel Excel data

import pandas as pd

# Takes the file directory and reads the CSV-file and makes it into a tabel
def load_raw_data(path: str) -> pd.DataFrame:
    #Load raw CSV data into a tabel.
    return pd.read_csv(path) 

#Return a copy with duplicate rows removed and the count removed.
def remove_duplicates(df: pd.DataFrame) -> Tuple[pd.DataFrame, int]:
    #Reads how many rows the tabel contains before any editing is done
    before = len(df)
    #Remove the rows that are entirely the same in a copy so we dont change the original
    out = df.drop_duplicates().copy()
    #Checks how many rows have been removed, from the original to the copy
    removed = before - len(out)
    #Retunrs the new tabel and the number of removed rows 
    return out, removed

# We start by taking the tabel and making a copy so we dont change the original
def handle_missing_values(df: pd.DataFrame, target_col: str = "loan_status") -> pd.DataFrame:
    out = df.copy()

    # Drop rows where target variable is missing
    if target_col in out.columns:
        out = out.dropna(subset=[target_col])
    #Return the cleaned model 
    return out