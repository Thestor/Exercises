# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:44:52 2019

@author: Matthew
"""

import json
import random

filename = r"JSON Files\significant_month.geojson - Copy.json"
list_of_earthquakes = []

def save_json_file(data):
    write_file = open(r"JSON Files\significant_month.geojson - Copy.json", "w")
    json.dump(data, write_file)
    write_file.close()
    
def record_an_earthquake(data_to_record, key):
    temp_dict = {"properties": {"place" : data_to_record}}
    list_of_earthquakes["features"].append(temp_dict)
    save_json_file(list_of_earthquakes)

def find_an_earthquake(earthquake_place):
    relevant_earthquakes = []
    for an_earthquake in list_of_earthquakes["features"]:
        if (earthquake_place.title() in an_earthquake["properties"]["place"]):
            relevant_earthquakes.append(an_earthquake)
    return relevant_earthquakes
        
with open(filename) as f:
    earthquake_json = json.load(f)
    list_of_earthquakes = earthquake_json
    f.close()
    
for e in list_of_earthquakes:
    print(list_of_earthquakes)
print("\n")

choice = input("Find an earthquake by its place (create one if nonexistent): ")
userEQ = find_an_earthquake(choice)
if userEQ != []:
    print(userEQ)
else:
    ran_num = random.randint(5000, 300000) #rough code to add numberings
    key = (ran_num)
    record_an_earthquake(choice, key)
    print(list_of_earthquakes)