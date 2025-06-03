import streamlit as st


def show_training_resources():
    st.title("📚 Training & Support Resources")
    st.markdown("""
    Below are training resources, SOPs, and quick start guides provided to help onboard
    clients and ensure smooth operation of deployed solutions.
    """)

    st.subheader("🔗 External Guides & Portals")
    st.markdown("- [Nexus One Client Portal (Notion)](https://www.notion.so/)")
    st.markdown("- [VoIP Quick Start Guide (PDF)](https://example.com/voip-guide.pdf)")
    st.markdown("- [CRM Cheat Sheet (PDF)](https://example.com/crm-cheat-sheet.pdf)")

    st.subheader("📄 Sample SOPs")
    st.markdown("- **Logging into Email for the First Time**")
    st.markdown("- **CRM Data Entry Process**")
    st.markdown("- **Resetting VoIP PINs**")

    st.info("Tip: You can replace these with actual live documentation or host PDFs in the assets folder.")
