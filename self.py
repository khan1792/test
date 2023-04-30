import streamlit as st
import pandas as pd

data = pd.read_csv('check.csv')
data = data[data['year']>2018][['link', 'text', 'user_description', 'user_name', 'year']]

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[0]
    return f'<a target="_blank" href="{link}">{text}</a>'

data['link'] = data['link'].apply(make_clickable)

i = st.number_input('Insert a number', min_value = 1, format = '%i')

st.write(data[i-1:i].to_html(escape=False, index=False), unsafe_allow_html=True)
st.video('https://twitter.com/MasonJameson99/status/1549911015843803137/video/1')

