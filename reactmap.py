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
        # rex = r"(<\([A-Za-z]+\).*>)|(<\(/[A-Za-z]+\).*>)|(<\([A-Za-z]+\).*/>)"
        rex = r"(<[a-zA-Z]+.*?>+|</[a-zA-Z]+.*?>)"
        regxmlnot = r"<[a-zA-Z]+.*?/>"
        matchreg = re.findall(reg, f)
        # print(matchreg)
        for eachmatchreg in matchreg:
            tempmatchreg = eachmatchreg 
            #operate on tempmatchreg and change it and replace eachmatchreg by tempmatchreg in g as 
            # g = g.replace(eachmatchreg, tempmatchreg)
            # tempmatchreg = tempmatchreg.replace(eachangularreg, tempangularreg)
            #find all expressions within angular bracket 
            angularreg = re.findall(rex, tempmatchreg)
            
            
            #operate on <.*>
            for eachangularreg in angularreg:
                tempangularreg = eachangularreg #tempmatchreg = tempmatchreg.replace(eachangularreg, tempangularreg) 
                
                #find <keyword.*/> and if keyword is in dictionary replace it otherwise /*<keyword.*/>*/ 
                keywordclosereg = re.findall(regxmlnot, tempangularreg)
                lengthkeywordclosereg = len(keywordclosereg)
                f = 0
                if lengthkeywordclosereg != 0:
                    f = 1
                    for eachkeywordclosereg in keywordclosereg:
                        tempkeywordclosereg = eachkeywordclosereg
                        seperateatopen = tempkeywordclosereg.split("<")
                        # print(seperateatopen[1])
                        sepcheckkey = seperateatopen[1].split(" ")
                        checkforkey = sepcheckkey[0]
                        # print(checkforkey)
                        if checkforkey in dictOfKeywords.keys():
                            tempkeywordclosereg = tempkeywordclosereg.replace(checkforkey, dictOfKeywords[checkforkey])
                            # print(tempkeywordclosereg)
                        else:
                            tempkeywordclosereg = "/*" + tempkeywordclosereg + "*/"
                            # print(tempkeywordclosereg)
                        tempangularreg = tempangularreg.replace(eachkeywordclosereg, tempkeywordclosereg)
                    # print(tempangularreg)
                if f != 1:
                    # print(eachangularreg)
                    temp = eachangularreg
                    regexp = re.findall(r"<([a-zA-Z]+|/[a-zA-Z]+)",temp)
                    s = regexp[0]
                    if s[0] == "/":
                        s1 = s[1:]
                        if s1 in dictOfKeywords.keys():
                            temp = temp.replace(s1,dictOfKeywords[s1])
                        else:
                            temp = temp + "*/"
                    else:
                        if s in dictOfKeywords.keys():
                            temp = temp.replace(s,dictOfKeywords[s])
                        else:
                            temp = "/*" + temp
                    tempangularreg = tempangularreg.replace(eachangularreg,temp)
                    # print(tempangularreg)
                    # print(type(regexp[0]))
                    # print(regexp[0])
                tempmatchreg = tempmatchreg.replace(eachangularreg, tempangularreg)
            g = g.replace(eachmatchreg,tempmatchreg)

        
        g = g.replace("$!^#@", "\n")
        newFile = open(AbsolutePathtowrite,'w')
        newFile.write(g)