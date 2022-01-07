import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn import metrics
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.pipeline import Pipeline

#from skopt import BayesSearchCV
import pickle
import datetime
import streamlit as st

df = pd.read_csv('../Data/salary_cleaned.csv')

with open('../Models/totalcomp_gs_gbr2.pkl', 'rb') as f:
    gs_gbr2 = pickle.load(f)

#with open('../Models/ColumnTransformer.pkl', 'rb') as f:
    #ct_pkl = pickle.load(f)

X = df[['company', 'title', 'yearsofexperience', 'yearsatcompany', 'year', 'month', 'state', 'inflation_rate',
            'inflation_rate_3mos', 'employment_rate', 'employment_rate_3mos']].copy()




#X_dummy = pd.get_dummies(X, columns = ['company', 'title', 'state_short'], drop_first = True)
y = df[['totalyearlycompensation']].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42)

X_train_ohe = OneHotEncoder(X_train)
X_test_ohe = OneHotEncoder(X_test)

#Feature Scaling
sc = StandardScaler()

X_train_sc = sc.fit_transform(X_train_ohe)
X_test_sc = sc.transform(X_test_ohe)

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
    company = st.selectbox(label = 'Company name:', options = df['company'].unique())
    title = st.selectbox(label = 'Position title:', options = df['title'].unique())
    yearsofexperience = st.number_input("Years of experience:")
    yearsatcompany =  st.number_input("Years at company:")
    state = st.selectbox(label = 'US State:', options = df['state'].unique())
submit = st.button('Predict')

new_data = {
    'company': company,
    'title': title,
    'yearsofexperience': yearsofexperience,
    'yearsatcompany': yearsatcompany,
    'year': str(year),
    'month': str(month),
    'state': state,
    'inflation_rate_3mos': inflation_rate_3mos,
    'employment_rate': employment_rate,
    'employment_rate_3mos': employment_rate_3mos
}

if submit:

    new_data_df = pd.DataFrame(new_data, index=[0])
    
    new_data_df_sc = sc.transform(new_data_df)
    
    
    

    prediction = gs_gbr2.predict(new_data_df_ct)
    st.write(prediction)
