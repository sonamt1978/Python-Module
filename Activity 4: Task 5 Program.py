import random

students = ["Karma","Pema Dorji","Yeshika","Amit"]
random.shuffle(students)
print(students)
for i in range(0,len(students)):
    print("Group {} captain {}".format(i+1,students[i]))
