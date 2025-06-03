import streamlit as st
from datetime import datetime
from utils.data_loader import save_intake_data

def show_intake_form():
    st.title("📝 Client Intake Form")
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
                "Business Name": business_name,
                "Contact Name": contact_name,
                "Email": email,
                "Phone": phone,
                "Industry": industry,
                "Number of Users": number_of_users,
                "Domain": domain,
                "Needs": ", ".join(needs),
                "Submitted_At": datetime.utcnow().isoformat()
            }

            st.write("DEBUG: Intake record =", intake_record)
            save_intake_data(intake_record)
            st.success("✅ Client intake form submitted successfully.")

