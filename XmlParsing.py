
#reference python for everybody pdf by Dr. chuck 
#reference python for everybody video lecture by Dr. chuck


import xml.etree.ElementTree as ET

data = '''
<person> 
	<name> servesh </name>
	<phone type = "intl">
	+919674623113
	</phone>
	<email hide = "yes" />
</person> '''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
