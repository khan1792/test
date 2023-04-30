import streamlit as st
import pandas as pd

data = pd.read_csv('check1.csv')
y = st.number_input('Insert a number', min_value = 2006, value = 2019, format = '%i')
data = data[data['year']==y][['link', 'text', 'user_description', 'user_name', 'year']]
data.index = range(len(data))

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[0]
    return f'<a target="_blank" href="{link}">{text}</a>'

data['link'] = data['link'].apply(make_clickable)

i = st.number_input('Insert a number', min_value = 1, format = '%i')

st.write(data[(i-1)*10:i*10].to_html(escape=False, index=False), unsafe_allow_html=True)


