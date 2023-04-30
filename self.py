import pandas as pd
import streamlit as st
data = pd.read_csv('check.csv')
st.dataframe(ddd[ddd['year']>2018][['link', 'text', 'user_description', 'user_name', 'year']])




