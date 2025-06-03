import os
from supabase import create_client, Client
from datetime import datetime

# Load Supabase credentials from Streamlit secrets
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_intake_data(record):
    # Add timestamp
    record["submitted_at"] = datetime.now().isoformat()

    # Rename keys to match table schema
    formatted_record = {
        "business_name": record["business name"],
        "contact_name": record["Contact Name"],
        "email": record["Email"],
        "phone": record.get("Phone", ""),
        "industry": record.get("Industry", ""),
        "number_of_users": record.get("Number of Users", 0),
        "domain": record.get("Domain", ""),
        "needs": record.get("Needs", ""),
        "submitted_at": record["submitted_at"]
    }

    data, count = supabase.table("intake_form_submissions").insert(formatted_record).execute()
    return data

def load_intake_data():
    response = supabase.table("intake_form_submissions").select("*").order("submitted_at", desc=True).execute()
    return response.data

def save_provisioning_status(client_name, status_dict):
    from supabase import create_client
    import os

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    supabase = create_client(url, key)

    updates = {
        "provisioning_status": status_dict,
        "last_updated": datetime.utcnow().isoformat()
    }

    supabase.table("intake_form_submissions").update(updates).eq("business_name", client_name).execute()
