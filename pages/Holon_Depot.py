import streamlit as st 

st.header(" Holon Depot ")

st.subheader(":building_construction: SP01_ID_OFFICE_2024")

cl1,cl2 = st.columns((2))


# with cl2:
#     # st.image("/Users/apple/Desktop/untitled folder/fotor-ai-20240207162856.jpg", width=400, caption="SP[]_Tower03")
     
with cl1: 
    st.markdown(''':wrench: **Scope Of Work :** <p style='color: #00FFFF;'>   <em> Wall, Floor, Room, Coloumn,Beam,Door,Window,Stair</p>''', unsafe_allow_html=True) 
    st.markdown(''':male-office-worker: **Users :**  <p style='color: #00FFFF;'> <em>User_ A, User_ B, User_ C, User_ D, User_ E,User_ F, User_ G, User_ H, User_ I, User_ J, User_ K</p>''',unsafe_allow_html= True)
    st.markdown("**Star Date :**   Nov3,2023")
    st.markdown("**Planned End Date :**   Feb3,2024")
st.divider()

st.subheader(''' :sky[Select Start & End Date For Categorty Wise Data]''')

