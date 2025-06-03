import os
from supabase import create_client, Client
from datetime import datetime

# Load Supabase credentials from Streamlit secrets
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_intake_data(record):
    # Ensure timestamp is present (already added in IntakeForm.py, but we'll be safe)
    if "submitted_at" not in record:
        record["submitted_at"] = datetime.now().isoformat()

    # DEBUG log
    print("DEBUG: Submitting intake record to Supabase =", record)

    # Submit directly
    data, count = supabase.table("intake_form_submissions").insert(record).execute()
    return data

def load_intake_data():
    response = supabase.table("intake_form_submissions").select("*").order("submitted_at", desc=True).execute()
    return response.data

def save_provisioning_status(client_name, status_dict):
    updates = {
        "provisioning_status": status_dict,
        "last_updated": datetime.utcnow().isoformat()
    }
    supabase.table("intake_form_submissions").update(updates).eq("business_name", client_name).execute()
