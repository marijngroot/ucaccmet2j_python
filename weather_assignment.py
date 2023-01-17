import json

# part 1

with open('precipitation.json', encoding='utf-8') as file:
    precipitation = json.load(file)

seattle = []    # a list containing all measurements (dictionaries) in seattle

# selecting the measurements from seattle
for measurement in precipitation:
    measurement['month'] = int(measurement['date'].split('-')[1])
    if measurement['station'] == 'GHCND:US1WAKG0038':
        seattle.append(measurement)

# initiating a list of 0's for each month
total_monthly_precipitation = []
for i in range(12):
    total_monthly_precipitation.append(0)

# summing the total precipitation for each month and writing into total precipitation list
for measurement in seattle:
    total_monthly_precipitation[measurement['month']-1] += measurement['value']
 
print(total_monthly_precipitation)

results = dict()
seattle_results = dict()
seattle_results["station"]="GHCND:US1WAKG0038"
seattle_results["state"]="WA"
seattle_results["total_monthly_precipitation"]=total_monthly_precipitation
results["Seattle"] = seattle_results
    
# part 2

# total_yearly_precipitation = 0
# for month_precipitation in total_monthly_precipitation:
#     total_yearly_precipitation += month_precipitation

# relative_monthly_precipitation = total_monthly_precipitation
# for i in range(12):
#     relative_monthly_precipitation[i-1] = total_monthly_precipitation[i-1]/total_yearly_precipitation

# print(relative_monthly_precipitation)
# print(total_yearly_precipitation)

# bonus

with open('results.json', 'w', encoding = 'utf-8') as file:
    json.dump(results, file, indent=4)