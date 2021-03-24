counties = ['Araphoe','Denver','Jefferson']
if "Araphoe" in counties or "El Paso" in counties:
    print ("Araphoe or El Paso is in the list of counties")
else:
    print ("Araphoe and El Paso are not in the list of counties")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
