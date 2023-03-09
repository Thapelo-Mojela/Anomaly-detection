import streamlit as st
import pandas as pd
import numpy as np 

Page1  = st.container()

with Page1:
    st.sidebar.image('lombard.png',use_column_width=True)
    st.sidebar.markdown('    ')
    options = ["Project summary", "A view of the data", "Risk calculation"]
    selection = st.sidebar.selectbox('Navigation', options)
    st.sidebar.markdown('    ')
    st.sidebar.subheader('Data science team members ')
    st.sidebar.write(' - Jacob Tshabalala ')
    st.sidebar.write(' - Pabatso Tejane ')
    st.sidebar.write(' - Olefile Ramoitheki ')
    st.sidebar.write(' - Matome Peta ')
    st.sidebar.write(' - Tetelo Ndlalani ')
    st.sidebar.markdown('    ')
    st.sidebar.subheader('Contact us')
    st.sidebar.markdown(' * Email: DataScience@lombardins.onmicrosoft.com')

    if selection == "Project summary":
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

    elif selection == "A view of the data":
        st.title('A view of the data')
        st.markdown('    ')
        st.write('Hoedspruit weather data (2018-2022) density distributions')
        st.image('density1.PNG')
        st.image('density2.PNG')
        st.markdown('    ')
        st.write('Rainfall data distribution throughout the 2018 to 2022 period')
        st.image('HoedRain.PNG')
        #st.write('Hoedspruit weather data')
    
    elif selection == "Risk calculation":
        st.title('Risk prediction')
        st.markdown('    ')
        #st.write('Risk calculation formula')
        st.image('risk-formula.png')
        st.markdown('    ')
        choices = ['Hail risk', 'Fire risk']
        choice = st.radio('Hoespruit weather analysis risk calculation', choices)
        RR = 0
        def Rrating():
            hail_severity_score = 0.62
            hail_ferquency_score = 0.07
            fire_severity_score = 0.76
            fire_frequecy_score = 0.12
            if choice == 'Hail risk':
                RR = round(hail_severity_score*hail_ferquency_score*100,2)
                #st.write('The risk of hail in Hoedspruit based on the weather data analysed is:', Hail_risk ,'%')

            elif choice == 'Fire risk':
                RR = round(fire_severity_score*fire_frequecy_score*100,2)
                #st.write('The risk of fire in Hoedspruit based on the weather data analysed is:', Fire_risk ,'%')
            st.success(f"Answer = {RR} %")

        if st.button("Calculate risk rating"):
            Rrating()





