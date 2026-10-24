import streamlit as st
from datetime import date

st.title("Age calculator")
name = st.text_input("Enter your name")
if name: 
    st.write(f"welcome {name} to Age Calculator")

min_dob = date(1900, 1, 1)
max_dob = date.today()
dob = st.date_input("Enter your dob", value=date(2000, 1, 1), min_value=min_dob, max_value=max_dob)
if dob:
    st.write(f" Your dob is {dob}")

current_date = st.date_input("Enter current date", value=max_dob, min_value=dob, max_value=max_dob)
if current_date:
    st.write(f"current date is {current_date}")

real_days = current_date.day - dob.day
real_years = current_date.year - dob.year
real_months = current_date.month - dob.month
if real_days < 0:
    real_months -= 1
    real_days += 30

if real_months < 0:
    real_years -= 1
    real_months += 12
    
st.write(f" your real age is {real_years} years {real_months} months and {real_days} days")


