import streamlit as st
import pandas as pd
import numpy as np 

Page1  = st.container()
Page2 = st.container()
Page3 = st.container()
Page4 = st.container()

with Page1:
    st.sidebar.image('lombard2.jpg',use_column_width=True)
    st.sidebar.markdown('    ')
    options = ["Project Summary", "Exploring The Data", "Peril Rating"]
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
        st.title('Anomaly detection')
        st.write('''Climate change has resulted in the occurrence of unpredictable and severe weather events.  
        The occurrence of these events may result in the loss of crops and vegetation, which can be catastrophic and detrimental to the livelihoods of the farmers affected. Crop insurance has become more popular with farmers being more aware of the benefits of indemnifying themselves against the loss of their crops from such events.  
        The purpose of this project is to explore the occurrence of these perils and provide guidance on pricing, in order to offer a reasonable product to the farmer while preventing loss on the insurers side.''')
        st.markdown('    ')
        st.markdown('The main perils we are interested in for crop insurance are hail are fire. Based on literature these are the factors/weather conditions that influence the perils:')
        st.markdown('* **Fire conditions**')
        st.write('''In the presence of dry vegetation:  
        Lightning(ignition source), low relative humidity, high wind speeds and high temperatures''')
        st.markdown('* **Hail conditions**')
        st.write('''Heavy rainfall, high relative humidity, high wind speeds and low temperatures''')

    elif selection == "Exploring The Data":
        st.write('prediction')
    
    elif selection == "Peril Rating":
        st.write('prediction')