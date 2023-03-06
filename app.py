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
    selection = st.sidebar.selectbox(" **Page Navigation options** ", options)
    st.sidebar.markdown('    ')
    st.sidebar.subheader('Contact us')
    st.sidebar.markdown(' * Email: DataScience@lombardins.onmicrosoft.com')
    st.sidebar.markdown('    ')
    st.sidebar.subheader('Team Members')
    st.sidebar.write(' - Jacob Tshabalala      Data Science Manager ')
    st.sidebar.write(' - Pabatso Tejane        Jnr Data Scientist ')
    st.sidebar.write(' - Olefile Ramoitheki    Jnr Data Scientist ')
    st.sidebar.write(' - Matome Peta           Jnr Data Scientist ')
    st.sidebar.write(' - Tetelo Ndlalani       Jnr Data Scientist ')