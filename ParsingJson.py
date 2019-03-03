import json

data = """
[
	{
		"id" : "001",
		"x" : "2",
		"name" : "servesh"
	},
	{
		"id" : "008",
		"x" : "6",
		"name" : "kamlesh"
	}
] """

info = json.loads(data)
print("user count",len(info))

for item in info :
	print("Name ", item['name'])
	print("id :",item['id'])
	
