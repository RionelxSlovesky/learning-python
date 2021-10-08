import json

data = json.load(open("D:\\Python Tutorial\\learning-python\\CODE\\Application 1\\data.json"))

print(type(data))

print("Atom definition: " + str(data["atom"]))

print(data["rain"])
