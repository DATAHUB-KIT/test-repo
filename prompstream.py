
import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env
#load_dotenv()

# Read API key securely
#api_key = os.getenv("GEMINI_API_KEY")

#if not api_key:
#    raise ValueError(
#        "GEMINI_API_KEY is missing. Check your .env file."
 #   )


try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    API_KEY = ""

if not API_KEY:
    st.error("Gemini API key not found. Add GEMINI_API_KEY to .streamlit/secrets.toml locally or Streamlit Cloud Secrets.")
    st.stop()

client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.1-flash-lite"




# Create Gemini client
client = genai.Client(api_key=api_key)


st.title("LLM Prompt and Response App")


# Get user prompt
prompt = st.text_area("Enter your prompt:")

# Generate response
if st.button("Generate Response"):

    if prompt.strip():

        with st.spinner("LLM is generating response..."):

            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt
            )

        st.subheader("LLM Response")
        st.write(response.text)

    else:
        st.warning("Please enter a prompt.")
