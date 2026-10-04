number = 34
attempts = 0

while True:
  guess = int(input("Guess the number: "))
  attempts += 1

  if guess < number:
    print("Too low, try agaim!")
  elif guess > number:
    print("Too high, try again!")
  else:
    break
print(f"Correct! The number is {number}")


for i in range(5, 0, -1):
  print(i)
print("Go!")


