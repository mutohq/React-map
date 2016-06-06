import os
import re
import json

# dictOfKeywords = {}

#load the dictionary 
with open('Dictionary/storage.json') as data_file:
    dictOfKeywords = json.load(data_file) 


print(dictOfKeywords)

f = open("jsfilestoparse/test.ios.js").read()

f = f.replace("\n", "$!^#@")

g = f

#regex to find return();
reg = r"return\s*?\((.*?)\);"


# r = r"<[A-Z][a-z]+[A-Z]*[a-z]*"
# r1 = r"</[A-Z][a-z]+[A-Z]*[a-z]*\s*>"

#regex to find Components 
# mixR = r"<([A-Z][a-zA-Z]*\s*|/[A-Z][a-zA-Z]*\s*)"

#for any case
mixR = r"<\s*(\s*[a-zA-Z]*\s*|/\s*[a-zA-Z]*\s*)"

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
            # print(s[1]) #key = s[1])
            listOfKeywordsToBeReplaced.append(s[1])
                                                              
        except:
            s = string.split(" ")
            listOfKeywordsToBeReplaced.append(s[0])
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
print("List of keywords to be replaced : ",listOfKeywordsToBeReplaced)
# print(index)
# listchange = list(set(listchange))
# print(type(listchange))
print(listchange)

# for keyword in listOfKeywordsToBeReplaced:
#     if keyword in dictOfKeywords.keys():
#         print("Present")
#     else:
#         dictOfKeywords[keyword] = 'Comment this line '   
    


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

# print("Old M ", m)
# print("============================================================================================================")
# print("NEW M ", newM)       
i = 0

for string in m:
    g = g.replace(string,newM[i])
    # print(string)
    # print("============================================================================================================")
    # print(newM[i])
    i+=1       

g = g.replace("$!^#@", "\n")

newFile = open('./webFiles/testweb.js', 'w')
newFile.write(g)

