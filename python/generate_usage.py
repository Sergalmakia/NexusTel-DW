import pandas as pd
import random
from faker import Faker

fake = Faker()

# Load CRM dataset
crm_df = pd.read_csv("../data/raw/crm_data.csv")

regions = [
    "North",
    "South",
    "East",
    "West",
    "Central",
    "Littoral"
]

connection_types = [
    "3G",
    "4G",
    "5G",
    "Fiber"
]

usage_data = []

for i in range(500000):

    customer = crm_df.sample(1).iloc[0]

    usage_date = fake.date_between(
        start_date='-1y',
        end_date='today'
    )

    usage_data.append({
        "customer_id": customer["customer_id"],
        "usage_date": usage_date,
        "data_usage_mb": round(random.uniform(50, 15000), 2),
        "call_duration_minutes": round(random.uniform(0, 500), 2),
        "sms_count": random.randint(0, 300),
        "internet_sessions": random.randint(1, 50),
        "dropped_calls": random.randint(0, 10),
        "network_region": random.choice(regions),
        "connection_type": random.choice(connection_types)
    })

usage_df = pd.DataFrame(usage_data)

usage_df.to_csv(
    "../data/raw/usage_data.csv",
    index=False
)

print("Usage dataset generated successfully.")