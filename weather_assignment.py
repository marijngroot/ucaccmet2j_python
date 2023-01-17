import json

with open('precipitation.json', encoding='utf-8') as file:
    precipitation = json.load(file)

seattle = []    # a list containing all measurements (dictionaries) in seattle
total_monthly_precipitation = []
for i in range(12):
    total_monthly_precipitation.append({(i + 1):0}) # a list containing dictionaries for each month, with value 0

for measurement in precipitation:
    measurement['month'] = int(measurement['date'].split('-')[1])
    if measurement['station'] == 'GHCND:US1WAKG0038':
        seattle.append(measurement)

for measurement in seattle:
    if {measurement['month']:0} in total_monthly_precipitation:
        total_monthly_precipitation[measurement['month']-1][measurement['month']] = measurement['value']
    else:
        total_monthly_precipitation[measurement['month']-1][measurement['month']] += measurement['value']

print(total_monthly_precipitation)