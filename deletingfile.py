#search if the learning exist int he file or not
word="learning"
with open("intro.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")
        