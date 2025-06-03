import streamlit as st
import pandas as pd
from utils.data_loader import load_intake_data

# Simulated provisioning statuses
def simulate_status(row):
    services = row.get("Needs", "").split(", ")
    provision_map = {
        "Email": "✅ Configured",
        "VoIP": "✅ Extension Created",
        "CRM": "✅ Pipeline Set",
        "Security": "✅ Agent Deployed",
        "File Sharing": "✅ Folder Shared"
    }
    return {service: provision_map.get(service, "❌ Not Available") for service in services}

def show_dashboard():
    st.title("🔧 Provisioning Dashboard")
    st.markdown("This dashboard shows the provisioning status for each submitted client.")

    data = load_intake_data()

    if data.empty:
        st.warning("No client submissions found. Please fill out the intake form first.")
        return

    selected = st.selectbox("Select a client:", options=data["Business Name"])
    row = data[data["Business Name"] == selected].iloc[0]
    statuses = simulate_status(row)

    st.subheader(f"Provisioning Summary for {selected}")
    st.write(f"**Domain:** {row['Domain']}  |  **Industry:** {row['Industry']}  |  **Users:** {row['Number of Users']}")

    status_df = pd.DataFrame(list(statuses.items()), columns=["Service", "Status"])
    st.table(status_df)

    st.markdown("---")
    st.markdown("**Sample Email Signature:**")
    st.code(f"{row['Contact Name']}\n{row['Business Name']}\ncontact@{row['Domain']}", language='text')

    st.markdown("**CRM Pipeline Preview:**")
    st.markdown("- Lead In → Qualification → Proposal → Closed Won/Lost")

    st.markdown("**IVR Call Flow (Sample):**")
    st.markdown("""
    - Press 1 for Service
    - Press 2 for Sales
    - Press 3 for Location & Hours
    """)
