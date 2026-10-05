email = "ada@example.com"
username = email[:email.find("@")]
print(username)

extension = email[email.find("."):]
print(extension)
print("\n")


print(f"Email: {email}")
print(f"Username is {username} and email extension is {extension}")
