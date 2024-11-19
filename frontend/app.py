import streamlit as st
import requests
import os

# Backend URL
backend_url = "https://cold-email-52xl.onrender.com"

st.title("EmailGenie: AI-Powered Cold Email Generator")

# Profile Form
with st.form("profile_form"):
    name = st.text_input("Your Name")
    industry = st.text_input("Industry")
    audience = st.text_input("Target Audience")
    background = st.text_area("Background Information")
    submitted = st.form_submit_button("Save Profile")

# Save profile data in session state
if submitted:
    profile = {"name": name, "industry": industry, "audience": audience, "background": background}
    st.session_state["profile"] = profile
    st.success("Profile saved!")

# Generate Email Section
if "profile" in st.session_state:
    st.header("Generate Your Email")
    
    # Template Selection
    templates = ["Sales Pitch", "Job Application", "Service Offer"]
    template_choice = st.selectbox("Choose a Template", templates)

    # Dynamic Placeholders and Custom Message
    placeholders = {
        "Name": st.session_state["profile"]["name"],
        "Industry": st.session_state["profile"]["industry"]
    }
    custom_message = st.text_area("Custom Message")

    # Generate Email Button
    if st.button("Generate Email"):
        try:
            response = requests.post(f"{backend_url}/generate-email/", json={
                "profile": st.session_state["profile"],
                "template": template_choice,
                "placeholders": placeholders,
                "custom_message": custom_message
            })
            if response.status_code == 200:
                email = response.json()["email"]
                st.session_state["generated_email"] = email  # Store generated email in session state
                st.success("Email generated successfully!")
                st.text_area("Generated Email", email, height=300)
            else:
                st.error(f"Failed to generate email: {response.text}")
        except Exception as e:
            st.error(f"Error connecting to backend: {str(e)}")