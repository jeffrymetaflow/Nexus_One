import os
from supabase import create_client, Client
from datetime import datetime
import streamlit as st

# Load Supabase credentials from Streamlit secrets
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_intake_data(record):
    # Ensure timestamp is present (already added in IntakeForm.py, but we'll be safe)
    if "submitted_at" not in record:
        record["submitted_at"] = datetime.now().isoformat()

    # DEBUG log
    print("DEBUG: Submitting intake record to Supabase =", record)

    # Submit directly
    data, count = supabase.table("intake_form_submissions").insert(record).execute()

    # Set redirect flag and rerun app to dashboard
    st.session_state["redirect_to_dashboard"] = True
    st.rerun()

    return data

def load_intake_data():
    response = supabase.table("intake_form_submissions").select("*").order("submitted_at", desc=True).execute()
    return response.data

def save_provisioning_status(client_name, status_dict):
    updates = {
        "provisioning_status": status_dict,
        "last_updated": datetime.utcnow().isoformat()
    }
    supabase.table("intake_form_submissions").update(updates).eq("business_name", client_name).execute()

def show_intake_form():
    st.title("📜 Client Intake Form")
    st.markdown("Please fill out the following information to begin onboarding.")

    with st.form("intake_form"):
        business_name = st.text_input("Business Name")
        contact_name = st.text_input("Contact Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        industry = st.text_input("Industry")
        number_of_users = st.number_input("Number of Users", min_value=1, step=1)
        domain = st.text_input("Domain")
        needs = st.multiselect("Select Needed Services", ["Email", "VoIP", "CRM", "Security", "File Sharing"])

        submitted = st.form_submit_button("Submit")

        if submitted:
            intake_record = {
                "business_name": business_name,
                "contact_name": contact_name,
                "email": email,
                "phone": phone,
                "industry": industry,
                "number_of_users": number_of_users,
                "domain": domain,
                "needs": ", ".join(needs),
                "submitted_at": datetime.utcnow().isoformat()
            }

            st.write("DEBUG: Intake record =", intake_record)
            try:
                save_intake_data(intake_record)
                st.success("✅ Client intake form submitted successfully.")
            except Exception as e:
                st.error(f"❌ Failed to submit intake form: {e}")


