# when a function calls itself
def show(n):
    if(n==0):
        return
    print(n) 
    show(n-1)
    print("END")


show(3)


#understand this factorial  concept by recursion
n=int(input("enter one number for finding that factorial"))

def fact(n):
    if(n==1 or n==0):
     return 1
    return n*fact(n-1)

print(fact(n))




# Question write a recursive function to calculate the sum of first n natural numbers
def calcsum(n):
   if(n==0):
      return 0
   return calcsum(n-1)+n

sum=calcsum(10)
print(sum )


#write a recursive function to print all elements in a list.
#hint:use list &index as parameters
def printlist(list,idx=0):
   if(idx==len(list)):
      return
   print(list[idx])
   printlist(list,idx+1)


fruits=("mango","litchi","apple","banana")

printlist(fruits)