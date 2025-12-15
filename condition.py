#conditional concept(if-elif-else)
#this is even or odd with using if else
#greatest of three number enter by the user
print("enter your three number ")
num1=int(input("enter your first number= "))
num2=int(input("enter your second  number= "))
num3=int(input("enter your third number= "))
if(num1>num2 and num1>num3):
    print("your biggest number is this",num1)
if(num2>num1 and num2>num3):
    print("your biggest number is this",num2)
else:
    print("your biggest number is this",num3)

