# Dictionary 1:

students = {
    "Amine": 15,
    "Sara": 8,
    "Youssef": 18,
    "Lina": 11
}

# 1. Search for a student by name
astudent = input("Enter a student name: ")

for student, grade in students.items():
    if astudent.lower() == student.lower():
        print(f"{student} obtained the grade: {grade}")
        break
else:
    print("Student not found.")

# 2. Search for students by grade
is_found = False
agrade = int(input("Enter a grade to search for: "))

for student, grade in students.items():
    if agrade == grade:
        print(f"{student} got {agrade}")
        is_found = True

if not is_found:
    print("No students found with that grade.")

# 3. Add a new student or update an existing student's grade
new_student = input("Enter student name: ").strip()
new_grade = int(input("Enter student grade (0-20): "))

while new_grade < 0 or new_grade > 20:
    print("Invalid grade. Enter a grade between 0 and 20.")
    new_grade = int(input("Enter student grade (0-20): "))

if new_student in students:
    students[new_student] = new_grade
    print("Student grade updated!")
else:
    students[new_student] = new_grade
    print("New student added!")

# 4. Delete a student
del_student = input("Enter student name to delete: ").strip()

if del_student in students:
    del students[del_student]
    print(f"Student {del_student} deleted.")
else:
    print("Student not found.")

# 5. Display the final list of students
print("\n--- Final Student List ---")

for student, grade in students.items():
    print(f"{student}: {grade}/20")

# 6. Calculate statistics
print("\n--- Statistics ---")

number_students = len(students)

if number_students == 0:
    print("No students in the dictionary.")
else:
    total = 0
    passed = 0

    # Initialize highest grade using the first student
    hstudent = next(iter(students))
    hgrade = students[hstudent]

    for student, grade in students.items():
        total += grade

        if grade >= 10:
            passed += 1

        if grade > hgrade:
            hgrade = grade
            hstudent = student

    average = total / number_students
    failed = number_students - passed

    print("\nStudents above average:")
    for student, grade in students.items():
        if grade > average:
            print(f"{student}: {grade}")

    print(f"\nNumber of students: {number_students}")
    print(f"Average grade: {average:.2f}/20")
    print(f"Number of students who passed: {passed}")
    print(f"Number of students who failed: {failed}")
    print(f"Highest grade: {hstudent} with {hgrade}/20")
