user_age = int(input("Enter your age: "))

weekday_input = input("Is it weekday? (yes/no): ")
is_weekday = True if weekday_input == "yes" else False

if user_age < 13:
  ticket_price = 8
elif user_age <= 64:
  ticket_price = 15
else:
  ticket_price = 10

if is_weekday:
  ticket_price -= 2

message = "Discount applied" if is_weekday else "Full Price"

print(f"Price: {ticket_price}.  Message: {message}")
