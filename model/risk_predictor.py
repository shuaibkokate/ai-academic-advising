
import pandas as pd

def calculate_risk(attendance_pct, gpa):
    if attendance_pct < 75 or gpa < 2.5:
        return 'High Risk'
    elif attendance_pct < 85 or gpa < 3.0:
        return 'Moderate Risk'
    else:
        return 'Low Risk'

def generate_risk_profile(attendance_df, grades_df):
    attendance_df['attendance_pct'] = (attendance_df['attended_classes'] / attendance_df['total_classes']) * 100
    grades_df['gpa'] = grades_df[['subject_1', 'subject_2', 'subject_3']].mean(axis=1)
    merged = pd.merge(attendance_df, grades_df, on='student_id')
    merged['risk_level'] = merged.apply(lambda row: calculate_risk(row['attendance_pct'], row['gpa']), axis=1)
    return merged[['student_id', 'attendance_pct', 'gpa', 'risk_level']]
