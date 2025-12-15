student={
    "name":"rahul kumar",
    "subjects":{
        "physics":97,
        "chem":98,
        "maths":95
    }
}
print(student)
#nested dictionary 
print(student["subjects"]["chem"])
#dictionary methods
print(student.keys())
print(student.values())
print(student.items())
print(student.get("subjects"))
student.update({"city":"delhi"})
print(student)


# practice question
#store following word meanings in a python dictionary
dictionary={
    "table":["a piece of furniture","list of fact and figures"],
    "cat":"a small animal"
}
print(dictionary)

# you are given a list of subjects for students.assume one classroom is require for 1 subject. how manyclassroom needed by all students
def min_classrooms_required(subjects):
    unique_subjects=set(subjects)
    return len(unique_subjects)
subjects=["maths","science","english","maths","science","history"]
min_classrooms=min_classrooms_required(subjects)
print("minimum number of classroom required",min_classrooms)


#create sets
subjects={
    "python","java","c++","python","javascript","java",
    "python","java","c++","c"
}
print(subjects)
print(len(subjects))


#figure out a way to store 9 & 9.0 as seprate values in the sets.
#(you can take help of built in data types)
values={9,9.0}
print(values)


#wap to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dict and add one by one.use subject name as key and marks as value
dict={}
x=int(input("enter your physics marks"))
dict.update({"physics":x})
x=int(input("enter your maths marks"))
dict.update({"maths":x})
x=int(input("enter your chemistry marks"))
dict.update({"chemistry":x})


