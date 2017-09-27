# Data loading

import pandas as pd
df = pd.read_csv('Mobile Phone Masts.csv')

# Task 1

current_rent_sorted_list = sorted(df["Current Rent"])
print(current_rent_sorted_list[:5])

# Task 2

lease_years_25 = df[df['Lease Years'] == 25]
print(lease_years_25)

# Task 3

tenant_masts = dict()
tenants = list(df['Tenant Name'])
for tenant in tenants:
    tenant_masts[tenant] = tenants.count(tenant)
print(tenant_masts)

# Task 4

df['Lease Start Date'] = pd.to_datetime(df['Lease Start Date'])
task = df[df['Lease Start Date'] >= pd.to_datetime('1999-6-01')]
task = task[task['Lease Start Date'] <= pd.to_datetime('2007-08-31')]
print(task)
