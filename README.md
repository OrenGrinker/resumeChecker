# Resume Analyzer

Resume Analyzer is a Streamlit application that allows users to upload resumes and find suitable candidates based on specific experience queries. The application uses the OpenAI GPT-4o model to analyze the resumes and determine if the candidates match the provided criteria.

## Features

- Upload multiple resume files in PDF or DOCX format.
- Enter a specific experience query to find matching candidates.
- View suitable candidates with a summary of their relevant experience and contact information.
- Display the full resume content within the application.

## Requirements

- Python 3.7+
- Streamlit
- OpenAI Python SDK
- PyPDF2
- python-docx
- python-dotenv

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/orengrinker/resumeChecker.git
cd resumeChecker
```
### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Up Environment Variables
Create a .env file in the root directory of the project and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
### 5. Run the Application
```bash
streamlit run app.py
```

### Usage

Enter your OpenAI API key when prompted or ensure it is set in the .env file.
Enter the experience you are looking for in the textbox.
Upload the resume files you want to analyze (PDF or DOCX format).
The application will process the resumes and display the suitable candidates based on the experience query.
### License
```bash
This project is licensed under the MIT License. See the LICENSE file for details.
```
### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

