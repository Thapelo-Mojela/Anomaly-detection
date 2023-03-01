"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os

# Libraries to be used in data cleaning and model
import nltk
from nltk.tokenize import word_tokenize
from nltk import TreebankWordTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus.reader import wordnet
from nltk.tag import pos_tag
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, KFold, cross_val_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score

import numpy as np # linear algebra
import re
import warnings

warnings.filterwarnings('ignore')

# Data dependencies
import pandas as pd
import numpy as np

#@st.cache(allow_output_mutation=True)
def get_data(filename):
	data = pd.read_csv(filename)

	return data

# Load your raw data
raw_tweets = get_data("data//train.csv")
tweets = get_data("data//train.csv")
test_data = get_data("data//test_with_no_labels.csv")

#Data pre-processing functions
def cleaner(tweet):
    tweet = tweet.lower()
    
    to_del = [
        r"@[\w]*",  # strip account mentions
        r"http(s?):\/\/.*\/\w*",  # strip URLs
        r"#\w*",  # strip hashtags
        r"\d+",  # delete numeric values
        r"rt[\s]+",
        r"U+FFFD",  # remove the "character note present" diamond
    ]
    for key in to_del:
        tweet = re.sub(key, "", tweet)
    
    # strip punctuation and special characters
    tweet = re.sub(r"[,.;':@#?!\&/$]+\ *", " ", tweet)
    # strip excess white-space
    tweet = re.sub(r"\s\s+", " ", tweet)
    
    return tweet.lstrip(" ")

def lemmatizer(df):
    df["length"] = df["message"].str.len()
    df["tokenized"] = df["message"].apply(word_tokenize)
    df["parts-of-speech"] = df["tokenized"].apply(nltk.tag.pos_tag)
    
    def str2wordnet(tag):
        conversion = {"J": wordnet.ADJ, "V": wordnet.VERB, "N": wordnet.NOUN, "R": wordnet.ADV}
        try:
            return conversion[tag[0].upper()]
        except KeyError:
            return wordnet.NOUN
    
    wnl = WordNetLemmatizer()
    df["parts-of-speech"] = df["parts-of-speech"].apply(
        lambda tokens: [(word, str2wordnet(tag)) for word, tag in tokens]
    )
    df["lemmatized"] = df["parts-of-speech"].apply(
        lambda tokens: [wnl.lemmatize(word, tag) for word, tag in tokens]
    )
    df["lemmatized"] = df["lemmatized"].apply(lambda tokens: " ".join(map(str, tokens)))
    
    return df


# Application of the function to clean the tweets
tweets['message'] = tweets['message'].apply(cleaner)
test_data['message'] = test_data['message'].apply(cleaner)

tweets = lemmatizer(tweets)
test_data = lemmatizer(test_data)

# The main function where we will build the actual app
def main():
	#Tweet Classifier App with Streamlit 
	# Creates a main title and subheader on your page -
	# these are static across all pages
	st.image('images//DataDot.PNG')
	st.title("Climate Change Belief Classifier")
	st.sidebar.image('images//DataDot.PNG')
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
		st.image('images//TwitterValue.PNG')
		st.markdown("   ")
		st.markdown("The Buzzwords used in the tweets.")
		st.image('images//wordcloud.png')
		st.markdown("   ")
		st.markdown("The most popular hashtags")
		st.image('images//frequent.png')

	# Building the "Information" page
	if selection == " Additional Information":
		st.subheader("Additional Information")

		st.subheader("Model description")
		st.markdown("* **Linear Support Vector Classifier**:The objective of a Linear SVC (Support Vector Classifier) is to fit to the data you provide, returning a best fit hyperplane that divides, or categorizes, your data. From there, after getting the hyperplane, you can then feed some features to your classifier to see what the predicted class is. ")
		st.markdown("* **Multinomial Naive Bayers Classifier**: The Multinomial Naive Bayes algorithm is a Bayesian learning approach popular in Natural Language Processing (NLP). The program guesses the tag of a text, such as an email or a newspaper story, using the Bayes theorem. It calculates each tag's likelihood for a given sample and outputs the tag with the greatest chance.")
		st.markdown("* **K-Neighnours Classifier**: KNN regression is a non-parametric method that, in an intuitive manner, approximates the association between independent variables and the continuous outcome by averaging the observations in the same neighbourhood. ")
		st.markdown('For more indepth information on these models, vist: https://monkeylearn.com/blog/classification-algorithms/')

		st.subheader("A look into the data")
		if st.checkbox('Show raw data'): # data is hidden if box is unchecked
			st.write(raw_tweets[['sentiment', 'message']]) # will write the raw df to the page

	if selection == 'Prediction':
		st.subheader('Classify your tweets using our machine learning models')
		data_source = ['Select option','Data Frame'] # differentiating between a single text and a dataset input
		source_selection = st.selectbox('What to classify?', data_source)

        # Loading model pickle files
		def load_prediction_models(model_file):
			loaded_models = joblib.load(open(os.path.join(model_file),"rb"))
			return loaded_models
		
		if source_selection == 'Data Frame':
            ### DATA FRAME TWEET CLASSIFICATION ###
			st.subheader('DataFrame tweet classification')
			text_input = st.file_uploader("Choose a CSV file", type="csv")
			if text_input is not None:
				text_input = pd.read_csv(text_input)
				
			uploaded_dataset = st.checkbox('See uploaded dataset')

			if uploaded_dataset:
				st.dataframe(text_input.drop('sentiment', axis=1).head(10))

			st.markdown("   ")
			st.image("images//Matrix.PNG")

			ml_models = ["Linear SVC","Multinomial NB","K-Neighbours"]
			model_choice = st.selectbox("Choose ML Model",ml_models)
			

			if st.button('Classify'):
				
				text_input['message'] = text_input['message'].apply(cleaner)
				text_input = lemmatizer(tweets)

				X = text_input['message']

				if model_choice == 'Linear SVC':
					predictor = joblib.load(open(os.path.join("models//LinearSVC.pkl"),"rb"))
					prediction = predictor.predict(X)

				if model_choice == 'Multinomial NB':
					predictor = load_prediction_models("models//MultinomialNB.pkl")
					prediction = predictor.predict(X)
            
				if model_choice == 'K-Neighbours':
					predictor = load_prediction_models("models//KNeighbours.pkl")
					prediction = predictor.predict(X)

				prediction_dict = {-1: 'Anti', 0: 'Neutral',1: 'Pro',2: 'News'}
				funt = lambda x: prediction_dict[x]
				a = list(map(funt,prediction))
				results = pd.DataFrame(a)
		
				results["tweet_id"] = text_input["tweetid"]
				results.columns = ['Predicted_sentiment', 'Tweet_id'] #renaming result dataframe columns
				results.set_index('Tweet_id', inplace=True)
				st.success(st.dataframe(results))

				
# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()

