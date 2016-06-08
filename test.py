import os
import re
import json
import xml.etree.ElementTree as ET

f = open('jsfilestoparse/ios/index.ios.js').read()

f = f.replace ("\n","$!^#@")

g = f

dictOfkeywords = {'View':'p', 'Text':'span', 'Nav':'xyz'}

reg = r"return\s*?\((.*?)\);" 
# rex = r"(<\([A-Za-z]+\).*>)|(<\(/[A-Za-z]+\).*>)|(<\([A-Za-z]+\).*/>)"
rex = r"(<[a-zA-Z]+.*?>+|</[a-zA-Z]+.*?>)"
regxmlnot = r"<[a-zA-Z]+.*?/>"
matchreg = re.findall(reg, f)
# print(matchreg)

for eachmatchreg in matchreg:
    tempmatchreg = eachmatchreg #operate on tempmatchreg and change it and replace eachmatchreg by tempmatchreg in g as g = g.replace(eachmatchreg, tempmatchreg)

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
                if checkforkey in dictOfkeywords.keys():
                    tempkeywordclosereg = tempkeywordclosereg.replace(checkforkey, dictOfkeywords[checkforkey])
                    # print(tempkeywordclosereg)
                else:
                    tempkeywordclosereg = "/*" + tempkeywordclosereg + "*/"
                    # print(tempkeywordclosereg)
                tempangularreg = tempangularreg.replace(eachkeywordclosereg, tempkeywordclosereg)
            print(tempangularreg)
        if f != 1:
           print(eachangularreg)
                            
# for match in m:
#     tempmatch = match
#     # match = match.replace("$!^#@","\n") 
#     # print(match)
#     n = re.findall(rex, match)
#     newN = []
#     # print(n)
#     for string in n:
#         tempstring = string
#         # print("-----")
#         # print(string)
#         # print("-----")
#         regexs = re.findall(regxmlnot, string)
#         newregexs = []
#         lengthregexs = len(regexs)
#         f = 0
#         if lengthregexs != 0:
#             f = 1
#             for singleregexs in regexs:
#                 tempsingleregexs = singleregexs
#                 seperateopen = singleregexs.split("<")
#                 # print(seperateopen[1])
#                 sepcheckkey = seperateopen[1].split(" ")
#                 checkforkey = sepcheckkey[0]
#                 # print(checkforkey)
                
#                 if checkforkey in dictOfkeywords.keys():
#                     singleregexs = singleregexs.replace(checkforkey,dictOfkeywords[checkforkey])
#                 else:
#                     singleregexs = "/*" + singleregexs + "*/"    
#                 # print(singleregexs)
#                 newregexs.append(singleregexs)            
#                 print(regexs,newregexs)
#                 string = string.replace(tempsingleregexs,singleregexs)
            
#             # print(newregexs)
#         if f != 1:
#             tempprocess = string
#             print(string[1])

#             # print(string)
#     print("****************")
# g = g.replace("$!^#@", "\n")

