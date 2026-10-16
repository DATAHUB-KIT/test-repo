import streamlit as st
from google import genai

# Streamlit page configuration
st.set_page_config(
    page_title="LLM Prompt and Response App",
    page_icon="🤖",
    layout="centered"
)

# Read API key from Streamlit Cloud Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except (KeyError, FileNotFoundError):
    API_KEY = ""

# Validate API key
if not API_KEY:
    st.error(
        "Gemini API key is missing. "
        "Please configure GEMINI_API_KEY in Streamlit Secrets."
    )
    st.stop()

# Create Gemini client only once
client = genai.Client(api_key=API_KEY)

# Model name
MODEL = "gemini-3.1-flash-lite"

# Application UI
st.title("LLM Prompt and Response App")
st.write("Enter a prompt and generate a response using Google Gemini.")

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Example: Explain Generative AI in simple words."
)

# Generate response
if st.button("Generate Response", type="primary"):

    if prompt.strip():

        try:
            with st.spinner("Gemini is generating a response..."):

                response = client.models.generate_content(
                    model=MODEL,
                    contents=prompt.strip()
                )

            st.subheader("LLM Response")

            if response.text:
                st.write(response.text)
            else:
                st.warning("Gemini returned an empty response.")

        except Exception as e:
            st.error(f"Unable to generate response: {e}")

    else:
        st.warning("Please enter a prompt.")
