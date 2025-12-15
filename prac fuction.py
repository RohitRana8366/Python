#WAP to print the length of a list.(list the parameter)
list=[1,2,3,4,5,6]

def lengthlist(list):
    print(len(list))
    
print(lengthlist(list))




#print list in the single line
def lengthlist1(list):
    for item in list:
        print(item,end="")#printing our elements of list h bha
    print(len(list))
    
print(lengthlist1(list))