students = {}
i = 1
while i <= 5:
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))

    students[name] = marks
    i = i + 1
name = input("Enter the student name to search: ")
marks = students.get(name)
if marks is None:
    print("Student not found")
else:
    print("Marks:", marks)

    # Grade classification
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")