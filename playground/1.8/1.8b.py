original = [8, 7, 5]

broken_copy = original
real_copy = original.copy()

broken_copy.append(12)
real_copy.append(13)

print(original)
print(broken_copy)
print(real_copy)
