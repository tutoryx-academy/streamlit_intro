import streamlit as st
import pandas as pd

st.title('This is our first streamlit app!')
st.header('This is our header!')
st.write('Hello ekipa!')
st.divider()
# button_1 = st.button('Press here!')
# print('Press button output',button_1)
if st.button('For markdown press here!'):
    st.markdown('This is our **markdown** written in _italic_ and with some __underlines__')

if st.checkbox('Do you aggree?'):
    st.warning('This code is run after agree button is checked')

options = st.multiselect(
    'Addition',
    # ['one','two','three']
    {'one':1,'two':2}
)

st.write(options)

operation_type = st.radio(
    'Choose the operation',
    options=['addition','subtraction','multiplication','division']
)
st.write(operation_type)

num_1 = st.number_input('Please write a number')
st.write(num_1)

st.divider()

slider_input_value = st.slider('Choose a value for slider')
st.write(slider_input_value)

st.divider()

date_input_var = st.date_input('Please enter a valid date')
st.write(date_input_var)
time_input_var = st.time_input('Please enter a time')
st.write(time_input_var)

st.divider()
text_input_var = st.text_input('Enter a text')
st.write(text_input_var)
text_area_var = st.text_area('Enter a longer text')
st.write(text_area_var)

st.divider()
file_uploaded = st.file_uploader('Upload a csv')
if file_uploaded:
    df = pd.read_csv(file_uploaded)
    st.dataframe(df)