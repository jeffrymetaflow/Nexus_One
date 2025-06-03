import pandas as pd
import os
from datetime import datetime

DATA_FILE = "intake_submissions.csv"

def save_intake_data(record):
    # Add timestamp to record
    record["Submitted At"] = datetime.now().isoformat()

    # Check if file exists
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
    else:
        df = pd.DataFrame([record])

    df.to_csv(DATA_FILE, index=False)


def load_intake_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame()
