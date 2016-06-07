import os
import re
import json
import argparse
import sys
from pprint import pprint
import glob
#python3 main.py config.json
#pycmd   argv[0]  argv[1]

# read from command line

try:
    x = sys.argv[1]
except Exception as e:
    raise(e)




#now open the config file and read different values from it 

with open(x) as config_file:
    config_file_data = json.load(config_file)

# to store all type of platforms
# ListOfPlatforms = ["android", "web", "ios"]

platform = config_file_data["mapping_from"]
# print(platform)

# ListOfPlatforms.remove(platform)
path = ""

y = config_file_data["paths"]
output_file_location = ""
# print(y)
# print(len(y),type(y))

if platform == "ios":
    path = y[0]["input_path"] + "/" + y[0]["input_file_regex"]
    output_file_location = y[0]["output_path"]
elif platform == "web":
    path = y[1]["input_path"] + "/" + y[1]["input_file_regex"]
    output_file_location = y[1]["output_path"]
elif platform == "android":
    path = y[2]["input_path"] + "/" + y[2]["input_file_regex"]
    output_file_location = y[2]["output_path"]
else:
    print("Conversion not possible for %s"%platform)
    exit


# print(output_file_location)

length_output_file_location=len(output_file_location)

    

#list of files to be parsed
file_list_to_be_parsed = glob.glob(path)
# print(path)
# print(file_list_to_be_parsed)
# print((output_file_location[0]))
# print((output_file_location[1]))

# print(length_output_file_location)
DictLocation = config_file_data["mapping"]  
# print(DictLocation)


with open(DictLocation) as total_dict:
    storage_file = json.load(total_dict)

i = 0
dict1 = {}  # dict1{'android': {}, 'web': {'AppRegistry': 'div', 'Text': 'p', 'StyleSheet': 'div', 'ProgressBarAndroid': 'div', 'View': 'span'}}
#                    [     1st   ]   [         2nd     
length = len(storage_file)
# print(length)
# print(type(length))  # get the length and iterate iter                                                            ]
for i in range(length):
    if storage_file[i]["mapping_from"] == platform:
        dict1[storage_file[i]["mapping_to"]] = storage_file[i]["mapping_def"]
        
# print(dict1)

# print(ListOfPlatforms)

# print(len(storage_file))

for files in file_list_to_be_parsed:
    
    for key in dict1:        
        file_to_send = files            #print(files)                   #input files
        dictionaryrules = dict1[key]  #it will be used for mapping each files      {RULES}  
        plot = key                     #type in which it is to be changed
        
        #outputpath, output_file_name + output_extension
        output_extension = ""
        index = 0
        for index in range(length_output_file_location):
            print(output_file_location[index])
        # print("******************************************************************************")
        # output_path_next = ""
        # output_file_extension = ""
        # k = 0
        # for key1 in output_file_location[k]:
        #     if key == key1:
        #         output_file_extension = output_file_location[k]["output_file_regex"]
        #         output_path_next = output_file_location[k][key1]
        #     k+=1
        # print(files)
        # print(key)
        # print(dictionaryusable)
        # print(output_path_next)
        # print(output_file_extension)