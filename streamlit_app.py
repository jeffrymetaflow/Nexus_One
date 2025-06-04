import streamlit as st
from Home import show_home
from IntakeForm import show_intake_form
from ProvisioningDashboard import show_dashboard
from SupportFlow import show_support_flow
from TrainingPortal import show_training_resources
from SupportTicket import show_support_ticket_form
from SupportTicketDashboard import show_support_dashboard

# --- Streamlit App Configuration ---
st.set_page_config(page_title="Nexus One MVP", layout="wide")

# --- Sidebar Header ---
st.sidebar.title("📡 Nexus One MVP")

# --- Redirect logic ---
if st.session_state.get("redirect_to_dashboard"):
    st.session_state["redirect_to_dashboard"] = False  # Reset flag
    selection = "Provisioning Dashboard"
else:
    selection = st.sidebar.radio("Navigate", [
        "Home",
        "Client Intake",
        "Provisioning Dashboard",
        "Training & Resources",
        "Support Escalation",
        "Submit Support Ticket",
        "Support Ticket Dashboard"
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
elif selection == "Submit Support Ticket":
    show_support_ticket_form()
elif selection == "Support Ticket Dashboard":
    show_support_dashboard()
