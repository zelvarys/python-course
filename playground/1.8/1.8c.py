days = ["Mon", "Tue", "Wed"]
high_temps = [72, 75, 68]

for day, temp in zip(days, high_temps):
  print(f"{day}: {temp}°F")

for index, day in enumerate(days, start=1):
  print(f"{index}. {day}")
