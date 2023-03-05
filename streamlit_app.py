
import streamlit as st
import joblib,os
import string

# Data dependencies
import pandas as pd
import numpy as np

# The main function where we will build the actual app
def main():
	#Tweet Classifier App with Streamlit 
	# Creates a main title and subheader on your page -
	# these are static across all pages
	st.title("Climate Change Belief Classifier")
	st.sidebar.subheader('About Data Dot Inc.')
	st.sidebar.markdown('Data Dot Inc. is a consultancy firm that uses data science processes to solve your everyday marketing problems')
	st.sidebar.markdown('    ')
	# Creating sidebar with selection box 
	# you can create multiple pages this way
	options = ["Project Summary", "Exploring The Data", " Additional Information"]
	selection = st.sidebar.selectbox("App Navigation options", options)
	st.sidebar.markdown('    ')
	st.sidebar.subheader('Contact us')
	st.sidebar.markdown(' * Website: www.DataDot.co.za')
	st.sidebar.markdown(' * Tel: 011 442 0000')
	st.sidebar.markdown(' * Twitter: @DataDot')
	st.sidebar.markdown(' * LinkedIn: www.linkedin.com/in/DataDot')

	# Building the "Summary" page
	if selection == "Project Summary":
		st.subheader("Team Members")
		st.markdown(" * **Euphrasia Mampuru** : Scrum master ")
		st.markdown(" * **Pabatso Tejane** : App developer ")
		st.markdown(" * **Olefile Ramoitheki** : Public relations ")
		st.markdown(" * **Nqobile Ncube** : Project manager")
		st.markdown(" * **Collen Bothma** : Programmer ")
	
		st.subheader("Project Problem Statement")
		st.markdown("Our client  **Quizzical Pictures (PTY) Ltd**  is a film production company that produced the film **Back To Eden**. Back to Eden is a film about a fictional eutopia, the film depicts what life would be like in a world where society took climate change seriously.")
		st.markdown("Data Dot Inc. was tasked to develop an app that will enable Quizzical Pictures to identify their target market from a customer tweet database. The assumptions made were that the poteintial viewers are pro climate change and that their tweets revealed this sentiment.")
		
	# Building the "EDA" page
	if selection == "Exploring The Data":
		st.subheader("Exploratory data analysis visuals")
		st.markdown("The distribution of the four possible sentiments")
		st.markdown("   ")
		st.markdown("The Buzzwords used in the tweets.")
		st.markdown("   ")
		st.markdown("The most popular hashtags")

	# Building the "Information" page
	if selection == " Additional Information":
		st.subheader("Additional Information")

		st.subheader("Model description")
		st.markdown("* **Linear Support Vector Classifier**:The objective of a Linear SVC (Support Vector Classifier) is to fit to the data you provide, returning a best fit hyperplane that divides, or categorizes, your data. From there, after getting the hyperplane, you can then feed some features to your classifier to see what the predicted class is. ")
		st.markdown("* **Multinomial Naive Bayers Classifier**: The Multinomial Naive Bayes algorithm is a Bayesian learning approach popular in Natural Language Processing (NLP). The program guesses the tag of a text, such as an email or a newspaper story, using the Bayes theorem. It calculates each tag's likelihood for a given sample and outputs the tag with the greatest chance.")
		st.markdown("* **K-Neighnours Classifier**: KNN regression is a non-parametric method that, in an intuitive manner, approximates the association between independent variables and the continuous outcome by averaging the observations in the same neighbourhood. ")
		st.markdown('For more indepth information on these models, vist: https://monkeylearn.com/blog/classification-algorithms/')

        # Loading model pickle files
	#	def load_prediction_models(model_file):
	#		loaded_models = joblib.load(open(os.path.join(model_file),"rb"))
	#		return loaded_models
