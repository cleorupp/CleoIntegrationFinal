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
# Put the while loop in to make sure whole number.
# I inputted loop as instructed from course website.
while True:
    try:
        first_number = input("Enter first number: ")
        num1 = int(first_number)
        break
    except ValueError:
        print("Error. Please enter a whole number.")
while True:
    try:
        second_num = input("Enter second number: ")
        num2 = int(second_num)
        break
    except ValueError:
        print("Error. Please enter a whole number.")
# Lines 32-69 were apart of the completion for Sprint 1.
print("")
print("The power of the first number to the second number equals to")
print(num1 ** num2)
print("")
print("Multiply the first number to the second number equals to")
print(num1 * num2)
print("")
print("Dividing the first number to the second number equals to")
print(num1 / num2)
print("")
print("The remainder of the first and second number equals to")
print(num1 % num2)
print("")
print(
    "Diving the 1st number to the 2nd number with rounded division equals to")
print(num1 // num2)
print("")
print("Adding the first number and the second number together equals to")
print(num1 + num2)
print("")
print("Subtracting the first number to the second number equals to")
print(num1 - num2)

course_label = "COP"
course_number = "1500"
course_name = course_label + course_number
print("Learning the following Python Code in my", course_name,
      "course. I am applying the new")
# Had to put in two separate lines so it doesn't go over 79 characters.
print("knowledge into creating this program.")
print("")

print("I have been struggling to understand the coding concept")
print(
    "but after this project and putting it together I think I'm understanding")
print("")
my_phrase = "Coding is cool when you get it! " * 5
print(my_phrase)
print("")

print("To continue, enter corresponding number to the selection you'd like")


# Demonstrating I know how to create function definitions and their meaning.
def choices(section):
    """
    lists selection options with numbers.
    :param section:
    """
    for s in section:
        print(s)


selections = ["1. Notes", "2. Grades", "3. Exit"]

choices(selections)
folders = 3

cycles = 3
options = 1


def menu():
    """
    choice selections
    """
    # to help integrate the try and except within an if/else while loop
    while cycles > options:
        try:
            selection = int(input())
        except ValueError:
            print("Please enter the number 1, 2, or 3.")
            continue
        if selection == 1:
            print("Entering Notes Section")
            print("All notes relating to the subject are located here")
            print("")
            break
        elif selection == 2:
            print("Entering Grades Section")
            grades_inputted = 5
            value = 0
            try:
                for scores in range(grades_inputted):
                    grade = float(input("Enter grade: "))
                    value += grade
                average = value / grades_inputted
                print("Average of scores:  ", format(average, '.2f'))
            except ValueError:
                print("Please enter a numeric value of grade.")
                for scores in range(grades_inputted):
                    grade = float(input("Enter grade: "))
                    value += grade
                average = value / grades_inputted
                print("Average of scores:  ", format(average, '.2f'))
            if 100 == average or average >= 89.9:
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
                print("Keep working hard!")
                break
        elif selection == 3:
            print("Exiting Program")
        else:
            print("Invalid entry. Please try again with a valid entry number.")
            print(choices(selections))
    print("Please enter another number to move onto another section")


menu()
# to help integrate the try and except within an if/else while loop
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
while cycles > options:
    try:
        number_selection = int(input())
    except ValueError:
        print("Please enter the number 1, 2, or 3.")
        continue

    if number_selection == 1:
        print("Entering Notes Section")
        print("All notes relating to the subject are located here")
        print("")
        break
    elif number_selection == 2:
        print("Entering Grades Section")
        scores_entered = 5
        starting_value = 0
        try:
            for grades_selection in range(scores_entered):
                grades = float(input("Enter grade: "))
                starting_value += grades
            avg_of_scores = starting_value / scores_entered
            print("Average of scores:  ", format(avg_of_scores, '.2f'))
        except ValueError:
            print("Please enter a numeric value of grade")
            for grades_selection in range(scores_entered):
                grades = float(input("Enter grade: "))
                starting_value += grades
            avg_of_scores = starting_value / scores_entered
            print("Average of scores:  ", format(avg_of_scores, '.2f'))
        if avg_of_scores == 100 or avg_of_scores >= 89.9:
            print("Great job! Your grades are averaging to an A!")
            print("")
        elif 69.5 <= avg_of_scores <= 79.4:
            print("Okay. You are averaging a C but keep working hard!")
            print("")
        elif 59.5 <= avg_of_scores <= 69.4:
            print("You are averaging with a D.")
            print("")
        elif avg_of_scores <= 59.4:
            print("You are currently failing the course.")
            print("")
        else:
            print("Good job. You are passing with at least a B!")
            print("")
        if avg_of_scores > 100:
            print("Grade is averaging over 100! Congratulations!!")
            print("")
        else:
            print("Keep working hard!")
            break
    elif number_selection == 3:
        print("Exiting Program")
    else:
        print("Invalid entry. Please try again with a valid entry number.")
        print(choices(selections))
print("Please enter another number to move onto another section")
choices(selections)
menu()
# to help integrate the try and except within an if/else while loop
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
while cycles > options:
    try:
        number_selection = int(input())
    except ValueError:
        print("Please enter the number 1, 2, or 3.")
        continue
    if number_selection == 1:
        print("Entering Notes Section")
        print("All notes relating to the subject are located here")
        print("")
        break
    elif number_selection == 2:
        print("Entering Grades Section")
        scores_entered = 5
        starting_value = 0
        try:
            for grades_selection in range(scores_entered):
                grades = float(input("Enter grade: "))
                starting_value += grades
            avg_of_scores = starting_value / scores_entered
            print("Average of scores:  ", format(avg_of_scores, '.2f'))
        except ValueError:
            print("Please enter a numeric value of grade.")
            for grades_selection in range(scores_entered):
                grades = float(input("Enter grade: "))
                starting_value += grades
            avg_of_scores = starting_value / scores_entered
            print("Average of scores:  ", format(avg_of_scores, '.2f'))
        if avg_of_scores == 100 or avg_of_scores >= 89.9:
            print("Great job! Your grades are averaging to an A!")
            print("")
        elif 69.5 <= avg_of_scores <= 79.4:
            print("Okay. You are averaging a C but keep working hard!")
            print("")
        elif 59.5 <= avg_of_scores <= 69.4:
            print("You are averaging with a D.")
            print("")
        elif avg_of_scores <= 59.4:
            print("You are currently failing the course.")
            print("")
        else:
            print("Good job. You are passing with at least a B!")
            print("")
        if avg_of_scores > 100:
            print("Grade is averaging over 100! Congratulations!!")
            print("")
        else:
            print("Keep working hard!")
            break
    elif number_selection == 3:
        print("Exiting Program")
    else:
        print("Invalid entry. Please try again with a valid entry number.")
        print(choices(selections))
print("Please enter another number to move onto another section")
choices(selections)
menu()

# to help integrate the try and except within an if/else while loop
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
while cycles > options:
    try:
        number_selection = int(input())
    except ValueError:
        print("Please enter the number 1, 2, or 3.")
        continue
    if number_selection == 1:
        print("Entering Notes Section")
        print("All notes relating to the subject are located here")
        print("")
        break
    elif number_selection == 2:
        print("Entering Grades Section")
        scores_entered = 5
        starting_value = 0
        try:
            for grades_selection in range(scores_entered):
                grades = float(input("Enter grade: "))
                starting_value += grades
            avg_of_scores = starting_value / scores_entered
            print("Average of scores:  ", format(avg_of_scores, '.2f'))
        except ValueError:
            print("Please enter a numeric value of grade.")
            for grades_selection in range(scores_entered):
                grades = float(input("Enter grade: "))
                starting_value += grades
            avg_of_scores = starting_value / scores_entered
            print("Average of scores:  ", format(avg_of_scores, '.2f'))
        if avg_of_scores == 100 or avg_of_scores >= 89.9:
            print("Great job! Your grades are averaging to an A!")
            print("")
        elif 69.5 <= avg_of_scores <= 79.4:
            print("Okay. You are averaging a C but keep working hard!")
            print("")
        elif 59.5 <= avg_of_scores <= 69.4:
            print("You are averaging with a D.")
            print("")
        elif avg_of_scores <= 59.4:
            print("You are currently failing the course.")
            print("")
        else:
            print("Good job. You are passing with at least a B!")
            print("")
        if avg_of_scores > 100:
            print("Grade is averaging over 100! Congratulations!!")
            print("")
        else:
            print("Keep working hard!")
            break
    elif number_selection == 3:
        print("Exiting Program")
    else:
        print("Invalid entry. Please try again with a valid entry number.")
        print(choices(selections))
print("Please enter another number to move onto another section")
choices(selections)
menu()
