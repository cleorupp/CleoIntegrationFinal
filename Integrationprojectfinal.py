# Cleo Rupp
# Integration project about applying what I have learned in my COP1500 course.
# This  program is created to navigate notes and grades.
# https://www.studytonight.com/post/the-sep-and-end-parameters-in-python-print-statement

print("Hello!")
print("Welcome to Cleo's Integration Project!")
print("This is where you will apply what you have learned in COP1500",
      " to navigate One Note.", sep='')

notes = input("What notes are you looking for? ")
print("You are looking for", notes, "notes.")
print("")
print("Some basic calculations are needed in order to access what you need.")
print("Please fill out the following below.")
while True:
    try:
        first_number = int(input("Enter a whole number: "))
        break
    except ValueError:
        print("Error. Must be a whole number.")


num1 = int(first_number)
num2 = int(second_number)


print("The power of the first number to the second number equals to")
print(num1 ** num2)

print("Multiply the first number to the second number equals to")
print(num1 * num2)

print("Dividing the first number to the second number equals to")
print(num1 / num2)

print("The remainder of the first and second number equals to")
print(num1 % num2)

print(
    "Diving the 1st number to the 2nd number with rounded division equals to")
print(num1 // num2)

print("Adding the first number and the second number together equals to")
print(num1 + num2)

print("Subtracting the first number to the second number equals to")
print(num1 - num2)

course_label = "COP"
course_number = "1500"
course_name = course_label + course_number
print("Learning the following Python Code in my", course_name,
      "course. I am applying the new")
print("knowledge into creating this program.")
print("")

print("I have been struggling to understand the coding concept")
print(
    "but after this project and putting it together I think I'm understanding")
print("")
my_phrase = "Coding is cool when you get it! " * 5
print(my_phrase)
print("")

print("To continue enter the corresponding number to the selection you'd like")


def choices(folders):
    """
    :param folders:
    """
    for s in folders:
        print(s)


selections = ["1. Math Notes", "2. Grades", "3. Exit"]

choices(selections)
folders = 3

cycles = 3
options = 1


def menu():
    """
    :
    """
    while cycles > options:
        selection = int(input())
        if selection == 1:
            print("Entering Math Notes Section")
            print("All notes relating to math are located here")
            print("")
            break
        elif selection == 2:
            print("Entering Grades Section")
            grades_inputted = 5
            sum = 0
            for scores in range(grades_inputted):
                grade = float(input("Enter math grade: "))
                sum += grade
            average = sum / grades_inputted
            print("Average of graded scores is: ", format(average, '.2f'))

            if average == 100 or average >= 89.9:
                print("Great job! Your grades are averaging to an A!")
                print("")
            elif 69.5 <= average <= 79.4:
                print("Okay. You are averaging a C but keep working hard!")
                print("")
            elif 59.5 <= average <= 69.4:
                print("You are averaging with a D.")
                print("")
            elif average <= 59.4:
                print("You are currently failing the course.")
                print("")
            else:
                print("Good job. You are passing with at least a B!")
                print("")
            if average > 100:
                print("Grade is averaging over 100! Congratulations!!")
                print("")
            else:
                print(
                    "Keep working hard!")
                break
        elif selection == 3:
            print("Exiting Program")
        else:
            print("Invalid entry. Please try again with a valid entry number.")
            int(input())
    print("Please enter another number to move onto another section")
    choices(selections)


menu()
while cycles > options:
    selection = int(input())
    if selection == 1:
        print("Entering Math Notes Section")
        print("All notes relating to math are located here")
        print("")
        break
    elif selection == 2:
        print("Entering Grades Section")
        grades_inputted = 5
        sum = 0
        for scores in range(grades_inputted):
            grade = float(input("Enter math grade: "))
            sum += grade
        average = sum / grades_inputted
        print("Average of graded scores is: ", format(average, '.2f'))

        if average == 100 or average >= 89.9:
            print("Great job! Your grades are averaging to an A!")
            print("")
        elif 69.5 <= average <= 79.4:
            print("Okay. You are averaging a C but keep working hard!")
            print("")
        elif 59.5 <= average <= 69.4:
            print("You are averaging with a D.")
            print("")
        elif average <= 59.4:
            print("You are currently failing the course.")
            print("")
        else:
            print("Good job. You are passing with at least a B!")
            print("")
        if average > 100:
            print("Grade is averaging over 100! Congratulations!!")
            print("")
        else:
            print(
                "Keep working hard!")
            break
    elif selection == 3:
        print("Exiting Program")
    else:
        print("Invalid entry. Please try again with a valid entry number.")
        selection = int(input())
print("Please enter another number to move onto another section")
choices(selections)
menu()
while cycles > options:
    selection = int(input())
    if selection == 1:
        print("Entering Math Notes Section")
        print("All notes relating to math are located here")
        print("")
        break
    elif selection == 2:
        print("Entering Grades Section")
        grades_inputted = 5
        sum = 0
        for scores in range(grades_inputted):
            grade = float(input("Enter math grade: "))
            sum += grade
        average = sum / grades_inputted
        print("Average of graded scores is: ", format(average, '.2f'))

        if average == 100 or average >= 89.9:
            print("Great job! Your grades are averaging to an A!")
            print("")
        elif 69.5 <= average <= 79.4:
            print("Okay. You are averaging a C but keep working hard!")
            print("")
        elif 59.5 <= average <= 69.4:
            print("You are averaging with a D.")
            print("")
        elif average <= 59.4:
            print("You are currently failing the course.")
            print("")
        else:
            print("Good job. You are passing with at least a B!")
            print("")
        if average > 100:
            print("Grade is averaging over 100! Congratulations!!")
            print("")
        else:
            print(
                "Keep working hard!")
            break
    elif selection == 3:
        print("Exiting Program")
    else:
        print("Invalid entry. Please try again with a valid entry number.")
        selection = int(input())
print("Please enter another number to move onto another section")
choices(selections)
menu()
while cycles > options:
    selection = int(input())
    if selection == 1:
        print("Entering Math Notes Section")
        print("All notes relating to math are located here")
        print("")
        break
    elif selection == 2:
        print("Entering Grades Section")
        grades_inputted = 5
        sum = 0
        for scores in range(grades_inputted):
            grade = float(input("Enter math grade: "))
            sum += grade
        average = sum / grades_inputted
        print("Average of graded scores is: ", format(average, '.2f'))

        if average == 100 or average >= 89.9:
            print("Great job! Your grades are averaging to an A!")
            print("")
        elif 69.5 <= average <= 79.4:
            print("Okay. You are averaging a C but keep working hard!")
            print("")
        elif 59.5 <= average <= 69.4:
            print("You are averaging with a D.")
            print("")
        elif average <= 59.4:
            print("You are currently failing the course.")
            print("")
        else:
            print("Good job. You are passing with at least a B!")
            print("")
        if average > 100:
            print("Grade is averaging over 100! Congratulations!!")
            print("")
        else:
            print(
                "Keep working hard!")
            break
    elif selection == 3:
        print("Exiting Program")
    else:
        print("Invalid entry. Please try again with a valid entry number.")
        selection = int(input())
print("Please enter another number to move onto another section")
choices(selections)
menu()
