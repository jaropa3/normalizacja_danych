import pandas as pd
from config import FILE_PATH
from pathlib import Path

def OPEN_FILE():
    return Path(FILE_PATH)

def read_input(file_path):
    df = pd.read_csv(file_path)
    return df