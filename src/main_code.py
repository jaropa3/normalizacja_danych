import pandas as pd
import sys
from transform import data_cleaning, sortowanie
from extract import OPEN_FILE, read_input


def main():
    
    df_path = OPEN_FILE()
    df_dane = read_input(df_path)
    df_dane = data_cleaning(df_dane)
    df_dane = sortowanie(df_dane)
    print(df_dane)
    #print(df_dane)

if __name__ == "__main__":
    main()