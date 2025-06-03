import streamlit as st
from Home import show_home
from IntakeForm import show_intake_form
from ProvisioningDashboard import show_dashboard
from SupportFlow import show_support_flow
from TrainingPortal import show_training_resources

# --- Streamlit App Configuration ---
st.set_page_config(page_title="Nexus One MVP", layout="wide")

# --- Main Navigation ---
st.sidebar.title("📡 Nexus One MVP")
selection = st.sidebar.radio("Navigate", [
    "Home",
    "Client Intake",
    "Provisioning Dashboard",
    "Training & Resources",
    "Support Escalation"
])

# --- Page Routing ---
if selection == "Home":
    show_home()
elif selection == "Client Intake":
    show_intake_form()
elif selection == "Provisioning Dashboard":
    show_dashboard()
elif selection == "Training & Resources":
    show_training_resources()
elif selection == "Support Escalation":
    show_support_flow()
