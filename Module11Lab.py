# Exercise 9.1
 with open('grades.txt', mode='a') as grades:
   ...:     while True:
   ...:         grade = input("Please enter your grade, type 'done' to quit: ")
   ...:         if grade.lower() == 'done':
   ...:             break
   ...:         try:
   ...:             grade = float(grade)
   ...:             grades.write(f'{grade}\n')
   ...:         except ValueError:
   ...:             print("Invalid input, it's gotta be a number or the word 'done'")
   ...:
# Exercise 9.2
with open('grades.txt', mode='r') as grades:
    ...:     google = grades.read().splitlines()
    ...:     print('Grades:')
    ...:     for grade in google:
    ...:         print(grade)
    ...:     grades_float = [float(grade) for grade in google]
    ...:     total = sum(grades_float)
    ...:     count = len(grades_float)
    ...:     average = total / count
    ...:     print(f'\nTotal: {total}')
    ...:     print(f'Count: {count}')
    ...:     print(f'Average: {average:.2f}')
    ...:
# Exercise 9.3

import csv

with open('grades.csv', mode='w', newline='') as grades:
    writer = csv.writer(grades)
    
    # Write the header
    writer.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])
    
    # Gathers student input
    while True:    
        firstname = input('Input the students first name, or type "done" to quit: ')
        if firstname.lower() == 'done':
            print ("exiting")
            break
        lastname = input ("Input the students last name: ")

# Gathers exam input 
        try:
            exam1 = int(input("Enter the grade for Exam 1: "))
            exam2 = int(input("Enter the grade for Exam 2: "))
            exam3 = int(input("Enter the grade for Exam 3: "))
        except ValueError:
                print("Incorrect value, please enter a valid integer for the exam grade") 

# Writes the content to the CSV file
    writer.writerow([firstname, lastname, exam1, exam2, exam3])
    print("Recorded successfully")
