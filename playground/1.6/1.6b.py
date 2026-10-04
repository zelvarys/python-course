number = 100
count = 0

while number > 1:
  number /= 2
  print(f"Current number: {number}")

  count += 1
  print(f"Current count: {count}")

print(f"\nNumber: {number}")
print(f"Total count: {count}")
