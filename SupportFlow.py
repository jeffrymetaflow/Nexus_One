import streamlit as st


def show_support_flow():
    st.title("🚨 Support Escalation Simulator")
    st.markdown("""
    This tool simulates how client issues are routed and resolved based on severity and issue type.
    """)

    issue_type = st.selectbox("Select an issue:", [
        "Can't access email",
        "VoIP not ringing",
        "CRM password reset",
        "File sharing permissions",
        "Suspicious activity on device"
    ])

    st.markdown("---")
    st.subheader("📶 Escalation Path")

    if issue_type == "Can't access email":
        path = ["Tier 1: Check credentials", "Tier 2: Reset email account", "Tier 3: Admin review & audit logs"]
    elif issue_type == "VoIP not ringing":
        path = ["Tier 1: Confirm device connectivity", "Tier 2: Reprovision extension", "Tier 3: Network analysis"]
    elif issue_type == "CRM password reset":
        path = ["Tier 1: Use reset link", "Tier 2: Admin reset in CRM", "Tier 3: Escalate to vendor"]
    elif issue_type == "File sharing permissions":
        path = ["Tier 1: Check user group access", "Tier 2: Admin permission update", "Tier 3: Vendor support"]
    else:  # Suspicious activity on device
        path = ["Tier 1: Isolate device", "Tier 2: Run endpoint scan", "Tier 3: Engage MDR team"]

    for step in path:
        st.markdown(f"- {step}")

    st.success("Escalation path displayed. Adjust scenarios to reflect client environment.")
