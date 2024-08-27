import os
import streamlit as st
from dotenv import load_dotenv
from openai_integration import OpenAIClient
from resume_processing import process_resumes, find_suitable_candidates

# Load environment variables from .env file
load_dotenv()

# Streamlit app layout
st.title("Resume Analyzer")
st.write("Upload resumes and find suitable candidates based on the experience you're looking for.")

# Textbox for updating OpenAI API key
api_key = st.text_input("Enter your OpenAI API key", type="password")
if not api_key:
    api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    # Initialize the OpenAI client
    client = OpenAIClient(api_key)

    # Textbox for entering the experience query
    experience_query = st.text_input("Enter the experience you're looking for")

    # Upload resumes button
    uploaded_files = st.file_uploader("Choose resume files...", type=["pdf", "docx"], accept_multiple_files=True)

    if uploaded_files and experience_query:
        st.write("Processing resumes...")

        # Process the resumes and find suitable candidates
        try:
            candidates = process_resumes(uploaded_files)
            suitable_candidates = find_suitable_candidates(client, candidates, experience_query)

            if suitable_candidates:
                st.write("Suitable Candidates:")
                for candidate in suitable_candidates:
                    st.markdown(f"**Name:** {candidate['name']}")
                    st.markdown(f"**Contact Information:** {candidate['contact_info']}")

                    # Use an expander to display the full resume content
                    with st.expander(f"Show full resume for {candidate['name']}"):
                        st.text_area("Resume", candidate['text'], height=300)
            else:
                st.write("No suitable candidates found.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
else:
    st.error("Please provide a valid OpenAI API key.")
