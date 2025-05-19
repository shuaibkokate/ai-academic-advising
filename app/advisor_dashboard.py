import streamlit as st
import pandas as pd
import sys
import os

# 🔧 Ensure correct path for importing model modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.risk_predictor import generate_risk_profile

st.title("📊 Advisor Dashboard")

attendance_df = pd.read_csv("data/attendance_records.csv")
grades_df = pd.read_csv("data/grades.csv")
profile = generate_risk_profile(attendance_df, grades_df)

st.subheader("📋 Student Risk Profiles")
st.dataframe(profile)