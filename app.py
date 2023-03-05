import streamlit
import pandas as pd
import numpy as np 

header  = st.beta_container()
dataset = st.beta_container()
feature = st.beta_container()
model = st.beta_container()

with header:
  st.title('Anomaly detection Project')
