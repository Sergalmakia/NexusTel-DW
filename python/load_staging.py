import pandas as pd
from sqlalchemy import create_engine

# =========================
# DATABASE CONNECTION
# =========================

username = "root"
password = "Your_Password"
host = "localhost"
database = "nexustel_dw"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# =========================
# LOAD CRM DATA
# =========================

crm_df = pd.read_csv("../data/raw/crm_data.csv")

crm_df.to_sql(
    name="staging_crm",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=5000
)

print("CRM data loaded successfully.")

# =========================
# LOAD BILLING DATA
# =========================

billing_df = pd.read_csv("../data/raw/billing_data.csv")

billing_df.to_sql(
    name="staging_billing",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=5000
)

print("Billing data loaded successfully.")

# =========================
# LOAD USAGE DATA
# =========================

usage_df = pd.read_csv("../data/raw/usage_data.csv")

usage_df.to_sql(
    name="staging_usage",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=5000
)

print("Usage data loaded successfully.")

# =========================
# LOAD CUSTOMER UPDATES
# =========================

updates_df = pd.read_csv("../data/raw/customer_updates.csv")

updates_df.to_sql(
    name="staging_customer_updates",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=5000
)

print("Customer updates loaded successfully.")