import csv

file = open('Mobile Phone Masts.csv', newline='')
reader = csv.reader(file)
header = next(reader)
data = [row for row in reader]

# Task 1

current_rent = [float(entry[header.index('Current Rent')]) for entry in data]
lease_years = [float(entry[header.index('Lease Years')]) for entry in data]
lease_amount = [current_rent[i] * lease_years[i] for i in range(len(current_rent))]
lease_amount_sorted = sorted(lease_amount)
print(lease_amount_sorted[:5])
print(' ')

# Task 2


# Task 3

print(sum(lease_amount))
print(' ')

# Task 4

tenant_masts = dict()
tenants = [entry[header.index('Tenant Name')] for entry in data]
for tenant in tenants:
    tenant_masts[tenant] = tenants.count(tenant)
print(tenant_masts)
print(' ')

# Task 5

months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', \
          'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
lease_start_dates = [entry[header.index('Lease Start Date')] for entry in data]
lease_end_dates = [entry[header.index('Lease End Date')] for entry in data]

index = 0
for date in lease_start_dates:
    for c in date:
        if c in ['J', 'F', 'M', 'A', 'J', 'S', 'O', 'N', 'D']:
            date = date[:date.index(c) - 1] + '/' + months[date[date.index(c): date.index(c) + 3]] + '/' + date[date.index(c) + 4:]
            lease_start_dates[index] = date
            break
    index += 1

index = 0
for date in lease_end_dates:
    for c in date:
        if c in ['J', 'F', 'M', 'A', 'J', 'S', 'O', 'N', 'D']:
            date = date[:date.index(c) - 1] + '/' + months[date[date.index(c): date.index(c) + 3]] + '/' + date[date.index(c) + 4:]
            lease_end_dates[index] = date
            break
    index += 1

index = 0
for date in lease_start_dates:
    if 2007 >= int(date[-4:]) >= 1999:
        if (date[-4:] == '2007' and int(date[3:5]) > 9) or (date[-4:] == '1999' and int(date[3:5]) < 6):
            continue
        print(data[index][:header.index('Lease Start Date')] + [date] + [lease_end_dates[index]] + data[index][header.index('Lease Start Date') + 2:])
    index += 1
