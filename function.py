#functions-fn is used for makes block of statements that perform a specific task
def calculatesum(a,b):
    s=a+b
    return s


sum=calculatesum(1,2)
print(sum)


def calcaverage(a,b,c):
    sum=a+b+c
    average=sum/3
    print("your average is=",average)
    return average

print(calcaverage(2,4,6))
print('')