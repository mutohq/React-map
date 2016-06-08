import os
import re
import json
import xml.etree.ElementTree as ET

f = open('jsfilestoparse/ios/index.ios.js').read()

f = f.replace ("\n","$!^#@")

g = f

dictOfkeywords = {'View':'p',  'Nav':'xyz'}

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
        f1 = 0
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
            # print(tempangularreg)
        if f != 1:
        #    print(eachangularreg)
            temp = eachangularreg
            regexp = re.findall(r"<([a-zA-Z]+|/[a-zA-Z]+)",temp)
            s = regexp[0]
            if s[0] == "/":
                s1 = s[1:]
                if s1 in dictOfkeywords.keys():
                    temp = temp.replace(s1,dictOfkeywords[s1])
                else:
                    temp = temp + "*/"
            else:
                if s in dictOfkeywords.keys():
                    temp = temp.replace(s,dictOfkeywords[s])
                else:
                    temp = "/*" + temp
            tempangularreg = tempangularreg.replace(eachangularreg,temp)
            # print(tempangularreg)    
            # print(type(regexp[0]))
            # print(regexp[0])
        tempmatchreg = tempmatchreg.replace(eachangularreg, tempangularreg)
    g = g.replace(eachmatchreg,tempmatchreg)

g = g.replace("$!^#@", "\n")
print(g)
