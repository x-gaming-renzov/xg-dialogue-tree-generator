import streamlit as st

st.title('XG Dialogue Tree Generator')

st.info('This is a simple app to generate dialogue trees using the XG format.')

with st.expander('How to use this app:'):
    st.write('''
    1. Enter Personality of NPC. It can be anything like moody, hilarious, etc.
    2. Give background of NPC. It could be why this npc is in the game, what they are doing, etc.
    3. Depth : Length of conversation.
    4. PlayerTag : Here you will enter conditions for player to enter certain branch of conversation.
             eg. if player has item x, go to branch 1, else go to branch 2.
    5. EndGoal : What you want to achieve from this conversation. Default : End conversation.
    ''')