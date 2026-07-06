print("Bitwise Operators")
#1
a = 5
b = 8
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise NOT:", ~b)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

#2
a = 5
b = 15
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise NOT:", ~b)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

#3
a = 12
b = 16
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise NOT:", ~b)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

#4
a = 11
b = 7
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise NOT:", ~b)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

#5
a = 57
b = 8
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise NOT:", ~b)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

#6
a = 1
b = 2
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise NOT:", ~b)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

#7
a = 22
b = 57
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise NOT:", ~b)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

#8
a = 9
b = 33
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise NOT:", ~b)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

#9
a = 20
b = 35
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise NOT:", ~b)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

#10
a = 3
b = 33
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise NOT:", ~b)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

#11
print("----------------")
a = 12
b = 52
print((a & b) >> (a | b))


#12 
x = 2
y = 5
print((x | y) << (x ^ y))


#13
y = 3
x = 5
print((y ^ x) & ( x ^ y))

#14
a = 5
b = 3
print((a & b) | (a ^ b))

#15
a = 23
b = 45
print((a | b) ^ (a << 2))


#16
x = 12
y = 5
print((x << 1) & (y >> 1))


#17 
c = 67
v = 34
print((c & v) << (c ^ v))


# 18
v = 12 
print((v << 2) | (v >> 2))

#19
a = 33
b = 12
print((a ^ b) & (a | b))

#20
f = 22
g = 19
print((f | g) & (f ^ g) <<(f >> 1))

print("------------------------")
print("INPUT/OUTPUT FUNCTION")
print("------------------------")

#example of escape character
print("hello\nworld")
print("hello\tworld")
print("my name is \"vedant\"")
print("It\'s my birthday today")
print("C:\\Users")
print("my name is vedant\ni am from niphad")
print("my name is vedant\ti am from niphad" )
print("All \"Students\" are important to school")
print("----------------")
print("% formating example")
x = "vedant"
print("my name is %s" %x)
age = 20
print("my age is %d" %age)
price = 99.5
print("price = %.2f"%price)
print("------------------------")
print("Dot formatting example")
print("hello {}".format("vedant"))
age = 20 
print("my age is {}".format(age))
price = 99.5
print("price = {}".format(price))
print("my age is {}".format(age))
price = 99.5
print("price = {:.4f}".format(price))
print("-----------------------------------")
print("f - string example")
name = "vedant"
print(f"my name is {name}")
age = 20
print(f"my age is {age}")
price = 99.5
print(f"price = {price:.4f}")

# if elif else 
battery = int(input("Enter battery % :  "))
if 0 < battery <= 20 :
    print("Connet charger")
elif 20 < battery <= 50 :
    print("Battery is much more")
elif  50 < battery <= 100:
    print("NO need to charge")
else :
    print("In valid Battery %")

ticket = input("Ticket (yes/no)? :")
if ticket == "yes":
    print("Ticket comformied")
elif ticket == "no":
    print("Ticket not comformied")
else :
    print("Not ticket avalible")
    
#3
num = int(input("Enter a number :"))
num1 = int(input("Enter a number :"))
if num > num1 :
    print("num is greater than num")
elif num < num1:
    print("num is smaller than num1")
else :
    print("num is equal to num1")

#4
patient= input("register (yes/no) :")
doctor = input("avaliability (yes/no) :")
if patient == "yes" and doctor == "no" :
    print("no doctor avaliable")
    if  patient == "no" and doctor == "no":
        print("No appointment")
    else :
        print("Thank you")
else :
    print("Come on next day")











