import streamlit as st

st.title('XG Dialogue Tree Generator')

st.info('This is a simple app to generate dialogue trees using the XG format.')

with st.expander('How to use this app:'):
    st.write('''
    1. Enter the dialogue tree in the text box.
    2. Click the button to generate the XG dialogue tree.
    3. The generated XG dialogue tree will be displayed in the text box below.
    ''')