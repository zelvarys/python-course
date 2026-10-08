person = {
  "name": "Ada",
  "age": 29,
  "city": "London"
}

print(person["name"])
print(person["age"])

print(person.get("email"))
print(person.get("email", "unknown"))
print(person.get("name", "unknown"))




place = dict(location = "Akure", distance = 23)
print(place)
