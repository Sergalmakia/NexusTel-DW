from faker import Faker
import pandas as pd
import random

fake = Faker()

regions = [
    "North", "South", "East",
    "West", "Central", "Littoral"
]

subscriptions = [
    "Basic", "Premium", "Business", "Unlimited"
]

statuses = [
    "Active", "Inactive", "Suspended"
]

segments = [
    "Youth", "Corporate", "Residential", "SME"
]

data = []

for i in range(100000):

    customer_id = f"CUST{i+1:06}"

    data.append({
        "customer_id": customer_id,
        "full_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 70),
        "region": random.choice(regions),
        "subscription_type": random.choice(subscriptions),
        "registration_date": fake.date_between(
            start_date='-5y',
            end_date='today'
        ),
        "customer_status": random.choice(statuses),
        "customer_segment": random.choice(segments)
    })

df = pd.DataFrame(data)

df.to_csv(
    "../data/raw/crm_data.csv",
    index=False
)

print("CRM dataset generated successfully.")