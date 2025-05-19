def generate_recommendation(risk_level):
    if risk_level == 'High Risk':
        return "Meet your advisor immediately. Focus on improving attendance and seek tutoring."
    elif risk_level == 'Moderate Risk':
        return "Improve consistency. Attend all classes and follow up on assignments."
    else:
        return "Keep up the good work. Continue attending and maintaining performance."