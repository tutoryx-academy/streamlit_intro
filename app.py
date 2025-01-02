import streamlit as st

st.title('This is our first streamlit app!')
st.header('This is our header!')
st.write('Hello ekipa!')
st.divider()
# button_1 = st.button('Press here!')
# print('Press button output',button_1)
if st.button('For markdown press here!'):
    st.markdown('This is our **markdown** written in _italic_ and with some __underlines__')
