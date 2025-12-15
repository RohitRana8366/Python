with open("hello.py","r")as f:
    data=f.read()
    print(data)


with open("hello.py","w")as f:
   f.write("new data")
   