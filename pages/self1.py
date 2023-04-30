import streamlit as st
import pandas as pd

data = pd.read_csv('check1.csv')
y = st.number_input('Insert a number', min_value = 2006, value = 2019, format = '%i')
rem = st.text_input(label="remove words", value = '驻京企业|風在吼|义和团|李鸿章｜清朝｜尋找所有人的匿名問題|图文小说|国有资产|风在吼')
data = data[data['year']==y][['link', 'text', 'user_description', 'user_name', 'year']]
data = data[~data['text'].str.contains(rem)]
data.index = range(len(data))

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[0]
    return f'<a target="_blank" href="{link}">{text}</a>'

data['link'] = data['link'].apply(make_clickable)

i = st.number_input('Insert a number', min_value = 1, format = '%i')

st.write(data[(i-1)*2:i*2].to_html(escape=False, index=False), unsafe_allow_html=True)
