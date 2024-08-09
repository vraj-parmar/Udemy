student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.items():
    print(grades) #each item is a stored as tuple

for grades in student_grades.keys():
    print(grades)

for grades in student_grades.values():
    print(grades)

for key, value in student_grades.items():
    print(f"{key} has grade {value}")


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))