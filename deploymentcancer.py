import streamlit as st
import requests
import pandas as pd
from streamlit_option_menu import option_menu
import streamlit_lottie as st_lottie
import joblib
import numpy as np
import PIL as image
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

st.set_page_config(
    page_title='Breast Cancer Survival Prediction',
    initial_sidebar_state='collapsed'
)

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

model=joblib.load(open("Survivalprediction",'rb')) # Ensure the correct file name

print(type(model))

with st.sidebar:
    choose = option_menu(None, ["Home", "About", "Contact"],
                         icons=['house', 'book', 'person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
                             "container": {"padding": "5!important", "background-color": "#fafafa"},
                             "icon": {"color": '#E0E0EF', "font-size": "25px"},
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                             "nav-link-selected": {"background-color": "#02ab21"},
                         }
                         )

if choose == 'Home':
    st.write('# Breast Cancer Survival Prediction')
    st.write('---')
    st.subheader('Enter your details to predict breast cancer survival')
    # User input
    age_at_diagnosis = st.text_input('Age at Diagnosis')
    chemotherapy = st.text_input('Chemotherapy')
    cohort = st.text_input('Cohort')
    neoplasm_histologic_grade = st.text_input('Neoplasm Histologic Grade')
    hormone_therapy = st.text_input('Hormone Therapy')
    lymph_nodes_examined_positive = st.text_input('Lymph Nodes Examined Positive')
    mutation_count = st.text_input('Mutation Count')
    nottingham_prognostic_index = st.text_input('Nottingham Prognostic Index')
    overall_survival_months = st.text_input('Overall Survival Months')
    radio_therapy = st.text_input('Radio Therapy')
    tumor_size = st.text_input('Tumor Size')
    tumor_stage = st.text_input('Tumor Stage')
    type_of_breast_surgery = st.text_input('Type of Breast Surgery')
    cancer_type = st.text_input('Cancer Type')
    cancer_type_detailed = st.text_input('Cancer Type Detailed')
    primary_tumor_laterality = st.text_input('Primary Tumor Laterality')

    # Create DataFrame for prediction
    df = pd.DataFrame({
        'age_at_diagnosis': [age_at_diagnosis],
        'chemotherapy': [chemotherapy],
        'cohort': [cohort],
        'neoplasm_histologic_grade': [neoplasm_histologic_grade],
        'hormone_therapy': [hormone_therapy],
        'lymph_nodes_examined_positive': [lymph_nodes_examined_positive],
        'mutation_count': [mutation_count],
        'nottingham_prognostic_index': [nottingham_prognostic_index],
        'overall_survival_months': [overall_survival_months],
        'radio_therapy': [radio_therapy],
        'tumor_size': [tumor_size],
        'tumor_stage': [tumor_stage],
        'type_of_breast_surgery': [type_of_breast_surgery],
        'cancer_type': [cancer_type],
        'cancer_type_detailed': [cancer_type_detailed],
        'primary_tumor_laterality': [primary_tumor_laterality]
    })

    if st.button('Predict'):
        result = model.predict(df)
        if result == 0:
            st.warning("Predicted cancer survival: Low")
            st.write("This indicates a low cancer survival rate.")
        elif result == 1:
            st.success("Predicted cancer survival: High")
            st.write("This indicates a high cancer survival rate.")
            st.balloons()
        

elif choose == 'About':
    st.write('# About Page')
    st.write('---')
    st.write("🎯💡 Welcome to Breast Cancer Survival Prediction! We specialize in providing advanced survival rate classification solutions that help doctors understand their patients' survival rates better. Our data-driven approach combines analytics and machine learning to create customized survival prediction models tailored to your needs. Contact us today to learn more. 📞📧")

elif choose == "Contact":
    st.write('# Contact Us')
    st.write('---')
    with st.form(key='contact_form', clear_on_submit=True):
        st.write('## Please help us improve!')
        name = st.text_input('Please Enter Your Name')
        email = st.text_input('Please Enter Email')
        message = st.text_area('Please Enter Your Message')
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for contacting us. We will respond to your questions or inquiries as soon as possible!')

# Load the data for additional usage if necessary
try:
    data = pd.read_csv('METABRIC_RNA_Mutation.csv')
    st.write('### Data Preview')
    st.dataframe(data.head())
except FileNotFoundError:
    st.write("Data file not found.")
