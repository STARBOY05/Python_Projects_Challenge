print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? ₹"))
people = int(input("How many people to split the bill? "))
payment = (bill/people)
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip = payment * (tip_percent/100)
total_payment = round(payment + tip,2)
print(f"Each person should pay: ₹{total_payment}")