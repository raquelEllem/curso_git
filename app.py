import stramlit as st
from src import load_data

st.set_page_config(layout='wide')

def main():
    df = load_data()
    
    st.dataframe(df)

if __name__ == '__main__':
    main()


