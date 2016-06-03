import os
import re


dictOfKeywords = {'Text':'p', 'View':'span', 'NavigatorIOS':'div', 'AppRegistry':'div', 'StyleSheet':'div',"ProgressBarAndroid":"div"}


f = open("jsfilestoparse/index.ios.js").read()

f = f.replace("\n", "$!^#@")

g = f

#regex to find return();
reg = r"return\s*?\((.*?)\);"


# r = r"<[A-Z][a-z]+[A-Z]*[a-z]*"
# r1 = r"</[A-Z][a-z]+[A-Z]*[a-z]*\s*>"

#regex to find Components 
mixR = r"<([A-Z][a-zA-Z]*\s*|/[A-Z][a-zA-Z]*\s*)"


#Find the xml part i.e. part within return()
m = re.findall(reg, f)

# print(m)
# print("\n\nlength is : %s"%len(m))
# print(dir(m))

listOfKeywordsToBeReplaced = []
for match in m:
    m3 = re.findall(mixR, match)

    for string in m3:   #strings in m3
        try:
          
            s = string.split("/")
            # print(s[1]) #key = s[1])
            listOfKeywordsToBeReplaced.append(s[1])
            
        except:
            s = string.split(" ")
            listOfKeywordsToBeReplaced.append(s[0])

listOfKeywordsToBeReplaced = list(set(listOfKeywordsToBeReplaced))
print("List of keywords to be replaced : ",listOfKeywordsToBeReplaced)

newM = []
for string in m:
    # print("Before conversion : ",string)
    for keyword in listOfKeywordsToBeReplaced:
        # print("keyword ",keyword, dictOfKeywords[keyword])
        string = string.replace(keyword, dictOfKeywords[keyword])
    newM.append(string)
    # print("After conversion : ",string) 

# print("Old M ", m)
# print("============================================================================================================")
# print("NEW M ", newM)       
i = 0

for string in m:
    g = g.replace(string,newM[i])
    print(string)
    print("============================================================================================================")
    print(newM[i])
    i+=1       

g = g.replace("$!^#@", "\n")

newFile = open('./webFiles/indexWeb.js', 'w')
newFile.write(g)

