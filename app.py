import streamlit as st
import pandas as pd
import numpy as np 

header  = st.container()
dataset = st.container()
feature = st.container()
model = st.container()

with header:
    st.title('Anomaly detection')
    st.sidebar.image('lombard2.jpg',use_column_width=True)
    st.sidebar.markdown('    ')
    options = ["Project Summary", "Exploring The Data", "Peril Rating", " Additional Information"]
    selection = st.sidebar.selectbox('Navigation', options)
    st.sidebar.markdown('    ')
    st.sidebar.subheader('Data Science Team Members ')
    st.sidebar.write(' - Jacob Tshabalala ')
    st.sidebar.write(' - Pabatso Tejane ')
    st.sidebar.write(' - Olefile Ramoitheki ')
    st.sidebar.write(' - Matome Peta ')
    st.sidebar.write(' - Tetelo Ndlalani ')
    st.sidebar.markdown('    ')
    st.sidebar.subheader('Contact us')
    st.sidebar.markdown(' * Email: DataScience@lombardins.onmicrosoft.com')
    if selection == "Project Summary":
        #st.subheader('Project Problem Statement')
        st.markdown('Climate change has resulted in the occurrence of unpredictable and severe weather events. The occurrence of these events may result in the loss of crops and vegetation, which can be catastrophic and detrimental to the livelihoods of the farmers affected. Crop insurance has become more popular with farmers being more aware of the benefits of indemnifying themselves against the loss of their crops from such events.')      
        st.markdown('The purpose of this project is to explore the occurrence of these perils and provide guidance on pricing, in order to offer a reasonable product to the farmer while preventing loss on the insurers side.')
        st.markdown('    ')
        st.markdown('The main perils we are interested in for crop insurance are hail are fire. Based on literature these are the factors/weather conditions that influence the perils:')
        st.markdown('* **Hail conditions**')
        st.markdown('* **Fire conditions**')