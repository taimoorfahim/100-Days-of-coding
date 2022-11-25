print("welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
tip_percentage=int(input("What percentage tip would you like to give? 10, 12, 15 or other? "))
split_bill=int(input("How people to split the bill? "))

tip=total_bill*(tip_percentage/100)
new_total_bill=tip+total_bill

bill_pay=round(new_total_bill/split_bill, 2)

print(f"Each person should pay: ${bill_pay}")