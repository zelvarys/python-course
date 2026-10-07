scores = [19, 16, 20, 13, 11]
print(f"The current scores are: {scores}")
new_score = int(input("Enter a fifth score: "))
scores.append(new_score)

# remove minimum score
minimum_score = sorted(scores)[0]
scores.remove(minimum_score)
print("Minimum removed: ", scores)

# copy and sort
sorted_copy = sorted(scores.copy())
print(f"Original: {scores}")
print(f"Sorted Copy: {sorted_copy}")

# calculate average
total_score = 0
for score in scores:
  total_score += score
average_score = total_score / len(scores)

lowest, highest = sorted_copy[0], sorted_copy[-1]
print("Lowest score: ", lowest)
print("Highest score: ", highest)
