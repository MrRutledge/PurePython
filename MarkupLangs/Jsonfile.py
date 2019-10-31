import json

data = """
{
    "name":"Chuck",
    "phone": {
        "type" : "intl",
        "number": "+255097864523"
    },
    "email" :{
        "hide":"yes"
    }
}
"""
info = json.loads(data)
print("Name:", info["name"])
print("Email: ", info["email"]["hide"])

input2 = """
[
    {
        "id":"001",
        "x":"2",
        "name":"Brown"
    },
    {
        "id":"002",
        "x":"7",
        "name":"Satun"
    }
]
"""
info2 = json.loads(input2)
print("User count:",len(info2))

for item in info2:
    print("Name:", item["name"])
    print('id:',item["id"])
    print('Attribute:',item["x"])