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
    selection = st.sidebar.selectbox("App Navigation options", options)