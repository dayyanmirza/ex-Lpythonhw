# Study drills for ex39

cities = {
    'Newcastle': 'NCL',
    'London': 'LDN',
    'Manchester': 'MAN',
    'Norwich': 'NRW',
}

Region = {
    'NCL': 'North',
    'LDN': 'South',
    'MAN': 'North West',
#    'NRW' : 'West'  # Do you see that below I make a duplicate key, this is not allowed and  --> 'NRW' : 'East' --> will overide this one if I uncomment the line.
}

# add a region
Region['NRW'] =  'East'

# print out each city's abbreviation
for city, abbrev in list(cities.items()):
    print(f"{city} has the abbreviation {abbrev}")

print(cities['London'])    

# print out the region using the city
print(Region[cities['Newcastle']])

# print out the region
for abbrev, region in list(Region.items()):
    print(f"{abbrev} is in the {region}")

# now print out both the cities and the region
for city, abbrev in list(cities.items()):
    print(f"{city} has the abbreviation {abbrev}")
    print(f" and the city is in the {Region[abbrev]}")    

# trying out stuff from docs on dictionaries --> https://python-reference.readthedocs.io/en/latest/docs/dict/

print(cities.get('London'))
print(Region.get('MAN'))

print(cities.items()) # Returns a copy of the dictionary’s list of (key, value) pairs.
print(Region.items())

print(cities.keys()) # Returns a copy of the dictionary's list of keys.
print(Region.keys())

print(cities.values()) # Returns a copy of the dictionary's list of values.
print(Region.values()) 

cities.update({'Birmingham': 'BRM'}) # Adds key:value elements to the dictionary.
print(cities.items())
Region.update({'BRM': 'West Midlands'})
print(Region.items())

# can use pop to remove and item from dictionary check the link above for more info.
# What if I need a dictionary, but I need it to be in order? --> check out --> collections.OrderedDict check it online.