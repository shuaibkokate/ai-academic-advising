import streamlit as st
import pandas as pd
from model.risk_predictor import generate_risk_profile
from model.recommender import generate_recommendation

st.title("🎓 AI Academic Advisor")

student_id = st.text_input("Enter your Student ID:")

if student_id:
    student_id = int(student_id)
    attendance_df = pd.read_csv("data/attendance_records.csv")
    grades_df = pd.read_csv("data/grades.csv")

    profile = generate_risk_profile(attendance_df, grades_df)
    student = profile[profile['student_id'] == student_id]

    if not student.empty:
        st.write(f"📊 Attendance: {student.attendance_pct.values[0]:.2f}%")
        st.write(f"📚 GPA: {student.gpa.values[0]:.2f}")
        st.write(f"⚠️ Risk Level: {student.risk_level.values[0]}")
        rec = generate_recommendation(student.risk_level.values[0])
        st.success(f"🎯 Recommendation: {rec}")
    else:
        st.error("Student ID not found.")
