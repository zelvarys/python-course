first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

username = (first_name[0] + last_name).lower()

if len(username) > 10:
  username = username[:10]

print(username)
print(username[::-1])
