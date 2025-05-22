# -*- coding: utf-8 -*-
"""
Created on Wed May 21 22:05:58 2025

@author: abose

streamlit app to deploy win predictor model for IPL matches

"""

import streamlit as st
import joblib
import pandas as pd

### necessary sklearn libraries

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

@st.cache_resource

def load_model():
    
    try:
        model = joblib.load('win_probability_model.joblib')
        return model
    except Exception as e:
        st.error(f'Error loading model: {e}')
        return None
    
predictor = load_model()

st.title("IPL Win Probability Model")

team_list = ['CSK','DC','GT','KKR','LSG','MI','PBKS','RCB','RR','SRH']

team_name_dict = {
    'CSK': 'Chennai',
    'DC': 'Delhi',
    'GT': 'Gujarat',
    'KKR': 'Kolkata',
    'LSG': 'Kochi',
    'MI': 'Mumbai',
    'PBKS': 'Punjab',
    'RCB': 'Bangalore',
    'RR': 'Rajasthan',
    'SRH': 'Hyderabad'
}

data_columns = ['batting_team', 'bowling_team', 'target_score', 'runs_needed', 'balls_remaining',
                'wickets_left', 'runrate', 'required_runrate', 'pressure_index']

def create_dataframe(input_data):
    data_dict = {}
    for i,col in enumerate(data_columns):
        data_dict[col] = input_data[i]
    return pd.DataFrame([data_dict])

if predictor:
    ## Input fields for features
    batting_team = st.selectbox('Batting Team', team_list)
    bowling_team = st.selectbox('Bowling Team', team_list)
    target = st.number_input('Target',value=200)
    curr_score = st.number_input('Current Score',value=100)
    wickets = st.number_input('Wickets',value=1)
    over = st.number_input('Over',value=7.2)
    
    str_over = str(over)    
    if '.' in str_over:
        num_over, num_balls = str_over.split('.')
    else:
        num_over = str_over
        num_balls = '0'

    if st.button("Calculate Win Probability"):
        if (batting_team == bowling_team):
            st.error('Error: Batting and Bowling team can not be same!')
        else:
            runs_needed = target - curr_score
            balls = float(num_over)*6. + float(num_balls)
            balls_rem = 120. - balls
            wickets_left = 10. - wickets
            rr = curr_score/(balls/6.)
            rrr = (target - curr_score)/((120 - balls)/6.)
            p_index = rrr/rr
        
            input_list = [batting_team,bowling_team,target,runs_needed,balls_rem,wickets_left,rr,rrr,p_index]
        
            input_df = create_dataframe(input_list)
        
            if ((balls_rem == 0) or (wickets_left == 0)):
                print('Match finished!')
            else:
                try:
                    prediction_prob = predictor.predict_proba(input_df)
                    batting_team_win_prob = round(prediction_prob[0][1]*100,2)
                    bowling_team_win_prob = round(prediction_prob[0][0]*100,2)
        
                    if (batting_team_win_prob >= bowling_team_win_prob):
                        st.info(f"{batting_team} Win Probability: {batting_team_win_prob}%")
                    else:
                        st.info(f"{bowling_team} Win Probability: {bowling_team_win_prob}%")
        
                except Exception as e:
                    st.error(f"Prediction error: {e}")
                    st.warning(f"Please ensure all inputs are valid and match the model's expectations.")
    
else:
    st.warning('Model could not be loaded. Please check the backend.')
