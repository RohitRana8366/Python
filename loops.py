#print the elements of the following list using a loop
# 1 4 9 16 25 36 49 64 81 100
number=[1,4,9,16,25,36,49,64,81,100]
index=0
while index<len(number):
    print(number[index])
    index=index


    #search for a number using loop 
    nums=(1,4,9,16,25,36,49,64,81,100) 
    idx=0
    while idx<len(nums):
        print(nums[idx])
        idx=idx+1


#WAP to find the sum of first n numbers.(using while)
n=5
sum=0
for i in range(1,n+1):
      sum+=i
print('total sum is=',sum)