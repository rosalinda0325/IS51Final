"""
This program will display the number of grades, the average grade and the percentange 
of grades that are above average grade.

We will open the file Final.txt
The code will read and copy the file then close it.
This program will output 3 function statements, 1) number of grades, 2)average grade 
3) percentage of grades above average

A main function will be created to initialize the application.
A function names calculate_percent_above_average will be created to calculate the 
percentage of the average grade.


"""
"""
initiate
main()
open final.txt in #read

function1
grade = int(grade)

function2
average =sum (grade) / length (grade)
num = 0

function3 
if grade > average
num += 1

print(" ")

main()

"""

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0
for grade in grades:
    if grade > average:
        num += 1
    print("Number of Grades: ", len(grades))
    print("Average grade: ", average)
    print("Percentage of grades avbove average: , {0:.2f}%".format(100 * num / len(grades)))
