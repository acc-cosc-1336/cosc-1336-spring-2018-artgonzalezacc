from src.homework.homework4 import get_credit_points
from src.homework.homework4 import get_grade_point_average
from src.homework.homework4 import get_grade_points
from src.homework.homework4 import valid_letter_grade


'''
Use the functions from homework4 to...
Write code to prompt the user for number of students and grades.
Create a nested loop to collect letter grades and credit hours for each student.
Validate the letter grade is in accepted range if not prompt user for letter again.
From the letter grade, get the credit points for that class.
Calculate grade points (How? Research GPA calculation).
Sum grade points and credit hours for each student.
Calculate GPA for each student.
Display Student 1(etc) GPA is 3.77. Format the GPA to two values.
'''

def main():

    students = int(input("Enter number of students: "))
    grades = int(input("Enter number of grades: "))

    for student in range(1, students + 1):

        grade_points_total = 0
        credit_hours_total = 0

        print("\nCollect data for Student ", student, '\n')

        for grade in range(grades):

            letter_grade = input("Enter letter grade: ")

            while not valid_letter_grade(letter_grade):
                print("Letter grade invalid...")
                letter_grade = input("Enter letter grade: ")

            credit_points = get_credit_points(letter_grade)

            credit_hours = int(input("Enter credit hours: "))

            grade_points_total += get_grade_points(credit_hours, credit_points)
            credit_hours_total += credit_hours
            print()

        gpa = get_grade_point_average(credit_hours_total, grade_points_total)
        print("Student", student, "GPA is", format(gpa, '.2f'), '\n')


main()
