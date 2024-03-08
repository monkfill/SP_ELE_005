import streamlit as st 
import pandas as pd 

paths =  ["V40_PLE-TR-G12-HLD.csv","V41_PLE-TR-G12-HLD.csv","V43_PLE-TR-G12-HLD.csv","V44_PLE-TR-G12-HLD.csv","V46_PLE-TR-G12-HLD.csv"]

all_df =  pd.DataFrame()

for path in paths:
    df  =  pd.read_csv(path)

    all_df = pd.concat( [ all_df,df])

st.write(all_df)

