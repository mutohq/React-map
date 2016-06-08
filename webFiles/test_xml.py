import xml.etree.ElementTree as ET

a = """<View style=stylescontainer>
      <Text style=stylesname>
      Hello Bhavyanth
      </Text>
      </View>"""

root = ET.fromstring(a)
print(root)
    