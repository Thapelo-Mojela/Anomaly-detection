import streamlit as st
import pandas as pd
import numpy as np 

header  = st.container()
dataset = st.container()
feature = st.container()
model = st.container()


def main():
	#Tweet Classifier App with Streamlit 
	# Creates a main title and subheader on your page -
	# these are static across all pages
	#st.image('images//DataDot.PNG')
	st.title("Climate Change Belief Classifier")
	#st.sidebar.image('images//DataDot.PNG')
	st.sidebar.subheader('About Data Dot Inc.')
	st.sidebar.markdown('Data Dot Inc. is a consultancy firm that uses data science processes to solve your everyday marketing problems')
	st.sidebar.markdown('    ')
	# Creating sidebar with selection box 
	# you can create multiple pages this way
	options = ["Project Summary", "Exploring The Data", "Prediction", " Additional Information"]
	selection = st.sidebar.selectbox("App Navigation options", options)
	st.sidebar.markdown('    ')
	st.sidebar.subheader('Contact us')
	st.sidebar.markdown(' * Website: www.DataDot.co.za')
	st.sidebar.markdown(' * Tel: 011 442 0000')
	st.sidebar.markdown(' * Twitter: @DataDot')
	st.sidebar.markdown(' * LinkedIn: www.linkedin.com/in/DataDot')