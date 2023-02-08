'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''

import json

infile = open("eq_data.json", "r")

eq_data = json.load(infile)


# 1) Print out the number of earthquakes

num = len(eq_data["features"])
print(f"There were {num} earthquakes.\n")


# 2) iterate through the dictionary and extract the location, magnitude, longitude and latitude of the location and put it in a new
#    dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a magnitude > 6. Print out the new dictionary.

eq_dict = {}
eq_dict["earthquakes"] = []

for i in eq_data["features"]:

   if i["properties"]["mag"] > 6:

      info = {}

      info["location"] = i["properties"]["place"]
      info["magnitude"] = i["properties"]["mag"]
      info["latitude"] = i["geometry"]["coordinates"][0]
      info["longitude"] = i["geometry"]["coordinates"][1]

      eq_dict["earthquakes"].append(info)

print("----------------- FULL EQ_DICT -----------------")
print(eq_dict)
print("------------------------------------------------\n")

# 3) using the eq_dict dictionary, print out the information as shown below: #

print("------- EARTHQUAKES WITH A MAGNITUDE > 6 -------")

for i in eq_dict["earthquakes"]:
   print("Location:", i["location"])
   print("Magnitude:", i["magnitude"])
   print("Longitude:", i["longitude"])
   print("Latitude:", i["latitude"], '\n')
