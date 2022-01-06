import pandas as pd
import pickle
import streamlit as st

# path difference b/c solution code
with open(#DATA path
    , 'rb') as pickle_in:
        pipe/#MODEL NAME OR PIPELINE
        = pickle.load(pickle_in)

st.sidebar.header('Total compensation Predictor')
select = st.sidebar.selectbox('Select Form', ['Form 1'], key='1')
if not st.sidebar.checkbox("Hide", True, key='1'):
    st.title('Fill in the following information:')
    company_name = st.selectbox(label = 'Company name:', options = df[company].unique())
    title = st.selectbox(label = 'Position title:', options = df[title].unique())
    years_of_experience = st.number_input("Years of experience:")
    years_at_company =  st.number_input("Years at company:")
    state = st.selectbox(label = 'US State:', options = df[state_short].unique())
submit = st.button('Predict')
if submit:
        prediction = #MODEL Name
        .predict([[company_name, title, years_of_experience, years_at_company, state]])
        st.write('You can expect a total compensation of' prediction '$.')

        
#https://towardsdatascience.com/diabetes-prediction-application-using-streamlit-fed6120124a5
