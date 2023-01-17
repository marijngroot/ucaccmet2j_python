import json
from csv import DictReader

# part 1

# with open('precipitation.json', encoding='utf-8') as file:
#     precipitation = json.load(file)

# seattle = []    # a list containing all measurements (dictionaries) in seattle

# selecting the measurements from seattle
# for measurement in precipitation:
#     measurement['month'] = int(measurement['date'].split('-')[1])
#     if measurement['station'] == 'GHCND:US1WAKG0038':
#         seattle.append(measurement)

# # initiating a list of 0's for each month
# total_monthly_precipitation = []
# for i in range(12):
#     total_monthly_precipitation.append(0)

# # summing the total precipitation for each month and writing into total precipitation list
# for measurement in seattle:
#     total_monthly_precipitation[measurement['month']-1] += measurement['value']
 
# print(total_monthly_precipitation)
    
# part 2

# total_yearly_precipitation = 0
# for month_precipitation in total_monthly_precipitation:
#     total_yearly_precipitation += month_precipitation

# print(total_yearly_precipitation)

# relative_monthly_precipitation = []
# for i in range(12):
#     relative_monthly_precipitation.append(total_monthly_precipitation[i-1]/total_yearly_precipitation)

# print(relative_monthly_precipitation)

# part 3 + bonus

with open('stations.csv', encoding='utf-8') as file:
    stations = list(DictReader(file))

with open('precipitation.json', encoding='utf-8') as file:
    precipitation = json.load(file)

# initiating a big results dictionary which will be used for results.json
results = {}

# calculating the total yearly precipitation of all stations combined
all_yearly_precipitation = 0
for measurement in precipitation:
    all_yearly_precipitation += measurement['value']

for station in stations:
    # creating a variable with the location of the station (ie Seattle)
    location = station['Location']
    # selecting measurements from the right location
    location_measurements = []
    for measurement in precipitation:
        measurement['month'] = int(measurement['date'].split('-')[1])
        if measurement['station'] == station['Station']:
            location_measurements.append(measurement)
    # initiating a list of 12 0's for total monthly precipitation
    total_monthly_precipitation = []
    for i in range(12):
        total_monthly_precipitation.append(0)
    # calculating the total monthly precipitation per location and including it in the initial list
    for measurement in location_measurements:
        total_monthly_precipitation[measurement['month']-1] += measurement['value']
    # calculating the total yearly precipitation per location
    total_yearly_precipitation = 0
    for month_precipitation in total_monthly_precipitation:
        total_yearly_precipitation += month_precipitation
    # calculating the relative monthly precipitation per location
    relative_monthly_precipitation = []
    for i in range(12):
        relative_monthly_precipitation.append(total_monthly_precipitation[i-1]/total_yearly_precipitation)
    # calculating the relative yearly precipitation
    relative_yearly_precipitation = total_yearly_precipitation/all_yearly_precipitation
    # creating a dictionary location_results with precipitation data for this location, which will be included in results.json
    location_results = {}
    location_results["station"]=station['Station']
    location_results["state"]=station['State']
    location_results["total_monthly_precipitation"]=total_monthly_precipitation
    location_results["total_yearly_precipitation"]=total_yearly_precipitation
    location_results["relative_monthly_precipitation"]=relative_monthly_precipitation
    location_results["relative_yearly_precipitation"]=relative_yearly_precipitation
    results[f'{location}'] = location_results

# print(results)

# bonus

# results = dict()
# seattle_results = dict()
# seattle_results["station"]="GHCND:US1WAKG0038"
# seattle_results["state"]="WA"
# seattle_results["total_monthly_precipitation"]=total_monthly_precipitation
# seattle_results["total_yearly_precipitation"]=total_yearly_precipitation
# seattle_results["relative_monthly_precipitation"]=relative_monthly_precipitation
# results["Seattle"] = seattle_results

with open('results.json', 'w', encoding = 'utf-8') as file:
    json.dump(results, file, indent=4)