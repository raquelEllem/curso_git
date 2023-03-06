import pandas as pd
import numpy as np
import stramlit as st

def loas_data():
    return pd.read_csv('data/processed/bokes_completed.csv')

def main():
    df = loas_data()
    
    st.dataframe(df)

if __name__ == '__main__':
    main()