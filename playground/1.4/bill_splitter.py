total_bill_amount = int(input("Enter the total bill amount: "))
number_of_people = int(input("Enter the number of people sharing it: "))

share = total_bill_amount // number_of_people

tip_request = input("Dyou want to include a 10% tip (yes/no): ")
if tip_request == "yes":
  share += share * 0.1

print(f"Bill amount per person: ${share}")
