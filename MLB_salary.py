# Imports
import pickle
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title ='What is your MLB salary?',
    initial_sidebar_state='expanded'
)

st.title('What is your MLB salary?')
st.subheader('Based on your stats')

st.sidebar.title('Your Position')
st.sidebar.text('Pitcher or Position Player?')
positions = st.sidebar.selectbox(
    'Position',
    ('Pitcher', 'Position Player')
)
def user_input_feats_pitchers():
    pitchers_dict = {} 
    pitchers_dict['yearID'] = st.slider(label= 'Year', min_value=1985, max_value=2020, step=1)
    pitchers_dict['W'] = st.slider(label= 'Wins', min_value=0, max_value=162, step=1)
    pitchers_dict['L'] = st.slider(label= 'Losses', min_value=0, max_value=162, step=1)
    pitchers_dict['G'] = st.slider(label= 'Games', min_value=0, max_value=162, step=1)
    pitchers_dict['GS'] = st.slider(label= 'Games Started', min_value=0, max_value=162, step=1)
    pitchers_dict['CG'] = st.slider(label= 'Complete Games', min_value=0, max_value=162, step=1)
    pitchers_dict['SHO'] = st.slider(label= 'Shutouts', min_value=0, max_value=162, step=1)
    pitchers_dict['SV'] = st.slider(label= 'Saves', min_value=0, max_value=162, step=1)
    pitchers_dict['IPouts'] = st.number_input(label= 'IPouts', min_value=0.0, step=1.0)
    pitchers_dict['H'] = st.number_input(label= 'Hits Allowed', min_value=0.0, step=1.0)
    pitchers_dict['ER'] = st.number_input(label= 'Earned Runs', min_value=0.0, step=1.0)
    pitchers_dict['HR'] = st.number_input(label= 'Home Runs Allowed', min_value=0.0, step=1.0)
    pitchers_dict['BB'] = st.number_input(label= 'Walks Allowed', min_value=0.0, step=1.0)
    pitchers_dict['SO'] = st.number_input(label= 'Ks', min_value=0.0, step=1.0)
    pitchers_dict['BAOpp'] = st.slider(label= 'Opponent Batting Average', min_value=0.000, max_value=1.000, step=.001)
    pitchers_dict['ERA'] = st.number_input(label='Earned Run Average', min_value=0.00, step=0.01)
    pitchers_dict['IBB'] = st.number_input(label= 'Intentional Walks Allowed', min_value=0.0, step=1.0)
    pitchers_dict['WP'] = st.number_input(label= 'Wild Pitches', min_value=0.0, step=1.0)
    pitchers_dict['HBP'] = st.number_input(label= 'Hit By Pitches Allowed', min_value=0.0, step=1.0)
    pitchers_dict['BK'] = st.number_input(label= 'Balks', min_value=0.0, step=1.0)
    pitchers_dict['BFP'] = st.number_input(label= 'Batters Faced', min_value=0.0, step=1.0)
    pitchers_dict['GF'] = st.number_input(label= 'Games Finished', min_value=0.0, step=1.0)
    pitchers_dict['R'] = st.number_input(label= 'Runs Allowed', min_value=0.0, step=1.0)
    pitchers_dict['SH'] = st.number_input(label= 'Sacrifice Hits Allowed', min_value=0.0, step=1.0)
    pitchers_dict['SF'] = st.number_input(label= 'Sacrifice Flies Allowed', min_value=0.0, step=1.0)
    pitchers_dict['GIDP'] = st.number_input(label= 'Grounded into Double Plays Induced', min_value=0.0, step=1.0)
    pitchers_dict['Years_Exp'] = st.slider(label= 'Years of Experience', min_value=1, max_value=35, step=1)
    pitchers_dict['allStar'] = st.slider(label= 'All-Star (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_ALCS_MVP'] = st.slider(label= 'ALCS MVP Award (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_AllStar_Game_MVP'] = st.slider(label= 'All Star Game MVP Award(0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_Gold_Glove'] = st.slider(label= 'Gold Glove Award (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_Most_Valuable_Player'] = st.slider(label= 'MVP Award (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_NLCS_MVP'] = st.slider(label= 'NLCS MVP Award (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_Rookie_of_the_Year'] = st.slider(label= 'Rookie of the Year Award (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_World_Series_MVP'] = st.slider(label= 'World Series MVP Award (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_Cy_Young_Award'] = st.slider(label= 'Cy Young (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_Rolaids_Relief_Man_Award'] = st.slider(label= 'Rolaids Relief Man (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_Pitching_Triple_Crown'] = st.slider(label= 'Pitching Triple Crown (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['awardID_Reliever_of_the_Year_Award'] = st.slider(label= 'Reliever of the Year (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pitchers_dict['WHIP'] = st.number_input(label='WHIP', min_value=0.00, step=0.01)
    pitchers_dict['H_per_9'] = st.number_input(label='H/9', min_value=0.00, step=0.01)
    pitchers_dict['HR_per_9'] = st.number_input(label='HR/9', min_value=0.00, step=0.01)
    pitchers_dict['BB_per_9'] = st.number_input(label='BB/9', min_value=0.00, step=0.01)
    pitchers_dict['SO_per_9'] = st.number_input(label='SO/9', min_value=0.00, step=0.01)
    order_features = ['yearID', 'W', 'L', 'G', 'GS', 'CG', 'SHO', 'SV', 'IPouts', 'H',
        'ER', 'HR', 'BB', 'SO', 'BAOpp', 'ERA', 'IBB', 'WP', 'HBP', 'BK',
        'BFP', 'GF', 'R', 'SH', 'SF', 'GIDP', 'Years_Exp', 'allStar',
        'awardID_ALCS_MVP', 'awardID_AllStar_Game_MVP',
        'awardID_Gold_Glove', 'awardID_Most_Valuable_Player',
        'awardID_NLCS_MVP', 'awardID_Rookie_of_the_Year',
        'awardID_World_Series_MVP', 'awardID_Cy_Young_Award',
        'awardID_Rolaids_Relief_Man_Award',
        'awardID_Pitching_Triple_Crown',
        'awardID_Reliever_of_the_Year_Award', 'WHIP', 'H_per_9',
        'HR_per_9', 'BB_per_9', 'SO_per_9']
    pitcher = pd.Series(pitchers_dict)
    return pitcher.loc[order_features]

 

# Change to Position Player Stats
def user_input_feats_pos_players():
    pos_player_dict = {}
    pos_player_dict['yearID'] = st.slider(label= 'Season', min_value=1985, max_value=2020, step=1)
    pos_player_dict['G'] = st.slider(label= 'Games Played', min_value=0, max_value=162, step=1)
    pos_player_dict['AB'] = st.number_input(label= 'At-Bats', min_value=0.0, step=1.0)
    pos_player_dict['R'] = st.number_input(label= 'Runs Scored', min_value=0.0, step=1.0)
    pos_player_dict['H'] = st.number_input(label= 'Hits', min_value=0.0, step=1.0)
    pos_player_dict['Doubles'] = st.number_input(label= 'Doubles', min_value=0.0, step=1.0)
    pos_player_dict['Triples'] = st.number_input(label= 'Triples', min_value=0.0, step=1.0)
    pos_player_dict['HR'] = st.number_input(label= 'Home Runs', min_value=0.0, step=1.0)
    pos_player_dict['RBI'] = st.number_input(label= 'Runs Batted In', min_value=0.0, step=1.0)
    pos_player_dict['SB'] = st.number_input(label= 'Stolen Bases', min_value=0.0, step=1.0)
    pos_player_dict['CS'] = st.number_input(label= 'Caught Stealing', min_value=0.0, step=1.0) 
    pos_player_dict['BB'] = st.number_input(label= 'Walks', min_value=0.0, step=1.0)
    pos_player_dict['SO'] = st.number_input(label= 'Strike Outs', min_value=0.0, step=1.0)
    pos_player_dict['IBB'] = st.number_input(label= 'Intentional Walks', min_value=0.0, step=1.0)
    pos_player_dict['HBP'] = st.number_input(label= 'Hit By Pitches', min_value=0.0, step=1.0)
    pos_player_dict['SH'] = st.number_input(label= 'Sacrifice Hits', min_value=0.0, step=1.0)
    pos_player_dict['SF'] = st.number_input(label= 'Sacrifice Flies', min_value=0.0, step=1.0)
    pos_player_dict['GIDP'] = st.number_input(label= 'Grounded into Double Plays', min_value=0.0, step=1.0)
    pos_player_dict['Years_Exp'] = st.slider(label= 'Years in the MLB', min_value=1, max_value=35, step=1)
    pos_player_dict['allStar'] = st.slider(label= 'All Star (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_ALCS_MVP'] = st.slider(label= 'ALCS MVP (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_AllStar_Game_MVP'] = st.slider(label= 'All Star Game MVP (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_Babe_Ruth_Award'] = st.slider(label= 'Babe Ruth Award (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_Gold_Glove'] = st.slider(label= 'Gold Glove (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_Hank_Aaron_Award'] = st.slider(label= 'Hank Aaron Award (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_Most_Valuable_Player'] = st.slider(label= 'MVP (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_NLCS_MVP'] = st.slider(label= 'NLCS MVP (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_Outstanding_DH_Award'] = st.slider(label= 'Outstanding DH Award (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_Rookie_of_the_Year'] = st.slider(label= 'Rookie of the Year (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_Silver_Slugger'] = st.slider(label= 'Silver Slugger Award (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_Triple_Crown'] = st.slider(label= 'Triple Crown (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['awardID_World_Series_MVP'] = st.slider(label= 'World Series MVP (0 = No, 1 = Yes)', min_value=0, max_value=1, step=1)
    pos_player_dict['AVG'] = st.slider(label= 'Batting Average', min_value=0.000, max_value=1.000, step=.001)
    pos_player_dict['OBP'] = st.number_input(label='On Base Percentage', min_value=0.000, max_value=1.000,step=0.001)
    pos_player_dict['SLG'] = st.number_input(label='Slugging Percentage', min_value=0.000, step=0.01)
    pos_player_dict['OPS'] = st.number_input(label='On Base Plus Slugging', min_value=0.00, step=0.01)
    order_features = ['yearID', 'G', 'AB', 'R', 'H', 'Doubles', 'Triples', 'HR', 'RBI',
       'SB', 'CS', 'BB', 'SO', 'IBB', 'HBP', 'SH', 'SF', 'GIDP',
       'Years_Exp', 'allStar', 'awardID_ALCS_MVP',
       'awardID_AllStar_Game_MVP', 'awardID_Babe_Ruth_Award',
       'awardID_Gold_Glove', 'awardID_Hank_Aaron_Award',
       'awardID_Most_Valuable_Player', 'awardID_NLCS_MVP',
       'awardID_Outstanding_DH_Award', 'awardID_Rookie_of_the_Year',
       'awardID_Silver_Slugger', 'awardID_Triple_Crown',
       'awardID_World_Series_MVP', 'AVG', 'OBP', 'SLG', 'OPS']
    pos_player = pd.Series(pos_player_dict)
    return pos_player.loc[order_features]
    




if positions == 'Pitcher':
    st.subheader('Salary Predictions for Pitchers')
    st.write('''
Enter your stats to generate your salary prediction!

    ''')
    features_for_pitchers = user_input_feats_pitchers()
    with open('pitchers.p', 'rb') as pickle_in:
        lr = pickle.load(pickle_in)   
        
    predicted_pitchers_salary = round(np.exp(lr.predict([features_for_pitchers]))[0], 2)
    predicted_pitchers_salary = "{:,.2f}".format(predicted_pitchers_salary)
    st.subheader('Results:')
    st.write(f'Your salary is $ {predicted_pitchers_salary}.')   

elif positions == 'Position Player':
    st.subheader('Salary Predictions for Position Players')
    st.write('''
Enter your stats to generate your salary prediction!

    ''')
    features_for_position_players = user_input_feats_pos_players()
    with open('position_players.p', 'rb') as pickle_in:
        lr = pickle.load(pickle_in) 

    predicted_pos_players_salary = round(np.exp(lr.predict([features_for_position_players]))[0], 2)
    predicted_pos_players_salary = "{:,.2f}".format(predicted_pos_players_salary)
    st.subheader('Results:')
    st.write(f'Your salary is $ {predicted_pos_players_salary}.')
