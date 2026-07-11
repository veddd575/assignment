#Assignment 1
print("range() function")
l1 = list(range(1,11))
print(l1)

#2
l2 = list(range(20,0,-1))
print(l2)

#3
l3 = list(range(2,51,2))
print(l3)


#4
l4 = list(range(1,51,2))
print(l4)


#5
l5 = list(range(7,71,7))
print(l5)

#6
l6 = list(range(100,0,-10))
print(l6)

#7
l7 = list(range(0,101,5))
print(l7)


#for loops
print("For loop")

#1
for i in range (10):
    print("vedant")


#2
for i in range(1,101):
    print(i)

#3
for i in range(1,11):
    print(i**2)

#4
for i in range(1,11) :
    print(i**3)


#5
total = 0
for i in range(1,101):
    total += i
print("Sum =",total)

#6
count = 0
for i in range(1,51):
    if i % 3 == 0:
        count = count + 1
print("divisible by 3:",count)

#7
for i in range(10,0,-1):
    print(i)


#8
text= "FutureBright"
for  ch in  text :
    if ch in "aeiou":
        print(ch)


#9
number = [25,67,12,98,45]
largest = number[0]
for num in number :
    if num > largest :
        largest = num
print(largest)

#10 
marks1 = [45,78,90,34,88,51]
for i in marks1 :
    if i > 50 :
        print(i)


#while loop
print("While loop")
count = 1
while count <= 20 :
    print(count)
    count += 1

#2
num = 20
while num >= 1:
    print(num)
    num = num - 1

#3
num = 1
while num <= 50 :
    if num % 2 == 0 :
        print(num)
    num = num + 1



#4 
print("-----------------")
num = 1
while num <= 10:
    print(num * 9)
    num = num + 1


#5
num = 1
while num <= 10 :
    print(num * 10)
    num = num + 1

#6
count = 10
while count >= 1 :
    print(count)
    count = count - 1
print("Happy New Year")



#7
balance = 5000
while balance > 0 :
    print("current balance :",balance)
    balance = balance - 500
    print("remaining balance",balance)
    print()


#8
# password = ""
# while password != "python123" :
#     password = input("Enter a password :")
#     if password != "python123" :
#         print("Wrong password .Try again")
# print("log in successfully")


#Assignemnt 4
marks = [78,56,89,91,45,62,98]
print(marks)

#2
total = 0
for mark in marks :
    total = total + mark 
print("Total Marks :",total)


#3
total = 0
for mark in marks :
    total = total + mark 
print("Total Marks :",total)
avarage = total / len(marks)
print("Total avarage :",avarage)


#4
count = 0 
for mark in marks :
    if mark > 75 :
        count = count + 1
print("Student score above 75: ",count)

#5
count = 0
for mark in marks :
    if mark % 2 == 0 :
        print(mark)

#6
count = 0
for mark in marks :
    if mark % 2 != 0 :
        print(mark)

#7
largest = marks[0]
for mark in marks :
    if mark > largest :
        largest = mark
print("Higest score :",largest)


#8 
lowest = marks[0]
for mark in marks :
    if mark < lowest :
        lowest = mark
print("Lowest marks :",lowest)

#9
count = 0 
for mark in marks :
    if mark < 50 :
        count = count + 1
print("Student score above 50: ",count)


print("------------------")

count = 0
for mark in marks :
    if mark >=90 :
         print(mark,"GRADE A")
    elif mark >= 74 :
         print(mark,"GRADE B")
    elif mark >= 50:
         print(mark,"GRADE C")
    else :
         print(mark,"fail")



#5 Nested loop 
print("Nested loop")
for i in range(4):
    for j in range(4):
        print("*",end = " ")
    print()

print("-----------------")
#2
for i in range(1,6):
    for j in range(i):
        print("*",end= " ")
    print()


#3
row = 5
for i in range(1,row+1):
    for space in range(row-i) :
        print("",end = "")
    for star in range(2 *(row - i)-1):
        print("*",end = "")
    print()


#4
for i in range(1,6):
    for j in range(1,i):
        print(j,end=" ")
    print()


#5
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end = " ")
    print()


#6
shirts = ["Red","Blue","Black"]
pants = ["jeans","Formal"]
for i in shirts :
    for j in pants:
        print(i ,"-", j)

#7
for i in range(1,4):
    for j in range(1,6):
        print("row",i,"seat",j)
    print()

#Assignment 6
print("Mixed practise")


#1
number =[12,-5,18,-20,34,-7,0]
count = 0
for i in number:
    if i < 0:
        count = count + 1
print("Negavtive number :",count)



#2
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0 :
        print(i)
    

#3
# num = int(input("Enter a number: "))

# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial =", fact)


#4
text = "Python"
print(text[::-1])

#5
number = [12,17,24,3,40,55]
total = 0 
for i in number :
    total = total + i 
print("Total Sum:",total)

#6
row = 5
for i in range(1,6):
    for j in range(i):
        print(i,end = " ")
    print()


#7
row = 5
ch = 65


    




    
    










