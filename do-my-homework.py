# imports
import time
import sys

# Values and lists
problems = []
TimesloopedQuestions = 0

# Main script
# tells the user about the program
print("Welcome to 'Do my homework!' ")
print("we are gonna be NOT tutoring you for the homwork but doing it for you!")
print("A famous quote the Creator loves: 'Roz do my homework!' - The Wild Robot Escapes By Peter B. ")
print()
print()
print()
print()
print("Well lets get down to real buisness let this computer do your homework!")
print("first of all we should state this is for MATH ONLY.")
# does the asking process here!
Questions = input("okay the first question is  how many problems are on your homework: ")
for i in range(int(Questions)):
    # add to the amount of times looped
    TimesloopedQuestions = TimesloopedQuestions + 1
    # ask for operater and see if correct
    while True:
        AddQuestionOperator = input(f"what is problem {TimesloopedQuestions}'s operator? (divide is '/', multiply is '*', add is '+', subtract is '-'): ") 
        if AddQuestionOperator in ["/", "*", "+", "-"]:
            print("Alright, got the operator!")
            break
        else:
            print("Oops, try again!")
    
    # ask for nums and see if correct
    AddQuestionNum1 = input(f"what is problem {TimesloopedQuestions}'s first number? : ")
    sure1 = input(f"are you sure the number is {AddQuestionNum1}? [yes,no]: ")
    if sure1 == "yes":
        print("okay!")
    else:
        while True:
            AddQuestionNum1 = input(f"what is problem {TimesloopedQuestions}'s first number? : ")
            sure1 = input(F"are you sure the number is {AddQuestionNum1}? [yes,no]: ")

            if sure1 == "yes":
                print("okay!")
                break
            else:
                print("alright enter it again!")

    AddQuestionNum2 = input(f"what is problem {TimesloopedQuestions}'s second number? : ")
    sure2 = input(F"are you sure the number is {AddQuestionNum2}? [yes,no]: ")
    if sure2 == "yes":
        print("okay!")
    else:
        while True:
            AddQuestionNum2 = input(f"what is problem {TimesloopedQuestions}'s second number? : ")
            sure2 = input(F"are you sure the number is {AddQuestionNum2}? [yes,no]: ")
            if sure2 == "yes":
                print("okay!")
                break
            else:
                print("alright enter it again!")
    # build a question
    BuiltQuestion = f"{AddQuestionNum1} {AddQuestionOperator} {AddQuestionNum2}"
    problems.append(BuiltQuestion)

# lets set this one varible
QuestionsTODO = TimesloopedQuestions

QuestionNumToDisaply = 0

# now lets do the homework!
for i in range(int(QuestionsTODO)):
    answer = eval(problems[QuestionNumToDisaply])
    print(f"Problem {QuestionNumToDisaply}'s answer is {answer}")
    QuestionNumToDisaply = QuestionNumToDisaply + 1

print()
print()
print()
print()
print("Thanks for using Do My Homework!")
time.sleep(6)
sys.exit()
