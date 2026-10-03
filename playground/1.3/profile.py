name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height (in cm): ")

# convert age and height to int
age = int(age)
height = int(height)

# print statements
print("=== Profile Card ===")
print(f"Name: {name},  Type: {type(name)}")
print(f"Age: {age} years,  Type: {type(age)}")
print(f"Height: {height}cm, Type: {type(height)}")
