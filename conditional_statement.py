#1 
age =int(input("Enter your age :"))
if age >= 18:
    print(" your are eligible to vote")

#2
marks = int(input("Enter your marks :"))
if marks >= 90:
    print("Passed")
#3
num = int(input("Enter a number :"))
if num > 0 :
    print("number is postive")

#4
stock = int(input("Enter stock quantity :"))
if stock > 0 :
    print("Product is in stock")

#5
age = int(input("Enter your age :"))
if age >= 18 :
    print("ADult")

#6
temp = float(input("Enter temperature :"))
if temp > 100:
    print("Temperature is above 100.")


#7
salary = int(input("Enter you'r salary :"))
if salary > 50000:
    print("you'r salary is greater than 50,000")

# if else
print("if else statement")

#1
num = int(input("Enter a number :"))
if  num > 0:
    print("Number is positive")
else:
    print("Number is negative")

#2


num = int(input("Enter a number :"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3
age = int(input("Enter your age :"))
if age >= 18 :
    print("You'r eligible for vote")
else :
    print("You'r are not eligible vote")
    
#4
marks = int(input("Enter you'r marks :"))
if marks >= 35 :
    print("Passed")
else :
    print("Failed")

#5
user = int(input("Enter balance :"))
payment = int(input("Enter payment amount : ")) 
if user >= payment :
    print("Payment successful")
else:
    print("Insufficient Balance")

#6
stock = int(input("Enter quantity : "))
if stock > 0 :
    print("available in stock")
else :
    print("Not in stock")

#7

temp = float(input("Enter body temperature : "))
if temp >= 100 :
    print("fever")
else :
    print("Normal")

#if- elif - else 
print("if- elif - else")

#1
marks = int(input("Enter Marks : "))
if marks > 90 :
    print("Grade A")
elif marks > 75 :
    print("Grade B")
elif marks > 60 : 
    print("Grade C")
elif marks > 35 :
    print("Grade D")
else :
    print("Failed")

#2
age = int(input("Enter age : "))
if age <= 12:
    print("Child")
elif age <= 19 :
    print("Teenager")
elif age <= 59 :
    print("adult")
else :
    print("senior citizen")

#3
signal = input("Enter a signal red/yellow/green : ")
if signal == "red" :
    print("Stop")
elif signal =="yellow" :
    print("Get Ready")
elif signal == "green" :
    print("GO")
else :
    print("NO Signal")

#4
temp = int(input("Enter temperature : "))
if temp < 20 :
    print("Cold")
elif temp < 30 :
    print("Warm")
elif temp < 50 :
    print("Hot")
else :
    print("Very hot")

#5
points = int(input("Enter points: "))
if points >= 1000:
    print("Platinum")
elif points >= 700 :
    print("Gold")
elif points >= 400 :
    print("Silver")
else :
    print("Regular")


# Nested if 
print("Nested if")
#1

attendence = int(input("Enter attendence (%): "))
fees = input("fees Paid? (yes/no :)")
if attendence >= 75 or fees == "yes" :
    print("you are eligible for exam")
else : 
    print("Not eligible")

#2
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Login")


#3
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Login")


#4
card = input("Card Inserted? (yes/no): ")
pin = int(input("Enter PIN: "))

if card == "yes" and pin == 1234:
    print("Access Granted")
else:
    print("Access Denied")

#5
marks = int(input("Enter marks: "))
documents = input("Documents Verified? (yes/no): ")

if marks >= 60 and documents == "yes":
    print("Admission Confirmed")
else:
    print("Admission Denied")

#6
stock = input("Product Available? (yes/no): ")
payment = input("Payment Successful? (yes/no): ")

if stock == "yes" and payment == "yes":
    print("Order Confirmed")
else:
    print("Order Failed")

#7
registered = input("Registered? (yes/no): ")
doctor = input("Doctor Available? (yes/no): ")

if registered == "yes" and doctor == "yes":
    print("Appointment Confirmed")
else:
    print("Appointment Not Possible")




