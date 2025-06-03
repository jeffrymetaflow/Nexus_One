import streamlit as st

def show_home():
    st.image("assets/nexus_one_logo.png", width=200)
    st.title("🚀 Nexus One MVP Demo")
    st.markdown("""
    Welcome to the Nexus One Prototype Environment for rural business IT modernization.

    This demo simulates the full lifecycle from client intake through provisioning, training,
    and support—all tailored for businesses with under 20 employees in underserved regions.

    **Modules Included:**
    - 📝 Client Intake & Needs Assessment
    - 🔧 Simulated Provisioning Dashboard
    - 📚 Training & Support Resources
    - 🚨 Support Escalation Simulator

    Use the sidebar to navigate between each module.
    """)

    st.info("Use the 'Client Intake' tab to start a demo session for a fictional business.")
