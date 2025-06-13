# app.py: Streamlit app for Breakup Recovery Agent

import streamlit as st
import re
from PIL import Image
import io
from agents import TeamLeader

# Streamlit page configuration
st.set_page_config(page_title="Breakup Recovery Agent", layout="wide")

# Simulated Gemini API (placeholder)
class GeminiAPI:
    def analyze_image(self, image_data: bytes) -> str:
        return "Detected emotional tone: Sadness"

    def generate_response(self, prompt: str) -> str:
        return f"AI Response to '{prompt}': I understand you're feeling this way. Let's work through it together."

# Input validation
def validate_input(user_input: str) -> bool:
    if not user_input or len(user_input.strip()) < 5:
        st.error("Input must be at least 5 characters long.")
        return False
    if not re.match(r'^[a-zA-Z0-9\s.,!?]*$', user_input):
        st.error("Input contains invalid characters. Use letters, numbers, spaces, and basic punctuation only.")
        return False
    return True

# Main Streamlit app
def main():
    st.title("💔 Breakup Recovery Agent")
    st.markdown("A supportive AI companion to help you heal emotionally after a breakup.")

    # Sidebar for API key (placeholder for real integration)
    st.sidebar.header("Configuration")
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password", value="placeholder-key")
    if api_key == "placeholder-key":
        st.sidebar.warning("Please replace with a real Gemini API key for full functionality.")

    # User input
    st.header("Tell Us How You're Feeling")
    user_input = st.text_area("Describe your emotions or situation:", height=150)
    screenshot = st.file_uploader("Upload a chat screenshot (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

    # Process input on button click
    if st.button("Get Recovery Plan"):
        if not validate_input(user_input):
            return

        # Process screenshot if uploaded
        image_data = None
        if screenshot:
            try:
                image_data = screenshot.read()
                Image.open(io.BytesIO(image_data))  # Verify it's a valid image
            except Exception as e:
                st.error(f"Invalid image file: {str(e)}")
                return

        # Coordinate agents
        with st.spinner("Generating your recovery plan..."):
            try:
                team_leader = TeamLeader()
                response = team_leader.coordinate(user_input, image_data)
            except Exception as e:
                st.error(f"Error generating recovery plan: {str(e)}")
                return

        # Display results
        st.header("Recovery Plan")
        st.subheader("Image Analysis")
        st.write(response["image_analysis"] or "No image provided")

        st.subheader("Empathetic Support")
        st.write(response["empathetic_response"])

        st.subheader("Daily Routine Suggestion")
        st.write(response["daily_routine"])

        st.subheader("Emotional Message (Unsent)")
        st.write(response["emotional_message"])

        st.subheader("Summary")
        st.write(response["summary"])

if __name__ == "__main__":
    main()
