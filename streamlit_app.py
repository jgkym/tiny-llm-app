import os
import streamlit as st
import requests

# Use environment variable API_URL or default to local host if not set.
API_URL = os.environ.get("API_URL", "http://api:8000")

# Specify the FastAPI endpoint URL (make sure FastAPI is running)
endpoint = f"{API_URL}/generate"

# Set the title of the Streamlit app
st.title("Tiny LLM Demo")

# Create an input field for the prompt
user_input = st.text_input("Enter your prompt:")

# When the user clicks the "Generate" button...
if st.button("Generate"):
    if not user_input.strip():
        st.error("Please enter a valid prompt!")
    else:
        # Prepare the payload for the API request
        payload = {"prompt": user_input}

        # Display a spinner while waiting for the API response
        with st.spinner("Generating response..."):
            try:
                response = requests.post(endpoint, json=payload)
                response.raise_for_status()  # Raise an error for bad responses
                result = response.json()

                # Display the generated text returned from the API
                st.success("Response received!")
                st.text_area("LLM Output", result.get("response", "Nope"), height=150)
            except requests.RequestException as e:
                st.error(f"Error: {e}")
