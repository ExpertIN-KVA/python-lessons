# import array

# my_array = array.array(["anastasios", "alkmini"])

# my_array = ["anastasios", "alkmini"]


# tuples - Πλειάδες
# my_tuple = (0, 1, 2, 3)

# # not
# # my_array = [1, "konstantinos", True]
# # my_tuple = (1, "konstantinos", True)


# # dictionaries - Λεξικά
# my_dict = {
#     "name": "anastasios",
#     "surname": "tsalmas",
#     "date_of_birth": "30-11-2004",
#     "age": 20,
#     "python": True,
# }

# # print(my_dict["age"])
# # print(my_dict.get("python"))

# my_dict["age"] += 1

# print(my_dict.get("age"))

# my_dict["city"] = "Kavala"
# del my_dict["date_of_birth"]


# people_count = [
#     {"name": "panagiotis", "surname": "christou", "python": True, "c++": False},
#     {
#         "name": "nikos",
#         "surname": "limpanovnos",
#         "languages": {
#             "python": True,
#             "javascript": True,
#         },
#     },
# ]


# people_count[0].get("name")


# # my_array = ["nikos", "limpanovnos"]
# # my_array2 = ["limpanovnos", "nikos"]

# nikos = {
#     "name": "nikos",
#     "surname": "limpanovnos",
# }

# nikos2 = {
#     "surname": "limpanovnos",
#     "pyton": True,
#     "java": True,
#     "age": 25,
#     "name": "nikos",
# }


# print(nikos.get("name"))
# print(nikos2.get("name"))


people = []
while True:
    people.append({})
    last_index = len(people) - 1

    people[last_index]["name"] = input("Give me your name: ")
    people[last_index]["surname"] = input("Give me your name: ")
    people[last_index]["age"] = int(input("Give me your name: "))

    # new_dict = {}
    # new_dict["name"] = input("Give me your name: ")
    # new_dict["surname"] = input("Give me your name: ")
    # new_dict["age"] = int(input("Give me your name: "))
    # people.append(new_dict)

    continue_answer = input("Do you want to continue? (yes/no): ")
    if continue_answer == "no":
        break


print("Persons data")
for person in people:
    print(
        "Name: "
        + person.get("name")
        + " - Surname: "
        + person.get("surname")
        + " - Age: "
        + str(person.get("age"))
    )


# for i in range(0, len(people)):
#     print(
#         "Name: "
#         + people[i].get("name")
#         + " - Surname: "
#         + people[i].get("surname")
#         + " - Age: "
#         + str(people[i].get("age"))
#     )


print("Tickets sold: ")
# 1. <vehicle_type> - <meters_long> - <cost_for_vehicle> - <seat> - <cost_for_seat> - <total> - <discount> - <fpa> - <total_after_disc_and_fpa>
