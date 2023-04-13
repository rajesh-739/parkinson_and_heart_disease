# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 00:02:06 2023

@author: J Rajesh
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


heart_model = pickle.load(open("D:\Project_Related Files\Heart Disease Prediction\heart_disease_model.sav",'rb'))
parkinson_model = pickle.load(open("D:\Project_Related Files\Parkinson's Disease Data Set\parkinson_disease_model.sav",'rb'))



#navigation sidebar

with st.sidebar:
    selected = option_menu('Parkinson and Heart Disease Prediction',
                           ['Parkinsons Disease Prediction','Heart Disease Prediction'],
                           icons=["activity","heart"],
                           default_index=0)
#Parkinson Detection Page

if selected == "Parkinsons Disease Prediction" :
    #st.header("Welcome to The Parkinsons Disease Prediction System Page")
    st.markdown("<h1 style='color:#FF4B4B'>Welcome to Parkinsons Disease Prediction System</h1>",unsafe_allow_html=True)
    st.code('Here You can Check You Parkinsons Disease Status and Heart Disease as Well',language="C")
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col1:
        Jitter_percent = st.number_input('MDVP:Jitter(%)',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col2:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col3:
        RAP = st.number_input('MDVP:RAP',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col1:
        PPQ = st.number_input('MDVP:PPQ',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col2:
        DDP = st.number_input('Jitter:DDP',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col3:
        Shimmer = st.number_input('MDVP:Shimmer',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col1:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col2:
        APQ3 = st.number_input('Shimmer:APQ3',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col3:
        APQ5 = st.number_input('Shimmer:APQ5',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col1:
        APQ = st.number_input('MDVP:APQ',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col2:
        DDA = st.number_input('Shimmer:DDA',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col3:
        NHR = st.number_input('NHR',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col1:
        HNR = st.number_input('HNR',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col2:
        RPDE = st.number_input('RPDE',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col3:
        DFA = st.number_input('DFA',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col1:
        spread1 = st.number_input('spread1',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col2:
        spread2 = st.number_input('spread2',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col3:
        D2 = st.number_input('D2',min_value=0.0,step=1e-6,format="%0.5f")
        
    with col1:
        PPE = st.number_input('PPE',min_value=0.0,step=1e-6,format="%0.5f")
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


    
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.markdown("<h1 style='color:#FF4B4B'>Welcome to Heart Disease Prediction</h1>",unsafe_allow_html=True)
    st.code(' Here you Can Check Your Heart Disease Status')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = int(st.number_input(label="Age",min_value=1,max_value=100))
    
        
    with col2:
        sex = str(st.selectbox('Gender',('Male-1','Female-0')))
        if sex == "Male-1":
            sex = int(1)
        else:
            sex = int(0)
        
        
    with col3:
        cp = (st.selectbox('Chest Pain Types',('typical angina-0','atypical angina-1','non — anginal pain-2','asymptotic-3')))
        if cp == "typical angina-1":
            cp = int(0)
        elif(cp == "atypical angina-2"):
            cp = int(1)
        elif(cp == "non — anginal pain-3"):
            cp = int(2)
        else:
            cp = int(3)
        
    with col1:
        trestbps = int(st.number_input('Resting Blood Pressure',max_value=370))
        
    with col2:
        chol = int(st.number_input('Serum Cholestoral in mg/dl',max_value=500))
        
    with col3:
        fbs = str(st.selectbox('Is Fasting Blood Sugar > 120 mg/dl',('Yes-1','No-0')))
        if fbs == "Yes-1":
            fbs = int(1)
        else:
            fbs = int(0)
        
    with col1:
        restecg = str(st.selectbox('Resting Electrocardiographic results',('Normal-0','Having ST-Wave Abnormality-1','left ventricular hyperthrophy-2')))
        if restecg == "Normal-0":
            restecg = int(0)
        elif(restecg == "Having ST-Wave Abnormality-1"):
            restecg = int(1)
        else:
            restecg = int(2)
        
    with col2:
        thalach = int(st.number_input('Maximum Heart Rate achieved',step=1))
        
    with col3:
        exang = str(st.selectbox('Exercise Induced Angina',('Yes-1','No-0')))
        if exang == "Yes-1":
            exang = int(1)
        else:
            exang = int(0)
        
    with col1:
        oldpeak = str(st.number_input('ST depression induced by exercise'))
        oldpeak = float(oldpeak)
        
    with col2:
        slope = int(st.number_input('Slope of the peak exercise ST segment 1 = upsloping 2 = flat 3 = downsloping', min_value=1,max_value=3))
        
    with col3:
        ca = int(st.number_input('Major vessels colored by flourosopy',min_value=0,max_value=3))
    
        
    with col1:
        thal = int(st.number_input('thal: 3 = normal; 6 = fixed defect; 7 = reversable defect',min_value=3,max_value=7,step=3))
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The Person is having heart disease'
        else:
          heart_diagnosis = 'The Person does not have any heart disease'
        
    st.info(heart_diagnosis)