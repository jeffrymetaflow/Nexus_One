import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_loader import load_intake_data, save_provisioning_status


# Simulated provisioning statuses
def simulate_status(row):
    services = row.get("Needs", "").split(", ")
    return {service: False for service in services}  # Default unchecked

def show_dashboard():
    st.title("🔧 Provisioning Dashboard")
    st.markdown("This dashboard shows the provisioning status for each submitted client.")

    data = load_intake_data()

    if not isinstance(data, pd.DataFrame) or data.empty:
        st.warning("No client submissions found. Please fill out the intake form first.")
        return

    selected = st.selectbox("Select a client:", options=data["Business Name"])
    row = data[data["Business Name"] == selected].iloc[0]
    statuses = simulate_status(row)

    st.subheader(f"Provisioning Tracker for {selected}")
    st.write(f"**Domain:** {row['Domain']}  |  **Industry:** {row['Industry']}  |  **Users:** {row['Number of Users']}")

    updated_status = {}
    with st.form("provisioning_form"):
        for service in statuses:
            updated_status[service] = st.checkbox(f"{service}", value=statuses[service])
        submitted = st.form_submit_button("✅ Save Provisioning Status")
        if submitted:
            save_provisioning_status(selected, updated_status)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.success(f"Provisioning status updated successfully at {timestamp}.")
            st.markdown(f"_Last updated: {timestamp}_")

    # Send Email Confirmation Button
    st.markdown("### 📧 Email Client Provisioning Summary")
    if st.button("Send Email to Client"):
        client_email = f"contact@{row['Domain']}"
        send_provisioning_email(
            to=client_email,
            client=row['Business Name'],
            contact=row['Contact Name'],
            statuses=updated_status
        )
        st.success(f"Provisioning summary sent to {client_email}.")

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

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_provisioning_email(to, client, contact, statuses):
    status_html = "".join(
        f"<li><strong>{service}:</strong> {'✅ Completed' if done else '❌ Pending'}</li>"
        for service, done in statuses.items()
    )

    html_content = f"""
    <p>Hello {contact},</p>
    <p>Here is the current provisioning summary for your business <strong>{client}</strong>:</p>
    <ul>{status_html}</ul>
    <p>Thank you,<br/>Nexus One Support Team</p>
    """

    message = Mail(
        from_email="noreply@nexusonetechnologies.com",
        to_emails=to,
        subject=f"Provisioning Summary for {client}",
        html_content=html_content
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(f"Email sent to {to}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email: {e}")
