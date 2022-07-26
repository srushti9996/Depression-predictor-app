import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Dell/OneDrive/Desktop/app file/Main Deployment/lr_trained_model.sav', 'rb'))

# Creating a function for Prediction

def Depression_Prediction(input_data):

    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'Not Deprresed'
    
    else:
        return 'Depressed'

def main():
    
    # giving a title
    st.title('Depression Prediction Web App')
    
    # getting the input data from the user
    #gender
    gender_display = ('--- Select ---','Male','Female')
    gender_options = list(range(len(gender_display)))
    gender = st.selectbox("Gender", gender_options, format_func= lambda x: gender_display[x])
   
    #age
    age = st.text_input('age') 

    #Marital Status
    mar_display = ('--- Select ---','No', 'Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options,format_func = lambda x: mar_display[x])

    #education level
    education_level_display = ('--- Select ---','Less Than 9th Grade','9-11th Grade','High School','Some College or AA Degree','College Graduate or Above')
    education_level_options = list(range(len(education_level_display)))
    education_level = st.selectbox("Education Level", education_level_options, format_func = lambda x: education_level_display[x])

    #Household Income
    household_income_display = ('--- Select ---','Below $5K','Below $10K','Below $15K','Below $20K','Below $25K', 'Below $35K', 'Below $45K', 'Below $55K', 'Below $65K', 'Below $75K', '$75K+', 'Over $20K', 'Under $20K', 'Below $100K', '$100K+')
    household_income_options = list(range(len(household_income_display)))
    household_income = st.selectbox("Household Income", household_income_options, format_func = lambda x: household_income_display[x])


    # Trouble Sleeping History
    trouble_sleeping_history_display = ('--- Select ---','No', 'Yes')
    trouble_sleeping_history_options = list(range(len(trouble_sleeping_history_display)))
    trouble_sleeping_history = st.selectbox("Trouble Sleeping History", trouble_sleeping_history_options, format_func = lambda x: trouble_sleeping_history_display[x])
    
    sleep_hours = st.text_input('sleep hours')
    sedentary_time = st.text_input('sedentary time')
    cant_work = st.text_input('cant work')
    limited_work = st.text_input('limited work')
    memory_problems = st.text_input('memory problems')
    prescriptions_count = st.text_input('prescriptions count')

    # code for Prediction
    diagnosis = ''
    
    # Creating a button for Prediction
    
    if st.button('Depression Test Result'):
        diagnosis = Depression_Prediction([gender, age, education_level, household_income, trouble_sleeping_history, sleep_hours, sedentary_time, cant_work, limited_work, memory_problems, prescriptions_count])
     
    st.success(diagnosis)
   
if __name__=='__main__':
    main()
