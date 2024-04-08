# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:17:30 2024

@author: KIIT
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open('C:/Users/KIIT/OneDrive/Desktop/Minor Project/Diabetes_model.sav','rb'))

#sidebar for Navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction'],
                           icons=['activity'],
                           default_index=0)
    
if(selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using Ml')
    
    #getting the input data from the user
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Level')
    with col1:
        SkinThickness = st.text_input('Skin Thickmess Level')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Level')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Level')
    with col2:
        Age = st.text_input('Age of the Person')
        
        
        
    #code for prediction
    diab_diagnosis= ''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin, BMI, DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The Person is Diabetic'
            
        else:
            diab_diagnosis='The Person is Non-Diabetic'
        
    st.success(diab_diagnosis)
     
    