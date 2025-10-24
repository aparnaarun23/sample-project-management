# grade_calculator.py
# Program to calculate average marks and assign grade

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

marks = []
num_subjects = int(input("Enter number of subjects: "))

for i in range(num_subjects):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

average = sum(marks) / num_subjects
grade = calculate_grade(average)

print(f"\nAverage: {average:.2f}")
print(f"Grade: {grade}")
