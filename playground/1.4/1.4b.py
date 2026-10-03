is_raining = True
has_umbrella = True

if not is_raining or (is_raining and has_umbrella):
  print("I will stay dry")


# second expression
has_item = True
logged_in = False
is_guest = True

if has_item and (logged_in or is_guest):
  print("Checkout")
