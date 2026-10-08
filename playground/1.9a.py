book = dict(title = "Naruto Shippuden", author = "Kishimoto", year = 2007)
print(book.get("publisher", "Unknown"))

if "title" in book:
  print(book["title"])
else:
  print("Title not provided!")
