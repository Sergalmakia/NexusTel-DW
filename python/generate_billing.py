import pandas as pd
import random
from faker import Faker

fake = Faker()

# Load CRM data
crm_df = pd.read_csv("../data/raw/crm_data.csv")

payment_methods = [
    "Mobile Money",
    "Credit Card",
    "Bank Transfer",
    "Cash"
]

service_types = [
    "Voice",
    "Data",
    "SMS",
    "Bundle"
]

invoice_statuses = [
    "Paid",
    "Pending",
    "Failed"
]

billing_data = []

for i in range(300000):

    customer = crm_df.sample(1).iloc[0]

    invoice_id = f"INV{i+1:07}"

    billing_date = fake.date_between(
        start_date='-2y',
        end_date='today'
    )

    payment_date = fake.date_between(
        start_date=billing_date,
        end_date='today'
    )

    amount_paid = round(random.uniform(5, 500), 2)

    billing_data.append({
        "invoice_id": invoice_id,
        "customer_id": customer["customer_id"],
        "billing_date": billing_date,
        "payment_date": payment_date,
        "amount_paid": amount_paid,
        "payment_method": random.choice(payment_methods),
        "service_type": random.choice(service_types),
        "invoice_status": random.choice(invoice_statuses)
    })

billing_df = pd.DataFrame(billing_data)

billing_df.to_csv(
    "../data/raw/billing_data.csv",
    index=False
)

print("Billing dataset generated successfully.")