import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px 
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu
from urllib.request import urlopen

import os

st.set_page_config(
    page_title="Project_Details_ELE0005",
    # page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)



# with st.sidebar:
#     selected = option_menu(
#     menu_title = "Main Menu",
#     options = ["Holod Depot"],
#     # options = ["Homee","Warehouse","Query Optimization and Processing","Storage","Contact Us"],
#     # icons = ["house","gear","activity","snowflake","envelope"],
#     # menu_icon = "cast",
#     # default_index = 0,
#     #orientation = "horizontal",
# )




# with st.sidebar:
#     selected = option_menu('SimiLo', ["Intro", 'Search','About'], 
#         icons=['play-btn','search','info-circle'],menu_icon='intersect', default_index=0)
#     lottie = load_lottiefile("similo3.json")
#     st_lottie(lottie,key='loc')



# # Define the folder path where your CSV files are located
# folder_path = "SP_ELE_005/dataset/Holon"

# # List all files in the folder
# files = os.listdir(folder_path)

# # Read each CSV file and store them in a dictionary
# data = {}
# for file in files:
#     if file.endswith(".csv"):
#         file_path = os.path.join(folder_path, file)
#         df = pd.read_csv(file_path)
#         data[file] = df

# # Example: Accessing data from a specific CSV file
# # Let's say you want to access the data from the first CSV file
# first_csv_data = data[files[0]]

# # Now you can use first_csv_data as a pandas DataFrame containing the data from the first CSV file
# # For example, you can print the first few rows:
# print(first_csv_data.head())

# df = pd.read_csv("https://github.com/monkfill/SP_ELE_005/tree/main/dataset/Holon")