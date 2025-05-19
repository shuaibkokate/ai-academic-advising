import pandas as pd
from model.risk_predictor import generate_risk_profile

attendance_df = pd.read_csv("data/attendance_records.csv")
grades_df = pd.read_csv("data/grades.csv")

risk_profile = generate_risk_profile(attendance_df, grades_df)
print(risk_profile.sort_values(by='risk_level'))
