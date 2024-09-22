# Health Report Analysis API

## Overview
This project implements a Health Report Analysis API using Flask, allowing users to upload their blood test reports in PDF format. The API processes the reports, analyzes the data, retrieves relevant health articles, and sends personalized health recommendations via email.

## Features
- **API Functionality**: Securely handles incoming PDF uploads and email communications.
- **Data Analysis**: Extracts and analyzes data from blood test reports.
- **Article Retrieval**: Searches for articles relevant to the user's health profile.
- **Health Recommendations**: Sends tailored recommendations and article links via email.

## Approach and Methodology
1. **Framework Selection**: Chose Flask for building the API due to its simplicity and flexibility.
2. **PDF Analysis**: Utilized AI models and libraries to extract data from the uploaded PDF reports.
3. **Web Search Integration**: Implemented a search mechanism to find health articles based on the analysis results.
4. **Email Functionality**: Integrated SMTP to send emails with recommendations and articles.
5. **Security**: Employed authentication mechanisms to secure the API endpoints.

## How I Approached the Task
1. **Understanding Requirements**  I reviewed the project requirements to identify the main functionalities needed, including PDF analysis, article retrieval, and email notifications.
2. **Technology Stack**: Chose Flask for the backend due to its lightweight nature and ease of use for creating APIs. I also integrated libraries for PDF processing and email functionality.
3. **Designing the API**: I structured the API to handle file uploads and user requests securely. Implemented endpoint for processing blood test reports.
4. **Data Extraction**: Developed an algorithm to extract and analyze data from the uploaded PDF files, ensuring accurate interpretation of health metrics.
5. **Web Search Integration**: Implemented a search function to retrieve health-related articles based on the analysis results.
6. **Email Notifications**: Set up SMTP email functionality to send personalized health recommendations and article links to the user.
7. **Testing and Documentation**: Thoroughly tested the API for various use cases and documented the setup and usage instructions for ease of understanding.

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd health-report-analysis

2.Set up your email configuration in utils.py:
- Update the send_email function with your SMTP server details.

3.Create an uploads directory to store uploaded PDF files:
  ```bash
    mkdir uploads
```

4.Run the application:

```bash
  python app.py
```

5.Access the API at http://127.0.0.1:5000/.

## API Endpoints
- POST /process: Upload a blood test report.
     - Body:
            - pdf_file: PDF file of the blood test report.
            - email: User's email address.

## Output
- A confirmation message will be sent to the user's email with analysis results and health recommendations.

## Acknowledgements
- Thanks to the open-source community for the libraries and frameworks that made this project possible.


### Final Steps
1. Make sure to replace `<repository-url>` with your actual Git repository URL.
2. Test your application thoroughly to ensure everything works as expected before submission.
3. Include any additional documentation relevant to specific parts of your code or any setup instructions unique to your project.

- Feel free to adjust any sections according to your project's specifics! If you have further requirements or questions, just let me know!
