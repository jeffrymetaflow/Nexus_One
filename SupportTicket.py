import streamlit as st
import datetime
from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def show_support_ticket_form():
    st.title("📩 Submit a Support Ticket")
    st.markdown("Need help? Fill out the form below and our support team will get back to you shortly.")

    with st.form("support_ticket_form"):
        email = st.text_input("Your Email")
        issue_type = st.selectbox("Issue Type", ["Technical", "Billing", "Account Access", "Other"])
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        message = st.text_area("Describe the issue")
        submitted = st.form_submit_button("Submit Ticket")

    if submitted:
        ticket = {
            "email": email,
            "issue_type": issue_type,
            "priority": priority,
            "message": message,
            "status": "Open",
            "submitted_at": datetime.datetime.utcnow().isoformat()
        }
        response = supabase.table("support_tickets").insert(ticket).execute()
        if response.status_code == 201:
            st.success("Your support ticket has been submitted. We'll be in touch soon!")
        else:
            st.error("There was an error submitting your ticket. Please try again.")
