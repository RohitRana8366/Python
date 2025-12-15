#waf to find the factorial of n.(n is parameter)
# this is our basic logic to calculate factorial by loop
n=5
fact=1
for i in range (1,n+1):
    fact=fact*i
print(fact) 

#this is our main logic to calculate factorial
# function creation
def calculatefact(n):
    n=int(input("enter a number for n="))
    fact=1
    for i in range(1,n+1):
        fact= fact*i
    print(fact)

# calling our function
calculatefact(6)


# waf to convert USD to INR
def converter(usd):
    inr=usd*83
    print(usd,"usd=",inr,"inr")
      

converter(3)




    
 