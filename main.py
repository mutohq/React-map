import os
import re
import json
import argparse
import sys
from pprint import pprint
import glob
#python3 main.py config.json
#pycmd   argv[0]  argv[1]

x = sys.argv[1]

#now open the config file and read different values from it 

with open(x) as config_file:
    config_file_data = json.load(config_file)
   
platform = config_file_data["mapping_from"]
# print(platform)
path = ""

y = config_file_data["paths"]
output_file_location = []
# print(y)
# print(len(y),type(y))

if platform == "ios":
    path = y[0]["input_path"] + "/" + y[0]["input_file_regex"]
    output_file_location = y[0]["output_path"]
elif platform == "android":
    path = y[2]["input_path"] + "/" + y[2]["input_file_regex"]
    output_file_location = y[2]["output_path"]
else:
    path = y[1]["input_path"] + "/" + y[1]["input_file_regex"]
    output_file_location = y[1]["output_path"]



#list of files to be parsed
file_list = glob.glob(path)
# print(path)
# print(file_list)
# print((output_file_location[0]))


DictLocation = config_file_data["mapping"]  
# print(DictLocation)


with open(DictLocation) as total_dict:
    storage_file = json.load(total_dict)



if platform == storage_file["mapping_from"]:
    

