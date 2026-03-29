import streamlit as st
import google.generativeai as genai
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Q&A Assistant",
    page_icon="🤖",
    layout="centered"
)

# --- HEADER ---
st.title("🤖 Simple AI Q&A Assistant")
st.markdown("Ask any question and get an AI-generated answer using the Gemini API.")

# --- API KEY CONFIGURATION ---
# The app tries to get the API key from Streamlit secrets (for deployment) 
# or from local environment variables.
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ Gemini API Key is missing. Please add it to your environment variables or Streamlit secrets.")
    st.stop() # Stop execution if there's no API key

# Initialize the Gemini client
genai.configure(api_key=api_key)

# We use the gemini-2.5-flash model as it is fast and excellent for general Q&A
model = genai.GenerativeModel('gemini-2.5-flash')

# --- SESSION STATE INITIALIZATION ---
# Session state is used to remember the chat history across reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- DISPLAY CHAT HISTORY ---
# Render all previous messages in the chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- USER INPUT & AI RESPONSE ---
# st.chat_input provides a clean text box at the bottom of the screen
if prompt := st.chat_input("Ask me a question..."):
    
    # 1. Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to session state history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 2. Generate and Display AI Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty() # Placeholder for streaming or loading text
        message_placeholder.markdown("Generating response... ⏳")
        
        try:
            # Call the Gemini API
            response = model.generate_content(prompt)
            
            # Display the final response
            message_placeholder.markdown(response.text)
            
            # Add AI response to session state history
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            # Error handling is crucial for a production-grade assessment
            error_msg = f"An error occurred: {str(e)}"
            message_placeholder.error(error_msg)