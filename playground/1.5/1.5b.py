temperature = int(input("Enter the temperature (in fahrenheit): "))

if temperature <= 32:
  print("Freezing")
elif temperature <= 60:
  print("Cold")
elif temperature <= 80:
  print("Mild")
else:
  print("Hot")
