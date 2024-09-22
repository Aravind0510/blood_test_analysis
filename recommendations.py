def get_health_recommendations(analysis_result):
    recommendations = []

    # Example recommendations based on cholesterol and glucose levels
    cholesterol = analysis_result.get('Cholesterol', 'normal')
    glucose = analysis_result.get('Glucose', 'normal')

    if cholesterol == 'high':
        recommendations.append("Reduce intake of saturated fats and cholesterol-rich foods.")
    
    if glucose == 'high':
        recommendations.append("Control your sugar intake and monitor your blood sugar regularly.")

    return recommendations
