print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? "))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip = bill * 12 / 100
total = bill + tip
bill_per_person = total / num_people

print(f"Each person should pay: {bill_per_person:.2f}")
