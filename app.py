import streamlit as st
import pandas as pd
import numpy as np 

header  = st.container()
dataset = st.container()
feature = st.container()
model = st.container()

with header:
    st.title('Anomaly detection')
    #st.sidebar.image('images//DataDot.PNG')
    st.sidebar.subheader('Lombard Data Science ')
    st.sidebar.markdown('    ')
    options = ["Project Summary", "Exploring The Data", "Peril Rating", " Additional Information"]
    selection = st.sidebar.selectbox("Page Navigation options", options)
    st.sidebar.markdown('    ')
    st.sidebar.subheader('Contact us')
    st.sidebar.markdown(' * Email: DataScience@lombardins.onmicrosoft.com')
    st.subheader('Team Members')
    st.markdown(" * **Jacob Tshabalala** : Data Science Manager ")
    st.markdown(" * **Pabatso Tejane** : App developer ")
    st.markdown(" * **Olefile Ramoitheki** : Jnr Data Scienctist")
    st.markdown(" * **Matome Peta** : Jnr Data Scienctist")
    st.markdown(" * **Tetelo Ndlalani** : Jnr Data Scienctist ")