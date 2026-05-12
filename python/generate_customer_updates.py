import pandas as pd
import random

crm_df = pd.read_csv("../data/raw/crm_data.csv")

updates = crm_df.sample(1000).copy()

subscriptions = [
    "Basic",
    "Premium",
    "Business",
    "Unlimited"
]

regions = [
    "North",
    "South",
    "East",
    "West",
    "Central",
    "Littoral"
]

statuses = [
    "Active",
    "Inactive",
    "Suspended"
]

updates["subscription_type"] = [
    random.choice(subscriptions)
    for _ in range(len(updates))
]

updates["region"] = [
    random.choice(regions)
    for _ in range(len(updates))
]

updates["customer_status"] = [
    random.choice(statuses)
    for _ in range(len(updates))
]

updates.to_csv(
    "../data/raw/customer_updates.csv",
    index=False
)

print("Customer update dataset generated.")