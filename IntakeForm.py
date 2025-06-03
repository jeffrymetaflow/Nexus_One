import streamlit as st
import pandas as pd
from utils.data_loader import save_intake_data
from email_notifier import send_notification_email, send_thank_you_email

def show_intake_form():
    st.title("📝 Client Intake Form")
    st.markdown("Fill out this form to simulate onboarding a rural business client.")

    with st.form("intake_form"):
        business_name = st.text_input("Business Name")
        contact_name = st.text_input("Contact Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        industry = st.selectbox("Industry", ["Retail", "Healthcare", "Construction", "Agriculture", "Professional Services", "Other"])
        num_users = st.slider("Number of Employees", 1, 20, 5)
        domain = st.text_input("Preferred Email Domain (e.g., sarahautoshop.com)")
        needs = st.multiselect("What services are needed?", ["Email", "VoIP", "CRM", "Security", "File Sharing"])
        submitted = st.form_submit_button("Submit")

    if submitted:
        intake_record = {
            "Business Name": business_name,
            "Contact Name": contact_name,
            "Email": email,
            "Phone": phone,
            "Industry": industry,
            "Number of Users": num_users,
            "Domain": domain,
            "Needs": ", ".join(needs)
        }
        save_intake_data(intake_record)
        send_notification_email(intake_record)
        send_thank_you_email(intake_record)
        st.success(f"Client '{business_name}' submitted successfully!")
        st.json(intake_record)

