def calculate_average_grade(m1, m2, m3):
    total_marks = m1 + m2 + m3
    average_grade = total_marks / 3
    return average_grade

def display_student_info(registration_number, m1, m2, m3):
    print("Registration Number:", registration_number)
    print("Grade in Subject 1 (m1):", m1)
    print("Grade in Subject 2 (m2):", m2)
    print("Grade in Subject 3 (m3):", m3)
    average_grade = calculate_average_grade(m1, m2, m3)
    print("Average Grade:", average_grade)

# Example usage
registration_number = input("Enter registration number: ")
m1 = float(input("Enter grade in Subject 1 (m1): "))
m2 = float(input("Enter grade in Subject 2 (m2): "))
m3 = float(input("Enter grade in Subject 3 (m3): "))

display_student_info(registration_number, m1, m2, m3)
