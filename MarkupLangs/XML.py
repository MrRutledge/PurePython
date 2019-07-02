#XML ---> extensible markup language
#XML has tags, attributes, and closing statement.
#xml is very sensitive to errors
import xml.etree.ElementTree as ET
  
data = """
<Person>
    <name> Don</name>
    <phone type="intl">
        +25849658
    </phone>
    <email hide="yes"/>
</Person>
"""

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))