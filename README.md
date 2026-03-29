# simple-Q-A
Simple AI Q&A Assistant

This is a simple Artificial Intelligence Question & Answer web application built using Python, Streamlit, and the Google Gemini API. It was created as part of a technical assessment.

Features

Clean, interactive chat UI using Streamlit.

Fast and accurate responses powered by the gemini-2.5-flash model.

Chat history memory within a single session.

Robust error handling for API failures.

💻 How to Run Locally

Prerequisites

Python 3.8 or higher installed.

A Google Gemini API Key. You can get a free one from Google AI Studio.

Installation Steps

Clone the repository (or create a folder with the files):
Ensure you have app.py and requirements.txt in your project folder.

Create a virtual environment (Recommended):

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Set up your API Key:
Create a folder named .streamlit in your project root, and inside it, create a file named secrets.toml. Add your API key like this:

GEMINI_API_KEY = "your_actual_api_key_here"


(Note: Never commit secrets.toml to a public GitHub repository!)

Run the application:

streamlit run app.py


The app will open automatically in your web browser at http://localhost:8501.

🚀 How to Deploy (Streamlit Community Cloud)

Deploying this app is completely free and takes about 2 minutes using Streamlit Community Cloud.

Upload to GitHub:

Create a new public or private repository on GitHub.

Upload app.py and requirements.txt to this repository.

Connect to Streamlit Cloud:

Go to share.streamlit.io and log in with your GitHub account.

Click "New app".

Select the repository, branch (usually main), and the main file path (app.py).

Add your API Key as a Secret:

Before clicking deploy, click on "Advanced settings...".

In the "Secrets" text box, enter your API key just like you did locally:

GEMINI_API_KEY = "your_actual_api_key_here"


Click Save.

Deploy:

Click "Deploy!".

Wait a minute or two for the server to install the requirements and launch your app.

Once deployed, you will get a public URL (e.g., https://your-app-name.streamlit.app/) that you can submit to your evaluators!
