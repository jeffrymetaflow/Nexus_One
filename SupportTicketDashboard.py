import streamlit as st
import pandas as pd
from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def show_support_dashboard():
    st.title("🛠️ Support Ticket Dashboard")
    st.markdown("View, filter, and manage all submitted support tickets.")

    # Fetch all tickets
    response = supabase.table("support_tickets").select("*").execute()
    tickets = response.data if response.data else []

    if not tickets:
        st.info("No support tickets found.")
        return

    df = pd.DataFrame(tickets)
    df = df.sort_values(by="submitted_at", ascending=False)

    # Filtering options
    status_filter = st.selectbox("Filter by Status", ["All", "Open", "Closed", "In Progress"])
    if status_filter != "All":
        df = df[df["status"] == status_filter]

    st.dataframe(df, use_container_width=True)

    # Edit a ticket
    st.subheader("Update Ticket Status")
    ticket_ids = df["id"].tolist()
    selected_id = st.selectbox("Select Ticket ID", ticket_ids)
    new_status = st.selectbox("New Status", ["Open", "In Progress", "Closed"])
    update = st.button("Update Status")

    if update:
        supabase.table("support_tickets").update({"status": new_status}).eq("id", selected_id).execute()
        st.success("Ticket status updated.")
