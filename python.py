has_card = False
has_cash = True
print(has_card or has_cash)

is_logged_in = True
print(not is_logged_in)


#atm eligibility cheecker
balance = 10000
withdraw_amount = 5000
print(withdraw_amount > 0 and withdraw_amount <= balance)


#student scholar ship eligibility checker
marks = float(input("Enter your marks: "))
attendance = float(input("Enter attendance: "))
eligible = marks >= 80 and attendance >= 75
print("scholarship Eligible:", eligible)

#identity operator
a= None

print(a is None)
print(a is not None)

#bit wise operator
a = 5
b = 3

print(a & b) 
print(a | b)
print(a ^ b)

#electricity bill calculator
units = int(input("Enter electricity units: "))

rate = 6
bill = units * rate
print("Electricity Bill: ", bill)

#travel expense calculator
travel = float(input("Travel expense: "))
food = float(input("Food expense: "))
hotel = float(input("Hotel expense: "))
total = travel + food + hotel
print("Total Expense: ", total)