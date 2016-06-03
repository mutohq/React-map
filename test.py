

dictOfKeywords = {'Text':'p', 'View':'span', 'NavigatorIOS':'div', 'AppRegistry':'div', 'StyleSheet':'div'}
listOfKeys = []

for key in dictOfKeywords.keys():
    listOfKeys.append(key)

print(listOfKeys)


testString = "View"

if testString in listOfKeys:
    print("found") 

string_test = """ <View style={styles.container}>
      <Text style={styles.name}>
      Hello, Bhavyanth!
      </Text>
      </View>"""

print(string_test.split(" "))
