import os
import re
import json
import argparse
import sys
import glob

#python3 main.py config.json
#pycmd   argv[0]  argv[1]

try:
    x = sys.argv[1]
except Exception as e:
    print("Pass the config as <python3 <file>.py config.json> ")

#now open the config file and read different values from it 

with open(x) as config_file:
    config_file_data = json.load(config_file)

# print(config_file_data)

Mapping_from = config_file_data["mapping_from"]
Dictionary_path = config_file_data["mapping"]
Paths = config_file_data["paths"]
# print(Mapping_from)
# print(Dictionary_path)
# print(Paths)

length = len(Paths)
i = 0
for i in range(length):
    if Paths[i]["source_platform"] == Mapping_from:
        Input_path = Paths[i]["input_path"]
        Input_file_regex =  Paths[i]["input_file_regex"]
        Output_path = Paths[i]["output_path"]

# print(Input_path)
# print(Input_file_regex)
# print(Output_path)

inputpathafter = Input_path +"/"+Input_file_regex
# print(inputpathafter)
filesToBeParsed = glob.glob(inputpathafter)
# print(filesToBeParsed)

for files in filesToBeParsed:
    input_file_to_parse = files
    s = files.split(".")
    i_name = s[0]
    k = 0
    length_out = len(Output_path)
    for k in range(length_out):
        Destination = Output_path[k]["destination"]
        Dest_platform = Output_path[k]["dest_platform"]
        Output_file_regex = Output_path[k]["output_file_regex"]
        Output_path_name = i_name +Output_file_regex
        s1 = Output_path_name.split("/")
        lengthOfOutput_path = len(s1)
        Output_file_name = s1[lengthOfOutput_path-1]
        AbsolutePathtowrite = Destination + "/" + Output_file_name
        # print(Destination)
        # print(Dest_platform)
        # print(Output_path_name)
        # print(Output_file_name)
        # print(AbsolutePathtowrite)
        
        #Dictionary is loaded keeping in mind that 
        #Dest_platfrom=mapping_to(storage.json) and 
        #Mapping_from=mapping_from(storage.json) 

        # dictOfKeywords = {}
        with open(Dictionary_path) as total_dict:
            storage_file = json.load(total_dict)
        length_dict = len(storage_file)
        i = 0
        for i in range(length_dict):
            if storage_file[i]["mapping_from"]==Mapping_from and storage_file[i]["mapping_to"] == Dest_platform:
                dictOfKeywords = storage_file[i]["mapping_def"]
                
        # print(dictOfKeywords)
        f = open(input_file_to_parse).read()
        f = f.replace("\n","$!^#@")
        g = f

        #regex to find return();
        reg = r"return\s*?\((.*?)\);"        
        
        #for any case
        mixR = r"<([a-zA-Z]+\s*|/[a-zA-Z]+\s*)"
        
        #Find the xml part i.e. part within return()
        m = re.findall(reg, f)
        # print(m)
        # print("\n\nlength is : %s"%len(m))
        # print(dir(m))

        listchange = []
        index = -1

        listOfKeywordsToBeReplaced = []
        for match in m:
            m3 = re.findall(mixR, match)
            index+=1
            # print("****  %s  ***"%index)

            for string in m3:   #strings in m3
                try:
                    s = string.split("/")
                    print(s[1]) #key = s[1])
                    listOfKeywordsToBeReplaced.append(s[1])
                except:
                    s = string.split(" ")
                    listOfKeywordsToBeReplaced.append(s[0])
                    print(s[0])
            f = 0
            fault = 1
            for keyword in listOfKeywordsToBeReplaced:
                if keyword in dictOfKeywords.keys():
                    fault = 0
                else:
                    dictOfKeywords[keyword] = keyword
                    if f == 0:
                        listchange.append(index)
                        f = 1
        listOfKeywordsToBeReplaced = list(set(listOfKeywordsToBeReplaced))
        # print("List of keywords to be replaced : ",listOfKeywordsToBeReplaced)
        # print(index)
        # listchange = list(set(listchange))
        # print(type(listchange))
        print(listchange)
        commentS = "/**********************************************************************************"
        commentE = "**********************************************************************************/"
        i = 0
        newM = []
        for string in m:
            # print("Before conversion : ",string)
            for keyword in listOfKeywordsToBeReplaced:
                # print("keyword ",keyword, dictOfKeywords[keyword])
                string = string.replace(keyword, dictOfKeywords[keyword])
            if i in listchange:
                string = commentS+string+commentE

            newM.append(string)
            i+=1
            # print("After conversion : ",string)
        i = 0
        for string in m:
            g = g.replace(string,newM[i])
            # print(string)
            # print("============================================================================================================")
            # print(newM[i])
            i+=1
        g = g.replace("$!^#@", "\n")
        newFile = open(AbsolutePathtowrite,'w')
        newFile.write(g)



            
