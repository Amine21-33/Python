# Exercice 1:
"""b = int(input("Entrez un nombre: "))
a = int(input("Entrez un nombre: "))
while b < a and b != a:
    a = int(input("Entrez un nombre: "))

if a % 2 == 0:
    for i in range(a, b + 1, 2):
        print(i)
else:
    for i in range(a + 1, b + 1, 2):
        print(i)"""

# Exercice 2:
"""Methode 1:
nbr = int(input("Entrez un nombre: "))
if nbr < 10:
    print(1)
else:
    B = 1000
    i = 1
    while B >= 10 :
        B = nbr // 10
        i += 1
        nbr = B
    print(i)

Methode 2:
nbr = int(input("Entrez un nombre: "))
i = 1
nbrx = nbr
while nbrx >= 10:
    nbrx = nbrx // 10
    i += 1
print(i)""" 

# Exercice 3:
"""wohoo = -20
while wohoo < 2 :
    wohoo = int(input("Entrez un nombre: "))
is_prime = True
for i in range(1 , wohoo // 2 + 1):
    if i == 1 :
        continue
    if wohoo % i == 0 :
        is_prime = False
        break
if is_prime:
    print("Le nombre est premier")
else:
    print("Le nombre n'est pas premier")"""

# Exercice 4:
"""stg = -20
S = 0
Mnote = 0
Bonstg = 0
while stg <= 0 :
    stg = int(input("Donner le nombre de stagaires: "))
for i in range(1, stg + 1, 1): 
    note = int(input(f"Donner la note du stagiaire {i}: "))
    if note < 0 or note > 20:
        print("La note doit être comprise entre 0 et 20")
        note = int(input(f"Donner la note du stagiaire {i}: "))
    S += note
    if Mnote < note:
        Mnote = note
    if note >= 10:
        Bonstg += 1
print(f"La moyenne des notes est: {S / stg}")
print(f"La meilleure note est: {Mnote}")
print(f"Le nombre de stagiaires ayant une note >= 10 est: {Bonstg}")"""

# Exercice 5:
"""n = int(input("Entrez un nombre: "))
for i in range(1, n + 1):
    print(i * "*")"""

# Exercice 6:
"""n = int(input("Entrez un nombre: "))
for i in range(n, 0, -1):     
    print(i * "*")"""

# Exercice 7:
"""n = int(input("Entrez un nombre: "))
j = 1
for i in range(n, 0 , -1): 
    print(i * " " , j * "*")
    j += 2"""

# List 1:
"""grades = [12, 7, 16, 9, 20, 14] 
S = 0
i = 0
j = 0
hgrade = grades[0]
lgrade = grades[0]

for grade in grades:
    if grade >= 10:
        print(grade)
        i += 1
    else :
        j += 1
    if hgrade < grade:
        hgrade = grade
    if lgrade > grade: 
        lgrade = grade
    S += grade

# print(f"Sum of grades: {S}")
print(f"Average grade: {S / len(grades)}")
print(f"Highest grade: {hgrade}")
print(f"Lowest grade: {lgrade}")
print(f"Number of students who passed: {i}")
print(f"Number of students who failed: {j}")
print(f"Percentage of students who passed: {i / len(grades) * 100:.2f}%")
"""
# Dictionary 1:
students = {
    "Amine": 15,
    "Sara": 8,
    "Youssef": 18,
    "Lina": 11
}
i = 0
S = 0
hgrade = list(students.values())[0]
hstudent = list(students.keys())[0]
for student, grade in students.items():
    if grade >= 10:
        i += 1
    S += grade
    if grade > hgrade:
        hgrade = grade
        hstudent = student
for student, grade in students.items():
    print(f"{student} a obtenu la note: {grade}")

average = S / len(students)
print(f"Number of students who passed: {i}")
print(f"Average grade: {average}")
print(f"Student with highest grade: {hstudent}")

astudent = input("gimme a student name: ")
for student, grade in students.items():
    if astudent == student:
        print(f"{astudent} a obtenu la note: {grade}")
        break
else:
    print("Student not found")
is_found = False
agrade = int(input("gimme a grade: "))
for student, grade in students.items():
    if agrade == grade:
        print(f"{student} got {agrade}")
        is_found = True
if not is_found:
    print("No students found with that grade")


print(f"Students got above average grade: ")
for student, grade in students.items():
    if grade > average:
        print(f"{student} got {grade}")

new_student = input("Enter a new student name: ")
new_grade = int(input("Enter the new student's grade: "))
for student, grade in students.items():
    if new_student == student:
        students[student] = new_grade
