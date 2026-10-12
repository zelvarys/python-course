#1
contacts = {
  "promise": {
    "phone": "08173628378",
    "email": "promislo11@gmail.com"
  },

  "akinya": {
    "phone": "07077358453",
    "email": "kolawole002@gmail.com"
  },

  "mom": {
    "phone": "08034120187",
    "email": "rosemary*75@gmail.com"
  }
}

#2
for name, contact in contacts.items():
  print(f"""Contact name: {name}
Phone number: {contact["phone"]}
Email address: {contact["email"]}\n""")

#3
user_input = input("Enter a contact name: ")
if user_input in contacts:
  print(f"Name: {user_input} | Phone: {contacts.get(user_input)["phone"]}")
else:
  print("Contact not found")

