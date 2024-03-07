import streamlit as st
import pandas as pd
import os

# Function to read all CSV files from a folder and concatenate them into a single DataFrame
def read_csv_from_folder(folder_path):
    dfs = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            try:
                file_path = os.path.join(folder_path, file_name)
                dfs.append(pd.read_csv(file_path))
            except Exception as e:
                st.error(f"Error reading {file_name}: {e}")
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    return None

read_csv_from_folder("dataset\Holon")

# def main():
#     st.title("Read CSV files from Folder")

#     # Path to the folder containing CSV files
#     folder_path = os.path.dirname(os.path.abspath(__file__))

#     st.write("CSV files to read:")
#     for file_name in os.listdir(folder_path):
#         if file_name.endswith('.csv'):
#             st.write(file_name)

#     # Read CSV files
#     df = read_csv_from_folder(folder_path)

#     if df is not None:
#         st.write("Concatenated DataFrame:")
#         st.write(df)
#     else:
#         st.error("No data found or unable to read CSV files.")

# if __name__ == "__main__":
#     main()


