#5 example of AND operator

print("LOGICAL OPERATORS AND")


age = 20
has_id = True
print(age >= 18 and has_id)

#
age = 16
has_permission = True
print(age >= 18 or has_permission)
 
 #

username = "Vedant"
password = "python123"
print(username == "Vedant" and password == "python123")

#
x = 5
print(x > 10 or x == 5)


print("LOGICAL OPERATORS OR")

#1
a = 5

if a == 5 or a == 10:
    print("Correct")

    #2
    x = 10

if x > 5 or x < 0:
    print("Yes")

    #3
    name = "Ram"

if name == "Ram" or name == "Ravi":
    print("Welcome")
     

    #4
    num = 7

if num == 5 or num == 7:
    print("Match")

    #5
    color = "Red"

if color == "Blue" or color == "Red":
    print("Found")

print("LOGICAL OPERATORS NOT")

#1
x = 5

if not x == 10:
    print("Correct")

#2
y = 15

if not y < 10:
    print("Yes")

#3
z = "Hello"

if not z == "World":
    print("Match")

#4
a = 20

if not a == 25:
    print("Found")

#5
b = False

if not b:
    print("Correct")
