grades = ["A", "B","A", "C", "B", "A", "B"]
grade_count = {}

for grade in grades:
  grade_count[grade] = grade_count.get(grade, 0) + 1

print(grade_count)
