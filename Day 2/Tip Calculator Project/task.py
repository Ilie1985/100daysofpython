print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15\n "))
percentage_tip = tip / 100
people = int(input("How many people to split the bill?\n"))
amount_to_pay= (bill/people) * percentage_tip
rounded_sum=round(amount_to_pay,2)
splited_bill_plus_tip = bill / people + amount_to_pay
print(f"The amount of money that everyone should pay is ${ splited_bill_plus_tip} ")


