#arthematic operator
a= 10
b= 3

print("Addition:", a + b)
print("Subtraction:", a - b)    
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b )
print("remainder:", a % b)




#simple caluculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#students marks caluculator
name = input("Enter student name: ")
m1 = int(input("Enter python marks : "))
m2 = int(input("Enter java marks : "))
m3 = int(input("Enter SQL marks : "))

total = m1 + m2 + m3
average = total / 3

print("\n----- Student Report -----")
print("Name:", name)
print("Total:", total)


#shopping bill caluculator
price1 = float(input("Enter product 1  price : "))
price2 = float(input("Enter product 2  price : "))
price3 = float(input("Enter product 3  price : "))

total = price1 + price2 + price3

discont = total * 0.10
final_price = total - discont

print("discont:", discont)
print("Final Price:", final_price)
print("Total bill :", total)


#comparion operators
a = 10
b = 20


print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#login 
correct_username = "admin"
correct_password = "1234"


username = input("Enter username: ")
password = input("Enter password: ")

print(username == correct_username )
print(password == correct_password)


#assignment operators
x=10

x +=5
print(x)

x -=2
print(x)

x *=3
print(x)

#age eligibility checker
age = int(input("Enter your age: "))
print("Eligible" , age >= 18)

#PASS OR FAIL CHECKER
marks = int(input("Enter your marks: "))

print("Passed" , marks >= 40)
