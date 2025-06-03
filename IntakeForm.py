import streamlit as st
from datetime import datetime
from utils.data_loader import save_intake_data
from ProvisioningDashboard import show_dashboard

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

                # Redirect to provisioning dashboard
                st.markdown("---")
                st.markdown("### Redirecting to Provisioning Dashboard...")
                show_dashboard()
            except Exception as e:
                st.error(f"❌ Failed to submit intake form: {e}")

