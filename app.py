import streamlit as st 
import pandas as pd
import joblib 

model=joblib.load("salary_model.pkl")
columns=joblib.load("columns.pkl")

st.title("salary prediction")
st.write("enter the details to predict salary")


experience = st.slider("Years of Experience", 0, 15, 1)
education = st.selectbox("Education Level", [0, 1, 2, 3])
company_size = st.selectbox("Company Size", [1, 2, 3, 4])

country = st.selectbox("Country", [
    "Brazil", "Canada", "France", "Germany", "India",
    "Japan", "Singapore", "UK", "USA"
])
skills = st.multiselect("Select Skills", [
    "Python", "Java", "JavaScript", "C++", "C#", "Go",
    "PHP", "Ruby", "Rust", "Swift",
    "Django", "Flask", "React", "Angular", "Vue",
    "Spring", "Laravel", "Express", "ASP.NET", "Ruby on Rails"
])

if st.button("Predict Salary"):
    new_data=pd.DataFrame(columns=columns)
    new_data.loc[0]=0
    new_data['experience']=experience
    new_data['education']=education
    new_data['company_size']=company_size

    country_col= f"country_{country}"
    if country_col in new_data.columns:
        new_data[country_col]=1
    for skill in skills:
        if skill in new_data.columns:
            new_data[skill]=1
    prediction=model.predict(new_data)[0]
    st.success(f"Predicted Salary: ${prediction:,.2f}") 