# file = open("lesson.txt", "r")
# print(file.read())


# lines = []
# with open("lesson.txt", "r") as file:
#     lines = file.readlines()


# for i in range(0, len(lines)):
#     print(lines[i])


# with open("lesson.txt", "w") as file:
#     file.write("New content")


# with open("lesson.txt", "a") as file:
#     file.write("\nNikos")


# file.close()


import os

if os.path.exists("lesson.txt"):
    print("File exists")


string1 = "nikos alkmini konstantinos"
str_array = string1.split(" ")
