import pandas as pd
import pickle
import streamlit as st


with open('../Models/totalcomp_gs_gbr2.pkl', 'rb') as f:
    gs_gbr2 = pickle.load(f)
        
year = 2020
month = 9
inflation_rate = 0.014
inflation_rate_3mos = 0.006
employment_rate = 0.93582054649934
employment_rate_3mos = 0.8939803405002691  
        
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
        
    new_data_df = pd.DataFrame([company_name, title, years_of_experience, years_at_company, year, month, state, inflation_rate,employment_rate,employment_rate_3mos])


    new_data_df_ct = ct.transform(new_data_df)
    gs_gbr2.predict(new_data_df_ct)
        
    prediction = gs_gbr2.predict(new_data_df_ct)
    st.write('You can expect a total compensation of' prediction '$.')

