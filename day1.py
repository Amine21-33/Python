# EX1
# name = (" aMiNe elJiD ")
# name = name.strip()
# print(name.title())

# EX2
# fruit = input("Enter a word: ")

# print(f"\nReserved: {fruit[::-1]}")
# print("Number of 'a': ", fruit.lower().count("a"))

# EX3
# grades = [12, 7, 18, 9, 15, 7]

# print("Unique sorted grades: ", sorted(set(grades)))
# print(f"Average:  {sum(grades)/len(grades):.2f}")
# print("Highest grade: ", max(grades))
# print("Lowest grade: ", min(grades))

#EX4
# class_a = ["Amine", "Sara", "Youssef", "Sara"]
# class_b = ["Sara", "Omar", "Amine", "Omar"]
# stc = sorted(set(class_a) & set(class_b))
# print(f"Common students: {stc}")

# #EX5
# students = {
#     "S001": {"name": "Amine", "grades": [15, 17, 14]},
#     "S002": {"name": "Sara", "grades": [18, 19, 17]},
#     "S003": {"name": "Youssef", "grades": [10, 12, 9]}
# }

# nametop = ""
# current_average = 0

# for key, value in students.items() :
#     print(value["name"], ":", sum(value["grades"])/len(value["grades"]))


#     if current_average < sum(value["grades"])/len(value["grades"]):

#         nametop = value["name"]
#         current_average = sum(value["grades"])/len(value["grades"])


# print(f"Top student: {nametop}: {current_average:.2f}" )

#EX6
# list50 = []
# multi = {}
#             Method 1:
# # for i in range(1, 51):
# #     if i % 3 == 0 and i % 5 == 0:
# #         list50.append(i)
# # print(list50)
# # for x in list50 :
# #     multi[x]= x**3
# # print(multi)
# for i in range(1, 51):
#     list50.append(i)
#             Method2
# result = [i for i in list50 if i % 3 == 0 and i % 5 == 0]
# print(result)
# multi = {i: i ** 3 for i in list50 if i % 3 == 0 and i % 5 == 0}
# print(multi)
