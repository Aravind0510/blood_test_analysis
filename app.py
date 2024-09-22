from flask import Flask, request, jsonify, render_template
from analysis import analyze_pdf
from search import search_articles
from recommendations import get_health_recommendations
from utils import send_email, save_pdf
import os

app = Flask(__name__)

# API Key for simple authentication (use something more secure for production)
API_KEY = os.getenv('API_KEY', 'Your key')

# Home route to render the upload form
@app.route('/')
def home():
    return render_template('index.html')

# Route for the health report processing
@app.route('/process', methods=['POST'])
def process_report():
    if 'pdf' not in request.files or 'email' not in request.form:
        return jsonify({"error": "Invalid input"}), 400
    
    pdf_file = request.files['pdf']
    email = request.form['email']

    # Save and process PDF
    pdf_path = save_pdf(pdf_file)
    analysis_result = analyze_pdf(pdf_path)

    # Search for relevant health articles
    articles = search_articles(analysis_result)

    # Generate health recommendations
    recommendations = get_health_recommendations(analysis_result)

    # Compile the email content
    email_content = f"""
    Blood Test Analysis Summary:\n{analysis_result}
    \nHealth Recommendations:\n{recommendations}
    \nRelated Articles:\n{articles}
    """

    # Send the email
    send_email(email, "Your Health Report Analysis", email_content)

    return jsonify({
        "message": "Report processed successfully. Recommendations sent to email.",
        "analysis": analysis_result,
        "recommendations": recommendations,
        "articles": articles
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
