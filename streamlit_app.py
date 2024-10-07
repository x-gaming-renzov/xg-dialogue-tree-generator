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

st.header('Dialogue Tree Generator')
personality = st.text_input('Personality of NPC', key='personality')
background = st.text_area('Background of NPC', key='background')
depth = st.number_input('Depth of conversation', min_value=1, max_value=10, value=3, key='depth')
player_tag = st.text_input('Player Tag', key='player_tag')
end_goal = st.text_input('End Goal', key='end_goal')

st.button('Generate Dialogue Tree')
if st.button:
    st.write('Dialogue Tree:')
    st.write(f'Personality: {personality}')
    st.write(f'Background: {background}')
    st.write(f'Depth: {depth}')
    st.write(f'Player Tag: {player_tag}')
    st.write(f'End Goal: {end_goal}')