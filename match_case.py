#Assignment 1 :
employee = {}
if employee :
    print("Record found")
else :
    print("No record found")

# Assignment 2
color = input("Enter signal colour :")
match color :
    case "red":
        print("Stop")
    case "yellow":
        print("Get ready")
    case "Green" :
        print("Go")
    case _ :
        print("Invalid signal")

#Assignment 3
print("1.Addition")
print("2,Subtraction")
print("3.Multiplication")
print("4.Division")
choise = int(input("Enter your choise :"))

num = int(input("Enter first number :"))
num1 = int(input("Enter second number :"))
match choise :
    case 1:
        print("Answer =",num + num1)
    case 2:
        print("Answer =",num - num1)
    case 3 :
        print("Answer =",num * num1)
    case 4 :
        print("Answer =",num / num1)
    case _:
        print("Invalid number")

#Assigment 4
print ("1.deposite")
print("2.Withdraw")
print("3.Check balance")
print("4.Exit")
choise = int(input("Enter your choise"))
match choise :
    case 1:
        print("Deposite amount :")
    case 2 :
        print("How much amount want to withdraw :")
    case 3:
        print("check balance")
    case 4 :
        print("Thank you")
    case _:
        print("Invalid selection")

#Assignment 5 
print("1.pizza")
print("2.Burger")
print("3.sandwich")
print("4.pasta")
choise = int(input("Enter your choise"))
match choise :
    case 1:
        print("Pizza ordered ")
    case 2 :
        print("Burger ordered")
    case 3 :
        print("Sandwich ordered")
    case 4 :
        print("Pasta ordered")
    case _ :
        print("please Order")


#Assignent 6
grade = input("Enter yours grade :")
match grade :
    case "A" :
        print("Excellent")
    case "B" :
        print("Best")
    case "C" :
        print("Better")
    case "D" :
        print("Good")
    case "F":
        print("Fail")

#assignment 7
account = input("Is your account is active?(yes/no) :")
kyc = input("Is your kyc completed? (yes/no) :")
deposit = int(input("Enter deposit amount :"))
if account == "no" :
    print("deposit rejected")
elif kyc == "no" :
    print("first complete your kyc")
elif deposit <= 0 :
    print("Invalid deposit amount")
elif deposit > 200000 :
    print("maneger approval requried")
elif deposit > 50000 :
    print("Pan verification requried")
else :
    print("Successfully deposit")

#Assignment 8
username = input("Enter username :")
password = int(input("Enter password :"))
otp= input("verified ?(true/false):")
if username == "" :
    print("Username cannot be empty")
elif password == "" :
    print("password cannot be empty")
elif otp == "true" :
    print("log in successfully")
else :
    print("login falied")



#assignment 9
course = input("Is you'r course completed?(yes/no) :")
project = input("Is you,r project submitted?(yes/no :)")
exam = input("Is you'r exam is passed?(yes/no :)")
if course == "yes" and project == "yes" and exam == "yes" :
    print("you'r certificate issued. ")
else :
    print("Certificate not issued")

# assignment 10
ticket = input("Is you'r ticket confirmed?(yes/no) :")
passport = input("Is you'r passport valid?(yes/no) :")
security = input("security check?(yes/no) :")
if ticket == "yes" and passport == "yes" and security =="yes" :
    print("satisfied")
else :
    print("deny bording")

#assignmet 11
balance = 10000

print("1. Deposit")
print("2. Withdraw")
print("3. Balance Enquiry")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:

    case 1:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit Successful")
            print("Balance =", balance)
        else:
            print("Invalid Amount")

    case 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid Amount")

        elif amount > balance:
            print("Insufficient Balance")

        else:
            balance -= amount
            print("Withdrawal Successful")
            print("Balance =", balance)

    case 3:
        if balance:
            print("Current Balance =", balance)
        else:
            print("Zero Balance")

    case 4:
        print("Thank You")

    case _:
        print("Invalid Choice")

