import streamlit as st 
import pandas as pd 
import plotly.express as px 


paths =  ["V38_PLE-TR-G12-HLD","V41_PLE-TR-G12-HLD.csv","V43_PLE-TR-G12-HLD.csv","V44_PLE-TR-G12-HLD.csv","V46_PLE-TR-G12-HLD.csv"]

all_df =  pd.DataFrame()

for path in paths:
    df  =  pd.read_csv(path)
    all_df = pd.concat( [ all_df,df])

st.write(all_df)

version_counts = all_df['Version'].value_counts()

date_counts  =  all_df["Date"].value_counts()

st.write( version_counts)
st.write( date_counts)


st.write(all_df.size/8)

fig =  px.pie(version_counts, values= "count")

st.plotly_chart(fig, use_container_width= False)


fig1 =  px.line(date_counts)
st.plotly_chart(fig1, use_container_width= False)

