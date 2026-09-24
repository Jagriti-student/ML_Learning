import streamlit as slt
import pandas as pd
import joblib

model=joblib.load("Logistic_heart.pkl")
scaler=joblib.load("scaler.pkl")
expected_columns=joblib.load("columns.pkl")

slt.title("Heart Stroke prediction by Jagriti ")
slt.markdown("Provide the following details")

age=slt.slider("Age",18,100,40)
sex=slt.selectbox("SEX",['M','F'])
chest_pain=slt.selectbox("Chest Pain Type",["ATA","NAP","TA","ASY"])
resting_bp=slt.number_input("Resting Bood Pressure (mm Hg)",80,200,120)
Cholesterol=slt.number_input("Cholesterol (mg/dl)",100,600,200)
fasting_bs=slt.selectbox("Fasting Blood Sugar > 120 mg/dl",[0,1])
resting_ecg=slt.selectbox("Resting ECG",["Normal","ST","LVH"])
max_hr=slt.slider("Max Heart Rate",60,220,150)
exercise_angina=slt.selectbox("Exercide-Induced Angina",["Y","N"])
oldpeak=slt.slider("OldPeak (ST Depression)",0.0,6.0,1.0)
st_slope=slt.selectbox("ST Slope",["Up","Flat","Down"])



if slt.button("Predict"):
    raw_input={
        'Age':age,
        'RestingBP':resting_bp,
        'Cholesterol':Cholesterol,
        'FastingBS':fasting_bs,
        'MaxHR':max_hr,
        'Oldpeak':oldpeak,
        'Sex_'+sex: 1,
        'ChestPainType_'+chest_pain: 1,
        'RestingECG_'+resting_ecg:1,
        'ExcerciseAngina_'+exercise_angina:1,
        'ST_Slope_'+st_slope:1
    }


    input_df=pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col]=0

    input_df=input_df[expected_columns]

    scaled_input=scaler.transform(input_df)

    prediction=model.predict(scaled_input)[0]
    if prediction==1:
        slt.error("High Risk of Heart Disease")
    else:
        slt.success("Low Risk of Heart Disease")
