# src/data_preprocessing.py prototype til at fjerne duplikates og missing values

#Import the Panda framework to work with coloms and rows and in generel Excel data, and call it pd for future use 
import pandas as pd
#The path dictated as where the raw data that should be processed is comming from 
Input_Path = "Fil stien på dataen indsættes her"
#The collum who will be checked for missing values 
Taget_Collum = "Indsæt det coloum man vil se om der er missing values i"
#The path  dictaceds as where the preprocced data should end up
Output_Path = "../data/preprocessed/NAVN MANGLER HER"

# Takes the file directory and reads the CSV-file and makes it into a tabel
def load_raw_data(Input_Path: str) -> pd.DataFrame:
    #Load raw CSV data into a tabel.
    return pd.read_csv(Input_Path) 

#Return a copy with duplicate rows removed and the count removed.
def remove_duplicates(df: pd.DataFrame):
    #Reads how many rows the tabel contains before any editing is done
    before = len(df)
    #Remove the rows that are entirely the same in a copy so we dont change the original
    out = df.drop_duplicates().copy()
    #Checks how many rows have been removed, from the original to the copy
    removed = before - len(out)
    #Retunrs the new tabel and the number of removed rows 
    return out, removed

# We start by taking the tabel and making a copy so we dont change the original, 
# and define a taget variable we will look at if that is missing or not 
def handle_missing_values(df: pd.DataFrame, target_col: str) -> pd.DataFrame:
    out = df.copy()

    # Drop rows where target variable is missing
    if target_col in out.columns:
        out = out.dropna(subset=[target_col])
        print(f"Removed rows with missing values in '{target_col}' column.")
    else:
        print(f"Warning: Target column '{target_col}' not found in data!")
    #Return the cleaned model 
    return out