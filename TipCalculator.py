bill_total = float(input("Enter the total amount: "))
tip_percentage = float(input("Enter the tip percentage: "))

print(f"Your tip amount is: {bill_total * (tip_percentage/100)}")
